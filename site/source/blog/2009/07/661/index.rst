:date: 2009-07-30 17:29:57
:tags: python, Programming, web

=============================================================
buildoutで開発3: easy_install できるように公開する
=============================================================

`eggの作り方が分からない`_, `buildoutで開発1: WSGIアプリをeggで作る`_, `buildoutで開発2: buildoutで環境を整える`_ の続き。buildoutというよりsetuptoolsネタ。

buildoutで自動的にパッケージを取ってくる仕組みは内部的にsetuptools/easy_install.pyを使用していて、setuptoolsはデフォルトでは対象パッケージ名を pypi_ (Python Package Index) に探しに行く。pypiへの登録は ``python setup.py register`` で出来るんだけど、前回作ったようなwsgiappは実験用なので登録したくないし、仕事で作っているパッケージ類は世界に公開してはまずい。ということで、easy_installの ``--find-links (-f)`` オプションでpypi以外のページを指定する方法でpypiに公開しなくても自動インストール出来るようにする。

(setuptoolsのマニュアルを読むと、そのまんまな記載がある: `Making your package available for EasyInstall`_, `Sumiさんの日本語訳`_)

前提
-----
* pypiに登録しない
* wsgiappをSubversionから取ってくる

Subversionリポジトリをhttpで公開する
-------------------------------------
SVNの公開方法は ``file:``, ``svn:``, ``http:`` とあるけど、easy_installの-fオプションではページ内のリンクにfile:と書いてあってもSVNとして認識されないので、素直にhttp:を使うことにする。あと、SVN以外のリポジトリも使えないっぽい。

ということで、httpdにmod_dav_svnで設定して公開する。URLは ``http://localhost:8080/repos`` でSVNのルートが見えるようにしておく。


easy_install用のindexページを用意する
---------------------------------------
easy_installの-fオプションは指定したページのリンクをチェックして、リンクURLがegg用リンクであれば使ってくれる。eggとして認識されるリンクは、URL末尾に ``#egg=projectname-version`` という記載があればよいので、開発版wsgiappの場合は ``http://localhost:8080/repos/wsgiapp/trunk#egg=wsgiapp-dev`` となっていればeasy_installで認識してくれるようになる。

ということで、http://localhost:8080/index.htmlというページを作って上記URLをaタグで書いておく。


easy_installでインストールしてみる
------------------------------------
実際に認識されるかどうか確認する。確認したいだけなので、 ``--dry-run`` オプションを付けて実行。dry-runのせいで最後はエラーになるけど、途中までは以下のようにsubversionからcheckoutしてくれて、index.htmlがうまく働いている事が確認出来た。

.. topic:: easy_install --dry-run
  :class: dos

  | > easy_install --dry-run -f http://localhost:8080/ wsgiapp
  | Searching for wsgiapp
  | Reading http://localhost:8080/
  | Best match: wsgiapp dev
  | Downloading http://localhost:8080/repos/wsgiapp/trunk#egg=wsgiapp-dev
  | Doing subversion checkout from http://localhost:8080/repos/wsgiapp/trunk to \\temp\\easy_install-tlvn6p\trunk
  | Processing trunk
  | Running setup.py ....


ここまでくれば、index.htmlを自動生成するようにwsgiappを改造すれば後々楽になりそう。

wsgiappで動的にPackageIndexページを生成する
-------------------------------------------
とりあえずてきとーに、'指定PATH/package名/trunk'を'package名#egg=package名-dev'としてリンクするように、 `buildoutで開発2: buildoutで環境を整える`_ で作成したwsgiapp.scraperに新しい関数を追加する。


wsgiapp/scraper.py の追加関数部分:

.. code-block:: python

    import urlparse
    import string

    def eggifyLinks(fileobj, basepath=''):
        """\
        eggifyLinks read html data from given fileobj and modify href
        attributes.
    
            >>> from StringIO import StringIO
            >>> fileobj = StringIO('''\
            ... <html><body><a href="wsgiapp">wsgiapp</a></body></html>
            ... ''')
            >>> content = eggifyLinks(fileobj)
            >>> 'href="wsgiapp/trunk#egg=wsgiapp-dev"' in content
            True
    
        ``basepath`` param effect for relative url.
    
            >>> fileobj = StringIO('''\
            ... <html><body><a href="wsgiapp">wsgiapp</a></body></html>
            ... ''')
            >>> content = eggifyLinks(fileobj, 'http://domain/sub/')
            >>> 'href="http://domain/sub/wsgiapp/trunk#egg=wsgiapp-dev"' in content
            True
    
        if href ends with '/', eggifyLinks return same result.
    
            >>> fileobj = StringIO('''\
            ... <html><body><a href="wsgiapp/">wsgiapp</a></body></html>
            ... ''')
            >>> content = eggifyLinks(fileobj)
            >>> 'href="wsgiapp/trunk#egg=wsgiapp-dev"' in content
            True
    
        work with full url.
    
            >>> fileobj = StringIO('''\
            ... <html><body><a href="http://localhost:8080/repos/wsgiapp/">wsgiapp</a></body></html>
            ... ''')
            >>> content = eggifyLinks(fileobj)
            >>> 'href="http://localhost:8080/repos/wsgiapp/trunk#egg=wsgiapp-dev"' in content
            True
    
        if url have #id, href is not modified.
    
            >>> fileobj = StringIO('''\
            ... <html><body><a href="wsgiapp#foo">wsgiapp</a></body></html>
            ... ''')
            >>> content = eggifyLinks(fileobj)
            >>> 'href="wsgiapp#foo"' in content
            True
            >>> '#egg' not in content
            True
    
        if url have no package name, href is not modified.
    
            >>> fileobj = StringIO('''\
            ... <html><body>
            ... <a href="..">Parent</a>
            ... <a href="http://domainonly/">domain</a>
            ... </body></html>
            ... ''')
            >>> content = eggifyLinks(fileobj)
            >>> 'href=".."' in content
            True
            >>> 'href="http://domainonly/"' in content
            True
            >>> '#egg' not in content
            True
    
        """
        baseparts = urlparse.urlparse(basepath)
    
        bs = BeautifulSoup(fileobj)
        for elem in bs.findAll('a'):
            if elem.has_key('href'):
                href = elem['href']
                parts = list(urlparse.urlparse(href))
    
                # #id check
                if parts[5]:
                    continue # #id already exist
    
                # modify path
                path = parts[2]
                if path.endswith('/'):
                    path = path[:-1]
                pkgname = path.split('/')[-1]
                if not pkgname or pkgname[0] not in string.letters:
                    continue # pkgname does not seem package name
                parts[2] = '%(path)s/trunk#egg=%(pkgname)s-dev' % locals()
    
                # modify domain
                if basepath and not parts[1]:
                    parts[0] = baseparts[0]
                    parts[1] = baseparts[1]
                    if parts[2][0] != '/':
                        p = baseparts[2]
                        if p.endswith('/'):
                            p = p[:-1]
                        parts[2] = p + '/' + parts[2]
    
                # update href
                elem['href'] = urlparse.urlunparse(parts)
    
        return bs.prettify()

テストする。

.. topic:: テスト
  :class: dos

  | > bin/test.exe
  | Running zope.testing.testrunner.layer.UnitTests tests:
  |   Set up zope.testing.testrunner.layer.UnitTests in 0.000 seconds.
  |   Ran 2 tests with 0 failures and 0 errors in 0.887 seconds.
  | Tearing down left over layers:
  |   Tear down zope.testing.testrunner.layer.UnitTests in 0.000 seconds.


呼出元を新しい関数に変更。

wsgiapp/startup.py の変更部分:

.. code-block:: python

    import urllib2

    def application(environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        return [scraper.eggifyLinks(
            urllib2.urlopen("http://localhost:8080/repos/"),
            "http://localhost:8080/repos/",
        )]


実際に動作させた時の出力を ``bin/paster request wsgi.ini /`` で確認。

.. topic:: paster request
  :class: dos

  | > bin/paster request wsgi.ini /
  | <html>
  |  <head>
  |   <title>
  |    repos - Revision 9: /
  |   </title>
  |  </head>
  |  <body>
  |   <h2>
  |    repos - Revision 9: /
  |   </h2>
  |   <ul>
  |    <li>
  |     <a href="http://localhost:8080/repos/wsgiapp/trunk#egg=wsgiapp-dev">
  |      wsgiapp/
  |     </a>
  |    </li>
  |   </ul>
  |   <hr noshade />
  |   <em>
  |    Powered by
  |    <a href="http://subversion.tigris.org/">
  |     Subversion
  |    </a>
  |    version 1.6.3 (r38063).
  |   </em>
  |  </body>
  | </html>


easy_installでうまく動くか確認するため、wsgiappをサーバー動作させてから、別コンソールでeasy_installを-fオプション付きで動かしてみてwsgiappパッケージを見つけられれば成功。8080ポートはapacheで使ってるので8180で起動するようにwsgi.iniを変更しておく。

.. topic:: paster serve
  :class: dos

  | > bin/paster serve wsgi.ini
  | Starting server in PID 6460.
  | serving on http://127.0.0.1:8180


.. topic:: easy_install --find-links
  :class: dos

  | > easy_install -n -f http://localhost:8180/ wsgiapp
  | Searching for wsgiapp
  | Reading http://localhost:8180/
  | Best match: wsgiapp dev
  | Downloading http://localhost:8080/repos/wsgiapp/trunk#egg=wsgiapp-dev
  | Doing subversion checkout from http://localhost:8080/repos/wsgiapp/trunk to \\temp\\easy_install-_oovzq\trunk
  | Processing trunk
  | Running setup.py ....

dry run なのでsetup.pyの実行には失敗する。実際にインストールする場合は-nを外して実行してみよう。

あとは、このwsgiappをmod_wsgiで動作するようにしておけば、超簡易版のローカル用パッケージ一覧生成ツールとして使える。使えるといいなぁ。

もっとちゃんとやろうと思ったら、pysvn等でパッケージの一覧を取ってきて、各パッケージのtrunkのURLに、 #egg=パッケージ名-dev と付けたり、tagsから自動で #egg=パッケージ名-tag名 としてみたりすればいいんだけど、毎回動的にやってると重いし、そこまでやるんだったらローカルにPyPIを立ち上げた方が良いと思う。作り方は `EggBasket`_ や `how to run your own private PyPI (Cheeseshop) server << Fetchez le Python`_ を参考すればよさそう。



.. _`eggの作り方が分からない`: http://www.freia.jp/taka/blog/655
.. _`buildoutで開発1: WSGIアプリをeggで作る`: http://www.freia.jp/taka/blog/659
.. _`buildoutで開発2: buildoutで環境を整える`: http://www.freia.jp/taka/blog/660

.. _`zc.buildoutを使ったプロジェクト管理`: http://nagosui.org/Nagosui/Docs/tutorial/managing-projects-with-zcbuildout/tutorial-all-pages
.. _`Managing projects with Buildout`: http://plone.org/documentation/tutorial/buildout/tutorial-all-pages
.. _`Using z3c packages,...`: http://www.ibiblio.org/paulcarduner/z3ctutorial/introduction.html
.. _`Zope 3の入門にはz3cのチュートリアルがおすすめ`: http://blog.livedoor.jp/matssaku/archives/50500810.html

.. _`pypi`: http://pypi.python.org/simple/
.. _`http://svn.zope.org/repos/main/`: http://svn.zope.org/repos/main/
.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
.. _`zc.recipe.egg`: http://pypi.python.org/pypi/zc.recipe.egg
.. _`zc.recipe.testrunner`: http://pypi.python.org/pypi/zc.recipe.testrunner
.. _`z3c.recipe.egg`: http://pypi.python.org/pypi/z3c.recipe.egg
.. _`Zope 3 Package Guide`: http://wiki.zope.org/zope3/Zope3PackageGuide
.. _`mr.developer`: http://pypi.python.org/pypi/mr.developer
.. _`mod_wsgiはGoogleCode`: http://code.google.com/p/modwsgi/

.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-09)`: http://d.hatena.ne.jp/SumiTomohiko/20070609/1181406701
.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-22)`: http://d.hatena.ne.jp/SumiTomohiko/20070622/1182537643
.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-23)`: http://d.hatena.ne.jp/SumiTomohiko/20070623/1182602060
.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-24)`: http://d.hatena.ne.jp/SumiTomohiko/20070624/1182665330

.. _`Making your package available for EasyInstall`: http://peak.telecommunity.com/DevCenter/setuptools#making-your-package-available-for-easyinstall
.. _`Sumiさんの日本語訳`: http://d.hatena.ne.jp/SumiTomohiko/20070623/1182602060

.. _`how to run your own private PyPI (Cheeseshop) server << Fetchez le Python`: http://tarekziade.wordpress.com/2008/03/20/how-to-run-your-own-private-pypi-cheeseshop-server/
.. _`EggBasket`: http://www.chrisarndt.de/projects/eggbasket/


.. :extend type: text/html
.. :extend:


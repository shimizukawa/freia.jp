:date: 2009-07-16 23:45:00
:tags: python, Programming, web

==================================================
buildoutで開発2: buildoutで環境を整える
==================================================

`eggの作り方が分からない`_, `buildoutで開発1: WSGIアプリをeggで作る`_ の続き。buildoutでテストまで。

現時点のファイル構成::

  c:\Project\buildout\env1\
   +-- wsgiapp
       +-- setup.cfg
       +-- setup.py
       +-- wsgi.ini
       +-- wsgiapp.egg-info
       |   +-- *.*
       +-- wsgiapp
           +-- __init__.py
           +-- __init__.pyc
           +-- startup.py
           +-- startup.pyc


とりあえずコミットしておく。
\*.pycと\*.egg-info は自動生成されるファイルなのでコミットしない。
Subversion上に以下のようになるようにコミットして、trunkをチェックアウト。

リポジトリの内容はこんな感じ::

  svn://
   +-- wsgiapp
       +-- trunk
           +-- setup.cfg
           +-- setup.py
           +-- wsgi.ini
           +-- wsgiapp
               +-- __init__.py
               +-- startup.py

以降、ソースコード管理に登録する手順を何度か書いてますが、以降の作業では、登録するべきファイルとそうでないファイルが混在し始めるため、必要なファイルを分かりやすくするためにコミットしてます。

.. topic:: SVNに登録
  :class: dos

  | > cd c:\Project\buildout\env1\wsgiapp
  | > svn mkdir file:///svnpath/wsgiapp -m "mkdir"
  | > svn mkdir file:///svnpath/wsgiapp/trunk -m "mkdir"
  | > svn import . file:///svnpath/wsgiapp/trunk -m "import"
  | > svn co file:///svnpath/wsgiapp/trunk . --force


閑話休題。buildoutを使うための環境を整える。

.. topic:: bootstrap.py を取得
  :class: dos

  | > cd c:\Project\buildout\env1\wsgiapp
  | > wget http://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/bootstrap.py
  | > dir /b
  | bootstrap.py
  | setup.cfg
  | setup.py
  | wsgi.ini
  | wsgiapp


buildout.cfg::

    [buildout]
    develop = .
    parts = wsgiapp
    newest = true
    
    [wsgiapp]
    recipe = zc.recipe.egg
    eggs =
        wsgiapp
        Paste
        PasteDeploy
        PasteScript


ここまでで一度コミット。

.. topic:: buildoutの初期ファイルをsvnに登録
  :class: dos

  | > svn add buildout.cfg bootstrap.py
  | > svn ci -m "initial buildout files"


おもむろに違う環境を作ってみる。別のコンソールを開くと良いと思う。

.. topic:: 新しい環境で動作確認
  :class: dos

  | > cd c:\Project\buildout
  | > virtualenv env2
  | > cd env2
  | > Scripts/activate
  | > svn co file:///svnpath/wsgiapp/trunk wsgiapp
  | > cd wsgiapp
  | > python bootstrap.py
  | > bin/buildout
  | ...
  | > bin/paster request wsgi.ini /
  | It's Python!
  | ...


この環境ではvirtualenv と setuptoolsが使える以外は何も入っていない。
bootstrap.py -> buildout -> setuptools... と関連して色々ダウンロードされて、環境が構築される。

ここで、元の環境にもどって、wsgiappに関連パッケージを定義する。
パッケージの関連づけはbuildoutとしてではなく、eggとして対応する。
このため setup.py を以下のように更新する。

setup.py:

.. code-block:: python

  install_requires=[
    'BeautifulSoup',
  ],


.. topic:: buildoutで環境を更新する（依存パッケージを取得する）。
  :class: dos

  | > buildout
  | ...
  | Updating wsgiapp.
  | Getting distribution for 'BeautifulSoup'.
  | ...


ここで、wsgiapp.egg-info/requires.txt を見ると、ちゃんとBeautifulSoupに依存しているという定義にUpdateされている。


これからBeautifulSoupを使うような実装を追加したいが、eggで追加されたパッケージの動作を確認したり、ヘルプを見たりするのにインタラクティブシェルからBeautifulSoupを呼び出したい。
でも、buildoutで関連づけられたeggパッケージはPythonにインストールされているわけではないので、そのままでは呼び出せない。


.. topic:: eggパッケージをimport出来ない
  :class: dos

  | > python
  | Python 2.4.4 (#71, Oct 18 2006, 08:34:43) [MSC v.1310 32 bit (Intel)] on win32
  | Type "help", "copyright", "credits" or "license" for more information.
  | >>>
  | >>> import BeautifulSoup
  | Traceback (most recent call last):
  |   File "<stdin>", line 1, in ?
  | ImportError: No module named BeautifulSoup
  | >>>


そこで、関連するeggを使える状態でPythonを起動するスクリプトを作成する。スクリプトの名前は適当にpyとしておきます。
スクリプトの用意は、以下のようにbuildout.cfgを書き換えれば、
あとはbuildoutがやってくれる。

buildout.cfg::

    [buildout]
    develop = .
    parts = wsgiapp eggpy
    newest = true

    [wsgiapp]
    recipe = zc.recipe.egg
    eggs =
        wsgiapp
        Paste
        PasteDeploy
        PasteScript

    [eggpy]
    recipe = zc.recipe.egg
    eggs = ${wsgiapp:eggs}
    interpreter = py
    scripts = py

``[eggpy]`` セクションを追加して、そのセクションがbuild対象であることをbuildoutに伝えるために、 ``parts =`` にeggpyを追加。
eggpyの中で、利用したいeggの指定はwsgiappと同じ内容で良いけど、それをまた書くのは面倒なので、 ``${wsgiapp:eggs}`` という感じで変数で指定。

この内容で環境を更新するために、buildoutコマンドを実行。

.. topic:: buildoutで環境を更新
  :class: dos

  | > bin/buildout
  | Develop: 'c:\\Project\\buildout\\env1\\wsgiapp\\.'
  | unrecognized .svn/entries format; skipping .
  | unrecognized .svn/entries format in
  | Updating wsgiapp.
  | Installing eggpy.
  | Generated interpreter 'c:\\Project\\buildout\\env1\\wsgiapp\\bin\\py'.


作られたpyコマンドでインタラクティブシェルを起動して、eggパッケージを呼び出せることを確認。

.. topic:: eggパッケージをimport出来る
  :class: dos

  | > bin/py
  | 
  | >>> import BeautifulSoup
  | >>> help(BeautifulSoup)
  | Help on module BeautifulSoup:
  | 
  | NAME
  |     BeautifulSoup
  | ...


OK.

BeautifulSoupを使ったWSGIアプリの実装部分関数を作る。とりあえずWSGIとか関係なく、与えられたURLをGETして、hrefの値を書き換えて返す関数を実装。動作確認用に、コンソールから実行された場合の動作も実装しておく。

wsgiapp/scraper.py:

.. code-block:: python

    # -*- coding: utf-8 -*-
    import urllib2
    from BeautifulSoup import BeautifulSoup
    
    def modifyLinks(url):
        bs = BeautifulSoup(urllib2.urlopen(url))
        for elem in bs.findAll('a'):
            if elem.has_key('href'):
                elem['href'] += "#foobar"
    
        return bs.prettify()
    
    
    if __name__ == '__main__':
        import sys
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = "http://pypi.python.org/simple/BeautifulSoup/"
        print modifyLinks(url)


で、動作確認。

.. topic:: コンソールで実行
  :class: dos

  | > bin/py wsgiapp/scraper.py
  | <html>
  | ...
  |   <a href="http://www.crummy.com/software/BeautifulSoup/#foobar" rel="homepage">
  | ...
  | </html>

OK. ちゃんと#foobarが追加されてた。
これをwsgiappとして組み込む。

wsgiapp/startup.py:

.. code-block:: python

    # -*- coding: utf-8 -*-
    import scraper
    
    def application(environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        return [scraper.modifyLinks(
            "http://pypi.python.org/simple/BeautifulSoup/"
        )]
    
    def application_factory(global_conf):
        return application


うまく動くか、pasterコマンドでrequestして確認したり、paster serve してブラウザで確認したり。

.. topic:: pasterで動作確認
  :class: dos

  | > bin/paster request wsgi.ini /
  | ...
  | > bin/paster serve wsgi.ini
  | ...


ここまでをとりあえず、コミット。


.. topic:: scraperをコミット
  :class: dos

  | > svn add wsgiapp\scraper.py
  | > svn ci -m "add and use scraper"


ここで、さっき作ったscraperのテスト方法が気に入らないので、書き換えてみる。


wsgiapp/scraper.py:

.. code-block:: python

    # -*- coding: utf-8 -*-
    import urllib2
    from BeautifulSoup import BeautifulSoup
    
    def modifyLinks(url):
        """modifyLinks get content from given url and modify href attributes.
    
           >>> content = modifyLinks("http://pypi.python.org/simple/BeautifulSoup/")
           >>> '#foobar"' in content
           True
        """
        bs = BeautifulSoup(urllib2.urlopen(url))
        for elem in bs.findAll('a'):
            if elem.has_key('href'):
                elem['href'] += "#foobar"
    
        return bs.prettify()
    
    
    if __name__ == '__main__':
        import doctest
        doctest.testmod()


で、改めてテスト。エラー無くテストが成功した場合は、 ``-v`` オプション無しだと何も表示されないので、心配なら-vを付けて動かしてみよう。


.. topic:: テストする
  :class: dos

  | > bin/py wsgiapp/scraper.py
  | > bin/py wsgiapp/scraper.py -v
  | ...
  | Test passed.


テストが通ったので、コミット。

最後に、buildoutで全モジュールを自動的にテストするためのスクリプトを用意する。まず、DocTestを外から呼び出すためにtests.pyを用意。

wsgiapp/tests.py:

.. code-block:: python

    # -*- coding: utf-8 -*-
    
    import unittest
    from doctest import DocTestSuite
    
    def test_suite():
        return unittest.TestSuite((
            DocTestSuite('wsgiapp.scraper'),
        ))
    
    if __name__ == '__main__':
        unittest.main()

次に、biuldout.cfgでテスト実行スクリプトを生成。
``[test]`` セクションを追加して、partsにtestセクションの呼び出しを追加。使っているレシピが今までと違ってzc.recipe.testrunnerであることと、テスト対象にPaste等を含めたくなかったので、${wsgiapp:eggs}は使わなかったところがポイント。

buildout.cfg::

  ...
  parts = wsgiapp eggpy test
  ...

  [test]
  recipe = zc.recipe.testrunner
  eggs = wsgiapp
  relative-paths = true


buildoutで環境を更新してテストする。


.. topic:: buildoutで環境を更新してテストする
  :class: dos

  | > bin/buildout 
  | ...
  | Installing test.
  | Generated script 'c:\\Project\\buildout\\env1\\wsgiapp\\bin\\test'.
  | 
  | > bin/test
  | Running zope.testing.testrunner.layer.UnitTests tests:
  |   Set up zope.testing.testrunner.layer.UnitTests in 0.000 seconds.
  |   Ran 1 tests with 0 failures and 0 errors in 0.757 seconds.
  | Tearing down left over layers:
  |   Tear down zope.testing.testrunner.layer.UnitTests in 0.000 seconds.


ZopeのTestRunnerが使われるけど、気にしない方向で。 ``bin/test -h`` でコマンドラインオプションもみれるよ。

今日はここまで。

.. topic:: コミット
  :class: dos

  | > svn add wsgiapp\tests.py
  | > svn ci -m "add test framework"


参考
------
* `zc.buildout`_
* `zc.recipe.egg`_
* `zc.recipe.testrunner`_


.. _`eggの作り方が分からない`: http://www.freia.jp/taka/blog/655
.. _`buildoutで開発1: WSGIアプリをeggで作る`: http://www.freia.jp/taka/blog/659

.. _`zc.buildoutを使ったプロジェクト管理`: http://nagosui.org/Nagosui/Docs/tutorial/managing-projects-with-zcbuildout/tutorial-all-pages
.. _`Managing projects with Buildout`: http://plone.org/documentation/tutorial/buildout/tutorial-all-pages
.. _`Using z3c packages,...`: http://www.ibiblio.org/paulcarduner/z3ctutorial/introduction.html
.. _`Zope 3の入門にはz3cのチュートリアルがおすすめ`: http://blog.livedoor.jp/matssaku/archives/50500810.html

.. _`http://svn.zope.org/repos/main/`: http://svn.zope.org/repos/main/
.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
.. _`zc.recipe.egg`: http://pypi.python.org/pypi/zc.recipe.egg
.. _`zc.recipe.testrunner`: http://pypi.python.org/pypi/zc.recipe.testrunner
.. _`z3c.recipe.egg`: http://pypi.python.org/pypi/z3c.recipe.egg
.. _`Zope 3 Package Guide`: http://wiki.zope.org/zope3/Zope3PackageGuide
.. _`mr.developer`: http://pypi.python.org/pypi/mr.developer
.. _`mod_wsgiはGoogleCode`: http://code.google.com/p/modwsgi/


.. :extend type: text/html
.. :extend:


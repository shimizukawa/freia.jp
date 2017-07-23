:date: 2009-08-09 19:20:47
:tags: python, Programming, web

===================================================================
buildoutで開発5: ファイル構成の整理とpaster-template対応
===================================================================

`buildoutで開発4: mod_wsgiからegg指定でアプリ起動する`_ 、というところまで開発してくると、開発に使っていたディレクトリの直下が、buildoutで自動生成されるDIRや、egg-infoなどでごちゃごちゃしてきたので、整理する。

ファイル・ディレクトリの再配置
---------------------------------

現状のファイル構成(コミット分のみ)::

  c:\Project\buildout\env1\
   +-- wsgiapp
       +-- bootstrap.py
       +-- buildout.cfg
       +-- setup.cfg
       +-- setup.py
       +-- wsgi.ini
       +-- wsgiapp/
           +-- __init__.py
           +-- scraper.py
           +-- startup.py
           +-- tests.py


これを以下のようにしたい。

新しいファイル構成(コミット分のみ)::

  c:\Project\buildout\env1\
   +-- wsgiapp
       +-- bootstrap.py
       +-- buildout.cfg
       +-- setup.cfg
       +-- setup.py
       +-- src/
           +-- wsgi.ini
           +-- wsgiapp/
               +-- __init__.py
               +-- scraper.py
               +-- startup.py
               +-- tests.py


`buildoutで開発4: mod_wsgiからegg指定でアプリ起動する`_ でインストールして使った部分は上記のsrcディレクトリに移動した部分だけなので、実際に配布するものだけを切り分けた感じ。実際に配布するもの、というのは ``python setup.py bdist_egg`` で作られるeggの中身に相当する。

ソースコードの配置に合わせてsetup.pyを書き換える。

setup.py(diff差分):

.. code-block:: diff

  @@ -16,3 +16,4 @@
         license='ZPL',
  -      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
  +      packages=find_packages('src'),
  +      package_dir={'': 'src'},
         include_package_data=True,


packagesの検索位置をsrcディレクトリにして、src以下には配布に必要なものしか置かないことにするので、find_packages()のexclude指定は不要になった。また、distutilsにパッケージ位置を教えるためpackage_dirの指定も追加。（find_packages()とpackage_dirについて、詳しくは `[Python] setuptools - SumiTomohikoの日記 (2007-06-22)`_ または原文 `Building and Distributing Packages with setuptools`_ を参照）

eggを作成して中身を確認。

.. topic:: bdist_egg
  :class: dos

  | > python setup.py bdist_egg
  | > ls dist
  | wsgiapp-0.1dev_r10-py2.4.egg

distディレクトリに wsgiapp-0.1dev_r10-py2.4.egg が出来ている。拡張子eggのファイルは実はzipファイルなので、拡張子をzipに変える等で中身を見ることが出来る。中身に問題がなければOK。


wsgi.ini, wsgi.py をPasteで作成する
------------------------------------

既にコミットしているwsgi.iniやwsgi.pyを配布物に含めたい。含めたいけど、 `前回(buildoutで開発4)`_ のようにeasy_installでパッケージとしてインストールする事を考えると、iniのような設定ファイルをwsgiappのパッケージ本体のフォルダに入れて配布するのは微妙。

今回はpasterコマンドで設定ファイルを作れるようにしてみる。参照: `Paste Script: Development &mdash; Paste Script v1.7 documentation`_

まず、setup.pyにtemplate対応を書く。

setup.py(diff差分):

.. code-block:: diff

  @@ -20,9 +20,14 @@
         zip_safe=False,
         install_requires=[
             'BeautifulSoup',
  +          'PasteDeploy',
  +          'PasteScript',
         ],
         entry_points="""
         [paste.app_factory]
         main = wsgiapp.startup:application_factory
  +
  +      [paste.paster_create_template]
  +      wsgiapp_ini = wsgiapp.paster_templates:WSGIAppTemplate
         """,
         )


まずはinstall_requiresを更新。 `前回(buildoutで開発4)`_ で手動で入れたPasteDeployと、今回template生成に使用することになるPasteScriptを追加する。

次にpaste用のtemplate登録コマンドをentry_pointsに追加する。 ``wsgiapp_ini`` はテンプレート名で、 ``wsgiapp.paster_templates:WSGIAppTemplate`` は今から作成するパッケージ名。

テンプレート作成方法を実装するプログラム src/wsgiapp/paster_templates.py を以下のように作成する。

src/wsgiapp/paster_templates.py:

.. code-block:: python

    from paste.script.templates import Template, var
    
    class WSGIAppTemplate(Template):
        summary = 'Template for creating a deploy setting files (include wsgi.ini).'
        _template_dir = 'paster-template'
        vars = [
            var('host', 'The host to serve on', '127.0.0.1'),
            var('port', 'The port to serve on', '8080'),
        ]


最後に、上記で ``_template_dir`` に指定したディレクトリを作成し、テンプレートファイルを追加する。ということで、src/wsgiapp/paster-templateディレクトリにwsgi.ini_tmplとwsgi.pyを置いた。ここで、wsgi.iniの後ろに ``_tmpl`` と付けているが、こうすると上記のプログラムで定義した変数(host, port)で文字列を置き換えて、ファイルを配置してくれる。

wsgi.ini_tmpl::

    [app:main]
    use = egg:wsgiapp
    
    [server:main]
    use = egg:Paste#http
    host = ${host}
    port = ${port}


最後に動作確認。

.. topic:: paster create
  :class: dos

  | > cd c:\Project\buildout\env1\wsgiapp
  | > buildout
  | ...
  |
  | > cd /tmp
  | > paster create --list-templates
  | Available templates:
  |   basic_package:  A basic setuptools-enabled package
  |   paste_deploy:   A web application deployed through paste.deploy
  |   wsgiapp_ini:    Template for creating a deploy setting files (include wsgi.ini).
  |
  | > paster create -t wsgiapp_ini deploy
  | Selected and implied templates:
  |   wsgiapp#wsgiapp_ini  Template for creating a deploy setting files (include wsgi.ini).
  | 
  | Variables:
  |   egg:      deploy
  |   package:  deploy
  |   project:  deploy
  | Enter host (The host to serve on) ['127.0.0.1']:
  | Enter port (The port to serve on) ['8080']: 8180
  | Creating template wsgiapp_ini
  | Creating directory .\deploy
  |   Copying wsgi.ini_tmpl to .\deploy\wsgi.ini
  |   Copying wsgi.py to .\deploy\wsgi.py


これでdeployというディレクトリが出来ていて、中にwsgi.iniとwsgi.pyがあればOK。今までのように起動もOKだし、mod_wsgiからの起動スクリプトにも指定可能になった。

.. topic:: paster serve
  :class: dos

  | > paster serve deploy/wsgi.ini
  | Starting server in PID 9140.
  | serving on http://127.0.0.1:8180



paster-template をeggに含める
---------------------------------

ところで、今の状態で ``python setup.py bdist_egg`` しても、pythonパッケージとして認識されないpaster-templateディレクトリはeggに含まれない。これが含まれるようにするため、setup.pyを以下のように修正する。

.. code-block:: python

  @@ -18,2 +18,3 @@
         package_dir={'': 'src'},
  +      package_data = {'': ['paster-template/*.*']},
         include_package_data=True,


これでeggにpaster-template以下も含まれるようになった。他にも.txtとか.gifとか含めたかったら、package_dataの[]部分に追加すればよい。

（じゃあinclude_package_data=Trueって何なの？ディレクトリが増えたらsetup.pyを書き換えなきゃいけないの？と、疑問は残る...）


まとめ
--------

最終的なファイル構成(コミット分のみ)::

  c:\Project\buildout\env1\
   +-- wsgiapp
       +-- bootstrap.py
       +-- buildout.cfg
       +-- setup.cfg
       +-- setup.py
       +-- src/
           +-- wsgiapp/
               +-- __init__.py
               +-- paster_template.py
               +-- scraper.py
               +-- startup.py
               +-- tests.py
               +-- paster-template
                   +-- wsgi.ini_tmpl
                   +-- wsgi.py


そういえば今までソースコードを付けてなかった。添付します。


.. _`eggの作り方が分からない`: http://www.freia.jp/taka/blog/655
.. _`buildoutで開発1: WSGIアプリをeggで作る`: http://www.freia.jp/taka/blog/659
.. _`buildoutで開発2: buildoutで環境を整える`: http://www.freia.jp/taka/blog/660
.. _`buildoutで開発4: mod_wsgiからegg指定でアプリ起動する`: http://www.freia.jp/taka/blog/666
.. _`前回(buildoutで開発4)`: http://www.freia.jp/taka/blog/666

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
.. _`Building and Distributing Packages with setuptools`: http://peak.telecommunity.com/DevCenter/setuptools
.. _`Paste Script: Development &mdash; Paste Script v1.7 documentation`: http://pythonpaste.org/script/developer.html#templates

.. _`how to run your own private PyPI (Cheeseshop) server << Fetchez le Python`: http://tarekziade.wordpress.com/2008/03/20/how-to-run-your-own-private-pypi-cheeseshop-server/
.. _`EggBasket`: http://www.chrisarndt.de/projects/eggbasket/


.. :extend type: text/html
.. :extend:


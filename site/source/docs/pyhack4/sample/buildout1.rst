buildoutで開発1: WSGIアプリをeggで作る
=======================================

`eggの作り方が分からない`_ のエントリで書いたように、egg対応アプリの作成手順についてまとまった情報が見つからなかったので、自分でやってみた手順をメモしていきます。
egg recipeの作り方 で検索しても、ハムエッグの調理法ばっかりひっかかる。

まずはegg対応のパッケージを作ってみる。せっかくなので、中身を超簡単なWSGIアプリにしてPasterで起動できるようにしてみる。
下準備として、virtualenvで独立した環境を用意。virtualenvはeasy_installでインストールしてある前提。

.. code-block:: bash

  > cd c:\\project\\buildout
  > virtualenv env1
  > cd env1
  > Scripts/activate
  > easy_install pastescript

これでpasterコマンドでスケルトンを作ったり色々できるようになったので、どんなテンプレートがあるのかを眺めつつ、スケルトンを作成。

.. topic:: eggパッケージのスケルトンを作る
  :class: dos

  | > paster create --list-templates
  | Available templates:
  |   basic_package:  A basic setuptools-enabled package
  |   paste_deploy:   A web application deployed through paste.deploy
  | > paster create -t basic_package wsgiapp
  | Selected and implied templates:
  |   pastescript#basic_package  A basic setuptools-enabled package
  | 
  | Variables:
  |   egg:      wsgiapp
  |   package:  wsgiapp
  |   project:  wsgiapp
  | Enter version (Version (like 0.1)) ['']: 0.1
  | Enter description (One-line description of the package) ['']: wsgi test application
  | Enter long_description (Multi-line description (in reST)) ['']:
  | Enter keywords (Space-separated keywords/tags) ['']: wsgi
  | Enter author (Author name) ['']: foo
  | Enter author_email (Author email) ['']: foo@example.com
  | Enter url (URL of homepage) ['']: www.example.com
  | Enter license_name (License name) ['']: ZPL
  | Enter zip_safe (True/False: if the package can be distributed as a .zip file) [False]:
  | Creating template basic_package
  | Creating directory .\\wsgiapp
  |   Recursing into +package+
  |     Creating .\\wsgiapp\\wsgiapp/
  |     Copying __init__.py to .\\wsgiapp\\wsgiapp\\__init__.py
  |   Copying setup.cfg to .\\wsgiapp\\setup.cfg
  |   Copying setup.py_tmpl to .\\wsgiapp\\setup.py
  | Running c:\\Project\\buildout\\env1\\Scripts\\python.exe setup.py egg_info

項目の内容は適当に入れたけど、将来的にpypiに登録するつもりならちゃんと入れたいところ。
コマンド一発でpypiに登録できるらしいけど、上記のような適当な内容で登録しちゃわないように気をつけること＞俺。

次に、pasterでWeb起動できるようにエントリポイントを登録する。使えるエントリポイント一覧は ``paster points --list`` で表示出来るっぽい。

.. topic:: エントリポイント一覧
  :class: dos

  | > paster points --list
  | 14 entry point groups found:
  | ...
  | [paste.app_factory]
  |   This gives a factory/function that can create WSGI apps
  | ...


wsgi.ini, startup.py を作成して、setup.pyにエントリポイントとして登録する。この3つの更新と各種の名前（モジュール名・関数名等）が関連しあっているようだ。エントリポイントについてはまだちゃんと理解しきれていないのであとでもうちょっと調べる。

wsgi.ini::

  [app:main]
  use = egg:wsgiapp

wsgiapp/startup.py:

.. code-block:: Python

    # -*- coding: utf-8 -*-
  
    def application(environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return ["It's Python!\\n"]
  
    def application_factory(global_conf):
        return application

setup.py (変更点のみ):

.. code-block:: Python

    entry_points="""
    [paste.app_factory]
    main = wsgiapp.startup:application_factory
    """,
  
setup.py を変更したので、eggとしての情報を更新するために ``python setup.py develop`` する。これで \*.egg-info が更新される。
ところで、この \*.egg-info はソースコード管理に入れない方が良いんだと思うけど、どうなんだろうか？


.. topic:: setup.pyの更新をeggに反映する
  :class: dos

  | > python setup.py develop
  | running develop
  | running egg_info
  | writing wsgiapp.egg-info\\PKG-INFO
  | writing top-level names to wsgiapp.egg-info\\top_level.txt
  | writing dependency_links to wsgiapp.egg-info\\dependency_links.txt
  | writing entry points to wsgiapp.egg-info\\entry_points.txt
  | reading manifest file 'wsgiapp.egg-info\\SOURCES.txt'
  | writing manifest file 'wsgiapp.egg-info\\SOURCES.txt'
  | running build_ext
  | Creating c:\\project\\buildout\\env1\\lib\\site-packages\\wsgiapp.egg-link (link to .)
  | 
  | Adding wsgiapp 0.1dev to easy-install.pth file
  | 
  | Installed c:\\project\\buildout\\env1\\wsgiapp
  | Processing dependencies for wsgiapp==0.1dev
  | Finished processing dependencies for wsgiapp==0.1dev


これでpasterから実行出来るようになった。
作ったアプリにrequestを投げてみる。

.. topic:: PasterでWSGIアプリにRequestを送る
  :class: dos

  | > paster request wsgi.ini /
  | It's Python!


It's Work!

アプリに渡ってきている環境変数とかを表示するように、改造してみる。

wsgiapp/startup.py:

.. code-block:: Python

    # -*- coding: utf-8 -*-
    from StringIO import StringIO
    from pprint import pprint

    def application(environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        buf = StringIO()
        pprint(environ, buf)
        return ["It's Python!\\n" + buf.getvalue()]

    def application_factory(global_conf):
        return application


今回はsetup.pyを(egg的な情報を)変更していないので、setup.py develop はしなくてもOK。
さっそくRequestにQueryを付けて投げてみる。

.. topic:: RequestにQueryを付ける
  :class: dos

  | > paster request wsgi.ini /url/here key=value key2=value2
  | It's Python!
  | {'CONTENT_TYPE': 'text/plain',
  |  'HTTP_ACCEPT': 'text/plain;q=1.0, */*;q=0.1',
  |  'HTTP_HOST': 'localhost',
  |  'PATH_INFO': '/url/here',
  |  'QUERY_STRING': 'key=value&key2=value2',
  |  'REQUEST_METHOD': 'GET',
  |  'SCRIPT_NAME': '',
  |  'SERVER_NAME': 'localhost',
  |  'SERVER_PORT': '80',
  |  'SERVER_PROTOCOL': 'HTTP/1.0',
  |  'paste.command_request': True,
  |  'wsgi.errors': <open file '<stderr>', mode 'w' at 0x0181E0B0>,
  |  'wsgi.input': <cStringIO.StringI object at 0x0181A698>,
  |  'wsgi.multiprocess': False,
  |  'wsgi.multithread': False,
  |  'wsgi.run_once': True,
  |  'wsgi.url_scheme': 'http',
  |  'wsgi.version': (1, 0)}


ちゃんと受け取れているっぽい。

ちょっといじれば、Webサーバーとして起動して、ブラウザでアクセスすることも出来るよ！

wsgi.ini::

  [app:main]
  use = egg:wsgiapp
  
  [server:main]
  use = egg:Paste#http
  host = 127.0.0.1
  port = 8080


.. topic:: サーバーとして起動する
  :class: dos

  | > paster serve wsgi.ini
  | Starting server in PID 3976.
  | serving on http://127.0.0.1:8080

これで、ブラウザで http://localhost:8080/hoge?foo=bar&baz=2 にアクセスすると以下のように表示される::

  It's Python!
  {'CONTENT_LENGTH': '0',
   'CONTENT_TYPE': '',
   'HTTP_ACCEPT': 'application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
   'HTTP_ACCEPT_CHARSET': 'Shift_JIS,utf-8;q=0.7,*;q=0.3',
   'HTTP_ACCEPT_ENCODING': 'gzip,deflate,bzip2,sdch',
   'HTTP_ACCEPT_LANGUAGE': 'ja,en-US;q=0.8,en;q=0.6',
   'HTTP_CONNECTION': 'keep-alive',
   'HTTP_HOST': 'localhost:8080',
   'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.33 Safari/530.5',
   'PATH_INFO': '/hoge'
   'QUERY_STRING': 'foo=bar&baz=2',,
   'REMOTE_ADDR': '127.0.0.1',
   'REQUEST_METHOD': 'GET',
   'SCRIPT_NAME': '',
   'SERVER_NAME': '127.0.0.1',
   'SERVER_PORT': '8080',
   'SERVER_PROTOCOL': 'HTTP/1.1',
   'paste.httpserver.thread_pool': <paste.httpserver.ThreadPool object at 0x01889F90>,
   'wsgi.errors': <open file '<stderr>', mode 'w' at 0x012EE0B0>,
   'wsgi.input': <socket._fileobject object at 0x019E80A0 length=0>,
   'wsgi.multiprocess': False,
   'wsgi.multithread': True,
   'wsgi.run_once': False,
   'wsgi.url_scheme': 'http',
   'wsgi.version': (1, 0)}

最後にApacheにmod_wsgiを設定して表示する。 `mod_wsgiはGoogleCode`_ から取得。自分の環境はWindowsなので自前でビルドしました。

httpd-wsgi.conf::

  LoadModule wsgi_module modules/mod_wsgi.so
  WSGIPythonPath c:/project/buildout/env1/lib
  WSGIPythonEggs c:/project/buildout/env1/wsgiapp
  WSGIScriptAlias /test c:/project/buildout/env1/wsgiapp/wsgiapp/startup.py

  <Directory c:/project/buildout/env1/wsgiapp/wsgiapp/>
      Order allow,deny
      Allow from all
  </Directory>


これでとりあえず http://localhost/test にブラウザでアクセスすると表示出来た！
けど、mod_wsgiとの繋ぎ込み部分(startup.py直接指定)が納得いかない。納得いかないけど、とりあえず放置。

最後に、egg化する。

.. topic:: サーバーとして起動する
  :class: dos

  | > python setup.py bdist_egg
  | running bdist_egg
  | ...
  | creating 'dist\wsgiapp-0.1dev-py2.4.egg' and adding 'build\bdist.win32\egg' to it
  | removing 'build\bdist.win32\egg' (and everything under it)

ということで、wsgiapp-0.1dev-py2.4.egg が作れました。今日はここまで。

次はこのeggを使ってApacheと繋げられるようになれば良いのかな。


.. _`eggの作り方が分からない`: http://www.freia.jp/taka/blog/655

.. _`zc.buildoutを使ったプロジェクト管理`: http://nagosui.org/Nagosui/Docs/tutorial/managing-projects-with-zcbuildout/tutorial-all-pages
.. _`Managing projects with Buildout`: http://plone.org/documentation/tutorial/buildout/tutorial-all-pages
.. _`Using z3c packages,...`: http://www.ibiblio.org/paulcarduner/z3ctutorial/introduction.html
.. _`Zope 3の入門にはz3cのチュートリアルがおすすめ`: http://blog.livedoor.jp/matssaku/archives/50500810.html

.. _`http://svn.zope.org/repos/main/`: http://svn.zope.org/repos/main/
.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
.. _`zc.recipe.egg`: http://pypi.python.org/pypi/zc.recipe.egg
.. _`z3c.recipe.egg`: http://pypi.python.org/pypi/z3c.recipe.egg
.. _`Zope 3 Package Guide`: http://wiki.zope.org/zope3/Zope3PackageGuide
.. _`mr.developer`: http://pypi.python.org/pypi/mr.developer
.. _`mod_wsgiはGoogleCode`: http://code.google.com/p/modwsgi/


Google App Engine の開発をbuildoutで行う
=========================================

buildoutのrecipeにはGoogleAppEngineの開発用もあります。
ここではその環境をつくる方法を紹介します。

VirtualEnvでGoogleAppEngineの開発をするのは出来ないらしいと聞いたのですが、
だれか成功している人は shimizukawa at gmail.com までご連絡下さい。

とりあえずbuildout.cfg
-----------------------
Python本体にzc.buildoutがインストールしてあれば、とりあえずbuildout.cfg
だけあれば環境は構築出来ます。これがbuildoutの強みですね。

ということで、以下の内容をbuildout.cfgとしてどこなの空フォルダに作成
してください。

.. code-block:: ini

   [buildout]
   parts = prepare debug app_lib gae_sdk gae_tools

   [prepare]
   recipe = iw.recipe.cmd:py
   on_install = true
   cmds =
      >>> buildout_dir = buildout.get('directory', '.')
      >>> path = os.path.join(buildout_dir, 'app')
      >>> if not os.path.exists(path):
      ...     os.makedirs(os.path.join(buildout_dir, 'app'))
      ...     open(os.path.join(path, 'app.yaml'), 'at').close()
      ...     open(os.path.join(path, 'main.py'), 'at').write(
      ...     """import sys; sys.path.insert(0, './distlib.zip')""")

   [debug]
   recipe = zc.recipe.egg:script
   eggs = ${app_lib:eggs}
   extra-paths =
       ${gae_tools:extra-paths}
       ${gae_tools:sdk-directory}
   interpreter = py
   
   [app_lib]
   recipe = appfy.recipe.gae:app_lib
   lib-directory = app/distlib
   use-zipimport = true
   
   eggs =
       jinja2
       feedparser
   
   ignore-globs =
       *.c
       *.pyc
       *.pyo
       */test
       */tests
       */testsuite
       */django
       */sqlalchemy
   
   ignore-packages =
       distribute
       setuptools
       easy_install
       site
       pkg_resources
   
   
   [gae_sdk]
   recipe = appfy.recipe.gae:sdk
   url = http://googleappengine.googlecode.com/files/google_appengine_1.3.5.zip
   destination = ${buildout:parts-directory}
   hash-name = false
   clear-destination = true
   
   
   [gae_tools]
   recipe = appfy.recipe.gae:tools
   sdk-directory = ${gae_sdk:destination}/google_appengine
   
   extra-paths =
       app/lib
       app/distlib

.. ** vim文字化け回避

保存したらいつも通り以下のコマンドで環境を構築します::

   $ python /tmp/bootstrap.py
   $ bin/buildout

はい、完了。

GoogleAppEngineのパッケージも自動的に最新を取ってきますし、他のPython
環境に影響することもありません。このプロジェクトではeggsにjinja2と
feedparserを同梱していますが、このライブラリはzip圧縮して一緒に
GAEにアップロードされるようにしています。サードパーティーパッケージ
を使うのも気軽にいけますね。

一応、空のapp.yamlとpath調整するだけのmain.pyを作るように仕掛けていますが、
中身は空です。中身は各自で用意して下さい。


サーバーを起動してappspotにアップロード
----------------------------------------

あとは開発して、動作確認して、サイトにアップロードするわけですが、それぞれ
以下のように行うことが出来ます。

サーバー起動::

   $ bin/dev_appserver app

アップロード::

   $ bin/appcfg update app


非常に楽ちんですね。


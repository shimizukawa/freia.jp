WSGIアプリをPasteで組み合わせるなど
====================================

シンプルなWSGIアプリを用意
---------------------------
まずは環境構築のために以下を実行します。

.. code-block:: bash

    $ python bootstrap.py -d init
    $ bin/buildout

bucho_ 0.0.5 からwsgiアプリケーション機能を提供しているので、これを使って
WSGIアプリを起動します。

.. _bucho: http://pypi.python.org/pypi/bucho

buildout.cfg:

.. literalinclude:: code/paste-wsgi/buildout_step1.cfg
    :language: ini

bin/buildout を実行してbucho環境を構築します。

.. code-block:: bash

    $ bin/buildout

Pythonインタプリタを起動して、以下のようにして実際にサーバー起動させます
(以下のコードはPython-2.5以降で動作します)。

.. code-block:: python

    $ bin/py

    >>> from wsgiref.simple_server import make_server
    >>> from bucho.wsgi import wsgi_app
    >>> make_server('', 8000, wsgi_app).serve_forever()

これで http://localhost:8000/ にアクセスすると、シンプルなテキストでbucho wsgiアプリが提供している機能が表示されます。bucho-0.0.5では以下のように表示されます::

    bucho provide below urls:
     * /show
     * /latest_status
     * /all_status
     * /torumemo

bucho wsgiアプリが提供するURLが表示されますが、テキストなのでリンクされていません。手でURLを書き換えてアクセスするとそれぞれのページを確認することが出来ます。とりあえずbuildout paste wsgiの説明としてはトップページが表示されれば十分ですね。

`bucho.wsgi.wsgi_app` がどのような作りなのかはコードを見てください。また、Pythonのドキュメントにも有用な情報が多く掲載されています。Python-2.5から導入された wsgiref パッケージのドキュメントを参照してください。


paster から起動する
--------------------

wsgiアプリを起動するために、前述のような `wsgiref.simple_server.make_server` を使った簡単なプログラムを書いても良いのですが、そのあたりもコードを書かずに手軽に動かしたいところです。そこで、PasteDeployを使用してwsgiサーバーを起動してみます(bin/pasterコマンド生成のためPasteScriptも必要)。

buildout.cfg:

.. literalinclude:: code/paste-wsgi/buildout_step2.cfg
    :language: ini


そして環境更新のために以下を実行します。

.. code-block:: bash

    $ bin/buildout

これで bin/paster が作成されました。

bin/paster でwsgiアプリを起動するためには、設定ファイルでどのようなアプリ構成で動かすのかを指定する必要があります。とりあえず動かすために以下のようにiniファイルを作成してください。

app.ini:

.. literalinclude:: code/paste-wsgi/app_step2.ini
    :language: ini

.. todo:: app.ini の内容を簡単に説明する

あとはサーバー起動するだけです。

.. code-block:: bash

    $ bin/paster serve app.ini
    Starting server in PID 6536.
    serving on 0.0.0.0:8080 view at http://127.0.0.1:8080

最初と同じように、 http://localhost:8000/ にアクセスすると、buchoが表示されますね。

paster の引数を設定済みの起動コマンドを作る
--------------------------------------------

.. todo:: 説明を書く


app.ini をbuildoutの設定から半自動生成する
-------------------------------------------

.. todo:: 説明を書く


apacheから接続するためのスクリプトを用意する
-----------------------------------------------
.. todo:: 説明を書く


apacheから接続するためのテンプレートを用意する
-----------------------------------------------
.. todo:: 説明を書く


まとめ
-------

最終的に以下のようになりました。

.. todo:: もうちょっと説明を書く


buildout.cfg:

.. literalinclude:: code/paste-wsgi/buildout.cfg
    :language: ini

実行すると以下のようになります:

.. code-block:: bash

    $ touch versions.cfg
    $ bin/buildout

サーバー起動

.. code-block:: bash

    $ bin/server
    Starting server in PID 6536.
    serving on 0.0.0.0:8080 view at http://127.0.0.1:8080

cat versions.cfg

.. code-block:: ini

    [versions]
    collective.recipe.modwsgi = 1.2
    collective.recipe.template = 1.8
    distribute = 0.6.14
    paste = 1.7.5.1
    pastedeploy = 1.3.4
    pastescript = 1.7.3
    pygments = 1.4
    tempita = 0.5dev
    weberror = 0.10.3
    webob = 1.0.3
    z3c.recipe.scripts = 1.0.1
    zc.recipe.egg = 1.3.2

$ cat etc/apache-vhost.conf

.. code-block:: html

    <Directory c:\Project\freia\buildout\source\code\paste-wsgi/parts/wsgiapp>
        Order deny,allow
        Allow from all
    </Directory>

    <VirtualHost *:80>
        ServerName www.example.com
        CustomLog /var/log/httpd/www.example.com-access.log combined
        ErrorLog /var/log/httpd/www.example.com-error.log

        WSGIDaemonProcess www.example.com processes=2 threads=2 maximum-requests=10000 user=www group=www
        WSGIScriptAlias / c:\Project\freia\buildout\source\code\paste-wsgi/parts/wsgiapp/wsgi
        WSGIProcessGroup www.example.com
        WSGIPassAuthorization On
    </VirtualHost>


.. **

cat etc/app.ini

.. code-block:: ini

    [DEFAULT]
    debug = true

    [server:main]
    use = egg:Paste#http
    host = 0.0.0.0
    port = 8080

    [composite:main]
    use = egg:Paste#urlmap
    /static = static
    / = bucho-pipeline


    [app:static]
    use = egg:Paste#static
    document_root = c:\Project\freia\buildout\source\code\paste-wsgi/static


    [pipeline:bucho-pipeline]
    pipeline = egg:WebError#evalerror
               bucho-main

    [app:bucho-main]
    use = egg:bucho#main


    ;#####################################
    ; logger setting for mod_wsgi app

    [loggers]
    keys=root

    [handlers]
    keys=hand01

    [formatters]
    keys=form01

    [logger_root]
    level=INFO
    handlers=hand01

    [handler_hand01]
    class=FileHandler
    level=INFO
    formatter=form01
    args=('python.log', 'w')

    [formatter_form01]
    format=F1 %(asctime)s %(levelname)s %(message)s
    datefmt=
    class=logging.Formatter


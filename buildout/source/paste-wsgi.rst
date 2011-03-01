WSGIアプリをPasteで組み合わせるなど
====================================

buildout.cfg:

.. literalinclude:: code/paste-wsgi/buildout.cfg
    :language: ini

実行すると以下のようになります:

.. code-block:: bash

    $ python bootstrap.py -d init
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


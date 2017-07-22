:date: 2009-08-08 16:45:24
:categories: ['Event', 'Zope', 'python']
:body type: text/x-rst

================================================================
2009/08/08 buildoutで開発 4: mod_wsgiからegg指定でアプリ起動する
================================================================

`buildoutで開発1: WSGIアプリをeggで作る`_ では、以下のようにwsgiappパッケージの中のstartup.pyを直接指定して起動していましたが、もっと取り回しやすくします。（今回はbuildout出てきません）

httpd-wsgi.conf::

  LoadModule wsgi_module modules/mod_wsgi.so
  WSGIPythonPath c:/project/buildout/env1/lib
  WSGIPythonEggs c:/project/buildout/env1/wsgiapp
  WSGIScriptAlias /test c:/project/buildout/env1/wsgiapp/wsgiapp/startup.py

上記を以下のように書けるようにします（違うのは最後の行だけ）。

httpd-wsgi.conf::

  LoadModule wsgi_module modules/mod_wsgi.so
  WSGIPythonPath c:/project/buildout/env1/lib
  WSGIPythonEggs c:/project/buildout/env1/wsgiapp
  WSGIScriptAlias /test c:/wsgi.py

このwsgi.pyはどこにあってもOK。中身は以下のようにpasteの仕組みを使っています。

wsgi.py:

.. code-block:: python

    import os
    from paste.deploy import loadapp

    ini = os.path.join(os.path.dirname(__file__), 'wsgi.ini')
    application = loadapp('config:%s' % ini)


wsgi.ini はwsgi.pyと同じ所に置いてください。別の所に起きたければini変数においたパスを入れてください。
こう書くことで、実際にapplicationに格納される関数は、wsgi.iniの[server:main]に記載されているものになるので、このラッパー(wsgi.py)があればpasterで起動するときもmod_wsgiで動かすときも、同じエントリーポイントが使用されます。

これで、pasterコマンドでテストしてるときと、mod_wsgiから呼び出されるときとでほぼ同じ挙動になるはず。あと、wsgiappがegg化されていて、eggファイル名にバージョン番号やpy24とかpy25とか付いていても大丈夫。


mod_wsgiで使えるディレクティブは
`ConfigurationDirectives - modwsgi - The mod_wsgi configuration directives. - Project Hosting on Google Code`_
を参照して設定する。


ということで改めて新しい環境にインストールから。
-------------------------------------------------

.. topic:: virtualenv & install
  :class: dos

  | > cd c:/project/buildout
  | > virtualenv env3
  | > cd env3
  | > bin/activate
  | > easy_install http://localhost:8080/repos/wsgiapp/trunk
  | > easy_install PasteDeploy


iniとpyファイルをenv3ディレクトリ直下に作る.

wsgi.ini::

  [app:main]
  use = egg:wsgiapp
  
  [server:main]
  use = egg:Paste#http
  host = 127.0.0.1
  port = 8180


wsgi.py:

.. code-block:: python

    import os
    from paste.deploy import loadapp

    ini = os.path.join(os.path.dirname(__file__), 'wsgi.ini')
    application = loadapp('config:%s' % ini)


httpd-wsgi.conf(env1->env3 に注意)::

    LoadModule wsgi_module modules/mod_wsgi.so
    WSGIPythonPath c:/project/buildout/env3/lib;c:/project/buildout/env3/lib/site-packages
    WSGIScriptAlias /test c:/project/buildout/env3/wsgi.py

    <Directory c:/project/buildout/env3/>
        Order allow,deny
        Allow from all
    </Directory>


動いた！
動いたけど、WSGIPythonPathの指定にsite-packagesも指定するなんて事かかずに、
WSGIPythonHomeを定義したい。
でもWindowsのmod_wsgiではWSGIPythonHomeを指定するとApacheが「そんなディレクティブないよ」とエラーになる！なんで？

とりあえずLinuxの人はWSGIPythonHomeを使いましょう。

なお、mod_wsgiで使えるディレクティブは
`ConfigurationDirectives - modwsgi - The mod_wsgi configuration directives. - Project Hosting on Google Code`_
を参照して設定する。


次は
-------

* easy_install PasteDeploy せずにwsgiappインストールだけですむようにする
* wsgi.ini と wsgi.py が自動的に作られるようにする（ドコに？）


.. _`ConfigurationDirectives - modwsgi - The mod_wsgi configuration directives. - Project Hosting on Google Code`: http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives#WSGIScriptReloading

.. _`buildoutで開発1: WSGIアプリをeggで作る`: http://www.freia.jp/taka/blog/659


.. :extend type: text/html
.. :extend:


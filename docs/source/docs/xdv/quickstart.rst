=====================
XDV クイックスタート
=====================

このクイックスタートでは、あるサイトの見た目を変化させて表示するHTTPサーバーを用意します。これで、xdvのルール設定をしながら画面がどう変わるかを確認することが出来るようになります。この目的のため、以下のパッケージを利用しています。

:xdv: ルールコンパイラ
:dv.xdvserver: WSGIフィルタ
:Paster: WSGIサーバー, Proxy


インストール: buildoutの場合
-----------------------------

zc.buildoutを利用すれば、OS上の/usr/lib/pythonなどにあるsite-packagesにインストールせずに色々なpythonライブラリを利用した環境を構築する事が出来ます。詳しくは....を参照してください。

buildout環境
~~~~~~~~~~~~~
まずはbuildout環境を初期化します。

.. code-block:: bash

    $ mkdir /tmp/xdvenv
    $ cd /tmp/xdvenv
    $ wget http://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/bootstrap.py
    $ python bootstrap.py init

buildout.cfg
~~~~~~~~~~~~~
つぎにbuildout.cfgが生成されているので、このファイルを以下の内容で記載します。

.. code-block:: ini

    [buildout]
    parts = xdv
    
    [xdv]
    recipe = zc.recipe.egg
    eggs =
    	xdv
    	dv.xdvserver
    	PasteDeploy
    interpreter = py

bin/buildout
~~~~~~~~~~~~~
以下のコマンドを実行して環境を構築して下さい。

.. code-block:: bash

    $ bin/buildout

これで環境構築は完了です。


dv.xdvserver-1.0b7 へのpatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dv.xdvserver-1.0b7には日本語関連のバグがあるので、ちょっとパッチあてます。なお、これはxdvのバグではなくWSGI層のバグなので、Ploneで使われているcollective.xdvなどを使っている場合は、問題無いはずです。

.. code-block:: diff

    --- C:/Project/buildout-eggs/dv.xdvserver-1.0b7-py2.6.egg/dv/xdvserver/filter.py.orig	Sat Aug 21 17:05:44 2010
    +++ C:/Project/buildout-eggs/dv.xdvserver-1.0b7-py2.6.egg/dv/xdvserver/filter.py	Sat Aug 21 17:57:38 2010
    @@ -66,10 +66,9 @@
         
         def apply_transform(self, environ, body):
             
    +        body = body.decode('utf-8') # add this line
             content = etree.fromstring(body, parser=etree.HTMLParser())
             transformed = self.transform(content)
    -        return etree.tostring(transformed)
    +        return etree.tostring(transformed, encoding='utf-8') # add encoding
         
         def __call__(self, environ, start_response):
         

設定ファイルの作成
-------------------

wsgi.ini
~~~~~~~~~
動作確認用に設定ファイルを書きます。buildout.cfg等と同じディレクトリにwsgi.iniを作成して以下の内容を記載します。bin/pasterコマンド(PasteDeployのスクリプト)にこのファイルを渡すとWSGIアプリケーションを動的に作成してくれます。

.. code-block:: ini

    [server:main]
    use = egg:Paste#http
    host = 0.0.0.0
    port = 8000
    
    [composite:main]
    use = egg:Paste#urlmap
    /static = static
    / = default
    
    [app:static]
    use = egg:Paste#static
    document_root = %(here)s/static
    
    [pipeline:default]
    pipeline = egg:Paste#cgitb
               egg:Paste#httpexceptions
               xdv.theme
               proxy
    
    [filter:xdv.theme]
    use = egg:dv.xdvserver#xdv
    theme = %(here)s/static/theme.html
    rules = %(here)s/static/rule.xml
    live = true
    
    [app:proxy]
    use = egg:Paste#proxy
    address = http://www.ruby-lang.org/

上記の例では最後の行でRubyの公式サイトを表示するようにしています。

最後に、上記設定ファイルで指定しているディレクトリやファイルを用意します。まずstaticディレクトリを作成して、その中にそれぞれ以下の内容でtheme.htmlとrule.xmlを置いて下さい。

theme.html
~~~~~~~~~~~
このファイルでこれから作成するサイトのデザインを定義します。このHTMLファイルに、動的に内容を埋め込んでいくルールを、次に説明するrule.xmlで指定します。

.. code-block:: html

    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>XDVの練習中です</title>
        </head>
        <body>
            ほげほげ
        </body>
    </html>


rule.xml
~~~~~~~~~
ルールです。取りあえず空。

.. code-block:: xml

    <rules xmlns="http://namespaces.plone.org/xdv"
           xmlns:css="http://namespaces.plone.org/xdv+css">
    
    </rules>


プログラムの実行とルールのカスタマイズ
---------------------------------------

起動とアクセス
~~~~~~~~~~~~~~~
以下のコマンドで起動して下さい。前述の設定通りであれば8000番ポートで起動します。

.. code-block:: bash

    $ bin/paster wsgi.ini

起動したら http://localhost:8000/ にアクセスして下さい。あ、対象サイトがリダイレクト応答を返してくる場合、今の設定ではリダイレクトしてしまうので、今回のrubyサイトの例では http://localhost:8000/ja/ にアクセスするなどしてください。

ルールのカスタマイズ
~~~~~~~~~~~~~~~~~~~~~

rule.xml を編集しましょう。例えば以下の行を追加します。

.. code-block:: xml

	<append theme="/html/head" content="/html/head/link"/>
	<replace theme="/html/body" content="/html/body"/>

.. todo:: あとで説明を書く

最終的には以下のようになりました。

.. code-block:: xml

    <rules xmlns="http://namespaces.plone.org/xdv"
           xmlns:css="http://namespaces.plone.org/xdv+css">

    <append theme="/html/head" content="/html/head/link"/>
    <replace theme="/html/body" content="/html/body"/>
    <drop css:content="#logo" />

    </rules>



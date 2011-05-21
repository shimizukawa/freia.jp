用語集
======

.. glossary::

    コンテンツ
        変換の対象となるHTMLコンテンツです。HTMLコンテンツはディスク上の
        ファイルや任意のWebサイトの出力から取得することが出来ますが、
        どこから取得するかなどはルール定義やシステム構成によって決まります。

    テーマHTML
        :term:`コンテンツ` と合成するためのHTMLデザインです。
        テーマHTMLはxdvで適用しやすいようなHTML構造とidやclassなどを
        備えていることが望ましいです。そのようになって居ない場合、ルール定義
        が複雑になり、将来的にテーマHTMLやコンテンツの構造が変わった場合に
        変更に弱くなってしまうでしょう。

    ルール定義
        :term:`コンテンツ` と :term:`テーマHTML` を合成するためのルール定義です。
        ルール定義はXMLによって記述されます。

    xdv
        xdvは :term:`Deliverance` を元に独自進化したツールです。
        独自進化の過程でDeliveranceが持っていたいくつかの機能が使えなくなる
        代わりに、より多くの機能、利便性、環境非依存な構成を提供するように
        なりました。

        xdvは :term:`テーマHTML` と :term:`ルール定義` をコンテンツ変換のための
        XSLTファイルにコンパイルするコンパイラです。xdvはコンパイルするだけで
        :term:`コンテンツ` の変換などは行わないため、別途コンテンツ変換のための
        仕組みを用いる必要があります。 :term:`dv.xdvserver` や
        :term:`collective.xdv` がこれに相当しますが、これらのPython製ツール
        以外にもApacheの :term:`mod_transform` などのXSLTによるHTML変換を
        扱う仕組みを利用することが出来ます。

    dv.xdvserver
        :term:`xdv` を :term:`WSGI` に組み込むためのミドルウェアです。
        コンテンツ変換の対象となる環境が :term:`WSGI` で構築されている場合や、
        手元で手軽にコンテンツ変換の結果を確認するために利用します。

    collective.xdv
        :term:`xdv` をPloneに組み込むためのプロダクトです。xdvの仕組みで
        Ploneのデザインを変更する事ができるようになります。

    mod_transform
        Apache-2.0以降用の拡張モジュール。 `mod_transform | freshmeat.net
        <http://freshmeat.net/projects/mod_transform/>`_

    Deliverance
        Deliveranceはxdvの元となったツールですが2010年以降のxdvの進化速度
        ほどの機能向上は行われていないようです。

        Deliveranceは現在も開発が続けられていますが、2010年8月時点の
        Deliverance-0.3で見る限り、積極的にDeliveranceを利用する必要は
        無いように思います。

    WSGI
        WSGIは、PythonにおけるWebアプリケーションサーバーの共通インターフェース
        です。WSGIが登場する以前はほとんどのWebアプリケーションサーバーが独自
        の実装をしていましたが、WSGIという共通規格が出来たおかげで、どんな
        Webアプリケーションも共通の仕組みで動作する事が出来るようになりました。
        PerlのPSGI, RubyのRackとおなじ概念のものです。

    paster
        pasterはPasteScriptというPythonパッケージで提供されるコマンドです。
        いくつかの便利な機能を提供していますが、そのなかの一つに :term:`WSGI`
        のサーバーとして動作する機能があります。dv.xdvserverを用いる場合に
        利用することになるでしょう。

    Sphinx
        Python製ドキュメンテーションビルダーです。
        reStructuredTextという文法で書かれたテキスト形式のドキュメントを
        HTML, PDF, ePub などに変換します。
        このドキュメントもSphinxを用いて作成しています。詳しくは
        `Sphinx-Users.jp <http://sphinx-users.jp/>`_


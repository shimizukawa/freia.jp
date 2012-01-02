:date: 2009-10-01 01:45:54
:categories: ['Zope', 'python', 'Plone']
:body type: text/x-rst

==========================================================
2009/10/01 Plone-3.3.1をWSGIで稼働させるための設定テンプレ
==========================================================

Zope3はTwisted,WSGI,など複数の稼働方法を提供していますが、Zope2では基本的にZServerでの起動しかありません。以前はFastCGIでの起動も提供されていましたが現在はサポート外です。しかし Repoze_ 開発チームが提供しているパッケージを使用すればZope2をWSGI起動させることが出来ます（標準外なので自己責任になりますが）。まあZope/Ploneは起動が遅いので初回アクセス時に重いのをナントカするとか、色々新しいノウハウが必要になるわけですが、WSGIのmiddlewareを使えるようになるというメリットもあります。

Apache/mod_wsgiの下にどのような構成でZopeに繋がるのか、という話は Repoze の `Developing and Deploying`_ ページに構成図付きで詳しく載っているのでそちらを参照してください。

buildoutで環境構築
--------------------

で、plone3-wsgi環境を作るためのbuildout.cfgを書いたんですが、どうせならpasterでテンプレート生成できると便利だよね、っていうことで作ってみました。以下のコマンドで環境を構築出来ます（easy_installしたくない人はvirtualenvしてください）。あ、Pythonは2.4です。

.. topic:: Zope2-WSGI 構築手順
  :class: dos

  | > easy_install elementtree
  | > easy_install http://svn.freia.jp/open/ZopeWsgiSkel
  | > paster create -t plone3_wsgi plone3
  |
  | (色々聞かれます. ドメインを plone3.freia.jp にしてみます)
  |
  | > cd plone3
  | > python bootstrap.py
  | > bin/buildout -c buildout-devel.cfg

これで開発用の環境が出来ました。ploneのインスタンスもZope内に自動生成しています。ドメイン名は当たり前ですが、DNS設定するなりhosts設定するなりが必要です。

ということで、bin/pasterで起動してみます。ここでbinを付け忘れると ``repoze.obob.publisherが見つからない`` 的なエラーになりますので注意してください。

.. topic:: Zope2-WSGI 開発環境起動
  :class: dos

  | > bin/paster serve etc/development.ini
  | Starting server in PID 35616.
  | 2009-09-30 23:51:11 INFO paste.httpserver.ThreadPool Cannot use kill_thread_limit as ctypes/killthread is not available
  | serving on 0.0.0.0:8080 view at http://127.0.0.1:8080


起動しました（本当はもうちょっとwarningが出ます）。標準では8080ポートで開発環境は起動します。本番はWSGIなのでZope自体はportを使用しません（代わりにZEOが別のportで起動します）。8080ポートにブラウザでアクセスしてみて、正しく表示されれば成功です。
なお、etcディレクトリにapache用の設定ファイル plone3.freia.jp.conf も生成されているので、このファイルをconf.d等に置けばドメイン名でアクセスすることも出来ます。


本番環境作成
----------------

次に本番用の環境を生成します。今のbuildout設定では開発用と本番用を両立できないので、改良の余地があります。普通は両立要らないと思いますが。

.. topic:: Zope2-WSGI 本番環境構築手順
  :class: dos

  | > bin/buildout -c buildout-production.cfg

これで本番用のWSGI環境が出来ました。本番環境はコマンドでの起動ではなくApacheのmod_wsgi経由での起動になります。mod_wsgiは使える状態にしておいてください。また、Data.fsに複数のWSGIプロセスからアクセスする事になるので、ZEOサーバーを起動しておく必要があります。

.. topic:: Zope2-WSGI ZEO起動
  :class: dos

  | > bin/zeoserver start
  | . daemon process started, pid=35700

ZEOが起動しました。次にapacheの本番用の設定 etc/plone3.freia.jp.conf をapacheに反映してください。このファイルはbuildoutで本番環境を生成したときに上書きされています。微妙？ conf.dから ln -s しておけば便利かも。

あとはブラウザで設定したドメイン（今回は http://plone3.freia.jp/ ）にアクセスすればPloneサイトが表示されるはずです。


参考文献
-----------

今回のbuildout設定などは、かなりの部分を Repoze_ と、そこからリンクされていた `Revotera Voja?o: Repoze, Zope, Plone, URISpace, and Deliverance`_ の記事を参考に作成しました。


.. _Repoze: http://repoze.org/
.. _`Developing and Deploying`: http://repoze.org/devdep.html
.. _`Revotera Voja?o: Repoze, Zope, Plone, URISpace, and Deliverance`: http://feneric.blogspot.com/2009/07/repoze-zope-plone-urispace-and.html


.. :extend type: text/html
.. :extend:

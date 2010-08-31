zc.buildout のレシピ・エクステンション例
==========================================

レシピ
--------
:zc.recipe.egg:
   eggインストールの定番。基本です。

:iw.recipe.cmd:
   コマンドライン操作をbuildout.cfgに記載できます。
   bulidoutを実行するだけでetcフォルダを作ったり、など。

:iw.recipe.fetcher:
   指定したURL からファイルをダウンロード。
   iw.recipe.cmdと組み合わせると色々できます。

:appfy.recipe.gae:
   Google App Engine 環境をbuildoutで管理。かなり楽ちん

:pbp.recipe.trac:
   Tracサーバーを立てます。初期設定も一気にやってくれます。

:collective.buildbot:
   buildbot環境を自動生成します。
   recipeが名前に入っていませんが、これもレシピです。

:collective.recipe.hudson:
   Hudsonでテストする人向け。

:gocept.nginx:
   nginxのコンフィギュレーションを行うレシピ。

:plone.recipe.varnish:
   Varnishのコンフィギュレーションを行います。
   Plone用? いいえ！汎用です。

:iw.recipe.pound:
   Pound（ロードバランサー）のコンパイルとインストール

:iw.recipe.squid:
   Squid（キャッシュサーバ）の設定と実行

:z3c.recipe.ldap:
   OpenLDAP のデプロイ

:collective.recipe.ant:
   Ant（Java）プロジェクトをビルド


エクステンション
-----------------

:mr.developer:
   svnやhg,bzrからチェックアウトしたソースコードをシステムに組み込みます。
   開発中の複数のパッケージを編集してコミットするサイクルをbuldout上で
   シームレスに行うことができるようになります。

:gp.vcsdevelop:
   mr.develperよりもシンプルな、同様の機能を提供するレシピです。



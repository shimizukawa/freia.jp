:date: 2005-11-15 00:26:08
:tags: Zope

===========================================
COREBlogのrefererを外部RDBに保存
===========================================

先日気が付いたらData.fsの容量が37GBになってました。合掌‥‥ていうネタを `サーバートラブル`_ で書いたのですが、対策としてZope内臓のRDB, GadflyにCOREBlogRefererPluginのデータを移植してみました。(その途中の成果?が `Python2.3から2.4でmarshal形式データが変更`_ です)

結果、RDBの容量自体は5MBで済んだのですがデータ更新のたびに5MBのmarshal形式データを全部書き出されるので、リファラ付き閲覧者がページ表示するのに4～6秒余計にかかってしまいました。

.. _`サーバートラブル`: http://www.freia.jp/taka/blog/264
.. _`Python2.3から2.4でmarshal形式データが変更`: http://www.freia.jp/taka/blog/266



.. :extend type: text/plain
.. :extend:

で、ここで話は変わって、リファラデータとアクセスログを眺めてて気づいた事が一つ（多分、今更なんだろーな...）

blogにスパムコメント・スパムトラックバックをしてくる誰かがいるんですが、アクセス元は一カ所なのにリファラが毎回違う。そして、検索サイトで、そのリファラのURLをキーに検索してる痕跡がログにありました。そうやってURLの宣伝をしているわけです。あったまくるなあ、もう。

ということで対策はやっぱり、トラックバックの言及チェックとコメント登録時のCAPTCHA入力かなあ。。。



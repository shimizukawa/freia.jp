:date: 2017-06-19 21:30
:categories: ['Sphinx']
:body type: text/x-rst

=============================================
2017/06/19 Sphinx Tea Night 2017.06 #sphinxjp
=============================================

:doc:`前回 <../sphinxjp-tea-night-201704/index>` に引き続き、 `Sphinx Tea Night 2017.06`_ に参加しました（5月は開催されなかったみたい）。

自己紹介
========

* usaturn: 最近転職しました

* 打田: 仕事ではsphinx使ってませんが、個人で使ってます。検索関連で、 `Apache Solr入門`_ 改訂版の執筆をして最近出版されました。

* shimizukawa: 最近執筆1つと飜訳2つを並行でやっていて、すべてSphinxを使ってやってます。仕事では最近Sphinx使ってません。

* 成田: Apple Help でSphinxに興味を持ちました。

* 石井(pashango): Qt使ってツールを書いてます。仕事ではドキュメントをSphinxで書いてます。最近MarkdownからSphinxに変換するツールを作ったので、みんなMarkdownでSphinx使ってます。Sphinx歴は1年くらい。

.. _Apache Solr入門: http://amzn.to/2rvccLB


場所は喫茶室ルノアール　市ヶ谷駅前店、です。


.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash">#sphinxjp</a> Tea Night 2017.06 に参加中～ (@ 喫茶室ルノアール 市ヶ谷駅前店 in 千代田区, 東京都) <a href="https://t.co/gk1n9vrsT4">https://t.co/gk1n9vrsT4</a> <a href="https://t.co/BhFGcU4Ldf">pic.twitter.com/BhFGcU4Ldf</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/876769080115593216">2017年6月19日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


話したこと
===========

pandoc
--------

* 「GFM(GithubのMarkdown)が、CommonMarkの仕様に従う変更をしたため、インデントが4から2になった。でもpandocは「いまさらそんな変更できん」と4インデントを継続中」、とのこと。これでまた新しいフレーバーが生まれたのか。

* 「 http://pandoc.org/ を見ると、変換できるフォーマット多すぎ！すごい、これがあればどんなフォーマットも相互変換が可能に・・・」（なりません）

reStructuredText
-----------------

* Sphinxのために生まれたの? -> No.

  * reSTは :pep:`287` で規定されてます
  * PEPで決まっているので、実装系であるdocutilsが仕様を変更することは出来ません
  * ですが、reST実装系であるdocutilsは仕様を「追加」することは可能かも。
  * roleやdirectiveを全てPEPで決めているわけではないはず

* reStructuredTextはいつ生まれたの？

  * 2002年くらい。 :pep:`287` を見ると2002/3/25に仕様が作られてるっぽい
  * たしかMarkdownは2002年後半だったかな
  * docutilsの実装より前に仕様が決まった？ -> たぶんNo。実装しながら仕様決めたんじゃないかな

電話とる、とらない
--------------------

* `電話に出なくて良い会社 - ビープラウド社長のブログ <http://shacho.beproud.jp/entry/2017/06/15/150726>`__ の話題がでた
* 「会社に電話して担当者につながらないと、お客さんから個人電話番号聞かれませんか？」教えません。または、追加工数もらいたいですねー
* みんな電話でるのいやなんだなー

やったこと
===========

* `Sphinxをはじめよう`_ の改訂作業

  遅れてますが、自分の担当範囲をもくもくと書きました。

.. _Sphinx Tea Night 2017.06: https://sphinxjp.connpass.com/event/58349/
.. _Sphinxをはじめよう: http://www.oreilly.co.jp/books/9784873116488/



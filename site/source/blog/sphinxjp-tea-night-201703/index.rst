:date: 2017-03-09 23:55
:tags: Sphinx
:body type: text/x-rst

=============================================
2017/03/09 Sphinx Tea Night 2017.03 #sphinxjp
=============================================

:doc:`前回 <../sphinxjp-tea-night-201702/index>` に引き続き、 `Sphinx Tea Night 2017.03`_ に参加しました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash">#sphinxjp</a> Tea Night にキター。この会場も今日で最後かー (@ ガスト 市ヶ谷駅前店 in 新宿, 東京都, 東京都) <a href="https://t.co/mezxy9vboX">https://t.co/mezxy9vboX</a> <a href="https://t.co/YzUHgqMrHp">pic.twitter.com/YzUHgqMrHp</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/839794007861571584">2017年3月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

:参加者: @usaturn, empress_012, @tk0miya, @shimizukawa


今回もガストで開催しているけど、いよいよ別のファミレスや喫茶店を探そうという話になりました。良い場所があれば教えてください。ドリンクバーは諦めても良いです。

話したこと.

* 今回初参加の empress_012 さんが、SphinxをPDF化するのに苦労しているという話だったので、 `Sphinxをはじめよう`_ を紹介した。
* 会社のインターネット接続が長時間のコネクションを切ってしまうらしく、TeXLiveのダウンロードが途中で失敗するらしい。つらそう。
* SphinxからPDFを作る手軽な方法は？

  * 簡単なのは ``make singlehtml`` した結果をwordに食わせてPDFで保存（1回限りなら簡単）(tk0miya)
  * 次点で ``make latexpdf`` (要TeXLive)だけど、出来合いのレイアウトをいじろうと思うと修行が必要(tk0miya)

* 章ごとにディレクトリを分けていて、章の中でもファイルを複数に分けているけれど、ビルドしたHTMLは章ごとに1つのHTMLになってほしい、という話。今回は ``make singlehtml`` で妥協。conf.pyのディレクトリ直下に章ディレクトリがあれば、直下より深い階層を1つのhtmlにまとめる ``make dirhtml`` を使う手もあったんだけど、今回は残念ながら複数の部門ディレクトリの下に章ディレクトリがあったので使えず。

やったこと.

* Sphinx Tea Night の場所探し

  * ガストいつも混んでるし、自分が近々引っ越すので、行きやすい場所を探してみた。
  * 新宿、新宿三丁目、市ヶ谷、のあたりがよさそうということになった
  * ためしに次回は、ルノアール市ヶ谷駅前店にしようか、という話を @usaturn としてた

* :doc:`前回 <../sphinxjp-tea-night-201703/index>` に引き続き、 `Sphinxをはじめよう`_ の改訂作業

  今日持って行ったノートPCにはリポジトリをCloneしてなかったので、cloneして環境を作ったところまで。

* SphinxのPRレビュー

  * @tk0miya が日々コミッターをがんばってくれていて、自分があんまり時間を取れてないので、PRレビューをだいぶ積んでしまっている
  * 帰り道でコードとコメントを読んで、3つLGTMを返した


.. _Sphinx Tea Night 2017.03: https://sphinxjp.connpass.com/event/51514/
.. _Sphinxをはじめよう: http://www.oreilly.co.jp/books/9784873116488/


:date: 2017-03-18 23:55
:tags: Sphinx

===================================================================================
2017/03/18 sphinx-extcode を作りました at Sphinx+翻訳 hack-a-thon 2017.03 #sphinxjp
===================================================================================

`Sphinx+翻訳 hack-a-thon 2017.03`_ に参加しました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash">#sphinxjp</a> モクモクhack-a-thonやってます。参加者8名、ここ数年で最多つぽい (@ タイムインターメディア in 新宿区, 東京都) <a href="https://t.co/73ATAAfYTO">https://t.co/73ATAAfYTO</a> <a href="https://t.co/cUEMUalpSb">pic.twitter.com/cUEMUalpSb</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/842977783831838725">2017年3月18日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash">#sphinxjp</a> モクモクhack-a-thonやってます。参加者8名、ここ数年で最多つぽい (@ タイムインターメディア in 新宿区, 東京都) <a href="https://t.co/73ATAAfYTO">https://t.co/73ATAAfYTO</a> <a href="https://t.co/XkkYdSJXEp">pic.twitter.com/XkkYdSJXEp</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/842977786159648768">2017年3月18日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

:参加者: @tk0miya (会長), @jbking (副会長), @yousken900 (副会長), @shimizukawa (会計), @pashango2 @nskgch @usaturn, @kashew_nuts

参加者が8人もいて、ここ数年で最多の参加人数だった気がします。

みんながやったこと
=====================

.. figure:: todo.*
   :width: 500

* @tk0miya: Sphinxのメンテ。画像を各ビルダーで扱えるように変換する仕組みを作っている。あとSphinx用にPythonのパーサーを書いてた
* @jbking: Blogツールのアップデート
* @yousken900: Sphinxの入門をしている。Sphinx-usres.jpの入門記事を読んでいろいろ書いてみた
* @pashango2: Sphinxの新規プロジェクトを始められるGUIツールをQtで作っていた。Sphinxがconf.pyのテンプレートをべた書きで持っていて、外部ツールが再利用するのはつらい。プロジェクトのソースディレクトリもconf.pyになくてMakefileにしかないのでつらい。
* @nskgch: Sphinx-1.6向け翻訳を進めた
* @kashew_nuts: Tinkererをためしてみた(`Sphinx+翻訳 Hack-a-thon 2017.3に参加しました #sphinxjp`_)
* @usaturn: Sphinxのissueをトリアージする
* @shimizukawa: Sphinxの本のリファレンスページを更新している。extcodeという拡張を最新のSphinxで動作するように修正していた

自分がやったこと
==================


`Sphinxをはじめよう`_ の改訂作業をやってました（ :doc:`../sphinx-book-writing-20170316/index` に引き続き）。

この執筆用にsphinx-extcodeという拡張を作りました。

.. figure:: sphinx-extcode.*
   :target: https://shimizukawa.github.io/sphinx-extcode/

   sphinx-extcodeの出力例

いくつかの出力例を https://shimizukawa.github.io/sphinx-extcode/ で見れます。


作った目的
------------

たくさんのサンプルコードをreSTで書いて、その出力結果を並記するというのを繰り返していますが、コードサンプル用とレンダリングイメージ用とで2回書くのが面倒です。
こんな感じです:

.. code-block:: rst

   .. code-block:: rst

      単語を * で囲うと *強調* になります。

      ** は **より強い強調** に使います。

   出力例

      単語を * で囲うと *強調* になります。

      ** は **より強い強調** に使います。


コピペは必ずミスに繋がるので、サンプルを ``sample.txt`` という外部ファイルに書いて以下のようにする方法もあります::

   .. literalinclude:: sample.txt
      :language: rst

   出力例

      .. include:: sample.txt

これはこれで良いのですが、いちいち外部ファイルを用意する必要があります。
これを簡単に済ませようというのがsphinx-extcodeの目的です。
`Sphinxをはじめよう`_ を2013年に執筆したときに作ったんですが、原稿ソースと一緒に埋もれていたので、今回の改訂用にSphinx-1.5で動作するように修正したのが、今日の成果です。

残念ながら、パッケージ公開するほど安定していませんが、使ってみたい人はリポジトリから取得してみてください。
https://github.com/shimizukawa/sphinx-extcode



.. _Sphinx+翻訳 hack-a-thon 2017.03: https://sphinxjp.connpass.com/event/52079/
.. _Sphinxをはじめよう: http://www.oreilly.co.jp/books/9784873116488/
.. _Sphinx+翻訳 Hack-a-thon 2017.3に参加しました #sphinxjp: http://kashewnuts.github.io/2017/03/18/sphinxhackathon201703.html


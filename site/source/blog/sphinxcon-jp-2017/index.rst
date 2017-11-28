:date: 2017-11-28 21:00
:tags: Sphinx, SphinxCon

===========================================================
SphinxCon JP 2017 に参加しました #sphinxjp
===========================================================

SphinxCon JP 2017 に参加しました。

:イベント: `SphinxCon JP 2017`_
:参加者: 38名前後
:会場: DeNA社（渋谷ヒカリエ）
:時間: 19:30 - 22:00

.. _SphinxCon JP 2017: https://sphinxjp.connpass.com/event/71056/

.. figure:: kanpai.*

   DeNAさん提供のケータリングでカンパイ!

.. contents::
   :local:

場つなぎ
==========

- Q1.

  - Q. Sphinxを使ったことのある方
  - A. かなりいますね！

- Q2.

  - Q. ヒカリエに初めて来た方
  - A. けっこう居ますね！

- Q3.

  - Q. 書籍関連の話を聞きたくて来た方
  - A. けっこう居ますね！


1: Sphinxが支える翻訳ドキュメント
=================================

* 発表者: `@cocoatomo`_
* 資料: TBD

.. _@cocoatomo: https://twitter.com/cocoatomo

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">SphinxCon JP 2017 トーク1人目 <a href="https://twitter.com/cocoatomo?ref_src=twsrc%5Etfw">@cocoatomo</a> さん！ <a href="https://twitter.com/hashtag/sphinxjp?src=hash&amp;ref_src=twsrc%5Etfw">#sphinxjp</a> <a href="https://t.co/D0b4mvfZpi">pic.twitter.com/D0b4mvfZpi</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/935459186757877760?ref_src=twsrc%5Etfw">2017年11月28日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


* `Pythonドキュメント`_ の翻訳をしている

  * 23万ワード
  * 本にして 1577 ページ、重量にして5.7kg
  * 原文は日々変わっていく
  * 翻訳は追いかけるのが大変、何人かでがんばっている

* 翻訳プロジェクトを始めるときに考えること

  * 原文と訳文が1対1で、構造が完全に一緒でよければSphinxが使える
  * 脚注訳注を入れたい、構造を変えたい、ならSphinxはあきらめよう
  * 単発型か継続型か。Pythonドキュメントは継続型

* 翻訳を支える機能・サービス

  * VCS (Git): https://github.com/python-doc-ja

  * Sphinx_ の ``make gettext`` コマンド

  * Transifex_ （統合翻訳環境）

  * Transifex CLI: transifex-client_

  * Sphinx-intl_


* Sphinx gettext

  * Sphinxが翻訳対象としている部分は ``make gettext`` でpotファイルを生成できる
  * なぜか翻訳対象になってない部分は、SphinxにPR出して対応してもらう

    * https://github.com/sphinx-doc/sphinx/pulls?q=is%3Apr+author%3Acocoatomo+is%3Aclosed

Q&A
----

* Q: (`@kmuto`_) potのメッセージはドキュメントの順番にならぶの？

  * A: （清水川）並ばないことがあります。同じメッセージが複数回でてくると初回のみカタログに出てくるし、あとで原文が追加されたらpotの末尾に追加されます

  * (kmuto) 前後を読みながら翻訳したいので、原文の通りに並んでてほしいなと思うんですよね

* Q: （鹿野桂一郎）TransifexはSphinx専用ではないですよね？一般的なpotを扱えるサービスですよね

  * A: はい
  * Q: それをSphinxから使いやすいように清水川さんが作ってくれたということですね
  * A: はい


.. _@kmuto: https://twitter.com/kmuto
.. _Pythonドキュメント: https://docs.python.org/ja/3/
.. _Transifex: https://www.transifex.com/
.. _transifex-client: https://pypi.python.org/pypi/transifex-client
.. _sphinx: https://pypi.python.org/pypi/sphinx
.. _sphinx-intl: https://pypi.python.org/pypi/sphinx-intl



2. Sphinxで売り物の書籍を作ってみた
===================================

* 発表者: 鹿野桂一郎(`@golden_lucky`_)
* 資料: TBD

.. _@golden_lucky: https://twitter.com/golden_lucky

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash&amp;ref_src=twsrc%5Etfw">#sphinxjp</a> トーク2人目、 <a href="https://twitter.com/golden_lucky?ref_src=twsrc%5Etfw">@golden_lucky</a> 鹿野さん！ <a href="https://t.co/1alwuI2Kh8">pic.twitter.com/1alwuI2Kh8</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/935468654082244608?ref_src=twsrc%5Etfw">2017年11月28日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


* Goならわかるシステムプログラミング

  * 元はASCIIさんで連載していた
  * 著者はいま目の前でなにかモグモグ食べている `@shibu_jp`_ さん
  * Sphinxで原稿を書いてHTML化していた
  * 書籍化にあたり、Sphinxから出力してなんとかしたい


* SphinxのTeXをハックした

  * 自分のLaTeXテンプレートを使いたい

  * 自作のLaTeXスタイルで見た目を変えたい

  * ブロック要素内の脚注を特別扱いしたくない

  * Sphinxは相互参照をHTMLのノリで作っちゃうのでやめたい

  * LaTeXの表は自動でキレイには組めない

* 自分のLaTeXテンプレートを使いたい

  * Sphinxには ``_template/latex.tex_t`` を置くとテンプレートとして使ってくれる機能がある。やったね！

  * でも目次の位置は固定で変えられない！

  * 独自のdirectiveを作って、コントロールできるようにした

* 自作のLaTeXスタイルで見た目を変えたい

  * Sphinxの ``code-block`` のデザインを変えたい
  * ``customenv`` ディレクティブで指定した環境で包むよにした

* ブロック要素内の脚注を特別扱いしたくない

  * テーブル内に脚注を書くとテーブルの下にしか脚注を出せない
  * Sphinxでもけっこう苦労して対策している跡が見える
  * それでも特定のケースではうまくいかない
  * しょうがないので、通常の脚注にして自分のLaTeXマクロ(?)を使った

* Sphinxは相互参照をHTMLのノリで作っちゃうのでやめたい

  * "第3章" を見てください、のように章番号だけ表示したい
  * ``:numdoc:`` を作った
  * ``:numdoc:`` と ``:doc:`` を並記しないといけないのは微妙だけど、まあしょうがない
  * ページで参照したい。どうしたらいいかな

  * しょうがないので ``:tex:`` ロールを作ってLaTeXを直接書き込んだ


* LaTeXの表は自動でキレイには組めない

  * Sphinxではtabularyパッケージにやらせている

  * しかしLaTeX側に全て自動で良い感じにやらせるのは無理

  * tabularcolumns_ ディレクティブで個別指定できる！！ (by tk0miya)

.. _tabularcolumns: http://www.sphinx-doc.org/ja/stable/markup/misc.html#directive-tabularcolumns

* まとめ

  * 困ったら日本語でツイートすればいい
  * ある程度リッチな紙の本を作るにはSphinxくらい充実してても手をかけないとイケない部分がたくさんある

  * `ラムダノート社`_ がお手伝いするよ

.. _ラムダノート社: https://www.lambdanote.com/


3. Re:VIEWとSphinxと、時々、ボク
================================

* 発表者: `@r_rudi`_
* 資料: TBD

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash&amp;ref_src=twsrc%5Etfw">#sphinxjp</a> 3人目、 <a href="https://twitter.com/r_rudi?ref_src=twsrc%5Etfw">@r_rudi</a> さん！ <a href="https://t.co/xa1y7EZ5IZ">pic.twitter.com/xa1y7EZ5IZ</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/935475025670373376?ref_src=twsrc%5Etfw">2017年11月28日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


.. _@r_rudi: https://twitter.com/r_rudi

* 軽量マークアップの傾向

  * Markdown -> Web

  * Re:VIEW -> 技術書籍

  * reStructuredText -> Web, PDF(not 組版)

* 技術書籍を書きたい、Sphinxで書きたい!

  * `sphinxcontrib-reviewbuilder`_ を作った

  * 作ったのは2,3年前
  * ``pip install sphinxcontrib-reviewbuilder`` して
  * conf.py に書き足して
  * ``make review``
  * できました

* reviewbuilder を使って書かれた本

  * `Sphinxをはじめよう 第2版 <https://www.oreilly.co.jp/books/9784873118192/>`_
  * `仕事ではじめる機械学習 <https://www.oreilly.co.jp/books/9784873118215/>`_
  * `Real World HTTP <https://www.oreilly.co.jp/books/9784873118048/>`_


* Re:VIEWからreSTへ

  * rstbuilderのPRを出して取り込んでもらった

  * https://github.com/kmuto/review/pull/733


* Big Mouth Data

  * 技術書典2で頒布
  * Re:VIEW -> reST -> Re:VIEW
  * 相互変換できるようになってきた

* Re:VIEW と reST

  * Re:VIEW: 組版用コマンドが豊富
  * reST: 汎用的、拡張が容易
  * カバー範囲が異なっている感じ
  * 相互変換できるといってもカバー範囲が違うので、変換を繰り返したら元には戻らない

* まとめ

  * Sphinxは拡張が豊富
  * 設計思想の違いがある。優劣ではない
  * Sphinxは拡張が PyPI_ にたくさんあるので色々さがしてみて
  * 拡張が無ければ自分で書けばいいじゃない！

.. _sphinxcontrib-reviewbuilder: https://pypi.python.org/pypi/sphinxcontrib-reviewbuilder
.. _PyPI: https://pypi.python.org/pypi


4. 社内のマニュアルをSphinxで作ってみた
========================================

* 発表者: Iosif Takakura (`@huideyeren`_)
* 資料: TBD

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash&amp;ref_src=twsrc%5Etfw">#sphinxjp</a> トーク3人目、タカクラさん！ <a href="https://t.co/xQeruanuI8">pic.twitter.com/xQeruanuI8</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/935478912468918272?ref_src=twsrc%5Etfw">2017年11月28日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


.. _@huideyeren: https://twitter.com/huideyeren

5. HTMLテンプレート再構築案
============================

* 発表者: 渋川よしき (`@shibu_jp`_)
* 資料: TBD

.. _@shibu_jp: https://twitter.com/shibu_jp


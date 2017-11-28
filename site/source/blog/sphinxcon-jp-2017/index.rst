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
* 資料: https://www.slideshare.net/k16shikano/sphinx-82905169

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
* 資料: http://tdoc.info/presentations/sphinxcon2017/

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

感想
------

* r_rudi さん、完全にbuilder職人になってる。すごい。
* 発表にはなかったかもだけど、 https://github.com/shirou/sphinxcontrib-indesignbuilder も作ってる

4. 社内のマニュアルをSphinxで作ってみた
========================================

* 発表者: Iosif Takakura (`@huideyeren`_)
* 資料: https://www.slideshare.net/iosiftakakurayusuke/sphinx-82892226

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash&amp;ref_src=twsrc%5Etfw">#sphinxjp</a> トーク4人目、タカクラさん！ <a href="https://t.co/xQeruanuI8">pic.twitter.com/xQeruanuI8</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/935478912468918272?ref_src=twsrc%5Etfw">2017年11月28日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

* 今日はドキュメントの技術的負債の話をします

  * 技術ドキュメントを残していく必要性がでてきた

  * 社内ではExcel方眼紙が跳梁跋扈している！

  * PCへのインストールは制限されている！

  * でもMacは管轄外だったのでSphinxいれちゃった

* ドキュメントのメンテナンスは手間が掛かる

  * reSTやMarkdownは学習コストが掛かる

  * メンバーの作業コストが高くなりドキュメントが放置された

  * この負債を解消するために、ドキュメントが素のHTMLで書き直されつつある

* まとめ

  * 独断でいれたツールはうまくいかないことが多い
  * 理解の難しい技術は、残されたメンバーが扱えなくなる
  * 中心メンバーが抜けた後の運用も考える必要が
  * 運用コストを考えると最終的にExcelが選択されることに..

  * 技術的負債とどう向き合うか

    * 技術レベルに合わない技術は爆死しやすい
    * 枯れすぎた技術を選んでも爆死する
    * 技術の学び方だけでなく、メンバーへの教え方も磨いていく必要がある

  * メンテナンスしやすいドキュメントの作り方

    * 何で作るかにこだわらず、誰でも編集出来ることが大事
    * 必要最低限のドキュメントだけ作る
    * 定期的にメンテナンスする機会を設ける

感想
------

* メンテしやすいの部分、必要最低限、よりは必要十分な方を狙って行きたいね。

.. _@huideyeren: https://twitter.com/huideyeren

5. HTMLテンプレート再構築案
============================

* 発表者: 渋川よしき (`@shibu_jp`_)
* 資料: TBD

.. _@shibu_jp: https://twitter.com/shibu_jp

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash&amp;ref_src=twsrc%5Etfw">#sphinxjp</a> トーク5人目、 <a href="https://twitter.com/shibu_jp?ref_src=twsrc%5Etfw">@shibu_jp</a> ！！ <a href="https://t.co/juAI7QAY7A">pic.twitter.com/juAI7QAY7A</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/935482850748481537?ref_src=twsrc%5Etfw">2017年11月28日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

* DeNA退職時に引き継ぎ資料をSphinxで書いた

  * ``make singlehtml`` で作ってHTMLをブラウザで全コピしてWordに貼ればOK
  * Word上でコードブロックもキレイに維持されて美味しい
  * medium.com の編集画面にも同じように貼れば良い感じになってくれる

* SphinxのHTML5

  * HTML5リリースから9年遅れ
  * Sphinxは docutils_ の上で作られている
  * docutilsのHTML5対応が必要だった

* Sphinx 2.0 に向けて

  * HTMLテンプレートの簡易化: 構造化よりコピーして使いやすい方がいい

  * 検索機能の向上: 検索インデックスの構造を変えて検索しやすく

  * Open Graph Protocol: Sphinxで標準対応したい

  * Offline Mode: Service Workerを使って

* まとめ

  * 未来に向かっていこう

  * カスタマイズしやすいようにしよう

  * 共有しやすく

  * パフォーマンスよく

.. _docutils: https://pypi.python.org/pypi/docutils/0.14

Q&A
----

* Q: (jbking) HTMLテンプレートをカスタマイズしやすくしよう、について具体的なProposalってありますか？

  * A: (shibu_jp) 今のところないです。こまかく分割されてしまっているのを1つにまとめる事を考えています。後方互換性は気にしてるけど、新しい仕組みを選択できるようにしようと思ってます。

* Q: (r_rudi) 検索の部分をなんとかしたいという話ですが、 Oktavia_ の開発は続けるんですか？

  * A: (shibu_jp) Oktavia_ はFM-Indexというのを使ってるんですが、検索エンジンとしてはそこまで良いものではない。ので、もういいんじゃないかなと思ってます。昔と違っていまは色々できるようになってきたので。

* Q: (?): Sphinxは使ったことがなくて今日初めて色々聞いたんですが、さきほどのHTML5サポートはどうやって出力するんですか？

  * A: (shibu_jp) たぶん今はデフォルトなのかな。利用者からはそんなに劇的に使いやすくなったとかはないです

    * （※ HTML5はまだオプションです: http://www.sphinx-doc.org/en/stable/config.html#confval-html_experimental_html5_writer ）

  * A: (shibu_jp) epubチェッカーにかけるとHTML4ベースだとエラーが数万でてしまうのを解消したかった

.. _Oktavia: http://oktavia.info/ja/


LT
=======

* 木製人がSphinxで幸せになる方法 ( `どりらん`_ )

  * 資料: https://slideship.com/users/@driller/presentations/2017/11/GX5q8tJTPHuctnT1LeAZZd/

  * FinTech関係のLT&忘年会やります: https://fin-py.connpass.com/event/73241/

  * Sphinx、先日某 `PythonユーザのためのJupyter[実践]入門`_ で使う事になって慌てて勉強し始めた

  * Sphinx経験: よくSphinx、reStructuredTextを打ち間違える

  * Jupyter使ってる方？ -> けっこういますねーじゃあ知ってる前提で続けます

  * Jupyterあるある1: Untitled1, Untitled2 とか色々あって見失う

  * Jupyterあるある2: GitHubのNotebookにStar付けても埋もれて見失う

  * 検索したい！Notebookを検索したい！

  * nbsphinx_ を使えばnotebookをSphinxに食わせてまとめられる

  * Jupyter Notebook で実はMarkdownだけじゃなくreSTも書ける（ことに先日気づいた）

* Sphinxユーザー会の紹介 ( `@usaturn`_ )

  * http://sphinx-users.jp/
  * `Sphinxをはじめよう 第2版`_
  * 「買ってないかた、ここにいらっしゃいますか？これから始める方は是非買った方が良いですよ」

  * Sphinxハンズオンやってます
  * Sphinx Tea Night を平日の夜に月イチでやってます
  * Sphinx + 翻訳 hacka-thon を週末日中に月イチでやってます
  * Sphinx合宿やります
  * イベント関連、詳しくはこちら!: https://sphinxjp.connpass.com/

.. _PythonユーザのためのJupyter[実践]入門: http://amzn.to/2zwhbQc
.. _nbsphinx: https://pypi.python.org/pypi/nbsphinx/
.. _どりらん: https://twitter.com/patraqushe
.. _@usaturn: https://twitter.com/usaturn


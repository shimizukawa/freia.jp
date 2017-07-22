:date: 2017-04-26 22:00
:categories: ['Plone', 'Python', 'CMS']
:body type: text/x-rst

=====================================================
2017/04/26 World Plone Day 2017 Tokyo に参加しました
=====================================================

`World Plone Day 2017 Tokyo`_ に参加しました。

.. _World Plone Day 2017 Tokyo: https://plonejp.connpass.com/event/51340/

会場はクリークアンドリバー社さん。 `Start Python Club`_ のイベントをやってる会場です。いつもありがとうございます。

.. _Start Python Club: https://startpython.connpass.com/

.. contents::
   :local:


.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">World Plone Day 2017 Tokyo にキター！（遅刻 (@ クリーク・アンド・リバー社 in 千代田区, 東京都 w/ <a href="https://twitter.com/takanory">@takanory</a>) <a href="https://t.co/4AsuAFekIV">https://t.co/4AsuAFekIV</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/857183042221289473">2017年4月26日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

自分がplone関連に触れていたのは、blog的には :doc:`../728/index` が最後のようです。7年ぶりかー。

Ploneの現状とロードマップ(@terapyon)
======================================

（40分遅れて参加したので始めの方を聞き逃しました）

:発表者:  CMSコミュニケーションズ 寺田さん
:資料: https://speakerdeck.com/terapyon/plonefalsexian-zhuang-torodomatupu

.. figure:: terada.*
   :width: 500


* Ploneの最近の動向

  * Headless CMS というワードが最近はやってきている

  * デカップル

  * 最近のWordPressで広まってきた

  * Ploneでは5年前くらいからDiazo（ダイアゾ）という仕組みでやっていた

  * 最近の動向としてPloneもフロントとバックエンドを分離したほうがいいんじゃないかという話がでてきた

  * REST API

* Ploneサーバー

  * 新しい動き（Headlessが落ち着いてきたかと思ったらもう次の動きが）
  * plone名前空間 (従来のPloneとは別の活動だけど同じ名前空間)
  * BSDライセンス


Plone5のOSSにおける進化と適応(日本語抜粋版) (@zenich)
============================================================

:発表者: 安田善一朗さん
:資料: https://speakerdeck.com/zenich/plone5falseossniokerujin-hua-toshi-ying-duan-suo-ban


.. figure:: yasuda.*
   :width: 500


進化

* 行動による擬似的な適応

* 収斂進化:  種としては異なるのに似た進化を遂げる

* 比喩的な意味での適応 

進化の歴史、誕生の経緯

* 1996年 Jim Fulton さんが飛行機での移動中にboboのアイディアを思い付いた

* Principia

* Digital Creation社がPrincipiaをOSSとして公開した

* ZOPE (Z Object Publishing Environment)

* 様々な革新

  * オブジェクト トラバーサル

  * セキュリティー機能

  * ブラウザ経由での開発

  * CMF（とっつきづらかった）

* CMFのテーマとして動作するCMFPlone

* Ploneのリリース

  * Ploneは画面上でコンテンツの操作ができた

  * 多くの組織に採用された、コミュニティーが急速に成長した

* ベルンでPloneイベント（スプリント）が開催された

  * コミュニティドリブン開発

  * お城などでイベントをやった

* 2003年にPloneカンファレンス開催

* 900人のコミッター

CMS

* Ploneの強み

  * カスタムコンテンツの作成

  * カスタムツールの提供

  * 見た目（テーマ）の変更

* 弱み

  * Web画面上で変更できるということは変更が全てDBに格納されると言うこと

  * テストできない、バージョン管理できない、ドキュメント管理できない

  * 開発コードはすべてPloneの外（ファイル）で管理する方針に変更された

* Pythonパッケージが使えるようになってきた(egg)

  * すべてパッケージ化した

  * テストできるようになった、ドキュメンテーションできるようになった

  * Pythonプログラマでないとコードを変更できなくなった

* Zopeコードの弊害

  * PEP-8 に対応していない（Zopeの方が5年早く生まれた）

  * MixInの多用コード

  * Plone言語（Zope言語）とでもいうべき作法をしらないと開発できなくなった

* Ploneの適応

  * 問題を解決するために舵を切った

  * Plone5で多くの適応を行った


* Plone5 擬似的な適応 (APIの適応)

  * ツールを使うためにとても難解なツールを使いこなす必要があった

  * 学生にPlone開発をおしえるセッションで、何時間かかけても開発できるようになる人がいなかった

  * この事件からPloneのドキュメンテーションとfacade開発が始まった

  * facadeパターンによるAPI提供 = 擬似的な適応

* 収斂進化

  * ところでその頃 Zope Component Archtechture 開発が始まっていた

  * Adapter Pattern: 既存クラスにアダプタすることでインターフェースを変更できる

  * Zope の Object Publishing を行うためには、5つのクラス、継承含めると16クラス使っている状態だった

  * PloneはこのZopeの特性を引き継いでしまっていた

  * Adapter Pattern でこの問題を解決し、コンテンツオブジェクトとViewが切り離された


* 比喩的な意味での適応

  * テーマの単純なカスタマイズのために大奥の知識が必要になってしまった

  * Python, ZopePageTemplate, XML, ...

  * ほんとうに必要なのはなんなの？

  * Diazo という技術が生まれた

    * （清水川註: オリジナルは Deliverance_, Ian Bicking作で、派生版として作られた xdv_ が改名してDiazoになりました。 :doc:`../728/index` でxdvいじってた）

  * 適応の考え方をテーマデザインの世界に当てはめることが出来た


.. _Diazo: https://pypi.python.org/pypi/diazo
.. _Deliverance: https://pypi.python.org/pypi/Deliverance
.. _xdv: https://pypi.python.org/pypi/xdv


PythonベースのWeb構築システム: Mezzanine (@takanory)
========================================================

:発表者: @takanory
:ツール名: Mezzanine__
:資料: https://speakerdeck.com/takanory/mezzanine

.. __: http://mezzanine.jupo.org/

.. figure:: takanory.*
   :width: 500



* Mezzanineの意味: 中二階


* 動的にページを作ります

  * ベースはDjango

  * WordPressっぽい

  * Best Django CMS （自称）


* 利用サイト

  * http://djangoproject.jp

* 気に入ってるところ

  * Cartridgeプラグインを入れると買い物機能が作れる。一通りあって良い感じ

  * 機能は一通りはいってる（他のCMS同様）

  * Cartridgeプラグインいれてインストールするだけで、bootstrapテーマのシンプルなサイトが立ち上げられる

* いまいちなところ

  * 個人でやってるのでリリースタイミングが不明

  * cartridgeプラグインのカスタマイズは苦行

    * 氏名の入力順がアメリカスタイル

    * カスタマイズが奥深いところに手を入れないとできなかった

  * Amazon S3で画像管理すると重くなって死

    * 1ファイルごとにファイル？ディレクトリ？と問い合わせて重くて大変

    * 一生懸命キャッシュする仕組みをはさまないとつらい


* コントリビューターです！(takanory)


PythonベースのWeb構築システム: Pelican  (@laugh_k)
========================================================

:発表者: @laugh_k
:ツール名: Pelican__
:資料: https://www.slideshare.net/laughk/pelican-world-ploneday2017tokyo

.. __: https://blog.getpelican.com/


.. figure:: laugh_k.*
   :width: 500


* 個人ブログでPelicanを使ってます

* Python製 静的ページジェネレータ

  * 静的なHTMLを出力する

  * Jinja2テンプレート

  * 原稿は reStructuredText, Markdown, AsciiDoc で書ける

* 特徴

  * サイト全体のHTMLを出力するたけ

  * 設定ファイルはPythonで書く

  * プラグインがアル

    * DISQUS
  
    * Google Analytics

* Pelicanを利用する際のイメージ

  * Wizard形式で答えていくと雛形を掃き出してくれる

  * contentディレクトリの下に原稿ファイルを置く

  * output以下に掃き出されたファイルをどこかにホスティングすればサイト公開完了

* 気に入っているところ

  * ホスティングの選択肢が多い: S3, github-pages, VPS, レンタルサーバー,...

  * セキュリティの心配が無い（静的なので）

  * 対応しているマークアップが豊富

  * テーマが多い

* いまいちなところ

  * 編集が面倒くさい



PythonベースのWeb構築システム: Kotti  (@t2y)
========================================================

:発表者: @t2y
:ツール名: Kotti__
:資料: https://www.slideshare.net/techblogyahoo/kotti

.. __: https://kotti.readthedocs.io/

.. figure:: t2y.*
   :width: 500


* 最近開発が落ち着いてきている

* 2015年頃に開発が始まった頃は活発で、そのころにi18n対応まわりでコントリビュートして、コントリビューターになりました

* 特徴

  * コア機能だけを提供

  * こまかい機能はアドオンで追加する

  * Pyramidの上にkotti層

  * Twitter Bootstrap, SQLAlchemy

* リポジトリ

  * 1.0.0 / 2015/11/20 リリース

  * 1.3.0 / 2016/10/10 メンテンスモードっぽい

  * Python3未対応

* 気に入ってるところ

  * Pyramidアプリを触ってみたかったので

  * コントリビュートできたこと


* 懸念点 = いまから使える？

  * 安定してるけど考えた方がよさそう

  * 開発がおちついてしまって、活発ではない

  * jQueryを使っているので周辺全部jQuery


* Python3対応やらないの？(by terapyon)

  * 「3時間くらい見てみたんですけど、けっこう大変そう」(t2y)


PythonベースのWeb構築システム: Symposion  (@yellow844)
========================================================

:発表者: @yellow844
:ツール名: Symposion__
:資料: 

.. __: http://symposion.readthedocs.io/

.. figure:: yellow.*
   :width: 500


* 概要

  * Djangoのうえにpinaxレイヤー、そのうえにsymposion

  * Web画面上でスポンサー登録やスピーカー登録、プロポーザル登録ができる

* いいところ

  * プロポーザルの提出とレビューをWeb上でできる

  * カスタマイズしやすい

* 困ったところ

  * フロントエンドのカスタマイズが辛い, jQuery固定でどうにもならない

  * コンテンツを追加しようと思うと、モデルの変更などが必要になる

  * API関連がいまひとつ弱い（モバイル向けAPIなどを自作した）

* まとめ

  * 管理機能が優秀

  * プロモーションサイトとしては微妙

  * https://pycon.jp/2017/ja/ 2017/9/7, 8, 9 で開催されるのでみんな来てね



「PyCon JP がsymposionで作られてる、ってちゃんと伝わりましたかね・・・」(takanory)


PythonベースのWeb構築システム: SubstanceD (@jbking)
========================================================

:発表者: @jbking
:ツール名: SubstanceD__
:資料: 

.. __: http://docs.pylonsproject.org/projects/substanced/

.. figure:: jbking.*
   :width: 500


* 1.0.0a1

  * そろそろこのバージョンになって2年...

* 作者:

  * Chris McDonough : Pyramidやrepozの作者
  * Tres Seaver

* つよいところ

  * ZODB上に作られている

  * オブジェクト単位でセキュリティ設定ができる

  * テキスト検索機能

  * ワークフロー: 公開フローみたいなのを使える

  * オブジェクト毎のアンドゥ

  * 人ごとにオブジェクトのセキュリティコントロールもできる

* Pooneとの違い

  * 学習曲線: Ploneは重い、SubstanceDは軽い

* こまったところ

  * Python3で動かないところがある

  * 日本語ドキュメントがない



PythonベースのWeb構築システム: Sphinx (@usaturn)
========================================================

:発表者: @usaturn
:ツール名: Sphinx__
:資料: 

.. __: http://sphinx-users.jp/

.. figure:: usaturn.*
   :width: 500

* 最近転職しました。ぜひ弊社に

* `Sphinxをはじめよう`_ という本を出しました、いま改訂作業中です。いまかぶってる帽子が執筆者におくられるオーサーズキャップです

* Sphinxとは

  * Sphinxをしらない方いますか？あっ、何名かいらっしゃいますね

  * SphinxはPythonのリファレンスドキュメントを作るために作られたツールです

  * Pelicanと同じ様な感じで、reStructuredText(reST)等で原稿を書いて、make htmlすると静的HTMLを生成するツールです

  * Markdownでも原稿を書けます

  * いろんなフォーマットでも出力できます

* 特徴

  * マルチインプット

    * （清水川註: マルチインプットとして、reST, Markdown, 画像、PowerPoint, ...等が紹介されていましたが、誤解を与えそうなので補足します。原稿に使えるのはreSTとMarkdownで、それ以外のフォーマットは、拡張プラグインを使って画像等のデータを取り出して埋め込めるということを表現したかったようです。画像にかかれている文字列を読み取ってHTMLにテキスト化して出力できるわけではありません。 「Sphinxはワンソース、マルチアウトプット」という紹介のほうが一般的な気がします。）
    * （清水川註: 原稿として使えるフォーマットは、デフォルトでreSTのみです。拡張を入れればMarkdownに対応します。他のフォーマット向けの拡張プラグインを書けばAsciiDocやTextileなども読み込めるようになります。だれか実装して拡張パッケージとして公開しないかな）

  * マルチアウトプット

* 気に入ってるところ

  * （聞き逃した）

* いまいちなところ

  * 初学者にすすめづらい

* sphinx-usres.jp のサイトもSphinxで書いてます

  * githubに更新した原稿をpush

  * werckerで自動ビルド

  * werckerでS3にデプロイ

.. _Sphinxをはじめよう: https://www.oreilly.co.jp/books/9784873116488/

全体を通しての質問タイム質問
=================================

* Q. (takanory) 寺田さんはいまのを聞いてどれが一番きにいりましたか？

  * A. (寺田) どうしよう、更新とまってるとか大変な部分とか聞くと、自分で作るね！


懇親会
============

かんぱーい！

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/plonejp?src=hash">#plonejp</a> World Plone Day 2017 Tokyo かんぱーい！ (@ クリーク・アンド・リバー社 in 千代田区, 東京都 w/ <a href="https://twitter.com/takanory">@takanory</a>) <a href="https://t.co/ggvbEIPkGF">https://t.co/ggvbEIPkGF</a> <a href="https://t.co/PJ2NNqOvlf">pic.twitter.com/PJ2NNqOvlf</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/857202374078812160">2017年4月26日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/plonejp?src=hash">#plonejp</a> World Plone Day 2017 Tokyo かんぱーい！ (@ クリーク・アンド・リバー社 in 千代田区, 東京都 w/ <a href="https://twitter.com/takanory">@takanory</a>) <a href="https://t.co/ggvbEIPkGF">https://t.co/ggvbEIPkGF</a> <a href="https://t.co/lMyDDw5PIR">pic.twitter.com/lMyDDw5PIR</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/857202405506781184">2017年4月26日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


感想: blogメモ書くのに疲れました。楽しかったです！


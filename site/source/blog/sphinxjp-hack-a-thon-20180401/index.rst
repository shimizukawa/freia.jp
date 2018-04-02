:date: 2018-04-01 17:00
:tags: Sphinx

===========================================
Sphinx + 翻訳 hack-a-thon 2018.04 #sphinxjp
===========================================

SphinxのHack-a-thonイベントに参加してきました。
今日は、仙台から来た人、Sphinxのドキュメント翻訳する人、など8名が参加しました。

.. figure:: attendees.*
   :width: 80%

自分は、乳児の沐浴があるので17時で撤収しました。

:イベント: `Sphinx+翻訳 hack-a-thon 2018.04`_
:参加者: @tk0miya, @shimizukawa, @KenOnodera1988, nskgch, @takuan_osho, @naru0ga, @cocoatomo, @usaturn
:会場: タイムインターメディア社（曙橋）

.. _Sphinx+翻訳 hack-a-thon 2018.04: https://sphinxjp.connpass.com/event/81858/


自己紹介、やること
==================

.. figure:: todos.*
   :width: 80%

   やること

* @tk0miya: 「Sphinx-1.8に向けてコード書きます」
* @KenOnodera1988: 「2010年くらいから研究室でSphinxを使っています。研究室や仕事でSphinxで書いても使ってもらえないというジレンマが。広めようにも仙台にSphinx/Pythonコミュニティがないので広めづらい。仙台でコミュニティを作りたい。勝手にやっていいんでしょうか？（いいとも！）」
* nskgch: 「Sphinxドキュメント翻訳の手伝いをしてます。今日もやります」
* @takuan_osho: 「Sphinxはユーザーとしてけっこう前から使ってます。今日やることはいまから考えます」
* @naru0ga: 「LibreOfficeの方からきました。ドキュメント作成ではあまりLibreOfficeでは書いてなくて、レポートからLibreOfficeに出してレタッチしてPDF化して提出するという使い方をしています。Sphinxで書いたものを同様にできたら面白いかなと今思い付きましたｗ」
* @shimizukawa「SphinxのIssueをたくさん振られたので倒していきます。あと、Sphinx公式ドキュメントの翻訳を自動的にサイトに反映する仕組みを先日刷新したので、その自動化をもうちょっと進めます」
* @cocoatomo: 「Python公式ドキュメント https://docs.python.org/ja/ の翻訳をしてます。Python-3.7がリリースされそうなので、メジャーバージョンが出たときにTransifexの切り替えをどういう手順でやるかをWikiにまとめる作業をします。もしPythonドキュメントを読んで分からない日本語とかあったら教えてください」
* @usaturn: 「普段はインフラ屋でクラウドフォーメーションとか使ってます。今日は社内勉強会でSphinxを紹介するのでそのプレゼン資料を作ります」


自分がやったこと
================

1. http://www.sphinx-doc.org/en/stable/ を再ビルドしてcanonical hrefにmasterを指定

   Sphinxプロジェクトは ``stable`` ブランチを廃止しました。

   - master: 開発中最新メジャーバージョン（未リリース）
   - stable: 以前は、リリース済み最新メジャーバージョン（廃止）
   - 1.7: リリース済みメジャーバージョン（新規）
   - 1.6: リリース済みメジャーバージョン（新規）
   - ...

   上記のように、stableを廃止して、リリース済みバージョンはバージョン番号でドキュメントを持つようにしました。この結果、URLが以下の様に変わりました。

   - 旧: http://www.sphinx-doc.org/en/stable/
   - 新: http://www.sphinx-doc.org/en/1.7/

   変わったんですが、以前からリンクしているサイトなどは ``/stable/`` を指していてGoogleのクローラーもやってくることもあり、Sphinxの何かをGoogle検索すると ``/stable/`` にたどり着いてしまう状態でした。

   ということで、Google検索の結果を ``/master/`` に向けるために、ReadTheDocsの設定を変えて、 `Sphinxドキュメントのヘッダにもテンプレートで設定 <https://github.com/sphinx-doc/sphinx/commit/d8c107a61b30bdf8d9f3e4e8b183c8e34ef7fb23>`_ して、stableドキュメントを再ビルドしました。

   とは言え、 ``/stable/`` はもう廃止したURLなので、ReadTheDocsのリンクでアクセスされないように、設定で非公開にして、 http://www.sphinx-doc.org 上ではリンクを提供しないように変更しました。（本当は ``/stable/*`` にアクセスされたときに ``/master/*`` にリダイレクトしたかったけど、ReadTheDocsではできなかったのでしょうがない）

   .. figure:: hide-stable.*
      :width: 80%

2. PRをいくつかレビューして、Issue見ました

   * https://github.com/sphinx-doc/sphinx/pull/4773

   * https://github.com/sphinx-doc/sphinx/pull/4798

   * https://github.com/sphinx-doc/sphinx/pull/4804

   * https://github.com/sphinx-doc/sphinx/issues/4778

おまけ
=======

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash&amp;ref_src=twsrc%5Etfw">#sphinxjp</a> に仙台から参加の <a href="https://twitter.com/KenOnodera1988?ref_src=twsrc%5Etfw">@KenOnodera1988</a> さんからお土産に萩の月（大好き）頂いた！ありがとうございますー！ (@ タイムインターメディア in 新宿区, 東京都) <a href="https://t.co/QQ818KeL6J">https://t.co/QQ818KeL6J</a> <a href="https://t.co/yHXgUcl3Ny">pic.twitter.com/yHXgUcl3Ny</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/980297491353669633?ref_src=twsrc%5Etfw">2018年4月1日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


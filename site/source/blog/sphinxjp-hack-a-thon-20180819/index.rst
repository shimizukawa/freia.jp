:date: 2018-08-19 23:59
:tags: Sphinx

===========================================
Sphinx + 翻訳 hack-a-thon 2018.08 #sphinxjp
===========================================

久々にhack-a-thon参加blog.

SphinxのHack-a-thonイベントに参加してきました。

.. figure:: oyatsu.*
   :width: 80%

   今日のオヤツ. @usaturn++

:イベント: `Sphinx+翻訳 hack-a-thon 2018.08`_
:参加者: @tk0miya, @shimizukawa, @cocoatomo, nskgch, @usaturn
:会場: タイムインターメディア社（曙橋）

.. _Sphinx+翻訳 hack-a-thon 2018.08: https://sphinxjp.connpass.com/event/96320/


自己紹介、やること
==================

.. figure:: todos.*
   :width: 80%

   やること

* @tk0miya: 「Sphinx-1.7.7と1.8.0b1のリリースに向けてコード書きます。」
* @shimizukawa「Sphinx-1.7.7リリースに向けてIssue/PR確認を手伝います」
* @cocoatomo: 「 `Python公式ドキュメント <https://docs.python.org/ja/>`_ の翻訳と関連チケットの確認をやります。疲れたらpipenvの翻訳、飽きたらdocutilsの型付け。逃げ道をたくさん用意してます。」
* nskgch: 「Sphinxドキュメント翻訳の手伝いをしてます。今日もやります」
* @usaturn: 「」


自分がやったこと
================

用事で15時に帰らないといけなくなったため、朝10時くらいから近所でhackしてました。@tk0miya が会場をはやく開けてくれたので、12時すぎくらいから現地でhack開始。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">pre- sphinx hack-a-thon!! <a href="https://twitter.com/hashtag/sphinxjp?src=hash&amp;ref_src=twsrc%5Etfw">#sphinxjp</a> (@ Starbucks Coffee 北の丸スクエア店 - <a href="https://twitter.com/Starbucks_J?ref_src=twsrc%5Etfw">@starbucks_j</a> in 千代田区, 東京都) <a href="https://t.co/3UkT5YdSvc">https://t.co/3UkT5YdSvc</a> <a href="https://t.co/CYYMBGnKoN">pic.twitter.com/CYYMBGnKoN</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/1030989327571079168?ref_src=twsrc%5Etfw">2018年8月19日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


.. 1. http://www.sphinx-doc.org/en/stable/ を再ビルドしてcanonical hrefにmasterを指定
.. 
..    Sphinxプロジェクトは ``stable`` ブランチを廃止しました。
.. 
..    - master: 開発中最新メジャーバージョン（未リリース）
..    - stable: 以前は、リリース済み最新メジャーバージョン（廃止）
..    - 1.7: リリース済みメジャーバージョン（新規）
..    - 1.6: リリース済みメジャーバージョン（新規）
..    - ...
.. 
..    上記のように、stableを廃止して、リリース済みバージョンはバージョン番号でドキュメントを持つようにしました。この結果、URLが以下の様に変わりました。
.. 
..    - 旧: http://www.sphinx-doc.org/en/stable/
..    - 新: http://www.sphinx-doc.org/en/1.7/
.. 
..    変わったんですが、以前からリンクしているサイトなどは ``/stable/`` を指していてGoogleのクローラーもやってくることもあり、Sphinxの何かをGoogle検索すると ``/stable/`` にたどり着いてしまう状態でした。
.. 
..    ということで、Google検索の結果を ``/master/`` に向けるために、ReadTheDocsの設定を変えて、 `Sphinxドキュメントのヘッダにもテンプレートで設定 <https://github.com/sphinx-doc/sphinx/commit/d8c107a61b30bdf8d9f3e4e8b183c8e34ef7fb23>`_ して、stableドキュメントを再ビルドしました。
.. 
..    とは言え、 ``/stable/`` はもう廃止したURLなので、ReadTheDocsのリンクでアクセスされないように、設定で非公開にして、 http://www.sphinx-doc.org 上ではリンクを提供しないように変更しました。（本当は ``/stable/*`` にアクセスされたときに ``/master/*`` にリダイレクトしたかったけど、ReadTheDocsではできなかったのでしょうがない）
.. 
..    .. figure:: hide-stable.*
..       :width: 80%
.. 
.. 2. PRをいくつかレビューして、Issue見ました
.. 
..    * https://github.com/sphinx-doc/sphinx/pull/4773
.. 
..    * https://github.com/sphinx-doc/sphinx/pull/4798
.. 
..    * https://github.com/sphinx-doc/sphinx/pull/4804
.. 
..    * https://github.com/sphinx-doc/sphinx/issues/4778


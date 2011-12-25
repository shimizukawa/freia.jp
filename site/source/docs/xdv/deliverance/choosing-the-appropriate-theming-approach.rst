=============================
テーマ適用アプローチの選択肢
=============================

.. warning::
    本ドキュメントの内容は plone.org の `Choosing the appropriate theming approach  <http://plone.org/documentation/manual/theming/choosing-the-appropriate-theming-approach>`_ の翻訳です。
    翻訳は2009年秋に行ったままのため、最新の状況と異なる可能性があります。

Ploneサイトにテーマを適用する方式はいくつかあります。それぞれの手法の違いを見ていきましょう。


はじめに
==========

* 内容は plone.org の `Choosing the appropriate theming approach  <http://plone.org/documentation/manual/theming/choosing-the-appropriate-theming-approach>`_ の翻訳です。


テーマ適用方式の比較
=====================

* 今現在、Ploneにテーマを適用するいくつかの方式について、どんな選択肢があって、それぞれがどんなシーンに適しているでしょう？

* 今回取り上げる３つの方式

  1. Ploneプロダクトパッケージ方式
  2. collective.xdv
  3. Deliverance

Ploneプロダクトパッケージ方式
==============================

* 良いところ:

  * フレキシビリティーと制御は究極。
  * More flexibility when it comes to theming select parts of a site or sub-sites


* 悪いところ:

  * 仕組みがとっても複雑で、ZCMLやPythonに親しんでいる必要がある。
  * テンプレートが変わったりするのでアップグレードしづらい。
  * Shipping your own templates will get you out of sync with the main product


collective.xdv
===============

* 良いところ:

  * 実行時にWebサーバー上で XSLT に変換されるので、 proxy とか WSGI とかをセットアップしなくても良い。つまり、 Deliverance よりもちょっとパフォーマンスが良い。
  * Plone への組み込みが簡単で始めやすい。

* 悪いところ:

  * 一般に親しまれているCSSセレクタではなく、XPathセレクタで書く必要がある。（でも実際の所、Firegub等のプラグインを使えばXPathセレクタは手に入るよ）

Deliverance
============

* xdvと比べて良いところ:

  * スタンドアローンなので、Plone以外の他のサイトでも使える。（WSGIならなおよい）
  * XPathの他に、CSSセレクタを使える。

* xdvと比べて悪いところ:

  * Ploneとの統合が面倒。多くの設定や仕組みを理解する必要がある。
  * 標準ではない（けれどCSS的な）文法も使えるので、あとで xdv に再利用して使うことは出来ない。


じゃあ、いつ、どれを使うべき？
==============================

* アドオンプロダクトを使うべき時とは...

  * 極度の粒度コントロールが必要で、そのために Python や ZCML を学んでも良い場合。

* xdv を使うべき時は...

  * テーマとプログラムコードを分離しておきたくて、テーマを再利用したいと思っている。この方法なら、プログラムとの "繋ぎ込み" を心配せずに、 Plone コミュニティーから良い手順などなどが手に入るのでやりやすい。

* Deliverance を使うべき時は...

  * 複数のフレームワーク/Webアプリケーション(Plone 等)に対して同時に同じテーマを適用したい場合で、 Deliverance を Proxy や WSGI としてセットアップしても良いと思っている場合。


まとめ
=======

* もちろん現実はいつももうちょっと複雑。実際のところ仕組みを理解すれば、 xdv ベースのテーマを Plone 以外にも適用することも出来ます。

* ここで知っておいて欲しいのは、 xdv と Deliverance はどちらかを覚えればもう片方に切り替えるのはそれほど難しくありません。仮に最終的に Deliverance を使うことになるのだとしても、まず collective.xdv から始めるのはとても良い選択だと思います。


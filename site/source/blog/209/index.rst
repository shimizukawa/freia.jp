:date: 2005-05-19 00:02:32
:categories: ['Zope']
:body type: text/x-rst

====================================================
2005/05/19 Drag & Drop Sortable Lists をZopeで使う案
====================================================

*Category: 'Zope'*

自分は今までJavaScriptをまじめに勉強したことが一度もないし、まじめに読んだこともほとんど無いので、これからも勉強するつもりはない。以上、おわり。

‥‥とも言ってられない。

JavaScript無しでやってると、主にform（リストボックスとか）でフラストレーションがたまることが多い。使っていて、ワンクリック毎にサーバーリクエスト＆レスポンス、というのがなんともイライラする。 `ZPhotoSlides`_ の管理画面で100枚近くある写真の順番を手動で並べ直したときは気絶するかと思いましたよ！っていうくらい大変。

で、このフラストレーションを解消出来そうな `Drag & Drop Sortable Lists with JavaScript and CSS`_ 技術を `日本のZope情報`_ 経由で入手。早速Zope(のコンテンツ)上に `載せてみた`_ 。

うまく動くみたいなので、この技術をOrderd Folderなんかに適用出来ないかな～と妄想してみる。多分この技術は、CSSの位置情報をJavaScriptで操作して実現しているので、適用するためにはtable使うの止めて全部 ul, li  タグで書かないといけないんだと思う。大変そうだ。

.. _`ZPhotoSlides`: http://zphotoslides.org/
.. _`日本のZope情報`: http://coreblog.org/jp/jzi/
.. _`Drag & Drop Sortable Lists with JavaScript and CSS`: http://tool-man.org/examples/
.. _`載せてみた`: http://www.freia.jp/taka/memo/javascript/javadrag/



.. :extend type: text/plain
.. :extend:


:Trackbacks:
:TrackbackID: 2005-11-28.5014445113
:BlogName: [CD]CoffeeDiary
:url: http://akiyah.bglb.jp/blog/754
:date: 2005-11-28 00:48:21

========================================================================
2005/11/28 Drag & Drop Sortable Lists で階層的な箇条書きをウンヌンしたい
========================================================================

*Category: 'Zope'*

Drag & Drop Sortable Lists をZopeで使う案 — 清水川 Webを見て、 Drag &
Dropをやってみたくなってダウンロードしてみた。
おぉ、サンプルを見てみると普通にドラッグアンドドロップが使える！
JsUnitでのテストもなんかグラフィカルですごいし。
で、マインドマップBBS的な物を想像すると、このドラッグアンドドロップが
階層的な箇条書きに対して使えるとすごくうれしいのだけど、
簡単に試してみたらうまく行かなかった。なんかエラーが出ちゃう。
まあ、一発でう...

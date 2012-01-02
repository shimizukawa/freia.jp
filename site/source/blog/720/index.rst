:date: 2010-06-21 23:25:12
:categories: ['Event', 'Zope', 'Plone']
:body type: text/x-rst

=======================================================
2010/06/21 Deliveranceから派生したxdvの開発が活発っぽい
=======================================================

*Category: 'Event', 'Zope', 'Plone'*

先日6/19の `(第12回)Zope/Plone開発勉強会`_ でDeliveranceを使いこなす練習をしようと思っていましたが、どうやら今はxdvというDeliveranceから派生したプロダクトの方が活発らしいということで色々と調べてみました。

Deliveranceって何？という方は `Deliveranceデモ`_ をどうぞ。

ということでxdvの特徴をまとめてみました。

* collective.xdv は Ian Bicking が開発したDeliveranceから派生
* xdvはcollective.xdvから分割されたコンテンツ変換ルールコンパイラ
* xdvはルールをコンパイルしてXSLTにしておくことでHTMLを高速に変換可能
* XSLT適用はDeliveranceの動的処理よりも高速
* XSLTの適用はmod_transformなどのXSLT専門モジュールで処理
* XSLT変換が扱えるApache,nginx,Varnish,Plone,WSGIなどに対応
* ルールはDeliverance同様にXPathとCSS3セレクタで記述可能
* Deliveranceで出来なかった特殊なルールも記述できるように拡張
* 実運用ではPython無しで動作可能(XSLT適用できればOK)
* ドキュメントが良い。PyPIのページを見るだけで大体理解できる

ということで、これだけあればOK的な使い方は出来なくなってしまいましたが、逆に組み合わせ自由なので色々な利点が増えました。そんなステキなxdvを詳しく知りたい方は `Python Package Index : xdv 0.3`_ の説明を読んでみて下さい。

来週末6/25からのPython温泉で、使いこなせるように練習する予定です。

-------------------------

勉強会では他にはsetuptoolsを使ったプラグイン機構についてサンプルコードを書いて@terapyonや@jhottaに説明してました。詳しくは次のエントリで。

次回の `(第13回)Zope/Plone開発勉強会`_ もよろしく。 `Sphinx-1.0 リリースパーティー`_ と日が被ってますケド。


.. _`(第12回)Zope/Plone開発勉強会`: http://atnd.org/events/5001
.. _`(第13回)Zope/Plone開発勉強会`: http://atnd.org/events/5844
.. _`Deliveranceデモ`: http://plone3d.freia.jp/deliverance
.. _`Python Package Index : xdv 0.3`: http://pypi.python.org/pypi/xdv
.. _`Sphinx-1.0 リリースパーティー`: http://atnd.org/events/5610


.. :extend type: text/x-rst
.. :extend:

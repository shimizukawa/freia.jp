:date: 2009-12-07 23:55:00
:categories: ['web']
:body type: text/x-rst

===========================================================
2009/12/07 Goドキュメント翻訳のSphinxテーマをカスタマイズ中
===========================================================

*Category: 'web'*

Goの翻訳サイトのデザインを変更しましょう、ということで、 `GoogleGroupsの方`_ で話が進んでいて、 http://www.oswd.org/ から渋川さんが探してきた Aqua デザインを適用作業中です。

.. _`GoogleGroupsの方`: http://groups.google.co.jp/group/golang-docjp/browse_thread/thread/b981adb28f992451

適用作業の初めのうちは、Sphinxのdefaultテーマに沿う形で(extendして)組み込んでいっていたのですが、Sphinxテーマのカスタマイズが初めてだったのと、AquaのHTML/CSSが構造的に合わなかったのとがあり、途中で一旦全部捨てて、defaultテーマを無視して(extendせずに)組み込みました。捨てるまで2時間、捨ててから2時間くらいで組み込みは出来ましたが、Sphinxで使われているJinjaにもう少し詳しければもっと速く出来たかもしれません。

適用ついでLiquid対応もしてみました。一応Liquid化は出来たものの、デザイン・レイアウトのためだけのタグが多すぎ。もうちょっときれいに出来そうな気がする。しかも試行錯誤含めて2時間もかかってしまって、まだまだHTML力が足りない。

-------

ところで、こうしてデザイン組み込みをやってると Deliverance ってやっぱり便利ですね。Deliveranceは作業のレイヤーが1段異なる気がします（HTMLの作りを気にしなくなるという意味で）。Deliveranceの簡便さでデザイン組み込みが出来るようにならないもんだろうか。

* `Deliveranceをインストールする手順 in Python Hack-a-thon #2`_

.. _`Deliveranceをインストールする手順 in Python Hack-a-thon #2`: http://www.freia.jp/taka/blog/683


.. :extend type: text/x-rst
.. :extend:

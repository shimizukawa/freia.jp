:date: 2009-08-08 00:17:21
:tags: python

===================================================
2009/08/08 DeliveranceがWindows上で正しく動作しない
===================================================

`Zope Essentials 7 で Deliverance の紹介を聞いてきた`_ に関連して。

Deliveranceの紹介を聞きながら自分の環境で動かそうとしてたんだけど、どうにも動かなくて色々調べてみたらそもそも起動時に設定ファイルを読んでくれてなかった。で、さらに調べたらWindowsで再現するファイルパス変換のバグがあったので、超つたない英語で報告してみた、というかDocTest的にインタラクティブシェルの内容と修正パッチを貼っておいたので、分かってくれるんじゃないかな－。

 報告 -> http://projects.openplans.org/deliverance/ticket/13


Windowsなんかで開発しなければいいのに、という声が聞こえてくる気がする。

.. _`Zope Essentials 7 で Deliverance の紹介を聞いてきた`: http://www.freia.jp/taka/blog/663


.. :extend type: text/html
.. :extend:


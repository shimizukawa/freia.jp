:date: 2005-04-19 01:01:59
:categories: ['Zope']
:body type: text/x-rst

=============================
2005/04/19 サーバー移行、成功
=============================

*Category: 'Zope'*

昨日の問題は::

  member.getProperty('formtooltips', showdefault)

でProductsフォルダを検索してみたところ、plone_template/header というファイルが引っかかったので、該当箇所を削除することで対処した。実際のところ、削除しちゃって良いのかというと::

  <!-- Old JS from Plone 1.0, remove tal:condition="nothing" if you need to use the old pop-ups.
  Will be removed in Plone 2.1 -->

と書いてあったので問題ないんだろう。多分。

:今日の反省: 問題箇所へのアプローチ方法はそんなに間違ってないと思うんだけど、解決方法に間違いがある、というかよく分からないけど解消したあたりに問題がありそうな。



.. :extend type: text/plain
.. :extend:

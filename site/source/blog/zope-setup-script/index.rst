:date: 2005-12-26 21:30:00
:categories: ['Zope']
:body type: text/x-rst

====================================================
Zopeインスタンス作成時の定型作業をスクリプトで自動化
====================================================

Zopeのインスタンスをmkzopeinstanceで作った後、たいていの場合management_page_charsetを設定したり、Ploneインスタンスを作ったり、portal_catalogのZCTextIndexをejSplitterに置き換えたりします。そんな定型作業はスクリプト化してしまえ！ということでやってみました。

この ZopeSetupScript_ スクリプトを以下のように使います。

.. topic:: zopectl run zopesetupscript.py
  :class: dos

  C:> zopectl run zopesetupscript.py


まだ、ZCTextIndex差しかえがうまくいってない感じなのが残念無念。とりあえずコメントアウトしておこう。

.. _ZopeSetupScript: http://www.freia.jp/taka/memo/zopesetupscript.py/file_view


.. :extend type: text/x-rst
.. :extend:

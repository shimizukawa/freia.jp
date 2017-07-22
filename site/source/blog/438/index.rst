:date: 2007-04-09 00:54:00
:categories: ['turbogears']
:body type: text/x-rst

========================================
2007/04/09 patchだらけのtgdatacontroller
========================================

`TurboGearsのお手軽Controller`_ として作成したtgdatacontrollerですが、利用するためにはSQLObjectやtgfastdataにpatchを手動で当てる必要があります。いちおうそれぞれtrackerに報告はしたのですが、本流に取り込まれるまでは、パッチ当て面倒＆動作保証が怪しい気がする、と、startupはあまりスムーズじゃない気がします。しかもtgfastdataについては0.9a6から更新が無くて、修正してくれるのかどうか怪しい感じ。

以下、適用の必要があるpatch（報告分＋既に報告されていた分）です。

- sqlobject/col.py

  - fix: ForeignKey validation.
         http://sourceforge.net/tracker/index.php?func=detail&aid=1696359&group_id=74338&atid=540672

  - fix: datetime validation.
         http://sourceforge.net/tracker/index.php?func=detail&aid=1696365&group_id=74338&atid=540672

- turbogears/paginate.py

  - fix: paginate page controll.
         http://trac.turbogears.org/ticket/1321

- tgfastdata/formmaker.py

  - fix: typo: column_widget_date_col to column_widget_datetime_col.
         http://trac.turbogears.org/ticket/1350

  - fix: ForeignKey field name include ID. (is correct?)
         http://trac.turbogears.org/ticket/1294

SQLObjectについては再現テストを作成してみました。
http://svn.freia.jp/open/tgdatacontroller/trunk/patch/sqlobject/tests/

.. _`TurboGearsのお手軽Controller`: http://www.freia.jp/taka/blog/437


.. :extend type: text/html
.. :extend:


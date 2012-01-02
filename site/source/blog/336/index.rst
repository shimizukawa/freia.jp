:date: 2006-04-25 10:58:46
:categories: ['Zope']
:body type: text/x-rst

=============================================================
2006/04/25 久しぶりにZope3をupdateしたら色々とDeprecatedに...
=============================================================

*Category: 'Zope'*

昨日、Zope3のtrunkを久々にupdateしたところ、起動時に4つくらいDeprecationWarningが表示されるようになってしまった。全部ZCMLのディレクティブについてのWarningで、

- content -> class
- vocabulary -> utility
- factory -> utility

に変わったらしい。これ以外も、 `Zope3Book`_ の内容からは色々な部分が変わってしまっているので、本の通りにサンプルを作っても動かないこともあるかも。かといってOnlineHelpでは仕組みとか概念は勉強できないからなぁ‥‥。

.. _`Zope3Book`: http://www.zope.org/Wikis/DevSite/Projects/ComponentArchitecture/Zope3Book


.. :extend type: text/x-rst
.. :extend:


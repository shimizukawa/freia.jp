:date: 2008-06-28 01:25:54
:tags: python

================================================================
Python温泉3,  1日目深夜. buildbotのバグを報告してみる
================================================================

`buildbot-0.7.7`_ のマイナーなバグを見つけたっぽいので、レポートを出してみました。
マイナーバグなので症状に遭遇する人は少ないかもしれません。

svn://.../ を使ってSubversionにcommitするとauthorが記録されません。このような使い方をしているSubversionリポジトリをbuildbotのSVNPollerでポーリングしているとauthorを取得しようとしてエラーになります。

といことで以下のレポートで超簡易なパッチを添付してみました。

- http://buildbot.net/trac/ticket/307

.. _`buildbot-0.7.7`: http://buildbot.net/


.. :extend type: text/html
.. :extend:


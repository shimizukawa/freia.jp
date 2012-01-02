:date: 2007-03-11 01:11:17
:categories: ['IT-PC']
:body type: text/x-rst

==================================================
2007/03/11 Google AnalyticsとAdWordsのリンクを解除
==================================================

*Category: 'IT-PC'*

Google AnalyticsとAdWordsのリンクを解除することは現時点では出来ない。将来的には実装するつもりらしいという2006年2月のML投稿は見たけど、今はまだない。

そもそもなぜ解除したいかというと、

1. AnalyticsとAdWordsがリンクしているとタイムゾーンはAdWords側が使用される
2. AdWordsのタイムゾーンをGMT-8にしてしまっていた(設定した覚えはない)
3. `AdWordsのタイムゾーン設定は1度しか変更できない (ヘルプより)`_
4. だからAnalyticsのタイムゾーンを変えられない

ということで、 `AnalyticsとAdWordsのリンク解除はフォームから依頼せよ (ヘルプより)`_ に従ってGoogle様にAnalyticsとAdWordsのリンク解除依頼を出してみた。

.. Epigraph::

  AdWordsとAnalyticsのリンク解除をお願いいたします。
  
  Google Analytics アカウントの ID
    UA-xxxxxxx
  
  AdWords のお客様 ID (AdWords アカウントのページ上部に表示
    xxx-xxx-xxxx
  
  以上、よろしくお願いします。


これで解除されれば、タイムゾーンの問題も解決される‥‥はず（自信なし）。


.. _`AdWordsのタイムゾーン設定は1度しか変更できない (ヘルプより)`: https://adwords.google.com/support/bin/answer.py?answer=32346&query=time+zone&topic=&type=f
.. _`AnalyticsとAdWordsのリンク解除はフォームから依頼せよ (ヘルプより)`: http://www.google.co.jp/support/analytics/bin/answer.py?answer=30322&ctx=sibling



.. :extend type: text/html
.. :extend:

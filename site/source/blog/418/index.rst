:date: 2007-03-16 21:17:57
:categories: ['python', 'Programming']
:body type: text/x-rst

===================================
PythonでHTML解析 with BeautifulSoup
===================================

アクセス解析してみたところ、以前書いた `pythonでHTML解析`_ のアクセス頻度がかなり高いことが分かったので、先日の `Python Workshop 04`_ やPython合宿で紹介されていた BeautifulSoup_ でHTML解析するエントリを書いてみようかと思う。というかアクセス解析した時に大量のURLから各ページのタイトルを抜き出したくなって、試しに使ってみた。

.. code-block:: python

  >>> urls = [
  ... "/taka/blog/109",
  ... "/taka/blog/117",
  ... "/taka/blog/135",
  ... "/taka/blog/159",
  ... "/taka/blog/169",
  ... "/taka/blog/171",
  ... "/taka/blog/176",
  ... "/taka/blog/209",
  ... "/taka/blog/223",
  ... "/taka/blog/226",
  ... ]
  >>> import urllib
  >>> base = 'http://www.freia.jp'
  >>> datas = [urllib.urlopen(base+x) for  x in urls]
  >>> datas = [x.read() for x in datas]
  >>> from BeautifulSoup import BeautifulSoup
  >>> BS = BeautifulSoup
  >>> datas2 = [BS(x).title.string.split()[0] for x in datas]
  >>> for id,title in zip(urls,datas2):
  ...   print id,',',title
  ...
  /taka/blog/109 , PloneのユーザーとグループをLDAPで管理する
  /taka/blog/117 , CSSのoverflowプロパティー
  /taka/blog/135 , PSX(DESR-7500)のバグ、D端子ケーブルが届いた
  /taka/blog/159 , FreeBSDのバックアップ
  /taka/blog/169 , pythonでHTML解析
  /taka/blog/171 , vpopmail
  /taka/blog/176 , YetiSportsおもしろすぎ
  /taka/blog/209 , Drag
  /taka/blog/223 , 新大久保の餃子「味むら」
  /taka/blog/226 , Apacheの認証をLDAPでActiveDirectoryに問い合わせ

**と　っ　て　も　ら　く　ち　ん　だ！**

なんと言っても、 BeautifulSoup.py 1ファイルで済むのが手軽で良いね。site-packagesに置いとこ。

.. _`pythonでHTML解析`: http://www.freia.jp/taka/blog/169
.. _`Python Workshop 04`: http://www.python.jp/Zope/workshop/200612
.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/


.. :extend type: text/html
.. :extend:

:date: 2007-12-28 19:34:30
:categories: ['python']
:body type: text/x-rst

=========================================
2007/12/28 SOAPpyでAmazonにアクセス その2
=========================================

`SOAPpyでAmazonにアクセス`_ の続き。

とりあえず分かったのは、提供されているメソッドに対して渡すパラメータはキーワード引数ではなく辞書で渡す必要があると言うこと。前回の記事のあとキーワード引数でなんどか試していて、正しそうなRequestが出ているもののレスポンスがエラーばっかりだった。

この違いはSOAPpyのドキュメントを読んでいてもなかなか気づかなかった。よくよく読むと SOAPpy-0.12.0/docs/MethodParameterNaming.txt に言及があるんだけど、自分は以下のサイトのコードを参考にしてやっと気づきましたよ。

- `ふってぃろぐ - PythonでSOAP版Amazon Web Service`_


実際にやってみると、キーワード引数の場合は以下のようにエラーになる。

.. code-block:: python

    >>> from SOAPpy import WSDL
    >>> proxy = WSDL.Proxy('http://soap.amazon.com/schemas3/AmazonWebServices.wsdl')
    >>> results = proxy.KeywordSearchRequest(keyword='python',
    ...                                      page='1',
    ...                                      mode='books-jp',
    ...                                      locale='jp',
    ...                                      type='lite',
    ...                                      tag='freiaweb-22',
    ...                                      devtag='D2XXXXXXXXXXX')
    ...
    Traceback...
    ...
    SOAPpy.Types.faultType: <Fault SOAP-ENV:Client: We encountered an error at
    our end while processing your request. Please try again
    : The request contains an invalid SOAP body.>
    >>>

以下は辞書渡しにしたらうまくいった例。

.. code-block:: python

    >>> from SOAPpy import WSDL
    >>> proxy = WSDL.Proxy('http://soap.amazon.com/schemas3/AmazonWebServices.wsdl')
    >>> results = proxy.KeywordSearchRequest(dict(keyword='python',
    ...                                           page='1',
    ...                                           mode='books-jp',
    ...                                           locale='jp',
    ...                                           type='lite',
    ...                                           tag='freiaweb-22',
    ...                                           devtag='D2XXXXXXXXXXX'))
    ...
    >>> results.TotalPages
    '3'
    >>> results.TotalResults
    '27'
    >>> book0 = results.Details[0]
    >>> book0.Asin
    '4797341815'
    >>> book0.ProductName
    u'\xe3\x81\xbf\xe3\x82\x93\xe3\x81\xaa\xe3\x81\xaePython Web\xe3\x82\xa2\xe3
    \x83\x97\xe3\x83\xaa\xe7\xb7\xa8 [\xe3\x81\xbf\xe3\x82\x93\xe3\x81\xaa\xe3
    \x81\xae\xe3\x82\xb7\xe3\x83\xaa\xe3\x83\xbc\xe3\x82\xba]'

ここで、ProductNameがへんな事になっている。中身はutf-8なのにu'...'になっていてうまく扱うことができない。とりあえず以下のようにして表示。

.. code-block:: python

    >>> print ''.join([chr(ord(x)) for x in book0.ProductName]).decode('utf-8')
    みんなのPython Webアプリ編 [みんなのシリーズ]

はて、コレを直すにはどうすればよいのだろうか...。SOAPpyが xml.sax でparseするときに正しくなるようにする方法があるのかなあ。

ところで、proxy.KeywordSearchRequestはうまくいくようになったけど、proxy.AsinSearchRequestはまだうまくいかない。何故だ！？

.. _`SOAPpyでAmazonにアクセス`: http://www.freia.jp/taka/blog/504/edit
.. _`ふってぃろぐ - PythonでSOAP版Amazon Web Service`: http://sun.ap.teacup.com/futot/21.html


.. :extend type: text/html
.. :extend:


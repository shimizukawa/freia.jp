:date: 2007-12-17 23:49:41
:categories: ['python']
:body type: text/x-rst

========================
SOAPpyでAmazonにアクセス
========================

実は今までSOAPを実際に触ったことがありませんでした。今回ちょっと必要があったので勉強中です。
とりあえず `python soap` で検索して見つけたIBM developerWorksの記事に目を通します。

`Python Web Servicesデベロッパー: Python SOAPライブラリー`_

で、次にSOAPpyをインストール。先にfpconstが必要っぽいです。

.. topic:: install
  :class: dos

  | C> easy_install fpconst
  | C> wget http://nchc.dl.sourceforge.net/sourceforge/pywebsvcs/SOAPpy-0.12.0.tar.gz
  | C> tar zxf SOAPpy-0.12.0.tar.gz
  | C> cd SOAPpy-0.12.0
  | C> python setup.py install
 
インストール完了。

次に、SOAPpy-0.12.0.tar.gzに同梱されていたサンプルコードを色々試してみようと思ったのですが、サンプルコードが利用しているURLのほとんど(全て？)が閉鎖されてしまっていたので、Amazonを例にして試してみようと思います。

.. code-block:: python

    >>> from SOAPpy import WSDL
    >>> proxy = WSDL.Proxy('http://soap.amazon.com/schemas3/AmazonWebServices.wsdl')
    >>> proxy.methods
    {u'ActorSearchRequest': <SOAPpy.wstools...>,
     u'AddShoppingCartItemsRequest': <SOAPpy.wstools...>,
     u'ArtistSearchRequest': <SOAPpy.wstools.WSDLTools...>,
     u'AsinSearchRequest': <SOAPpy.wstools.WSDLTools...>,
    ...

とりあえず、wsdlファイルからメソッドを取得することが出来ました。しかし、実際の呼び出しは次のようにうまくいきませんでした。

.. code-block:: python

    >>> proxy.AsinSearchRequest()
    faultType: <Fault SOAP-ENV:Client:
    We encountered an error at our end while processing
    your request. Please try again: The request contains
    an invalid SOAP body.>

ううむ、引数に何を渡せば良いんだろう？WSDLには定義されてるんだろうけど、interactive shellで表示できると良いなあ‥‥、というところで、次回に続く。


.. _`Python Web Servicesデベロッパー: Python SOAPライブラリー`: http://www.ibm.com/developerworks/jp/webservices/library/ws-pyth5/


.. :extend type: text/html
.. :extend:

:date: 2005-10-18 21:35:00
:categories: ['Zope', 'python']
:body type: text/x-rst

==============================================
2005/10/18 Zopeから既存のCGIを動かす方法って？
==============================================

*Category: 'Zope', 'python'*

`mixiの新着情報をRSSで取得`_ で使ったRSS取得CGIはPerl製なので、うちのZopeサーバーで動かすのは微妙にめんどくさい。

- FrontにApacheを立てて、特定のURLだけApacheに実行させる
- ZopeがREQUESTを受けて、ExternalMethodでCGIを実行
- 他、何か無いか...(絶対Productとかありそう)

Apache使うのが普通かも。でも今回はExternalMethodでやってみた。


.. _`mixiの新着情報をRSSで取得`: http://www.freia.jp/taka/blog/259



.. :extend type: text/plain
.. :extend:

.. code-block:: python

    def feed(self):
        from urlparse import urlparse
        import os
        request = self.REQUEST
    
        url = request.get('URL')
        u = urlparse(url)
        os.putenv('SERVER_PORT', u[0].find('https') and '443' or '80')
        os.putenv('SERVER_NAME', u[1])
        os.putenv('REQUEST_URI', u[2])
        pi,po,pe = os.popen3("/usr/local/www/ZInstance/Extensions/feed.cgi")
        return po.read()

これをExternalMethodから呼ぶようにする。Extensionsディレクトリに置いた上記コードのファイルのオーナーがZope実行ユーザーになっていなかったり、ファイルを書き換えたらExternalMethodもSaveしないと反映されなかったり、selfが渡ることを知らなかったり、まあけっこう苦労した。いやこんなので苦労してちゃだめなんだが‥‥。

とりあえずCGIが使う環境変数だけでっちあげて完成。ああ、環境変数も最初SERVER_NAMEをそのままコピーしたら公開サーバー名じゃなくてローカルサーバー名になってしまったんだっけ‥‥。



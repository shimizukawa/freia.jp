:date: 2004-04-24 17:10:04
:tags: Memo, Zope

=============================================================
ZWikiでコメント追加後にOperaでリロードされない問題
=============================================================

`ZWiki <http://zwiki.org>`_ で以前から気になっていた挙動に、"コメント追加後にOperaでリロードされない"という問題があります。ただ、コメント追加後にリロードするとちゃんとコメントは追加されているようです。



.. :extend type: text/plain
.. :extend:

これについてもResponseHeaderのContent-Typeを調べたとき同様パケットキャプチャーしてみたところ、POSTメソッドでコメント追加を行った後で以下のような応答がサーバーからありました::

  HTTP/1.1 302 Moved Temporarily
  Date: Sat, 24 Apr 2004 06:56:13 GMT
  Content-Length: 0
  Etag: 
  Location: http://www.freia.jp/taka/test/zwiki28/X_e5_ae_9f_e9_a8_93_e7_94_a8#bottom
  Content-Type: text/plain; charset=UTF-8

また、ZWiki以外の掲示板ではどうなるのかな、と思って、COREblogのコメント追加で実験してみました::

  HTTP/1.1 302 Moved Temporarily
  Date: Sat, 24 Apr 2004 08:02:07 GMT
  Content-Length: 36
  Etag: 
  Content-Type: text/plain; charset=UTF-8
  Location: http://www.freia.jp/taka/test/blog/4
  X-Pad: avoid browser bug

  http://www.freia.jp/taka/test/blog/4

一番の違いは、後者には本文にLocationと同じURIがあることです。もしかしたらこれが原因？と思い、 `RFC2616 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>`__  を読んでみましたが‥‥よく分かりませんでした(^^;; ZWiki改造して本文にもURI書いたら直るかなぁ‥‥

#実はX-Padの方が原因だったりして。


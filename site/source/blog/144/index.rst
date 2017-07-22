:date: 2005-02-23 01:03:50
:categories: ['Zope']
:body type: text/x-rst

============================================================
2005/02/23 ZPhotoSliderの画像を表示するportlet_recent_images
============================================================

ploneの便利な点は、拡張性が高いことで、ちょっとHTML(PageTemplate)を書くと「最近公開の画像」という感じでページの左や右に配置することができる。

先日ZPhotoSliderを追加した際に思いついて早速作ってみた。‥‥が、ちょっと横幅取りすぎ。ZPhotoSliderから適切な画像サイズを取得する、あるいは取得した画像を適切なサイズに縮小するひつようがあるんだけど、どうやるんだろう？

‥‥と、簡単に配置できたようなことを書いてるけど、実はものすごい悩んだ。ZCatalogのresultって実オブジェクトじゃなくてカタログインデックスオブジェクト(?)なのね‥‥。

portal_catalog.searchResults()にオブジェクトタイプを指定したまではよかったんだけど‥‥そこから先が分からずにかなり悩んだ。

誤::

  <img tal:replace="structure python:obj.getSymbolicTag()"/>

正::

  <img tal:replace="structure python:obj.getObject().getSymbolicTag()"/>

いままでZCatalogなんてさわったこと無いからなぁ‥‥。



.. :extend type: text/plain
.. :extend:


:date: 2006-04-08 00:58:58
:categories: ['Zope']
:body type: text/x-rst

=========================================================
2006/04/08 全ページにURLのQRコードを表示するZope3アダプタ
=========================================================

先日、 `日本のZope情報`_ 経由で `python で QR コード`_ という記事を見て、早速Zopeで使えるようにZope3用プロダクトを作ってみました。

:Zope.org: http://www.zope.org/Members/shimizukawa/
:SVN: http://svn.freia.jp/open/z3qrcodeadapter
:Download: http://www.freia.jp/taka/svn/svnview/getExportZip?path=z3qrcodeadapter/tags/0.1&revision=117

タイトルとURLから自動生成してくれるので、細かいことを考えずに全ページにQRコードを表示したい場合はこれで十分だけど、ページ毎に埋め込みたい情報が違う場合はもうちょっと手を入れないといけません。

作った勢いついでに、zope.orgにも登録してみました。承認されたらそのうち出てくるでしょう。
あと、パッケージングのためのドキュメントやライセンスのテンプレートが少しずつ溜まってきたので、パッケージングの手間が最初(ATCTSmallほげほげ)に比べたら大分早くなってきた気がします（勢いで30分くらいでzope.orgに登録できるくらいには）。

Zope3用が一段落したので、めんどくさいZope2用の作成をしようと思ったのですが、Five使えば実は簡単に作れるのかな？

.. _`日本のZope情報`: http://coreblog.org/jp/jzi
.. _`python で QR コード`: http://mooya.ath.cx/CubeDeZope/2006/04/20060404004544

.. :extend type: text/x-rst
.. :extend:


.. :comments:
.. :comment id: 2006-04-08.6380364954
.. :title: Re:全ページにURLのQRコードを表示するZope3アダプタ
.. :author: masaru
.. :date: 2006-04-08 20:27:19
.. :email: 
.. :url: 
.. :body:
.. おお、すばらしい
.. 

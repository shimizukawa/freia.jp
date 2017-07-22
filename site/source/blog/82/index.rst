:date: 2004-11-20 16:39:38
:tags: Zope
:body type: text/x-rst

=================================
2004/11/20 Zopeでナビゲーション２
=================================

`先ほど`_ 作ったナビゲーション用の仕組みはstandard_html_headerに仕込んでいるのだが、COREblogではstandard_html_headerを読み込まないようになっているようなので、standard_html_headerを読み込むように修正してみた。

と言っても、ごくごく簡単で、blog_headerの中身を::

  <dtml-var standard_html_header>

の一行に置き換えただけ。
ただ、これだけだと元のblog_headerにせっかく書いてある *<link rel="alternate" ...>* を消してしまうことになるので、contentsフォルダ内に alternate という名前でPython Scriptを書いて、元々書いてあったタグを返すように変更した。

また、同様にstyle seetの読み込みも消えてしまう、というかstandard_html_headerで指定しているものに置き換わってしまう。自分の場合、standard_html_headerでは default.css というのを読み込んでいるため、先ほどと同様にcontentsフォルダ内に default.css という名前のDTML Methodを作成して、中に一行::

  @import url("style_css");

としてあげた。

これでCOREblogのページでもナビゲーションが表示されるはず。対応ブラウザの方、表示されてますか？（笑）

実は、 `先ほど`_ のnavigationスクリプトはCOREblogで上記の処理をしたときに発生した問題の対処がされている。というのは、ナビゲーション名 "search" がCOREblogのプロパティー(?)とぶつかってしまっていたため、 search.meta_type なんてアクセスするとエラーになってしまっていたのだ。というかそもそもナビゲーションの名前は up とか next とかなのであちこちぶつかりそうな予感がしなくもない。

さて、どうしよう‥‥。


.. _`先ほど`: http://www.freia.jp/taka/blog/81



.. :extend type: text/plain
.. :extend:



.. :comments:
.. :comment id: 2005-11-28.4540920650
.. :title: Re: Zopeでナビゲーション２
.. :author: つかぽん
.. :date: 2004-11-21 21:16:40
.. :email: 
.. :url: http://jab-an.plus9.info/
.. :body:
.. Firefox1.0+LinkToolbar0.9で動きましぇーん。
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4542069115
.. :title: Re: Zopeでナビゲーション２
.. :author: つかぽん
.. :date: 2004-11-21 21:20:29
.. :email: 
.. :url: http://jab-an.plus9.info/
.. :body:
.. ちなみに動かないのは前後移動ね。
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4543212418
.. :title: Re: Zopeでナビゲーション２
.. :author: 清水川
.. :date: 2004-12-06 01:41:09
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. 実は前後は実装してないのでした。まだ親階層とホームだけです。
.. 
.. で、今日ちょっとやってみたけどこれがなかなか‥‥むずいーー
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4544358357
.. :title: Re: Zopeでナビゲーション２
.. :author: 清水川
.. :date: 2004-12-06 02:10:38
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. できました。分かってみたら簡単でした。
.. 
.. 	return '' % item.entry_url()
.. 
.. と書くべき所を
.. 
.. 
.. としていたのが原因。関数オブジェクトをforループに渡してもうまく動く訳がなかったという‥‥。DTMLとごっちゃになってるなあ。
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4545502823
.. :title: Re: Zopeでナビゲーション２
.. :author: つかぽん
.. :date: 2004-12-07 20:40:52
.. :email: 
.. :url: http://jab-an.plus9.info/
.. :body:
.. おお、動いた動いた。

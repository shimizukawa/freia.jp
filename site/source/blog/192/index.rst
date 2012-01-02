:date: 2005-04-26 08:55:28
:categories: ['Zope', 'Plone']
:body type: text/x-rst

========================
COREBlog1.2+Plonified0.8
========================

`COREBlog 1.2a1`_ がML限定公開されました。同時にCOREBlogをPloneと融合して表示するためのSkin, Plonified0.8 が公開されています。

ということで、早速 `実験してみました`_ 。Plone対応という事でCOREBlogオブジェクトのプロパティーが変更になっているため、Plonifiedを使う場合は一度SkinをPlonifiedに切り替えるか、skin/plonified/skin_propertiesを実行する必要があります。また、これまでPloneインスタンス以下にCOREBlogをおいた場合に `ちょっとした問題`_ があったのですが、それも修正されていました。

ということで、まだちょっとしか触っていませんが、大体問題なく動作するようです。一部、COREBlogがCMF対応プロダクトではないために、ナビゲーションやパンくず表示がおかしくなるようですが、分かる部分についてはSkin(ZPT)をいじりながら修正してみようと思います。

とりあえずは、 `旧日記`_ っぽい表示にしてみようかな。あと、refererやZWeatherも表示追加しないと。


.. _`COREBlog 1.2a1`: http://coreblog.org/ats/637
.. _`実験してみました`: http://www.freia.jp/taka/blog/skin/plonified
.. _`ちょっとした問題`: http://www.freia.jp/taka/blog/139
.. _`旧日記`: http://www.freia.jp/taka/taka_old/diary/




.. :extend type: text/plain
.. :extend:


.. :comments:
.. :comment id: 2005-11-28.4946007441
.. :title: Re: COREBlog1.2+Plonified0.8
.. :author: naka-z
.. :date: 2005-04-26 23:08:34
.. :email: 
.. :url: 
.. :body:
.. これやばいっすね！。さっきメールチェックしてて存在しりました
.. 今出張中なので戻ったら早速導入しようと思ってます。
.. 
.. P.S.　コメント入力時は普通の画面になるんですね
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4947155159
.. :title: Re: COREBlog1.2+Plonified0.8
.. :author: 清水川
.. :date: 2005-04-27 23:30:00
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. コメント入力時に以前のスタイルになってしまうのは、URLを見ると分かるのですが、skin/plonified で表示しなくなるからですね。これはCOREBlogに設定したblog_urlがコメント入力等のリンク先に使用されるためだとおもいます。
.. 
.. それにしても、プロダクトをCMF対応しなくてもこういうことが出来る、というのは勉強になりますねー。

:date: 2005-06-03 00:16:18
:categories: ['Plone', 'Zope']
:body type: text/x-rst

===========================================================
2005/06/03 plonifiedなCOREBlogのトップページにRDFを埋め込む
===========================================================

`トップページに各記事の RDF がコメントされない２ - Feel Fine!`_ でplonifiedのindex_htmlにRDFが埋め込まれない問題について対策されていますが、別アプローチで対応してみました。以下ようにplonifiedのindex_html(19行目あたり)を修正する、というので合ってるかな？

.. code-block:: xml

  <div tal:repeat="entry python:here.rev_day_entry_items(count=here.top_days)">
  <!-- Entry RDF -->
  <span tal:replace="structure python:here.entry_rdf(entry)" />
  <div metal:use-macro="here/entry_macros/macros/entrybody">



.. _`トップページに各記事の RDF がコメントされない２ - Feel Fine!`: http://forestlaw.ddo.jp/blog/58


.. :extend type: text/plain
.. :extend:
最初、RDFを挿入するだけだろ！と思って replace="structure here/entry_rdf" なんて書いたらNGでした。そりゃそうだ、と思いつつ replace="structure entry/entry_rdf" と書いてまたNG。PATH式はcontextを切り替えてくれないので、entry_rdfをentryに対して実行しているわけではないからです。ならば実行対象のcontextを渡してあげれば、、、という事で上記のコードになりました。

ところで、自分はRDFとPINGの関係について全く知らないので、 ```なぜそれがPING時に困ったことになるのか``` が分かっていません。あとでgoogleで調べてみます。





.. :comments:
.. :comment id: 2005-11-28.5073046278
.. :title: Re: plonifiedなCOREBlogのトップページにRDFを埋め込む
.. :author: JJ
.. :date: 2005-06-03 09:14:53
.. :email: 
.. :url: http://forestlaw.ddo.jp/blog/
.. :body:
.. これがやりたかったんですよ。
.. ありがとうございます。
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.5074189453
.. :title: Re: plonifiedなCOREBlogのトップページにRDFを埋め込む
.. :author: 清水川
.. :date: 2005-06-03 12:35:20
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. お役に立てたようで(^^
.. 
.. RDFの埋め込みに関して調べてみたところ、以下のサイトが見つかりました。
.. サンプルでindexページ（複数エントリが表示されているページ）に対してAuto-Discoveryを行っているみたいですね。必要条件かどうかはわかりませんが・・・。
.. 
.. 
.. 
.. :Trackbacks:
.. :TrackbackID: 2005-11-28.5075336902
.. :title: COREBlogのplonifiedスキン対策
.. :BlogName: Pingサーバ開発日記
.. :url: http://ping.glyle.com/blog/5
.. :date: 2005-11-28 00:48:27
.. :body:
.. さすが清水川さん。対策をしていらっしゃいました。
.. 私も対策を立てていましたが、もっと複雑に考えていてこの対策が一番簡単であるということが判りました。
.. plonifiedなCOREBlogのトップページにRDFを埋め込む
.. ##Ping送信時には、BlogURL,BlogTitleなどは送信されてきますが、...

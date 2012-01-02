:date: 2005-05-09 08:45:30
:categories: ['Plone']
:body type: text/x-rst

========================================
2005/05/09 COREBlogのRSS用metaタグを追加
========================================

*Category: 'Plone'*

COREBlog関連のポートレットやカスタマイズをぼちぼちやっていく予定ですが、とりあえず、 `takanory.net`_ さんのRSSフィードアイコン追加を参考に、「最近のBlogエントリ」にアイコンを追加しました。

あと、RSSフィード用のmetaタグをheaderに仕込むために、plonified/index_html, entry_html 等の *fill-slot="main"* を持っているZPTファイルに以下のコードを追加しました。

.. code-block:: xml

    <metal:main fill-slot="head_slot">
        <link rel="alternate"
              type="application/rss+xml"
              title="RSS 0.91"
              href=""
              tal:attributes="href string:${here/blogurl}/rdf91_xml" />
        <link rel="alternate"
              type="application/rss+xml"
              title="RSS 1.0" href=""
              tal:attributes="href string:${here/blogurl}/rdf10_xml" />
        <link rel="EditURI"
              type="application/rsd+xml"
              title="RSD"
              href=""
              tal:attributes="href string:${here/blogurl}/rsd_xml" />
    </metal:main>


# `SyntaxColoring`_ も使わせてもらっています。柴田さんありがとうございます.

.. _`takanory.net`: http://takanory.net/takalog/183/
.. _`SyntaxColoring`: http://coreblog.org/ats/640



.. :extend type: text/plain
.. :extend:



:Trackbacks:
:TrackbackID: 2005-11-28.4993996777
:BlogName: Feel Fine!
:url: http://forestlaw.ddo.jp/blog/44
:date: 2005-11-28 00:48:19

================================================================
2005/11/28 PlonifiedでもFirefoxなどがRSSを見つけられるようにする
================================================================

*Category: 'Plone'*

COREBlogのRSS用metaタグを追加（清水川記）を参考に Feel Fine!
でも Mozilla Firefox などが RSS を見つけられるようにした。 Zope で
Syntax Coloring（TRIVIAL TECHNOLOGIES）もすばらしいなぁ。
reStructuredTextの書き方が解らないので手を出さなかったのだが、後でやってみよう。

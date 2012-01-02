:date: 2006-12-26 11:30:00
:categories: ['python']
:body type: text/x-rst

==============================
2006/12/26 自前RSSアグリゲータ
==============================

複数のRSSを集約してRSS2.0で出力する機能があると便利かなー、と思って feedparser_ を使ってちょろっと書いてみました。集約して最新を取り出す部分は10行程度。feedparser便利だなあ。

.. code-block:: python

    # -*- coding: utf-8 -*-
    # http://feedparser.org/
    import feedparser
    
    # RSS URL list for aggregation.
    urls = [
        'http://pc.watch.impress.co.jp/sublink/pc.rdf',
        'http://internet.watch.impress.co.jp/cda/rss/internet.rdf',
        'http://www.watch.impress.co.jp/av/sublink/av.rdf',
    ]
    
    d=[]
    # get early 10 entries.
    for u in urls:
        f=feedparser.parse(u)
        for e in f.entries:
            d.append((e.updated_parsed,e.updated,e.title,e.link))
    d.sort()
    d.reverse()
    d = d[:10]
    
    
    # print 10 entries with RSS2.0 format.
    template = u'''<?xml version="1.0"?>  
    <rss version="2.0">
      <channel>
        <title>%(site_title)s</title>
        <link>%(site_link)s</link>
        <description>%(site_desc)s</description>
    %(items)s
      </channel>
    </rss>
    '''
    
    item_tmpl = u'''
        <item>
          <title>%(item_title)s</title>
          <link>%(item_link)s</link>
          <description>%(item_desc)s</description>
          <pubDate>%(item_date)s</pubDate>
        </item>
    '''
    
    item_list = []
    for x in d:
        item_date, item_title, item_link = x[1],x[2],x[3]
        item_desc = u''
        item_list.append(item_tmpl % locals())
    
    items = u''.join(item_list)
    site_title = u'Impress'
    site_link = u'http://watch.impress.co.jp/'
    site_desc = u''
    
    print template % locals()
    

ちなみに、RSSで再出力するだけだと全然意味無かったです。集約なんてRSSリーダがやってくれるもの。。。


.. _feedparser: http://feedparser.org/


.. :extend type: text/html
.. :extend:


.. :comments:
.. :comment id: 2006-12-28.7951504173
.. :title: Re:自前RSSアグリゲータ
.. :author: M.Shibata
.. :date: 2006-12-28 03:23:17
.. :email: 
.. :url: 
.. :body:
.. 本題ではないのですが、最後の一行が勉強になりました。
.. こんなやりかたもあるんですね。
.. 
.. :comments:
.. :comment id: 2006-12-29.4569941967
.. :title: Re:自前RSSアグリゲータ
.. :author: しみずかわ
.. :date: 2006-12-29 04:17:38
.. :email: 
.. :url: 
.. :body:
.. > こんなやりかたもあるんですね。
.. 
.. 怠け者なので(笑)
.. 明示的でない方法なので、時々はまります。あまりお勧めはしません...

:date: 2005-12-16 01:52:30
:tags: Zope
:body type: text/x-rst

========================================
2005/12/16 ZopeをApacheのSSLで動かすメモ
========================================

ポイントは、RewriteRuleのVurtualHostBaseの後ろにhttpsと書くこと。ここをhttpで書いてしまうと、Zope君がページを構築するときに同一サーバー内へのリンクをhttpで書いてしまう。

‥‥と、syd.jpの中の人に教わった。詳しくは http://wiki.zope.jp/VHMSetupSample2 を参照。

前提
-----
- ZopeにVirtualHostMonsterがあること(2.7.5からrootに標準である)
- ApacheのSSL設定が終わっていること

設定
----

Apacheのssl.conf::

  RewriteEngine On
  RewriteRule ^/(.*) http://localhost:8080/VirtualHostBase/https/www.freia.jp:443/VirtualHostRoot/$1 [P,L]

manage等にアクセスしたら自動的にhttpsに迂回するhttpd.conf::

  # forwarding to https for manage aceess.
  RewriteRule ^(.*)/manage$ https://www.freia.jp$1/manage [L]
  RewriteRule ^(.*)/manage_(.*) https://www.freia.jp$1/manage_$2 [L]

  # proxy to zope server.
  RewriteRule ^/(.*) http://localhost:8080/VirtualHostBase/http/www.freia.jp:80/VirtualHostRoot/$1 [P,L]


.. :extend type: text/x-rst
.. :extend:


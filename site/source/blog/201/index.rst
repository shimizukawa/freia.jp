:date: 2005-05-06 10:53:35
:categories: ['work']
:body type: text/x-rst

===========================================
今日は会社でFreeBSD5.3 on DELL PowerEdge800
===========================================

社内サーバー用に購入した `DELL PowerEdge800`_ にFreeBSD5.3で環境構築中。Broadcom 5721用のドライバが無かったので、 `FreeBSD5-stableのソースを取ってきてdiffして`_ if_bgeにパッチしました。

チップの定義を追加するくらいなら、カーネルソースを全く読んだことが無くても出来るけど、動作の保証はヒトバシラーになって使ってみるしか無いわけで。この辺、即対応可能なオープンソースの強みでもあり、保証がない（自分で保証を作っていくしかない）という弱みでもあるなぁ。というか会社のサーバーで人柱するなと。


.. _`DELL PowerEdge800`: http://www1.jp.dell.com/content/products/productdetails.aspx/pedge_800?c=jp&l=jp&s=soho&~tab=specstab#tabtop

.. _`FreeBSD5-stableのソースを取ってきてdiffして`: http://www.freebsd.org/cgi/cvsweb.cgi/src/sys/dev/bge/if_bge.c.diff?r1=1.72.2.2%3ARELENG_5_3&tr1=1.82&r2=1.72.2%3ARELENG_5&tr2=1.72.2.10.2.1


.. :extend type: text/plain
.. :extend:

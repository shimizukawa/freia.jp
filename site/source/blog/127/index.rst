:date: 2005-01-26 21:33:31
:tags: Unix, work
:body type: text/x-rst

================================================
2005/01/26 FreeBSDのインストーラのkernel入れ替え
================================================

FreeBSDの4.11-Releaseでは、ICH6がサポートされていないためにSATA150を認識してくれない。あまつさえIntel915なマザーでSATAなHDDが搭載されていると、インストーラの起動途中でハングアップしてしまう。

で、 調べてみたら `デバイス名の定義を追加するだけ`_ で動いてくれそうなので、別のPCに入れたFreeBSDのカーネルソースにパッチを当てて試してみたところ問題なく動作している。ついでにインストーラのkernelを入れ替えれば万事OK!‥‥でもやりかたが分からない。

ということでさらに調べたら `本家ML`_ と `QandA`_ でヒントを見つけた。これでCDのインストーラーイメージを編集して試してみよう。。

.. _`デバイス名の定義を追加するだけ`: http://archive.pilgerer.org/mharc/html/freebsd-stable/2004-09/msg00125.html
.. _`QandA`: http://www.jp.freebsd.org/cgi/print-QandA.cgi?QandA=1451
.. _`本家ML`: http://home.jp.freebsd.org/cgi-bin/showmail/FreeBSD-users-jp/60516




.. :extend type: text/plain
.. :extend:


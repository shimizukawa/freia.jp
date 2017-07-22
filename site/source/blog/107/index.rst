:date: 2005-01-15 17:35:56
:categories: ['Unix']
:body type: text/x-rst

===========================================
2005/01/15 実験用LDAPサーバーをjailで立てる
===========================================

Plone_ のユーザー・グループ管理をLDAPで行うための実験をしようとして、さすがに運用中の Zope_ やLDAPを使って実験するのは怖いのですべて実験用に環境を用意することにした。

で、ちょっと調べてみたけれどOpenLDAPを同一サーバー上に複数立てる方法がわからなくて、しょうがないのでJailで環境を作って立てることにした。ところが、実際にLDAPに行き着くまで結構時間がかかってしまった。

1. FreeBSD-5.2.1-Releaseのソースをcvsupで取ってくる (cvsupに15分)
2. `FreeBSD 5.1-Release でJAILを試すメモ`_ を参考にjail環境を作成する (make world に1時間)
3. ports環境の用意 (cvsupに15分)
4. portsからOpenLDAPをインストールする (make install に30分)

ほとんどが待ち時間というのが‥‥。しかも、LDAPの環境作成してからやっと本題が始まる。遠い‥‥。

.. _Plone: http://plone.jp/
.. _Zope: http://zope.jp/
.. _`FreeBSD 5.1-Release でJAILを試すメモ`: http://www.fkimura.com/jail0.html



.. :extend type: text/plain
.. :extend:


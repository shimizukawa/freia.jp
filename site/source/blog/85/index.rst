:date: 2004-12-07 01:16:55
:categories: ['Zope', 'python']
:body type: text/x-rst

==============================
2004/12/07 ZopeのPython2.4動作
==============================

*Category: 'Zope', 'python'*

FreeBSDのportsで、Zopeが利用するPythonのバージョンが2.4から2.3に戻された。これ自体は良いとして、問題はPython2.4ベースで入れてしまった自宅サーバーのZopeの扱いをどうするか。

1. make.conf(かpkgtools.conf？)にPython2.4を使うように設定してみる
2. Python2.3を使うようにして入れ直す

‥‥問題が出るまではとりあえず１かな（COREBlogは問題じゃないのか？）。同サーバーを利用しているユーザー様にも意見を聞いてみよう。



.. :extend type: text/plain
.. :extend:

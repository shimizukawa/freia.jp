:date: 2005-07-18 21:14:00
:categories: ['Zope']
:body type: text/x-rst

============================================================
2005/07/18 NetDriveというWebDAVをDrive名にマウントするツール
============================================================

*Category: 'Zope'*

会社でSubversionを使っている。というか勝手に使い始めた。で、WebDAV使えば、開発しないけどソースは見たい＆丸ごと取得したい、という用途にピッタリだなーと思いながら `Subversion によるバージョン管理`_ を読んでいたところWindowsのWebフォルダはイケテナイらしいと言うことが分かった。

.. _`Subversion によるバージョン管理`: http://subversion.bluegate.org/doc/book.html



.. :extend type: text/x-rst
.. :extend:
.. highlights::

  この問題の回避策として他にもさまざまなうわさがありますが、
  Windows XP のすべてのバージョンとパッチレベルでうまく
  動作するものはなさそうです。私たちのテストでは今示した
  アルゴリズムがどのシステムでも常にうまくいく ように
  思えます。WebDAV コミュニティーの一般的な合意事項として:

  - Webfolder の新しい実装は避けること。古いものを使おう。 

  - Windows XP のファイルシステムレベルのクライアントが
    本当に必要なら、WebDrive か NetDrive を使おう。

  -- `Subversion によるバージョン管理 - Windows Webfolders, WebDrive, Netdrive`_

むむ。 **NetDrive** とな。WebDAVをWindowsのドライブレターにマウントしてくれるとな。これってもしかして、Zopeの ```webdav-source-server``` に利用したら、WebDAVを理解しないエディタ(WZとか)からも編集出来る？

... デキター！

ということで、気になる人は ```NetDrive.exe``` で検索だ。

.. _`Subversion によるバージョン管理 - Windows Webfolders, WebDrive, Netdrive`: http://subversion.bluegate.org/doc/book.html#svn.webdav.clients.windows

追記 7/19
-----------

http://support.microsoft.com/?kbid=287402




:Trackbacks:
:TrackbackID: 2005-11-28.5112182612
:BlogName: 週刊東京Worker　（東京労働者）
:url: http://tkworker.exblog.jp/3425830
:date: 2005-11-28 00:48:31

======================================================
2005/11/28 FTP を仮想ドライブ化する無料ソフト NetDrive
======================================================

*Category: 'Zope'*



NetDrive

英語が苦手な人は、こっち　＞　清水川ｗｅｂ


他に有料版ソフトとしては WebDrive が有名。
こちらは日本語版もあり、FTP だけでなく WebDAV にも対応している。




:Trackbacks:
:TrackbackID: 2006-05-10.1115514921
:BlogName: Jicoo Corp. PukiWiki plus (PukiWiki/TrackBack 0.3)
:url: http://host4.headoffice.jicoo.co.jp/wiki/index.php?Windows%2Ftools%2FNetDrive
:date: 2006-05-10 13:25:12

=================================
2006/05/10 Windows/tools/NetDrive
=================================

*Category: 'Zope'*

Windows    NetDriveでWebDAVフォルダをマウント    NetDriveでWebDAVフォルダをマウント    MaruhanのM-GISでhalldataサーバをNetDriveでマウントしています http://blog.livedoor.jp/dualcomputer/archives/50255738.html http://www.novell.com/coolsolutions/qna/999....


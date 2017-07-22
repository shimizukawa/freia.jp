:date: 2007-02-06 02:18:26
:tags: Unix
:body type: text/x-rst

==========================================
2007/02/06 portupgradeが動作しなくなってた
==========================================

FreeBSDのパッケージ管理はportupgradeで行っていて、毎日 portversion -vL= の結果がメールで送信される仕組みで運用している。で、いくつかのパッケージ更新があったようなのでportupgradeで更新しようとしたら::

  missing key: categories: Cannot read the portsdb!

なんてエラーが出て止まってしまった。あぁ、先週くらいにMLで出てたなあ、とメールを探したら発見。 `90342`_ からのスレッドで回避策が提示されていた。結局、/usr/ports/Makefileの ``.if ${OSVERSION} >= 601101`` あたりをコメントアウトした状態でportupgrade自身をアップデートしてからMakefileのコメントアウトを解除して残りのパッケージも更新した。というか今更新してる最中。ねむ。

.. _`90342`: http://home.jp.freebsd.org/cgi-bin/showmail/FreeBSD-users-jp/90342


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2007-02-06.8674717075
.. :title: Re:portupgradeが動作しなくなってた
.. :author: setomits
.. :date: 2007-02-06 03:07:48
.. :email: 
.. :url: 
.. :body:
.. 僕は FreeBSD は使わないのでまるでわかっていないのですが、
.. FreeBSDユーザは要注意!「ports-mgmt」設置、portupgradeはカテゴリ移動へ (MYCOMジャーナル)
.. http://journal.mycom.co.jp/news/2007/02/05/360.html
.. というあたりが関係あるのでしょうか。
.. 
.. :comments:
.. :comment id: 2007-02-09.4022325718
.. :title: Re:portupgradeが動作しなくなってた
.. :author: Anonymous User
.. :date: 2007-02-09 23:13:22
.. :email: 
.. :url: http://echo.dip.jp/20070205.html
.. :body:
.. 手順としてはここが一番簡潔でした。
.. 
.. :comments:
.. :comment id: 2007-02-18.2473161902
.. :title: Re:portupgradeが動作しなくなってた
.. :author: しみずかわ
.. :date: 2007-02-18 18:17:27
.. :email: 
.. :url: 
.. :body:
.. 情報ありがとうございます。
.. ports-mgmtに移動する前に数日間実行できない状態になってしまっていたようです。
.. 
.. その後、portversion -vL= とかでバージョン一覧を表示すると
.. portupgrade-2.2.2_3,2 (=> 'ports-mgmt/portupgrade')
.. と表示されるようになりました。

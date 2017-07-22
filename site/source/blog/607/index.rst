:date: 2008-08-10 01:04:37
:tags: IT-PC

=================================================================
2008/08/10 ThinkVantage Access Connections がfopen failedとか言う
=================================================================

Thinkpad X61s を Windows Vista SP1 で使っていますが、いつの頃からか画面に ``fopen failed`` というダイアログが表示されるようになりました。しばらく原因が分からなかったのですが、レジュームから復帰した後や無線のAPが切り替わったときに発生することに気づき、最近になってようやくどのプロセスがそのダイアログを出しているのかを突き止めました。

最近、たまたまそのダイアログが出たときにProcessExplorerを使っていて、それでやっとAcSvc.exeというやつが出しているダイアログだと気づいた次第。Spy++とかで特定できるのは知ってたんだからもっと早く気づけよ俺、と。

で、AcSvc.exeはThinkpad付属のロケーションプロファイラ、AccessConnectionsというやつでした。そこまで分かれば、検索でたどり着くのも楽で、 `Re: printff - fopen failed error by AcSvc.exe on Vista - ThinkVantage Access Connections`_ というそのまんまな記事を発見。

**AccessConnectionsの4.52をVista SP1で使うとダイアログ出るから、4.42のインストーラ** `7rcn38ww.exe`_ **を使えばOKさ！**

という事らしいので早速インストールしたところ、無事ダイアログが出なくなりました。１ヶ月くらい我慢して使ってたのかな。Lenovoになってからなのか、Vistaになってからなのか、最近のThinkpadの付属ソフトウェアはあんまり安定していない気がしますな。最近、輝度コントロールの挙動も変だし。コンピュータをロックしたときにわざわざ暗くしなくても良いと思うんだけどなあ‥‥。

.. _`Re: printff - fopen failed error by AcSvc.exe on Vista - ThinkVantage Access Connections`: http://forums.lenovo.com/lnv/board/message?board.id=T_Series_Thinkpads&message.id=9207

.. _`7rcn38ww.exe`: ftp://ftp.software.ibm.com/pc/pccbbs/mobiles/7rcn38ww.exe


.. :extend type: text/html
.. :extend:


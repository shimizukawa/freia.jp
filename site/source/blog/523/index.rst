:date: 2008-01-26 22:39:48
:tags: IT-PC

==================================================
ML115が届いたのでメモリを8G搭載してみた
==================================================

木曜日に注文したML115が金曜日には配達されていた（不在だったけど）。で、今日の朝受け取って昼過ぎにメモリを買いに秋葉原へ。ML115でVMWareを動かして、その上でfreia.jpを稼働させようかと思っている。ということで、メモリはまあまあ載せた方がいいのかな。

今日買ってきたメモリは、UMAXのDDR2-800 2GBが1枚で約4000円。2000円/GB。安すぎ。とりあえず4GB購入で8200円。

一緒に行ったとみたも同じメモリを4GB買ったので、それを借りて合計8GBをML115に搭載。memtest86を走らせてみたけど特に問題なくテスト完了。ML115は公式にはECCメモリが必要なんだけど、 `ML115のwiki`_ にも書いてあるようにECCじゃなくても動作するらしい。一部のメモリで相性問題が出るっぽいけど、今日買ったUMAXのやつは相性問題はなさそう。

早速 `Ubuntu 7.10 server`_ と `VMWare Server 1.0.4`_ をインストールしてみよう。

.. _`ML115のwiki`: http://wiki.nothing.sh/page/hp%BB%AA-ProLiant-ML115(%B3ʰ%C2Server)/Linux
.. _`Ubuntu 7.10 server`: http://www.ubuntu.com/getubuntu/download
.. _`VMWare Server 1.0.4`: http://www.vmware.com/download/server/


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2008-01-27.0375569931
.. :title: Re:ML115が届いたのでメモリを8G搭載してみた
.. :author: voluntas
.. :date: 2008-01-27 00:07:18
.. :email: 
.. :url: 
.. :body:
.. ぅぁーいいですねー。
.. 8G が格安すぎです。
.. 
.. 8200 円て ...
.. 
.. どこら辺で売ってます？
.. 
.. :comments:
.. :comment id: 2008-01-27.9612237903
.. :title: Re:ML115が届いたのでメモリを8G搭載してみた
.. :author: しみずかわ
.. :date: 2008-01-27 03:42:42
.. :email: 
.. :url: 
.. :body:
.. あ、いや、4Gで8200円です。紛らわしくてすみません。
.. 買ったのはツクモでしたが、どの店でも非バルクでだいたい2GBが4000円くらいでしたよ。
.. 
.. 
.. :comments:
.. :comment id: 2008-01-27.1725030863
.. :title: Re:ML115が届いたのでメモリを8G搭載してみた
.. :author: koma2
.. :date: 2008-01-27 11:16:13
.. :email: koma2@lovepeers.org
.. :url: http://bloghome.lovepeers.org/daymemo2/
.. :body:
.. 4G 8200円でもじゅーぶん安いよ。ｗ
.. わたしゃトランセンドでECC付きのを買ったので倍ぐらいしたけど、それでも安いと思ってしまった。
.. 
.. :comments:
.. :comment id: 2008-04-24.1467398320
.. :title: Re:ML115が届いたのでメモリを8G搭載してみた
.. :author: Anonymous User
.. :date: 2008-04-24 02:35:48
.. :email: 
.. :url: 
.. :body:
.. つんでもみました。グラフィックボードを認識しなくなりました。2Gにしたら復活。うーん、いくらなんでも2Mのオンチップグラフィックで使えというのは、酷じゃないかなと思うのですが。
.. 


.. image:: 20080126_memory8gb.*
   :width: 33%

.. image:: 20080126_natto1.*
   :width: 33%

.. image:: 20080126_natto2.*
   :width: 33%


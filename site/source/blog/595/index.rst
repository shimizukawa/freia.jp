:date: 2008-07-04 01:28:32
:categories: ['IT-PC']
:body type: text/x-rst

======================================================
2008/07/04 VistaでVMWareが固まる件、とりあえずの回避策
======================================================

*Category: 'IT-PC'*

`VistaでVMWare Serverが固まる`_ で書いたように、うちのVista君でVMWwareを実行しようとすると3回くらいブルースクリーン→リセットを眺める必要があった。これに対してとりあえずの対策が出来たように思える。その対策とは....

1. メモリを4MB割り当てた最小限のVMを作成する
2. このVMをHost起動時に自動的に起動するよう設定する

以上。

運が良ければHostが起動する。運が悪ければHostが起動しない（涙

今のところ、うまくいっているっぽい。しかし、PC起動は遅くなった。抜本的な解決方法が欲しい今日この頃。 VirtualBox_ に移行するという手もあるな...。

.. _`VistaでVMWare Serverが固まる`: http://www.freia.jp/taka/blog/546
.. _VirtualBox: http://www.virtualbox.org/


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2008-07-04.2858251577
.. :title: Re:VistaでVMWareが固まる件、とりあえずの回避策
.. :author: nakai
.. :date: 2008-07-04 12:48:06
.. :email: 
.. :url: 
.. :body:
.. Virtual Boxええよ:_0
.. 
.. :comments:
.. :comment id: 2008-07-04.0347145845
.. :title: Re: Virtual Boxええよ:_0
.. :author: しみずかわ
.. :date: 2008-07-04 13:00:34
.. :email: 
.. :url: 
.. :body:
.. とりあえずインストールだけしてみた:)
.. 

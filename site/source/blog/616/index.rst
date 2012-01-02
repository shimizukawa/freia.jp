:date: 2009-01-22 02:37:12
:categories: ['IT-PC']
:body type: text/x-rst

=======================================================================
2009/01/22 VistaでVMWare Serverが固まる件はVMWare Server 2.0 にして解決
=======================================================================

*Category: 'IT-PC'*

* `VistaでVMWare Serverが固まる`_
* `VistaでVMWareが固まる件、とりあえずの回避策`_

上記のときの VMWare Server のバージョンは1.0.4～1.0.8のどれでも発生していて、結局のところちゃんと解決する方法が見つかっていなかった。

昨日、ふと思い立って再度Googleで検索してみたら以下の記事が見つかった。

.. Highlights::
  VMWare 2.0 Beta 2 にすればこのバグによってVM起動時に発生するシステムの無応答状態は解消されるようだ。

  -- `VMWare Server Causes System Frozen, Hang and Unresponsive When Power/Start Up in Vista`_

ということで、VMWare1.0.5をアンインストールして2.0を入れ直したらすんなり起動するようになった。解決。

でも VMWare Server 2.0 は VMWare Server Console が JavaApplet になってしまったので使いづらい気がする。慣れの問題かもしれんけど。他にもWindows Guest用のVMWareToolsが用意されていないように見えるとか、UIが英語になってしまったとか、色々気になるところがあるなあ。Windows VistaがHostの環境で準仮想化(paravirtualization)が使えれば良いんだけどな。XenとかVMWareのそのへんの最新動向はどうなってるのかな？


.. _`VistaでVMWare Serverが固まる`: http://www.freia.jp/taka/blog/546
.. _`VistaでVMWareが固まる件、とりあえずの回避策`: http://www.freia.jp/taka/blog/595
.. _`VMWare Server Causes System Frozen, Hang and Unresponsive When Power/Start Up in Vista`: http://www.tipandtrick.net/2008/vmware-server-causes-system-frozen-hang-and-unresponsive-when-powerstart-up-in-vista/


.. :extend type: text/html
.. :extend:


.. :comments:
.. :comment id: 2009-01-23.6870163907
.. :title: Re:VistaでVMWare Serverが固まる件はVMWare Server 2.0 にして解決
.. :author: jack
.. :date: 2009-01-23 11:28:08
.. :email: 
.. :url: 
.. :body:
.. いいこときいた。やってみようかな。でもメモリがあまり載ってないのが・・・
.. 
.. :comments:
.. :comment id: 2009-01-23.9526548440
.. :title: Re:VistaでVMWare Serverが固まる件はVMWare Server 2.0 にして解決
.. :author: しみずかわ
.. :date: 2009-01-23 12:39:13
.. :email: 
.. :url: 
.. :body:
.. > いいこときいた。やってみようかな。でもメモリがあまり載ってないのが・・・
.. 
.. 2.0 になって管理画面がJavaAppletになったりJava環境が専用でインストールされたりtomcatが稼働していたり、と、DISKもMEMも使用量が増えた感じがしますね。
.. 
.. Guest起動してない状態で調べてみた:
..  * VMWare Server 1.0 DISK: 106MB, MEM: 30MBくらい。
..  * VMWare Server 2.0 DISK: 650MB, MEM: 260MBくらい。
.. 
.. 増えた感じ、どころじゃないな...
.. 

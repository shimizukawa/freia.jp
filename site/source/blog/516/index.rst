:date: 2008-01-21 21:10:50
:tags: IT-PC

=======================================
2008/01/21 X61sのIntel VTをOnにしてみた
=======================================

Core2Duoに搭載されている ``Virtualization Technology`` 機能は、ThinkPad X61sのBIOSではデフォルトでOffになっていた。しばらくこれに気づかずにVirtualPC2007を使っていて、X40で動かしてたときに比べてあんまり速くないなー、と思ってました。すみません。

で、BIOSのCPU設定でIntelVTをEnableに変更したところ、VirtualPCの中断データがすべて無効になってしまった。処理の途中だったのに。

気を取り直して仮想化機能を有効にした状態のVirtualPCで処理をやり直してみたところ‥‥有効にする前よりも遅くなった気がする。少なくとも体感では速くなっていないと思う。なんでだろう？と思って調べてみると以下のような記事が見つかった。

.. highlights::

  結果は見て分かるように、VT-xでもAMD-Vでも有効にしない方が速いという結果になっている。
  この結果だけを見るならば、どちらも今のところ意味がないとしか言いようがない。

  -- `笠原一輝のユビキタス情報局`__ (2007/3/15)

.. __: http://pc.watch.impress.co.jp/docs/2007/0315/ubiq177.htm

つまり、仮想化機能はあんまり意味がないどころじゃなく、使うと遅くなると言うことか。それってどうなの？
しかも、ついさっき突然Windows上であらゆるコピー操作ができなくなった。上記引用はすべて手入力。きっとVTのせいに違いない。VTイクナイ。


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2008-01-23.9931930167
.. :title: Re:X61sのIntel VTをOnにしてみた
.. :author: M.Shibata
.. :date: 2008-01-23 13:36:34
.. :email: nospam.mshibata@emptypage.jp
.. :url: 
.. :body:
.. VT を有効にしたほうが遅くなるという話があったんですね。
.. Virtual PC はラップトップで動かすと（電力管理との相性みたいなもので？）パフォーマンスに問題が出るという話は読んだことがあります。以前 MSDN のブログに、その現象と対策についていくつか記事が出てました。
.. 
.. Virtual PC Guy's WebLog : Last resort for performance issues with Virtual PC on laptops
.. http://blogs.msdn.com/virtual_pc_guy/archive/2007/03/27/last-resort-for-performance-issues-with-virtual-pc-on-laptops.aspx
.. 
.. 上の記事とそこから辿れるふたつです。すでにお読みでしたらご容赦を。
.. でももう乗り換えちゃったからあんまり関係ないかしら。
.. 
.. 
.. :comments:
.. :comment id: 2008-01-23.8583399026
.. :title: Re:X61sのIntel VTをOnにしてみた
.. :author: しみずかわ
.. :date: 2008-01-23 23:50:59
.. :email: 
.. :url: 
.. :body:
.. Virtual PC Guy で言及されているのは電力が低下してるときの事みたいですね。とりあえず乗り換えちゃったというのと、自分の時の性能低下は電源供給時の現象だったので。。でもリンク先のSppedSwitchXPはおもしろそう。GuestOSに入れてみようかな。
.. 
.. 
.. :comments:
.. :comment id: 2008-01-24.1526525803
.. :title: Re:X61sのIntel VTをOnにしてみた
.. :author: M.Shibata
.. :date: 2008-01-24 02:09:13
.. :email: nospam.mshibata@emptypage.jp
.. :url: 
.. :body:
.. 電力というか、どのプロセス（スレッド）にどれだけ処理能力を分けるかというスケジューリング（ていうの？）の問題でしょう。モバイル CPU はこれをまめに必死でやるので Virtual PC にはかえってあだになっているという。それはバッテリー駆動時でなくてもやってますよね（省電力設定にもよると思いますが）。自分は最後の options.xml の設定変更でずいぶん改善を感じました。
.. そういえば、別件で Windows XP がパフォーマンスを発揮できないという問題もあったような気がします。いいのか MS。
.. 終わった話で長々とゴメンナサイ。それでは。
.. 
.. :comments:
.. :comment id: 2008-01-24.9281117446
.. :title: Re:X61sのIntel VTをOnにしてみた
.. :author: しみずかわ
.. :date: 2008-01-24 23:45:28
.. :email: 
.. :url: 
.. :body:
.. 確かに、細かく電源管理してるからって書いてますね。試しにコンセントぬいてバッテリー駆動モードにしたらものすごく遅くなった‥‥ VirtualPCとVMWare Server両方とも‥‥。とりあえずバッテリー駆動中の仮想マシンパフォーマンスは今のところ求めてないけど、対策は用意しておいた方がいいかも。
.. 
.. it will drain your battery power much faster than normal. ってのが気になりますが(^^;;

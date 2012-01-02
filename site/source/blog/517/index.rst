:date: 2008-01-22 23:59:48
:categories: ['IT-PC']
:body type: text/x-rst

=====================================
やっぱりVirtualPCよりVMWareの方が速い
=====================================

VirtualPCはUIが使いやすいんで「ちょっと使おう」という気にはなるんだけど、HDDアクセス速度がすぐに実用に耐えない速度になってしまう。これはHDDイメージサイズを非固定長にして使っているせいなのかもしれないけど。VMWareはそのへんの問題が起こらないっぽいんだけど、時々大量SWAPが発生してものすごく重くなるときがある(気がする)。

総合的に見てやはりVMWareの勝利だなあ、と思いつつVirtualPCから乗り換え。

でも、VirtualPCにある、HOSTの任意のフォルダをClientの仮想ドライブとしてマウントする機能は超便利だった。VMWareでは同じことはできないのか？ぜひほしい機能だ。

ところで、 VMWare Server 1.0.4 の機能にVirtualPCからのインポート機能があるんだけど、うまくいったためしがない。HDDイメージサイズが非固定長だからじゃないかと、とみたが言っていたけど、どうなんだろう。


.. :extend type: text/html
.. :extend:


.. :comments:
.. :comment id: 2008-01-23.7001008004
.. :title: Re:やっぱりVirtualPCよりVMWareの方が速い
.. :author: Yujiro Nakamura
.. :date: 2008-01-23 10:28:21
.. :email: 
.. :url: 
.. :body:
.. VMwareはWorkstationのv4を使っていましたが、任意フォルダのドライブマウントは可能でした。今は使ってないので具体的な設定などは分かりませんが……。
.. 
.. ちなみに、今はVirtualBoxを使っていますが、こちらはドライブではなく共有フォルダとしてマウントできます。
.. 個人的な評価ですが、VirtualBoxはVirutl PCよりはパフォーマンスがよく、VMwareよりはUIが使いやすいという、ちょうど両ソフトの中間に位置するような印象です。信頼性は若干両ソフトに劣る（Vistaでブルースクリーン経験あり、あとクリップボードが突然ホストと共有できなくなることがときどき）ので、開発系での利用は微妙かもしれませんが……。
.. 
.. :comments:
.. :comment id: 2008-01-23.5378131114
.. :title: Re:やっぱりVirtualPCよりVMWareの方が速い
.. :author: しみずかわ
.. :date: 2008-01-23 11:48:58
.. :email: 
.. :url: 
.. :body:
.. VMWare Server 1.0.4 では共有フォルダ機能が無いっぽいです。VMWare Tool に共有フォルダ機能があるんですが標準ではインストールされない(インストール時にcustomで指定)うえに、インストールしても特に何も変わらない‥‥。
.. 
.. 無理矢理使えるように頑張ってる人もいるみたいですが...
.. http://www.katch.ne.jp/~kakonacl/douga/virtualmachine/vmware/sharedfolder.html
.. 
.. VirtualBoxはおもしろそうですね。今度いれてみよう。
.. http://www.forest.impress.co.jp/article/2007/03/01/virtualbox.html

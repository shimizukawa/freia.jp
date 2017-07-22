:date: 2008-01-28 23:27:57
:tags: Windows

============================
2008/01/28 ckwとnyacusとztop
============================

開発にWindowsを使っているとcmd.exeを結構な頻度で使う。Windowsで開発する人はcoLinuxかcygwinを使う人が多そうな気もするけど、ここではそれは置いておく。（cygwinはちょっと苦手...）

で、このcmd.exeというやつが結構使いにくくて、

- コピー・ペーストの手順がちょっと多い(putty等に比べて)
- 最大化しても横幅が変わらない
- Windowの半透明化ツール(`ZTop`_ など)を使っても半透明にならない

などという困った点がある。横幅固定とか半透明にならないとか、どういう仕様なんだろう？

...といった問題を解消してくれるのが、 `ckw`_ 。しかし、バイナリは入手できなかったので、
ソースを自分でビルドしてたんだけど、ckwのバグを修正した版を公開してくれてる人がいたので
そっちに乗り換えました。

- `ckw 0.8.10 改造版`_

ついでに、この方のページで紹介されていた `NYACUS`_ も使用開始。
tcshっぽい操作感ですごく便利だ！


.. _`ckw`: http://www.softantenna.com/lib/3553/index.html
.. _`ckw 0.8.10 改造版`: http://d.hatena.ne.jp/hideden/20071115/1195229532
.. _`NYACUS`: http://www.nyaos.org/
.. _`ZTop`: http://www15.plala.or.jp/then/


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2008-01-30.9113847360
.. :title: Re:ckwとnyacusとztop
.. :author: jack
.. :date: 2008-01-30 11:41:51
.. :email: 
.. :url: 
.. :body:
.. これはよさそう・・・
.. 
.. :trackbacks:
.. :trackback id: 2009-05-31.1226238521
.. :title: Windowsのコマンドプロンプトをフリーソフトで便利にする
.. :blog name: ナレッジエース
.. :url: http://blog.blueblack.net/item_358
.. :date: 2009-05-31 01:15:22
.. :body:
.. 
.. 
.. Windowsのコマンドプロンプト(cmd.exe)を開発などで頻繁に使っていると、何かと不便な点が気になってきます。
.. 
.. ウィンドウの最大化が制限されていたり、コピー・ペーストが右クリックメ...
.. 

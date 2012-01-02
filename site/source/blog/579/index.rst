:date: 2008-06-20 23:56:16
:categories: ['Unix']
:body type: text/x-rst

==========================================================
2008/06/20 VMWareのUbuntuは複製するとNetwork設定変更が必要
==========================================================

*Category: 'Unix'*

いろいろな人がはまっているようで、解決方法はいくつかネット上に転がっていますが、自分もはまって解決にちょっとてまどりました。

問題は、Ubuntuのネットワーク設定はMACアドレスをベースに設定されていて、VMWareのイメージを複製したり別のホストOSに持って行ったりすると（おそらくこのときにuuidを再生成すると）MACアドレスが変わってしまいeth0だったのがeth1やeth2とかになってしまうこと。これに気づかないと、/etc/network/interfaces の記述がeth1のままのために起動してもネットワークが見つからないことになってしまう。

というか。

``/sbin/ifconfig`` したら /etc/network/interfaces に記載のないethデバイスも表示して欲しいと思う。あるいは起動ログとかに表示して欲しい。気づかんて。

ということで、自分の場合の解決方法。

1. ethの番号がずれていることを疑う
2. ``lshw -C network`` で表示されるethの番号を確認する

.. Topic:: Ubuntu-7.1 Server
    :class: dos

    | root:/etc# lshw -C network
    |   \*-network
    |        description: Ethernet interface
    |        product: 79c970 [PCnet32 LANCE]
    |        logical name: eth3
    |        serial: 00:0c:29:48:d8:6e

上記は一部省略。なんかeth3になってました。3って。。

3. eth3をeth0に戻すために ``/etc/udev/rules.d/70-persistent-net.rules`` を編集

::

  # PCI device 0x1022:0x2000 (pcnet32)
  SUBSYSTEM=="net", DRIVERS=="?*", ATTRS{address}=="00:0c:29:48:d8:6e",NAME="eth3"

上記のeth3をeth0に修正。古い設定（eth0,eth1,eth2）は削除。

4. 再起動

これで完了。無事、/etc/network/interfacesに設定したとおりのネットワーク接続ができました。めでたしめでたし。

ところで、ググったときに /etc/iftabを修正する、という記載がいくつか見つかって、結局その方法ではうまくいかなかったんだけど、なんでだろう？そもそも/etc/iftab無いし・・・。Ubuntuはよくわからないです。最近VMイメージ作るたびにFreeBSD, CentOS, RedHat, Debian, Ubuntu, Windows2000, Windows2003, Windows2008, WindowsXP....と違うOS入れてるので、設定の書き方がよく分からなくなってきたよ。

参考
----

- `VMware ubuntu server ネットワークできない - 連絡拒否`_
- `別マシンにVMware仮想イメージを移した時のネットワーク設定 - Syo-Takasakiの日記`_


.. _`VMware ubuntu server ネットワークできない - 連絡拒否`: http://d.hatena.ne.jp/winty/20061112/1163358690
.. _`別マシンにVMware仮想イメージを移した時のネットワーク設定 - Syo-Takasakiの日記`: http://d.hatena.ne.jp/Syo-Takasaki/20070829/1188336460


.. :extend type: text/html
.. :extend:


.. :comments:
.. :comment id: 2008-10-29.2767632699
.. :title: Re:VMWareのUbuntuは複製するとNetwork設定変更が必要
.. :author: Anonymous User
.. :date: 2008-10-29 11:27:58
.. :email: jyo.rakuraku@gmail.com
.. :url: 
.. :body:
.. Ubuntu 8でも上記の方法で問題を解決してきた。
.. どうもありがとうございます。
.. 
.. :comments:
.. :comment id: 2008-10-29.5858170025
.. :title: Re:VMWareのUbuntuは複製するとNetwork設定変更が必要
.. :author: しみずかわ
.. :date: 2008-10-29 20:59:46
.. :email: 
.. :url: 
.. :body:
.. お役に立てたようで何よりです:-)
.. 

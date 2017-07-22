:date: 2005-03-14 21:58:38
:tags: Unix

================================
2005/03/14 FreeBSDのバックアップ
================================

新しいサーバー機を組んだのでドライバの関係もありFreeBSD5.3-RELEASEを入れることにした。で、HDDストック [1]_ の中からMaxtorの80GBを取り出してつないだところ、一代前のサーバー環境が入ってた。そういえばあとで必要なファイル取りだそうとか思ってたんだっけ‥‥。

ほかに手頃な空きDISKもないし、M/BのS-ATAでRAID1をやろうにもHDDを買う余裕はさすがにもうないので、環境をバックアップすることに。さてどうやってバックアップしよう？

1. cpでコピー
2. tar+gzipで圧縮
3. dump （‥‥してからどうするんだろう？）
4. dd + vnconfig [2]_ で仮想DISK化
5. FreeBSD5のsnapshot

一番いいのは4なんだけど、ddはパーティションそのものをイメージ化するのでサイズがでかすぎる。20GBのパーティションを取っておくのに20GBの容量が必要‥‥。そこで！ddしたイメージを圧縮して、その圧縮イメージのままmdconfigしてmount出来れば！::

  # dd if=/dev/zero of=zerofile
  # rm zerofile
  # dd if=/dev/ad0s1e | gzip -9 > volume.img.gz
  # mdconfig -a -t vnode -f volume.img.gz -u 0
  # mount /dev/md0 /mnt

  Invalid super block!

‥‥とりあえず出来ませんでしたorz。同じようなことを「出来ないようだ」と結論づけてる人もいたけど、writableは難しいとしても、read-onlyなら出来そうな気がするんだけどなぁ‥‥。

しかたがないので、とりあえずtarで必要な部分だけ固めておくことにした [3]_ ::

  # tar cfjpv - /etc | ssh user@backup.server.jp dd of=/backup/etc.tbz

tarを標準出力からsshに流し込んで相手先サーバーでddで受け取ってファイルに書き出す。今回いろいろバックアップ方法を調べて初めて知ったヨ。

.. [1] 二代前のサーバー環境でvinumなRAID5用に使っていた4台のうちの一つ。残りは「現行サーバー」「実験用環境」「とみたに里子」。

.. [2] FreeBSD5系ではmdconfigになっていた。

.. [3] /etcのほかに/usr/local, /var, /boot を保存。



.. :extend type: text/plain
.. :extend:


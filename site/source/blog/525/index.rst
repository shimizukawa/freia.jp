:date: 2008-01-27 19:12:29
:categories: ['Unix', 'IT-PC']
:body type: text/x-rst

=============================
2008/01/27 ML115 Challenge! 1
=============================

*Category: 'Unix', 'IT-PC'*

とりあえずメモリを標準搭載のDDR2-677-512MB-ECCからDDR2-800-4096MB-NonECCに変更してmemtest86は特に問題なし。

VMWareのHostにするOSの選択に迷い、とりあえずUbuntu Server 7.10を入れてみたが、VMWareを動かすには色々と手動でパッケージを入れる必要があり(makeとかgccとか)、初めてさわるRedHat以外のLinuxなのであまり調査もせずに断念。

次にUbuntu Desktop 7.10ならXとか色々入ってるだろうと思い入れてみた。が、なぜか解像度が720x400という不思議な解像度しか選択できず、VMWareをインストールしてみたけど結局起動までは至らず断念。このへんで明け方4時。

次にDebianをインストールしてみたが、こちらもなぜか解像度が720x400という不思議な解像度しか選択できず。仕方がないのでそのままVMWareのインストールを続行し、libX11.so.6が無いという警告にはまる。検索してみたら ``apt-get install ia32-libs`` すれば良いことが分かる。でもia32ですか？と思いつつもVMWareは無事起動した。この辺で明け方5時過ぎ。

ところでVMWareのライセンスキーはWindowsとLinuxとで互換性がないことに気づいた。VMWareのusサイトでLinux用のライセンスキーを10個ほど入手し設定。無事仮想マシンが起動。朝7時。

睡眠。

`debian-amd64`_ というページを見つけ、先は長そうだな‥‥とため息。＜いまここ


.. _`debian-amd64`: http://kmuto.jp/open.cgi?debian-amd64


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2008-01-27.1497783066
.. :title: Re:ML115 Challenge! 1
.. :author: Anonymous User
.. :date: 2008-01-27 20:42:32
.. :email: 
.. :url: 
.. :body:
.. Ubuntu Server で、VMware Server は下記を sorces.list に追加するだけで aptitude で入りますよ:-)
.. 
.. deb http://archive.canonical.com/ubuntu gutsy partner
.. 
.. aptitude install vmware-server
.. 
.. 
.. :comments:
.. :comment id: 2008-01-29.4662976930
.. :title: Re:ML115 Challenge! 1
.. :author: しみずかわ
.. :date: 2008-01-29 01:24:27
.. :email: 
.. :url: 
.. :body:
.. おお！天の声が！aptitudeって何だろう！？FreeBSDのportutilみたいなもんかな。
.. 今は画面解像度問題の方が気になってるので、後ほど試してみます。
.. 
.. 
.. :comments:
.. :comment id: 2008-01-30.6405240245
.. :title: Re:ML115 Challenge! 1
.. :author: voluntas
.. :date: 2008-01-30 09:57:21
.. :email: 
.. :url: 
.. :body:
.. あ ... Anonymous になってました ... 。
.. すみません ... 。
.. 

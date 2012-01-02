:date: 2004-08-09 03:29:33
:categories: ['Unix', 'Zope']
:body type: text/x-rst

=============================
2004/08/09 mod_proxyはいずこ？
=============================

Zopeのフロントエンドにapacheを配置して、VirtualHostNameを用いてZopeへマッピングする方法はよく使われる方法ですが、今回FreeBSD(5.2.1)サーバーを再構築した際にapacheのバージョンを2.0.50へ上げたところmod_proxyが使えなくなってしまい、かなり苦労しました。


.. :extend type: text/x-rst
.. :extend:
apacheが窓口となる場合、例えば http://www.freia.jp/ というサイトへのアクセスをapacheが受信した際に http://localhost:8080/ へ問い合わせて結果をブラウザへ返すことが出来ます。例えば::

  
    ServerAdmin owner@www.freia.jp
    ServerName www.freia.jp
    ErrorLog /var/log/httpd/freia-error.log
    CustomLog /var/log/httpd/freia-access.log combined
    RewriteEngine On
    RewriteRule ^/(.*) http://localhost:8080/$1 [P]
  

と書くと、ブラウザのURL表示は http://www.freia.jp/ のままapacheが内部的にlocalhost:8080へ問い合わせを行ってくれます。ここでポイントとなるのが *RewriteRule* 行の最後にある *[P]* です。これはproxy動作のためのフラグで、これを付けずに::

    RewriteRule ^/(.*) http://localhost:8080/$1

などと書いてしまうと、ブラウザが直接 *http://localhost:8080/* へ問い合わせてしまいますので、ブラウザが稼働しているパソコン自身の8080ポートへ問い合わせが行われます。

このproxyはmod_proxyという外部モジュールで実現されているのですが、FreeBSDのportのデフォルトではmod_proxyが無効になっていました。もしかしたらapache2.0.50標準で無効なのかもしれませんが、調べていません。(セキュリティー上の問題?)

結果的には::

  > make -DWITH_PROXY_MODULES="YES"

としてapacheをビルドし直し、無事使用できるようになったのですが、ここにたどり着くために Makefile, Makefile.modules, Makefile.modules.3rd などを読み解いたり、apacheのproxy/rewrite周りのドキュメントを解読したりと、かなりの時間を食ってしまいました。

ちなみに、ZopeのVirtualHostMonsterを組み合わせて以下のように *RewriteRule* を記述するとZope上の任意のフォルダをそのサイトのルートフォルダとして表示することが出来ます::

    RewriteRule ^/(.*) http://localhost:8080/VirtualHostBase/http/www.freia.jp:80/freiaroot/VirtualHostRoot/$1 [P]

上記の例では freiaroot というZope上のパスをwww.freia.jpにアクセスしたときに表示します。同じページをZopeで直接表示するには www.freia.jp:8080/freiaroot/ となります。これを使えば複数のドメインを単一のZopeサーバーで管理することが出来るようになります。

それにしてもmod_proxyがデフォルトで使えないとなると、またZope環境構築の障害が一つ増えてしまうのではないかと心配です。



.. :comments:
.. :comment id: 2005-11-28.4436138366
.. :title: Re: mod_proxyはいずこ？
.. :author: えぐち
.. :date: 2004-08-29 00:15:57
.. :email: eguchi@sandeinc.com
.. :url: 
.. :body:
.. わたしも 2.0.50 にアップデートしたあたりで mod_proxy でコンパイルされない問題に遭遇し参考になりました。
.. 
.. １点気づいたのですが
.. > make -DWITH_PROXY_MODULES="YES"
.. は
.. > make WITH_PROXY_MODULES="YES"
.. ですね
.. 
.. また　portupgrade を使うのであれば
.. /usr/local/etc/pkgtools.conf に
.. ---
..    MAKE_ARGS = {
.. +   'www/apache2' => "WITH_PROXY_MODULES=yes",
..    }
.. ---
.. を追加すると良いですね。
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4437345753
.. :title: Re: mod_proxyはいずこ？
.. :author: 清水川
.. :date: 2004-08-29 12:21:40
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. > make WITH_PROXY_MODULES="YES"
.. 
.. あれ？-Dで指定しないとmakeのターゲットになるんだと思って、他のportsの時も付けてました。
.. 
.. >/usr/local/etc/pkgtools.conf に.....
.. 
.. なるほど。
.. portupgradeの設定系はほとんど調べてなかったので知りませんでした‥‥。ので、毎回引数に指定していたのでした(--;;
.. 
.. 
.. 
.. :Trackbacks:
.. :TrackbackID: 2005-11-28.4438538680
.. :title: 迷走の日々
.. :BlogName: 週刊ミケ猫通信
.. :url: http://blog.livedoor.jp/nadias/archives/18243395.html
.. :date: 2005-11-28 00:47:23
.. :body:
.. なにもかもがうまくいかない。
.. あんまり質問しすぎたせいか鯖缶さんからも無視される始末。
.. ううう、すいません、他に質問できるならしてますってば！
.. 
.. ということでSSLのほうは放っておいてqwiweb。
.. あとちょっとという感はあるんだけど、あまりにも情報がすくなすぎ。
.. 
.. 
.. :Trackbacks:
.. :TrackbackID: 2005-12-18.6771786076
.. :title: apacheのアップデート
.. :BlogName: Ryuji's Note
.. :url: http://ryujisnote.homeunix.org/blog/15
.. :date: 2005-12-18 03:21:18
.. :body:
.. 
.. さて私はtake-laboさんの所の記事を参考にportsのソースを更新→メールで報告
.. update があった ports を手動で　portsupgtrade する。
.. ということをいつもやってますが、６日の報告メールで初の事態が。
.. /usr/sbin/pkg_version -v | grep -v =　 等でVersionを確認。 apache-2.0.55 ?
.. orphaned: www/apache2 Σ（￣□￣；）みなしご！？
.. UPDATINGによるとApache2.2がリリースされ...
.. 

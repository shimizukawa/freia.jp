:date: 2008-07-20 22:10:15
:tags: Unix
:body type: text/x-rst

=========================================
2008/07/20 サーバーを FreeBSD7.0 に移転中
=========================================

移転元も移転先も自宅サーバー内なんだけど、移転先はML-115のDebianで動作しているVMWareの上のFreeBSD7.0。とりあえずWeb機能だけを移転してみた。とりあえずZopeだけ移転するつもりだったんだけど、色んなライブラリやProductに依存していて、インストールにかなりてまどってしまった。

特に、apache, subversion, openldap の依存関係が良くなくて、openldap-2.4を先にインストールしたら、あとでapache-2.2のldapサポートがopenldap-2.3に依存してることが分かったり。微妙に、なんだかなーな感じだった。あと、make.confにWITHOUT_X11=yesを入れ忘れてて、Xがビルドされちゃったりとか。途中で止めたけど。

1ヶ月前くらいにFreeBSD上でzfsを使うつもりで色々実験してたんだけど、仮想環境上にzfs構築してもあんまり意味がない気がしてきたのでやめ。今回は普通にufs2で領域確保して運用。個人環境では結局のところRAID1が一番良さそうな気がする。

とりあえず今の時点で手動で入れたportsを列挙してみる::

    apache-2.2.6_2
    jpeg-6b_4
    openldap-sasl-client-2.3.41
    openldap-sasl-server-2.3.41
    pam_ldap-1.8.4
    pamtester-0.1.2
    portupgrade-2.3.1,2
    py24-ldap2-2.3
    python-2.4,2
    python24-2.4.4_2
    ruby-1.8.6.111_1,1
    screen-4.0.3_1
    subversion-1.4.4_1
    subversion-python-1.4.4_1
    sudo-1.6.9.6
    vim-7.1.145
    wget-1.10.2_1
    zope29-2.9.7_1
    zsh-4.3.4_2

あと、pythonパッケージ::

    PIL (PythonImagingLibrary)
    SilverCity
    python-ldap
    setuptools (easy_install)
    pysvn


おまけ。/etc/make.conf::

    # PORTS MASTER SITE
    MASTER_SORT_REGEX?=     ^file: ^ftp://ftp\.FreeBSD\.org/pub/FreeBSD/ports/local-
    distfiles/ ://[^/]*\.jp/ ://[^/]*\.jp\.
        
    # Ports can place their working directories somewhere other than under
    # /usr/ports.
    WRKDIRPREFIX=   /var/tmp/ports
    
    # Where to get gzip'd, tarballed copies of original sources
    #
    DISTDIR=        /usr/ports/distfiles
    
    # FETCH_CMD     - Full path to ftp/http fetch command if not in $PATH
    #                       (default: &quot;/usr/bin/fetch -A&quot;).
    FETCH_CMD=      /usr/bin/fetch -A -p -r -T 30



.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2008-07-21.5293297771
.. :title: Re:サーバーを FreeBSD7.0 に移転中
.. :author: koichiro
.. :date: 2008-07-21 05:08:49
.. :email: koichiro@meadowy.org
.. :url: http://ko.meadowy.net/~koichiro/diary/
.. :body:
.. portsも7.0-Releaseを入れたんだね。
.. ports-CURRENTだとちょっと前からSubversionまわりのパッケージ構成が激しく変わっていて
.. ウチも依存関係でハマったのでｗ注意。
.. 
.. subversion -> subversionとsubversion-develとsubversion-freebsdの派生パッケージができてる
.. subversion-python -> py-subversionに変更。同じルールでsubversion-perl -> p5-subversionとか。
.. 
.. portupgradeのpkgtools.confでALT_PKGDEPを設定しつつ調整するといいよ。

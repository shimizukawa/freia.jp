:date: 2008-06-28 21:50:12
:tags: Event, python

=====================================
Python温泉3, 2日目 翻訳Day
=====================================

amachangキター！

ということで2日目。朝8時起床。大雨。土曜はいつも昼過ぎまで寝てるので果てしなく眠い。

今日やったこと。


tracをインストール
-------------------
easy_install trac でいけた。後は::

    trac-admin /path/to/instance initenv

して::

    vi /path/to/instance/conf/trac.ini

で設定。
initenvで対話形式で入力しただけで、tracからsvnを参照できるようになった。


tracの認証をapacheでやろうと思った
-----------------------------------
tracd --port 8000 /path/to/instance で起動はできるけど、通常運用を考えるとサーバーはapacheにやってもらうのがいいよね。認証もapacheにおまかせ。


ということでapache2をインストール::

    apt-get install apache2


apache2の認証をopenldapに持たせようと思った
---------------------------------------------
認証のためにldapを立てるのはめんどくさいなあ、と思いつつ、個別に用意するのはそれはそれで面倒そうだったので、設定することにした。


とりあえずopenldapを入れた::

    apt-get install slapd
    apt-get install ldap-utils


ldapaddで認証用ユーザーを追加
------------------------------
ldapaddコマンドで手入力::

    ldapadd -x -W -D cn=admin,dc=localdomain

    dn: ou=Users,dc=localdomain
    objectClass: organizationalUnit
    ou: Users

    dn: cn=taka,ou=Users,dc=localdomain
    objectClass: top
    objectClass: person
    cn: taka
    sn: Shimizukawa
    userPassword: dummy


パスワードを変えてみる::

    ldappasswd -x -W -S -D cn=taka,ou=Users,dc=localdomain


pam_ldapを入れた
-----------------
インストールして::

    apt-get install libpam-ldap

/etc/pam.d/apache2 に設定::

    auth       required   /lib/security/pam_ldap.so  no_warn try_first_pass
    account    required   /lib/security/pam_ldap.so  no_warn try_first_pass


mod_auth_pamを入れた
---------------------
インストールして::

    apt-get install libapache2-mod-auth-pam

/etc/apache2/sites-enabled 以下のファイルに::

    AuthName "LDAP ID / password for repos"
    AuthType Basic
    AuthPAM_Enabled on

等を記述してapacheを再起動。だがしかし、BASIC認証が通らない。/var/log/apache2/error.log を確認するとユーザーIDが無いと記録されている::

    PAM: user 'taka' - not authenticated: User not known to the underlying authentication module


apacheで認証できずにはまる
---------------------------
``/etc/ldap.conf`` の設定をほとんどデフォルトのままで使っていたので、 ``objectClass: person`` にはuidが無くてユーザーが見つかっていなかった。あとbind dnの設定を変えていなかったため、ou=Users以下を見る設定になっていなかった。

/etc/ldap.conf に以下を設定::

    base ou=Users,dc=localdomain
    scope sub
    pam_login_attribute cn


http経由でsvnを読み書きできるようにする
----------------------------------------
apt-get install libapache2-svn して

/etc/apache2/sites-enabled/002-svn::

    <Location /repos>
        DAV svn
        SVNPath /var/lib/svn/repos
    </Location>


svnのコミット時にldapで認証する
--------------------------------
svnリポジトリ ``/var/lib/svn/repos`` の所有者をwww-dataにして、グループをsvnusersに変更する。また/etc/groupのsvnusersにwww-dataとsvnプロトコルでアクセスするユーザーを所属させる。これでsvnプロトコルとhttpプロトコル両方でコミットできる。あとはldap認証するようにLocationを設定する。

/etc/apache2/sites-enabled/002-svn::

    <Location /repos>
        DAV svn
        SVNPath /var/lib/svn/repos

        AuthName "LDAP ID / password for repos"
        AuthType Basic
        AuthPAM_Enabled on

        <LimitExcept GET PROPFIND OPTIONS REPORT>
             Require valid-user
        </LimitExcept>
    </Location>


昼ご飯を食べる
--------------
麓まで下山すると再登山が大変なので、みんなで仕出し弁当を食べる。


tracをmod_wsgiで動かそうとしてはまる
-------------------------------------
apt-getにmod_wsgiが無い。unstableを使えるようにしてインストールしてみたけど、結局正しく動かなかった。 ``trac-admin /path/to/instance deploy /path/to/deploy`` で作成したtrac.wsgiの中で from trac.util import compat しているんだけど、compatが無いと言われる。原因不明。誰かがdelしてるに違いない。

しょうがないのでとりあえずcgiモードで動かす。


tracにbuildbotのwaterfallを表示しようとしてはまる
--------------------------------------------------
trac-0.11ではTracBB-0.1.2はうまく動かない？とりあえず保留。


buildbot-0.7.7のマニュアルを翻訳し始めてみる
---------------------------------------------
キーワードと各章のタイトルだけ翻訳した時点で3時間くらい経ってた。何回か眠気に負けそうになったので温泉に浸かってくる。晩ご飯まであと1時間頑張ろう。


晩ご飯を食べる
---------------
昨日より品数が増えた。普通にうまい。


iPhoneアプリ開発ハンズオンを見る
---------------------------------
いまここ。NDAとかなんか大変らしい。



.. :extend type: text/html
.. :extend:



.. image:: 20080628_pyspa3_day2_dinner.*
   :width: 33%


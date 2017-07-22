:date: 2004-11-23 14:37:53
:categories: ['Unix', 'Memo']
:body type: text/x-rst

===================================================================
2004/11/23 WindowsからのVPN接続認証をLDAPで管理する on FreeBSD5.2.1
===================================================================

以前からWindowsクライアントからのVPN接続時の認証管理をLDAPで出来ないか、と考えていましたが、freeradiusを使うことで成功しました。実は mpd (PPPサーバー・クライアントソフト) がRADIUSサーバーと連携できることは知っていたのだけど「RADIUSじゃなくてLDAPと連携して欲しいなぁ‥‥」と思うにとどまっていました。で、ふと思いついて、"RADIUS LDAP"で検索したら「 `LDAP を使った Radius 認証`_ 」というページがあっさりと引っかかったので、他のサイトも調べつつ色々と試してみたらうまくいきました。

ということで、目標。

1. mpdとfreeradiusを連携させる
2. freeradiusとOpenLDAPを連携させる
3. LDAP内にプレーンテキストでパスワードを格納しない（重要！）


.. _`LDAP を使った Radius 認証`: http://www.linux.or.jp/JF/JFdocs/LDAP-Implementation-HOWTO/radius.html



.. :extend type: text/x-rst
.. :extend:

以下、環境構築手順ですが、自分の環境用に書いているので設定ファイルの場所はFreeBSDでportsを使用した場合の場所です。と言っても、Linuxの場合は/usr/local/etcを/etcに読み替えるだけで良いような気もします。

サーバー環境
-------------

- FreeBSD-5.2.1-SECURITY
- IP: 192.168.1.200
- mpd-3.18
- freeradius-1.0.1
- openldap-2.2.17
- samba-3.0.7

最後のsambaが意外なところで重要でした。VPNのクライアントがWindowsなので当たり前と言えば当たり前ですが‥‥。結局、sambaアカウントをLDAPで管理していたため、環境の用意が比較的簡単に済みました。というのは、VPN接続認証で使用されるMS-CHAPでsambaパスワード（と言うかNTLMハッシュ）が使われるからです。

ということで、設定法補を順番に説明します。



mpd-3.18の設定
---------------

2004/11/23現在最新の、3.18に付属してくるmpd.conf.sampleには、radiusと連携するための設定が"radius:"セクションに書かれています。ただし、pptpセクション内で"load radius"という行がコメントアウトされているのでそのままでは動作しません。手元の環境にはだいぶ前に作ったmpd.confがあるので、"radius:"セクションをコピーして使いました。

今回使用したmpd.conf::

	default:
		load pptp

	pptp:
		load pptp1
		load pptp2
		load pptp3
		load pptp4

	pptp1:
		new -i ng1 pptp1 link-pptp
		load pptp-conf
		set ipcp ranges 192.168.1.200/32 192.168.1.240/32

	pptp2:
		new -i ng2 pptp2 link-pptp2
		load pptp-conf
		set ipcp ranges 192.168.1.200/32 192.168.1.241/32

	pptp3:
		new -i ng3 pptp3 link-pptp3
		load pptp-conf
		set ipcp ranges 192.168.1.200/32 192.168.1.242/32

	pptp4:
		new -i ng4 pptp4 link-pptp4
		load pptp-conf
		set ipcp ranges 192.168.1.200/32 192.168.1.243/32

	pptp-conf:
		load radius
		set bundle yes radius-acct
		set iface disable on-demand
		set iface enable proxy-arp
		set iface idle 1800
		set bundle disable multilink
		set link yes acfcomp protocomp
		set link no pap chap
		set link enable chap
		set link keep-alive 10 240
		set ipcp yes vjcomp
		set ipcp nbns 192.168.1.200
		set ipcp dns 192.168.1.200
		set bundle enable compression
		set ccp yes mppc
		set ccp yes mpp-e40
		set ccp yes mpp-e128
		set ccp yes mpp-stateless

	radius:
		set radius config /etc/radius.conf
		set radius retries 3
		set radius timeout 3
		set radius acct-update 300
		set bundle enable radius-auth radius-fallback
		set bundle enable radius-acct
		set iface enable radius-idle radius-session radius-mtu radius-route
		set bundle enable compression
		set ccp yes mppc
		set ccp enable radius


この中で使用している /etc/radius.conf::

	auth 127.0.0.1 testing123
	acct 127.0.0.1 testing123

記述の意味としては、radiusサーバーでアカウント確認(acct)と認証(auth)を行うということになります。その際の接続先は127.0.0.1(localhost)で、radiusサーバーとの接続に使用するパスワードが"testing123"です。


freeradius-1.0.1の設定
-----------------------

/usr/local/etc/raddb/radius.conf のデフォルトではたくさんの認証方法が記述されていますが、今回の *LDAPで認証する* ための設定はごくごく少ない行数で書くことが出来ます。（と言っても基本設定部分は残しました）::

	prefix = /usr/local
	exec_prefix = ${prefix}
	sysconfdir = ${prefix}/etc
	localstatedir = /var
	sbindir = ${exec_prefix}/sbin
	logdir = /var/log
	raddbdir = ${sysconfdir}/raddb
	radacctdir = ${logdir}/radacct

	confdir = ${raddbdir}
	run_dir = ${localstatedir}/run/radiusd
	log_file = ${logdir}/radius.log
	libdir = ${exec_prefix}/lib
	pidfile = ${run_dir}/radiusd.pid
	max_request_time = 30
	delete_blocked_requests = no
	cleanup_delay = 5
	max_requests = 1024
	bind_address = *
	port = 0
	hostname_lookups = no
	allow_core_dumps = no
	regular_expressions	= yes
	extended_expressions	= yes
	log_stripped_names = no
	log_auth = yes
	log_auth_badpass = no
	log_auth_goodpass = no
	usercollide = no
	lower_user = no
	lower_pass = no
	nospace_user = no
	nospace_pass = no
	checkrad = ${sbindir}/checkrad
	$INCLUDE  ${confdir}/clients.conf


	modules {
		mschap {
			authtype = MS-CHAP
		}
		ldap {
			server = "localhost"
			basedn = "ou=Users,dc=freia,dc=jp"
			filter = "(uid=%{Stripped-User-Name:-%{User-Name}})"
			start_tls = no
			ldap_connections_number = 5
			timeout = 4
			timelimit = 3
			net_timeout = 1
		}
	}
	authorize {
		ldap
		mschap
	}
	authenticate {
		Auth-Type MS-CHAP {
			mschap
		}
	}

modulesセクション内のldapセクションは環境に合わせて書き換える必要があります。自分の環境ではLDAP通信の暗号化はしていないので、上記のような設定となります。あと、ここではbinddnに関する記述がありませんので、 **LDAPは無認証で一部の情報を参照できるようにしておく必要がありました** （自分はここではまりました‥‥）。

とりあえずLDAPの設定は後にして、radiusの残りの設定を行います。

/usr/local/etc/raddb/clients.conf::

	client 127.0.0.1 {
		secret    = testing123
		shortname = localhost
		nastype   = other
	}

*secret* にはradiusを利用するための認証パスワードを記述します。/etc/radius.conf に記述したパスワードですね。

/usr/local/etc/raddb/users::

	DEFAULT	Auth-Type = LDAP
		Fall-Through = 1

いちおう上記のように書いていますが、デフォルトの設定のままで問題ないようです。このファイルはユーザー個別に認証方式を変えたいときに使うんだと思いますが、今回はLDAPで管理するので、、、、もしかしてusersファイルは空でも問題ないんじゃ‥‥と思い空にしてみたところ、ちゃんと動作しました。不思議。


radius設定の最後は、/usr/local/etc/raddb/ldap.attrmapです。samba2.xを使用している場合は編集する必要はないのですが、samba3以降でスキーマが変更されているため、新しいアトリビュート名に書き換える必要があります。

変更前(samba2用)::

	checkItem	LM-Password			lmPassword
	checkItem	NT-Password			ntPassword

変更後(samba3用)::

	checkItem	LM-Password			sambaLMPassword
	checkItem	NT-Password			sambaNTPassword


これでfreeradiusの設定は完了です。単体で動作確認をしたいところですが、今回のように色々な要素が連携しているとテストするのがなかなか難しくて困りものです。

とりあえず `動作テスト`_ については最後の方に書きます。


openldap-2.2.17の設定
----------------------

LDAPの設定は完了しているものとして、ポイントだけ。

- sambaスキーマを利用している
- VPN接続アカウントは、objectClass=sambaAccountである
- 無認証で sambaNTPassword, sambaLMPassword を参照できる
- VPN接続時のパスワードにはsambaのパスワードが利用される

自分は、sambaNTPassword, sambaLMPassword を認証後でないと閲覧できないようにslapd.confを設定してしまっていたため、radiusdのログで::

  rlm_mschap: No User-Password configured.  Cannot create LM-Password.
  rlm_mschap: No User-Password configured.  Cannot create NT-Password.

なんて怒られていました。


samba-3.0.7の設定
-------------------

がんばりましょう（笑）。こちらもポイントだけ。

- VPN接続時のパスワードにはsambaのパスワードが利用される
- posixのパスワード(userPassword)とsambaのパスワードが同期している必要はない

同期している必要はないですが、認証統合するためには同期していた方がいいですね。自分の環境では、nssを使ってUnixシェル(ssh)の認証をLDAPで行ったり、Zopeのアカウント管理をLDAPでやっていたりします。詳しくは `Wikiページの方`__ を参照してください。（情報古めですが‥‥）

.. __: http://www.freia.jp/taka/wiki/X_e3_82_a2_e3_82_ab_e3_82_a6_e3_83_b3_e3_83_88_e4_b8_80_e6_8b_ac_e7_ae_a1_e7_90_86


動作テスト
-----------

動作テストのために、/usr/local/sbin/mpd -b, および /usr/local/sbin/radiusd -X で起動します。radiusの"-X"オプションはコンソールモードでの起動指定で、認証の流れを見るために指定しています。今回mpdの方は"-b"でバックグラウンド動作にしていますが、必要であれば別のコンソールで /usr/local/sbin/mpd で起動することで、両方ともコンソールモードで起動しておくことも出来ます。

そして、WindowsクライアントからVPN接続したときのradiusの画面出力は以下のようになります（IP・サーバー名・パスワードのハッシュ値などは書き換えてあります）::

	root% /usr/local/sbin/radiusd -X

	Starting - reading configuration files ...
	reread_config:  reading radiusd.conf
	Config:   including file: /usr/local/etc/raddb/clients.conf
	 main: prefix = "/usr/local"
	 main: localstatedir = "/var"
	 main: logdir = "/var/log"
	 main: libdir = "/usr/local/lib"
	 main: radacctdir = "/var/log/radacct"
	 main: hostname_lookups = no
	 main: snmp = no
	 main: max_request_time = 30
	 main: cleanup_delay = 5
	 main: max_requests = 1024
	 main: delete_blocked_requests = 0
	 main: port = 0
	 main: allow_core_dumps = no
	 main: log_stripped_names = no
	 main: log_file = "/var/log/radius.log"
	 main: log_auth = yes
	 main: log_auth_badpass = no
	 main: log_auth_goodpass = no
	 main: pidfile = "/var/run/radiusd/radiusd.pid"
	 main: user = "(null)"
	 main: group = "(null)"
	 main: usercollide = no
	 main: lower_user = "no"
	 main: lower_pass = "no"
	 main: nospace_user = "no"
	 main: nospace_pass = "no"
	 main: checkrad = "/usr/local/sbin/checkrad"
	 main: proxy_requests = yes
	 main: debug_level = 0
	read_config_files:  reading dictionary
	read_config_files:  reading naslist
	Using deprecated naslist file.  Support for this will go away soon.
	read_config_files:  reading clients
	read_config_files:  reading realms
	radiusd:  entering modules setup
	Module: Library search path is /usr/local/lib
	Module: Loaded MS-CHAP
	 mschap: use_mppe = yes
	 mschap: require_encryption = no
	 mschap: require_strong = no
	 mschap: with_ntdomain_hack = no
	 mschap: passwd = "(null)"
	 mschap: authtype = "MS-CHAP"
	 mschap: ntlm_auth = "(null)"
	Module: Instantiated mschap (mschap)
	Module: Loaded LDAP
	 ldap: server = "localhost"
	 ldap: port = 389
	 ldap: net_timeout = 1
	 ldap: timeout = 4
	 ldap: timelimit = 3
	 ldap: identity = ""
	 ldap: tls_mode = no
	 ldap: start_tls = no
	 ldap: tls_cacertfile = "(null)"
	 ldap: tls_cacertdir = "(null)"
	 ldap: tls_certfile = "(null)"
	 ldap: tls_keyfile = "(null)"
	 ldap: tls_randfile = "(null)"
	 ldap: tls_require_cert = "allow"
	 ldap: password = ""
	 ldap: basedn = "ou=Users,dc=freia,dc=jp"
	 ldap: filter = "(uid=%{Stripped-User-Name:-%{User-Name}})"
	 ldap: base_filter = "(objectclass=radiusprofile)"
	 ldap: default_profile = "(null)"
	 ldap: profile_attribute = "(null)"
	 ldap: password_header = "(null)"
	 ldap: password_attribute = "(null)"
	 ldap: access_attr = "(null)"
	 ldap: groupname_attribute = "cn"
	 ldap: groupmembership_filter = "(|(&amp;(objectClass=GroupOfNames)(member=%{Ldap-UserDn}))(&amp;(objectClass=GroupOfUniqueNames)(uniquemember=%{Ldap-UserDn})))"
	 ldap: groupmembership_attribute = "(null)"
	 ldap: dictionary_mapping = "/usr/local/etc/raddb/ldap.attrmap"
	 ldap: ldap_debug = 0
	 ldap: ldap_connections_number = 5
	 ldap: compare_check_items = no
	 ldap: access_attr_used_for_allow = yes
	 ldap: do_xlat = yes
	rlm_ldap: Registering ldap_groupcmp for Ldap-Group
	rlm_ldap: Registering ldap_xlat with xlat_name ldap
	rlm_ldap: reading ldap＜-＞radius mappings from file /usr/local/etc/raddb/ldap.attrmap
	rlm_ldap: LDAP radiusCheckItem mapped to RADIUS $GENERIC$
	rlm_ldap: LDAP radiusReplyItem mapped to RADIUS $GENERIC$
	rlm_ldap: LDAP radiusAuthType mapped to RADIUS Auth-Type
	rlm_ldap: LDAP radiusSimultaneousUse mapped to RADIUS Simultaneous-Use
	rlm_ldap: LDAP radiusCalledStationId mapped to RADIUS Called-Station-Id
	rlm_ldap: LDAP radiusCallingStationId mapped to RADIUS Calling-Station-Id
	rlm_ldap: LDAP sambaLMPassword mapped to RADIUS LM-Password
	rlm_ldap: LDAP sambaNTPassword mapped to RADIUS NT-Password
	rlm_ldap: LDAP radiusExpiration mapped to RADIUS Expiration
	rlm_ldap: LDAP radiusServiceType mapped to RADIUS Service-Type
	rlm_ldap: LDAP radiusFramedProtocol mapped to RADIUS Framed-Protocol
	rlm_ldap: LDAP radiusFramedIPAddress mapped to RADIUS Framed-IP-Address
	rlm_ldap: LDAP radiusFramedIPNetmask mapped to RADIUS Framed-IP-Netmask
	rlm_ldap: LDAP radiusFramedRoute mapped to RADIUS Framed-Route
	rlm_ldap: LDAP radiusFramedRouting mapped to RADIUS Framed-Routing
	rlm_ldap: LDAP radiusFilterId mapped to RADIUS Filter-Id
	rlm_ldap: LDAP radiusFramedMTU mapped to RADIUS Framed-MTU
	rlm_ldap: LDAP radiusFramedCompression mapped to RADIUS Framed-Compression
	rlm_ldap: LDAP radiusLoginIPHost mapped to RADIUS Login-IP-Host
	rlm_ldap: LDAP radiusLoginService mapped to RADIUS Login-Service
	rlm_ldap: LDAP radiusLoginTCPPort mapped to RADIUS Login-TCP-Port
	rlm_ldap: LDAP radiusCallbackNumber mapped to RADIUS Callback-Number
	rlm_ldap: LDAP radiusCallbackId mapped to RADIUS Callback-Id
	rlm_ldap: LDAP radiusFramedIPXNetwork mapped to RADIUS Framed-IPX-Network
	rlm_ldap: LDAP radiusClass mapped to RADIUS Class
	rlm_ldap: LDAP radiusSessionTimeout mapped to RADIUS Session-Timeout
	rlm_ldap: LDAP radiusIdleTimeout mapped to RADIUS Idle-Timeout
	rlm_ldap: LDAP radiusTerminationAction mapped to RADIUS Termination-Action
	rlm_ldap: LDAP radiusLoginLATService mapped to RADIUS Login-LAT-Service
	rlm_ldap: LDAP radiusLoginLATNode mapped to RADIUS Login-LAT-Node
	rlm_ldap: LDAP radiusLoginLATGroup mapped to RADIUS Login-LAT-Group
	rlm_ldap: LDAP radiusFramedAppleTalkLink mapped to RADIUS Framed-AppleTalk-Link
	rlm_ldap: LDAP radiusFramedAppleTalkNetwork mapped to RADIUS Framed-AppleTalk-Network
	rlm_ldap: LDAP radiusFramedAppleTalkZone mapped to RADIUS Framed-AppleTalk-Zone
	rlm_ldap: LDAP radiusPortLimit mapped to RADIUS Port-Limit
	rlm_ldap: LDAP radiusLoginLATPort mapped to RADIUS Login-LAT-Port
	conns: 0x80b8400
	Module: Instantiated ldap (ldap)
	Listening on authentication *:1812
	Listening on accounting *:1813
	Listening on proxy *:1814
	Ready to process requests.
	rad_recv: Access-Request packet from host 127.0.0.1:60238, id=122, length=164
		NAS-Identifier = "host.freia.jp"
		NAS-Port = 0
		NAS-Port-Type = Virtual
		Service-Type = Framed-User
		Framed-Protocol = PPP
		Calling-Station-Id = "219.121.60.xxx"
		User-Name = "taka"
		MS-CHAP-Challenge = 0xbb1068a606df60de71a4068500527c74
		MS-CHAP2-Response = 0x010082e63035745600d200aaa4bf454656070000000000000000b286b1c7530b18a80c82289f90e7ad4db5b01db28a0af076
	  Processing the authorize section of radiusd.conf
	modcall: entering group authorize for request 0
	rlm_ldap: - authorize
	rlm_ldap: performing user authorization for taka
	radius_xlat:  '(uid=taka)'
	radius_xlat:  'ou=Users,dc=freia,dc=jp'
	rlm_ldap: ldap_get_conn: Checking Id: 0
	rlm_ldap: ldap_get_conn: Got Id: 0
	rlm_ldap: attempting LDAP reconnection
	rlm_ldap: (re)connect to localhost:389, authentication 0
	rlm_ldap: bind as / to localhost:389
	rlm_ldap: waiting for bind result ...
	rlm_ldap: Bind was successful
	rlm_ldap: performing search in ou=Users,dc=freia,dc=jp, with filter (uid=taka)
	rlm_ldap: looking for check items in directory...
	rlm_ldap: Adding sambaNTPassword as NT-Password, value B70F540C80BBC4C037910072C04837ED &amp; op=21
	rlm_ldap: Adding sambaLMPassword as LM-Password, value 5F029DC02B6C0D0C87690D42E08DF5EE &amp; op=21
	rlm_ldap: looking for reply items in directory...
	rlm_ldap: user taka authorized to use remote access
	rlm_ldap: ldap_release_conn: Release Id: 0
	  modcall[authorize]: module "ldap" returns ok for request 0
	  rlm_mschap: Found MS-CHAP attributes.  Setting 'Auth-Type  = MS-CHAP'
	  modcall[authorize]: module "mschap" returns ok for request 0
	modcall: group authorize returns ok for request 0
	  rad_check_password:  Found Auth-Type MS-CHAP
	auth: type "MS-CHAP"
	  Processing the authenticate section of radiusd.conf
	modcall: entering group Auth-Type for request 0
	  rlm_mschap: Found LM-Password
	  rlm_mschap: Found NT-Password
	  rlm_mschap: Told to do MS-CHAPv2 for taka with NT-Password
	rlm_mschap: adding MS-CHAPv2 MPPE keys
	  modcall[authenticate]: module "mschap" returns ok for request 0
	modcall: group Auth-Type returns ok for request 0
	Login OK: [taka] (from client localhost port 0 cli 219.121.60.111)
	Sending Access-Accept of id 122 to 127.0.0.1:60238
		MS-CHAP2-Success = 0x01533d41324643393538044345373733063439463246024331353330324146423601383431430241303936
		MS-MPPE-Recv-Key = 0x408c031d5390d2c72b140b004f0df5fc
		MS-MPPE-Send-Key = 0x56815e0082a820e2e891bc02aa20628e
		MS-MPPE-Encryption-Policy = 0x00000001
		MS-MPPE-Encryption-Types = 0x00000006
	Finished request 0


まず起動から見ていきましょう。

起動時にradius上の設定情報とLDAPの情報をマッピングしている箇所で、正しくsambaNTPassword,sambaLMPasswordをマッピングしていればOKです::

	rlm_ldap: LDAP sambaLMPassword mapped to RADIUS LM-Password
	rlm_ldap: LDAP sambaNTPassword mapped to RADIUS NT-Password

WindowsクライアントからVPN接続を行い、mpdから認証要請が来た部分が以下の行です::

	rad_recv: Access-Request packet from host 127.0.0.1:60238, id=122, length=164

その後、mpdからの問い合わせ情報を元に、ldapから認証のための情報を取得しています。LDAPではパスワード認証ではなくアカウントの存在だけがチェックされますが、もう一つの重要な情報、sambaパスワードのハッシュ値がradiusに渡されます::

	modcall: entering group authorize for request 0
	rlm_ldap: - authorize
	rlm_ldap: performing user authorization for taka
	radius_xlat:  '(uid=taka)'
	radius_xlat:  'ou=Users,dc=freia,dc=jp'
	rlm_ldap: ldap_get_conn: Checking Id: 0
	rlm_ldap: ldap_get_conn: Got Id: 0
	rlm_ldap: attempting LDAP reconnection
	rlm_ldap: (re)connect to localhost:389, authentication 0
	rlm_ldap: bind as / to localhost:389
	rlm_ldap: waiting for bind result ...
	rlm_ldap: Bind was successful
	rlm_ldap: performing search in ou=Users,dc=freia,dc=jp, with filter (uid=taka)
	rlm_ldap: looking for check items in directory...
	rlm_ldap: Adding sambaNTPassword as NT-Password, value B70F540C80BBC4C037910072C04837ED &amp; op=21
	rlm_ldap: Adding sambaLMPassword as LM-Password, value 5F029DC02B6C0D0C87690D42E08DF5EE &amp; op=21
	rlm_ldap: looking for reply items in directory...
	rlm_ldap: user taka authorized to use remote access
	rlm_ldap: ldap_release_conn: Release Id: 0
	  modcall[authorize]: module "ldap" returns ok for request 0

上記で、LDAPとうまく連携できていれば、sambaNTPasswordとsambaLMPasswordが NT-Password, LM-Password という変数に取得されていることが表示されます。もしこの二つの値を取得できなかったとしてもldapモジュールでのauthorizeは成功したと表示されてしまう(最後の行)ため、注意してみておく必要があります（ありました...)。

そして最後にMS-CHAPによるパスワードチェックです::

	  rad_check_password:  Found Auth-Type MS-CHAP
	auth: type "MS-CHAP"
	  Processing the authenticate section of radiusd.conf
	modcall: entering group Auth-Type for request 0
	  rlm_mschap: Found LM-Password
	  rlm_mschap: Found NT-Password
	  rlm_mschap: Told to do MS-CHAPv2 for taka with NT-Password
	rlm_mschap: adding MS-CHAPv2 MPPE keys
	  modcall[authenticate]: module "mschap" returns ok for request 0
	modcall: group Auth-Type returns ok for request 0

ここで、以下の二行::

	  rlm_mschap: Found LM-Password
	  rlm_mschap: Found NT-Password

はLDAPからアカウント確認時に取得している値が使用されます。もしLDAPから取得できていない場合、この部分のログが以下のようになってしまいます::

	rlm_mschap: No User-Password configured.  Cannot create LM-Password.
	rlm_mschap: No User-Password configured.  Cannot create NT-Password.
	rlm_mschap: Told to do MS-CHAPv2 for taka with NT-Password

最初これを見て、radiusにUser-Passwordを渡す方法を調べたり、やっぱりLDAP内にプレーンテキストでパスワードを格納するしかないんじゃないか、とか思ったりしていました。


ということで、全てうまく動作すると最後に::

	Login OK: [taka] (from client localhost port 0 cli 219.121.60.111)
	Sending Access-Accept of id 122 to 127.0.0.1:60238
		MS-CHAP2-Success = 0x01533d41324643393538044345373733063439463246024331353330324146423601383431430241303936
		MS-MPPE-Recv-Key = 0x408c031d5390d2c72b140b004f0df5fc
		MS-MPPE-Send-Key = 0x56815e0082a820e2e891bc02aa20628e
		MS-MPPE-Encryption-Policy = 0x00000001
		MS-MPPE-Encryption-Types = 0x00000006
	Finished request 0

となり、VPN接続が行われます。

あとは通常運用用に /usr/local/etc/rc.d/radius.sh が起動するように、rc.conf に以下を記述します::

	radiusd_enable="YES"



参考にしたサイト
-----------------

非常に参考になりました。こういったサイトが無ければ分厚いradiusの本と格闘したり、英語の森の中を1ヶ月くらいさまよっていたのではないかと思います。筆者の方々に深くお礼申し上げます。

- `RADIUSのMS-CHAP認証にLDAPを使う`_ (シーザーサラダとエビカレーの日々 より)
- `mpdとFreeRadius(+PostgreSQL)の連携`_ (未整理文章/コラムの種 より)
- `LDAP を使った Radius 認証`_ (LDAP Implementation HOWTO より)
- `freeRADIUS and openldap on FreeBSD`_ (Nob's Home Page より)

.. _`LDAP を使った Radius 認証`: http://www.linux.or.jp/JF/JFdocs/LDAP-Implementation-HOWTO/radius.html
.. _`freeRADIUS and openldap on FreeBSD`: http://www.y-min.or.jp/~nob/FreeBSD/freeradius-openldap.html
.. _`mpdとFreeRadius(+PostgreSQL)の連携`: http://kozuka.jp/tdiary-blog_html/20030507.html
.. _`RADIUSのMS-CHAP認証にLDAPを使う`: http://www.aineas.net/linux/ldap/radius.php






.. :trackbacks:
.. :trackback id: 2006-06-15.9254128351
.. :title: 続 sambaldap-tools
.. :blog name: uep on hayate
.. :url: http://uep.hayate.mine.nu/archives/2006/06/_sambaldaptools.php
.. :date: 2006-06-15 08:15:26
.. :body:
.. pptpの認証もLDAPで行いたいと思い、色々調べてみた。 どうやら、pptp-...
.. 

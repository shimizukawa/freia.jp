:date: 2005-06-09 01:20:12
:tags: Unix
:body type: text/x-rst

==========================================================
2005/06/09 Apacheの認証をLDAPでActiveDirectoryに問い合わせ
==========================================================

Apache2からWindows2003/ActiveDirectoryに対してLDAPで認証を行ってみた。試行錯誤の末、とりあえず目的の半分は達成した。

Windows2003なActiveDirectoryに格納されているユーザーの認証はうまくいっているのに、どうやらWindows2000なActiveDirectoryへの問い合わせがうまくいかないらしい。この2台が同一ドメインの親子関係にあるため ＆ ActiveDirectoryの中身をよく知らなかったことで、問題の切り分けに手間取ってしまった。




.. :extend type: text/x-rst
.. :extend:

以下は最終的にとりあえず落ち着いている設定。

.. code-block:: apache

  AuthName "Please enter your ID and password"
  AuthType Basic

  ## for Windows2003 ActiveDirectory
  AuthLDAPBindDN Administrator@dom.example.com
  AuthLDAPBindPassword secret
  AuthLDAPUrl ldap://sub1.dom.example.com:389/dc=sub1,dc=dom,dc=example,dc=com?sAMAccountName?sub

  ## for OpenLDAP
  #AuthLDAPUrl ldap://openldap.example.com:389/ou=Users,dc=example,dc=com?uid?sub

  Require valid-user

DNの記述
---------

BindDNでLDAPだと ```cn=Manager,dc=example,dc=com``` と書くところが、ActiveDirectoryだと ```Manager@example.com``` としないといけないようだ。それでいてユーザー検索のBaseDNは ```ou=Users,dc=example,dc=com``` だったり。混乱するなぁ！

ユーザーIDの指定
-----------------

認証先がOpenLDAPなら、uidとかcnとかのいわゆるアカウント名をブラウザの認証ダイアログに指定する。以下の例なら *taka* と入れるわけだ::

  dn: uid=taka,ou=Users,dc=example,dc=com
  uid: taka

ところが、ActiveDirectoryの場合は(自分には)ちょっと複雑で以下のようになっている::

  dn: CN=清水川,DC=dom,DC=example,DC=com
  cn: 清水川
  userPrincipalName: taka@dom.example.com
  sAMAccountName: taka

Windowsのログイン名がそのまま使えます！と言うためには sAMAccountName 属性を使って認証するしかない？ていうかdnはログイン名(taka)じゃないの？え？日本語？

検索と認証の二段階
-------------------

最初はLDAPにbindする事で認証出来るようにしたかった。そうすればLDAPにアクセスするための管理者アカウント設定等を.htaccessとかに書かなくて良くなるからだ。ところが、前述の `ユーザーIDの指定`_ のようになっていると、ブラウザの認証ダイアログに入力されたアカウント名でもってbindする方法がよくわからなかった。AuthLDAPUrlでは無理なのかも？ということで、今はLDAPにアクセス出来るアカウントが.htaccessに書かれている。セキュリティー気をつけないと。

そして問題
-----------

認証先のActiveDirectoryはドメインツリーを構成しているので、ユーザーが ```dom.example.com``` と ```sub1.dom.example.com``` に分割登録されている。そこで、 ```dom.example.com``` の方にscope=subで検索をかければ全員認証出来るかな？と思って試してみたところ、どうもうまくいかない。で、ldapsearchで試してみたところ、以下のように表示された::

  % ldapsearch -h dom.example.com -a always -s sub -D \
    "Administrator@dom.example.com" -W -b "dc=dom,dc=example,dc=com"

    #中略(親側サーバーに入っている全ユーザーのデータ表示)

  # search reference
  ref: ldap://sub1.dom.example.com/DC=sub1,DC=dom,DC=example,DC=com

あー、サブドメイン側 ```sub1.dom.example.com``` のデータは reference になってるのか...。referenceはよくわからんのだけど、 `mod_auth_ldap`_ では解決してくれないのかな？もしかしてこれのせいでうまくいってないのかな？？

でも冒頭に書いたように、単にWindows2000の方(親の方)でなにか問題が起きてるのかも？そういえばLDAPで直接問い合わせてもなぜかmod_auth_ldapがエラーを起こして認証出来なかったし！と今これを書きながら思ったり。

.. _`mod_auth_ldap`: http://httpd.apache.org/docs-2.0/ja/mod/mod_auth_ldap.html

まとめと逃避
-------------

認証ダイアログでPrincipalNameを打ち込む事にすると解決する問題なのかもしれない。あるいはもしかしたら、LDAP使わなければ簡単に解決出来るんだろうか？Radius認証とか色々Apache用の認証モジュールはあるみたいだし、pamに逃げるという手もある。pam -> samba -> AD とか。簡単に解決する方法を調べるために、もうちょっともがいてみよう....。


*# カテゴリ、Windowsかな..*




.. :comments:
.. :comment id: 2005-11-28.5090157732
.. :title: Re: Apacheの認証をLDAPでActiveDirectoryに問い合わせ
.. :author: 佐藤敦司
.. :date: 2005-06-28 19:49:01
.. :email: atsushi.satoh@gmail.com
.. :url: http://www.bloglines.com/blog/SatoAtsushi
.. :body:
.. Good Job!!
.. ありがとうございました。
.. 半年ぶりの懸案が片付いたところです。
.. 
.. ただ、やはり王道は pam => winbind/samba => AD
.. のような気がします。
.. 
.. ＃パスワードっていうのがはやり。。。。
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.5091314934
.. :title: Re: Apacheの認証をLDAPでActiveDirectoryに問い合わせ
.. :author: 清水川
.. :date: 2005-06-28 22:44:13
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. ＞半年ぶりの懸案が片付いたところです。
.. 
.. おお！それはよかった！
.. こちらは未だにWindows2000Serverに対してmod_auth_ldapでユーザー認証できません...orz。ldapsearchならちゃんと認証してくれるんだけどなぁ..。
.. 
.. 
.. :comments:
.. :comment id: 2006-01-23.4221108234
.. :title: Re:Apacheの認証をLDAPでActiveDirectoryに問い合わせ
.. :author: Anonymous User
.. :date: 2006-01-23 15:57:02
.. :email: 
.. :url: http://www.eyesom.com
.. :body:
.. Windows2000Serverに対してmod
.. 
.. :comments:
.. :comment id: 2008-03-17.8058409750
.. :title: Re:Apacheの認証をLDAPでActiveDirectoryに問い合わせ
.. :author: Anonymous User
.. :date: 2008-03-17 09:46:46
.. :email: nospam
.. :url: 
.. :body:
.. ADではAnonymous認証でないからユーザとパスワードがいるんじゃないの？
.. 
.. 
.. :comments:
.. :comment id: 2008-03-17.0854601007
.. :title: Re:Apacheの認証をLDAPでActiveDirectoryに問い合わせ
.. :author: しみずかわ
.. :date: 2008-03-17 13:28:05
.. :email: 
.. :url: 
.. :body:
.. cnが日本語じゃなくアカウントIDならそのIDでbindしてしまえるので問題ないんだけど、この例では管理者権限でbindするために.htaccessに記載している。危ない。
.. 

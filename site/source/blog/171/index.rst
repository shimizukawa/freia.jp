:date: 2005-03-24 01:22:53
:categories: ['Unix']
:body type: text/x-rst

==========================================================
2005/03/24 vpopmail with LDAP認証 by FreeBSD ports (第2回)
==========================================================

*Category: 'Unix'*

`第1回`_ に引き続き、vpopmail-ldapの設定を行う。

README.ldap を読み進めたところ、昨日改造したvldap.hに埋め込まれているDNで重要になるポイントは

1. vpopmail から LDAP へアクセスする際の認証アカウント
2. vpopmail から LDAP へアクセスする際の認証パスワード
3. バーチャルドメインを格納するBaseディレクトリ

の3つだった。ということは、1,2については既存のManagerアカウントを指定することにして、3だけを（実験なので深く考えずに）専用ディレクトリとして用意する。デフォルトでは o=vpopmail なのだが、既存のマイLDAP構成に合わせて以下のように変更して、vpopmailのビルド＆インストールをやり直した。

patch-vldap.hの記述変更点::

  #define VLDAP_BASEDN "o=vpopmail,dc=example,dc=jp"

slapd.conf に以下の記述を追加::

  include         /usr/local/etc/openldap/schema/qmailUser.schema
  schemacheck off

vpopmail-5.4.6/ldap/vpopmail.ldif を patch-vldap.h に合わせて修正::

  dn: o=vpopmail,dc=example,dc=com
  objectClass: Organization
  o: vpopmail

LDAPに上記のvpopmail.ldifを食わせる::

  host# ldapadd -f vpopmail.ldif -D 'cn=Manager,dc=example,dc=com' -W

ここまで成功したら、最後にバーチャルドメインを作成してみる::

  /usr/local/vpopmail/bin/vadddomain host.example.com postmasterpassword

うまくいっていれば、postmasterアカウントが作成されているはず::

  host# ldapsearch -LLL -b 'o=vpopmail,dc=example,dc=jp'

  dn: o=vpopmail,dc=example,dc=jp
  objectClass: organization
  o: vpopmail
  
  dn: ou=host.example.jp,o=vpopmail,dc=example,dc=jp
  ou: host.example.jp
  objectClass: organizationalUnit
  
  dn: uid=postmaster,ou=host.example.jp,o=vpopmail,dc=example,dc=jp
  uid: postmaster
  qmailUID: 1
  qmailGID: 0
  qmaildomain: Postmaster
  mailMessageStore: /usr/local/vpopmail/domains/host.example.jp/postmaster
  mailQuota: NOQUOTA
  objectClass: qmailUser


どうやらここまでは成功したみたいなので、次はメールの送受信を確認してみようと思う。

ところで、LDAP上に追加されたアカウント情報を既存のアカウントとどうやって一元管理すればいいのかわからない。ショートカットみたいにして、別のディレクトリにあるuidを参照するような機構ってLDAPにあるのかな‥‥。読みかけで放置してるLDAP本もうすこしちゃんとよまないといかんなぁ。



.. _`第1回`: http://www.freia.jp/taka/blog/168




.. :extend type: text/plain
.. :extend:


:date: 2005-03-23 00:07:19
:categories: ['Unix']
:body type: text/x-rst

=======================================
vpopmail with LDAP認証 by FreeBSD ports
=======================================

vpopmailでldap認証を使うには::

  ./configure --enable-auth-module=ldap

する。（と README.ldap に書いてあった）

でもこのままmakeしても、-lresolv リンカオプションで引っかかるので、configure, configure.in から -lresolv を削除してみたところ、ビルドに成功したようだ。

あと、vpopmailでLDAPを使うためには、vldap.hにBaseDNやらLDAPアクセス用のパスワードやらを埋め込んでからビルドする必要がありそうなのでそれも入れる‥‥なんてことを毎回手動でやるのはタルイので、port/mail/vpopmail/files にパッチとして置いてみる。

最後に、MakefileをLDAP対応に書き換える‥‥いいやもうLDAPきめうちにしちゃえ。

- `vpopmail-5.4.6-port20050322.tgz`_ (patch-vldap.h書き換えてネver)

というかビルドしただけで全然動かしてもいないのに公開していいものなのか？とりあえず明日動作確認しよう‥‥。

.. _`vpopmail-5.4.6-port20050322.tgz`: file/vpopmail-5.4.6-port20050322.tgz


.. :extend type: text/plain
.. :extend:

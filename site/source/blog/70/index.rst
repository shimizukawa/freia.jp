:date: 2004-09-25 23:19:21
:categories: ['Unix']
:body type: text/x-rst

=========================
2004/09/25 samba3.0へ移行
=========================

*Category: 'Unix'*

先日サーバーを入れ替えたときにsambaを2.2.xから3.0.xへ移行したのですが、LDAPスキーマの移行が面倒そう(笑)だったのでとりあえず自分のアカウントだけsmbpasswdに作っておいたのでした。とはいえ、そろそろあちこち中途半端なのをなんとかせねばなぁ……ということで、samba.schemaを2.2.xから3.0.xへ移行しました。



.. :extend type: text/plain
.. :extend:

移行はUNIX USER 2003年12月号を参考に行いました。以下、その概要です。

1. slapcat -l samba2.ldif
2. net getlocalsid > sid
3. [samba3]/example/LDAP/convertSambaAccount --sid=[2のsid] --input samba2.ldif --output samba3.ldif
4. ldapのデータを初期化
5. slapadd -l samba3.ldif

上記4で、データの上書き・初期化方法が分からなかったので、データベースファイルを削除してしまいました。……いいのかな？

とりあえずsambaのアカウントをLDAP参照にすることはできました。あとこのほかにZope上から変更とか、Unixアカウントと同期とか、pythonでスクリプト組むとかいろいろとやりたいことが残っていますが、ま、ぼちぼちやっていこうと思います。



:date: 2005-01-08 20:14:36
:tags: Zope, python
:body type: text/x-rst

==============================================
2005/01/08 LDAPのアカウント管理をZopeProductで
==============================================

昨年末からLDAPのユーザーアカウント管理を Zope_ [1]_ 上で行うためのProduct [2]_ を作成している。Productを作るのは初めてなので、ちょっとしたことが分からずに苦労が多い。

LDAPUserFolder_ というProductはZopeのユーザー管理をLDAPで行うことが出来るが、自分が作ろうとしているのはもうちょっとLDAP全般のアカウントやグループを管理するもの。思いつくところで、samba,unix,zope,apache,qmail,radius....というところか。

最初に名前を付けたときに思いつきで *LDAPAccountManager* という名前にしたら、PHPで `同じ名前のツール`_ があることを最近知った...。これつかえば良いような気がしないでもない今日この頃。


.. [1] オブジェクトデータベース型Webアプリケーションサーバー....であってるかな？
.. [2] Zopeの機能を拡張するpluginみたいなもの

.. _Zope: http://zope.jp/
.. _LDAPUserFolder: http://www.dataflake.org/software/ldapuserfolder/
.. _`同じ名前のツール`: http://lam.sourceforge.net/


.. :extend type: text/plain
.. :extend:


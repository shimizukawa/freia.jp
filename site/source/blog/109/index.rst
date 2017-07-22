:date: 2005-01-16 19:55:15
:tags: Zope
:body type: text/x-rst

====================================================
2005/01/16 PloneのユーザーとグループをLDAPで管理する
====================================================

LDAPですべてのユーザー管理を行うことを目標に、今回はPloneのユーザー・グループ管理をLDAPでやってみる実験をしてみた。

結論： **難解**

結局今のところ、Plone2.1待ちだったりGRUF3.2待ちだったりするので、今公開されているPlone2.0.5やGRUF3.2RC1で運用するにはいくつか我慢しないといけない部分がある。
詳しくは、GRUF3.2RC1に添付されているREADME.txt, README-Plone.stx, README-LDAP.stx を参照。README.txtに同梱されているIRCのチャットログがすべてを物語っている気がする。

それはそれとして。今のバージョンでLDAP管理を使おうとした場合の手順と、自分の作業課題をメモメモ。

*# あーー、つかれたー*


.. :extend type: text/x-rst
.. :extend:

確立した手順
--------------
- Products
    - `Plone2.0.5`_
    - `GRUF3.2RC1`_
    - `LDAPUserFolder2.4`_
- Setup （すべてPloneSiteオブジェクト以下で作業）
    - portal_skin/gruf_ldap_required_fields をcustomへ。
        - 何も変更せずに保存。(標準ではなぜかsyntax error）
    - acl_users→sourceの変更
        - UserSourceをLDAPUserFolderに設定、Group Stored on LDAPとする
        - GroupSourceをLDAPGroupFolderに設定
    - ZopeRoleのマッピング
        - PloneのRole名と同じ名前のGroupをLDAPに作り、mappingする
            - acl_users/Groups/LDAPGoupsFolderへ移動
            - GroupsタブでManager,Member,ReviewerをgroupOfUniqueMemberで追加
            - ページ下のAdd LDAP group to Zope role mapping で上記3つをマップ
    - Ploneグループの追加
        - Ploneの管理画面上でふつうに追加可能。
        - Role名がGroupとして見えるが、無視。
    - ユーザー追加
        - ふつうに追加
        - ログインするまではそのままでは検索一覧に見えない


残った問題と課題
----------------
- ユーザーデータ
    - plone上からパスワード変更を行った場合にsambaパスワードも変更したい
    - uidを使えるようにしたい
    - mailaddrをLDAP上に格納したい
    - FullNameをLDAP上に格納したい
    - LDAPのcn,snがどちらもloginIdと同じになる問題
- Plone上でユーザー一覧が表示されない（LDAPUserFolderの制限）
- Plone上にZopeRoleにマッピングしたLDAPのGroupが表示される
- manageページのGRUFでユーザー追加直後に"Clicking here"のリンク先が間違っている
    - リロードしてもNG
    - Usersタブを一度クリックするとOK
- 追加後manageページのGRUFのUser一覧から追加ユーザーのリンクがエラーとなる
    - そのユーザーでログオンするとOKとなる。(readme-plone.stx)
- 追加後ユーザーグループ管理で一覧に出てこない
    - そのユーザーでログオンして個人設定を保存した直後は一覧にでる
    - Groupの追加等を行うと再び表示されなくなる
- manageの各ユーザー設定で、SetGroups,SetRolesでchangeするとエラーとなる
    - グループにroleを割り当てられない件と同一原因ではない。


罠
----
- LDAPUserFolderExtはGRUF3.1.xに取り込まれているため不要
- LDAPUserFolder non-ASCII support complete はLDAPUserFolder2.3β3に取り込まれているため不要


.. _`Plone2.0.5`: http://plone.org/downloads
.. _`GRUF3.2RC1`: http://ingeniweb.sourceforge.net/Products/GroupUserFolder/
.. _`LDAPUserFolder2.4`: http://www.dataflake.org/software/ldapuserfolder/



:date: 2009-01-22 02:16:01
:tags: Zope, Plone

==========================================
2009/01/22 ATExtFlashをPlone3対応にする(1)
==========================================

試行錯誤メモです。

技術のノウハウって試行錯誤で得られた結果も大事だけど、課程も大事だよね、というもっともらしい理屈をつけてblogのエントリを水増しする計画。

:元ソースコード: http://svn.freia.jp/open/ATExtFlash/branches/plone2.1.x
:Python: 2.4.4
:Zope: 2.10.7
:Plone: 3.1.6
:OS: Windows Vista


CMFCorePermissionsが無い
-------------------------

permissions.py で::

  from Products.CMFCore.CMFCorePermissions import setDefaultRoles

がエラーになってZopeを起動できなかった。
以下のようにして修正。(code from Products/kupu)::

  try:
      from Products.CMFCore.permissions import setDefaultRoles
  except ImportError:
      # for CMF 1.4
      from Products.CMFCore.CMFCorePermissions import setDefaultRoles


CMFQuickInstallerTool のエラー
------------------------------

Ploneインスタンス追加時にGenericSetupのログに混じって以下のエラーが表示された::

  2009-01-22 01:53:44 ERROR CMFQuickInstallerTool ATExtFlash, ImportError: No module named migrate

何だろう。GenericSetupじゃなくて従来のCMFQuickInstallerでうまくやってくれようとしたけど、何かmigrateという名前のモジュールがないというエラーが出ている。エラーは出ているもののplone siteオブジェクトの追加は出来たので、Ploneの画面でアドオンプロダクトの追加画面で追加しようと思ったけど、追加Productの一覧にATExtFlashが表示されていなかった。やっぱり直さないとだめか。

調べてみたら、 ATExtFlash/Extensions/Install.py の中で::

  from Products.CMFDynamicViewFTI.migrate import migrateFTIs

という記載があり、Products.CMFDynamicViewFTIにmigrateというモジュールが無くなっていた。そしてmigrateFTIsというモジュール?/関数? も見あたらなかった。これを追っかけるのが早いか、GenericSetup対応に書き換えるのが早いか...。多分Ploneの開発者向けドキュメントを見ながらGenericSetup対応したほうが早そうだ。


今日はここまで。


.. :extend type: text/html
.. :extend:


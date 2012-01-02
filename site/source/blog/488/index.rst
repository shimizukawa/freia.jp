:date: 2007-10-27 23:18:22
:categories: ['Zope', 'Plone']
:body type: text/x-rst

=============================================================
2007/10/27 PASRadius-0.2 for PluggableAuthService(Zope/Plone)
=============================================================

*Category: 'Zope', 'Plone'*

PASRadius - Radius authentication plugin for PluggableAuthService ver 0.2 Python温泉リリース。

- `PASRadius-0.2`_　

Web投稿で以下のようなメッセージをもらった(原文は英語)。

.. Topic:: もらったメッセージ超訳

  Hi there, PASRadiusにemailアドレスが見つからなかったのでweb formから送るよ。
  PluggableAuthService(1.5-final)でPASRadius使うと、以下のエラーがでるよ：
  
    File "/home/faassen/working/instances210/RadiusZope/Products/PASRadius/radiusplu gin.py", line 26,
    in ? from Products.PluggableAuthService.utils import classImplements,Interface

    ImportError: cannot import Interface
  
  これはradiusplugin.pyを次のようにすれば簡単に修正できる：
  
  :元:
      from Products.PluggableAuthService.utils import classImplements, Interface
  
  :先:
      from Products.PluggableAuthService.utils import classImplements

      from zope.interface import Interface
  
  （classImplementsもzope.interfaceからimportすれば良いんじゃない？）
  この修正を行って新しい版をリリースしない？

ということで、Python温泉合宿タスクとして、直してみました。PAS-1.5対応。

classImplementsはPluggableAuthService.utilsで何かやってるので、まだ直接importするのは
避けた方がいいかなぁ、ということでそこはとりあえずtry/exceptでゴニョゴニョ。

# 半月放置ごめんなさい..

.. _`PASRadius-0.2`: http://www.zope.org/Members/shimizukawa/PASRadius



.. :extend type: text/html
.. :extend:


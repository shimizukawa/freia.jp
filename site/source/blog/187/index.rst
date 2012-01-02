:date: 2005-04-18 00:13:45
:categories: ['Zope']
:body type: text/x-rst

=============================
2005/04/18 サーバー移行、失敗
=============================

*Category: 'Zope'*

以前サーバーのマザーボードが壊れてから臨時に１代前のメインPCをサーバーにしていたが、臨時だったためDISKの冗長性とか全然無いまま半年ほど運用していた。で、先日やっと新サーバーを用意して、いろいろと移行の事前テストやら冗長性のテストやらを行って今日やっと移行まで行うことが出来た。

が。なぜか実験時には問題なかったZopeの移行がうまくいかない。Ploneサイトを表示しようとするとAnonymousで許可しているページにもかかわらずエラーになってしまう。

エラー時のログ(抜粋)::

  <FSPageTemplate at /taka/login_form>
  Module Products.PageTemplates.TALES, line 221, in evaluate
  Line 131, Column 4
  Expression: <PythonExpr member.getProperty('formtooltips', showdefault)>

  Unauthorized: Your user account does not have the required permission. 
  Access to 'getProperty' of Anonymous User denied. Your user account, 
  Anonymous User, exists at /acl_users. Access requires 
  View_management_screens_Permission, granted to the following roles: 
  ['Manager']. Your roles in this context are ['Anonymous']. (Also, an 
  error occurred while attempting to render the standard error message.)

うーん、Manager権限が必要なのにAnonymousでアクセスしようとしている、、と言われてもなぁ。とりあえずZopeだけ旧サーバーに戻した。原因解析は明日だなぁ‥‥。



.. :extend type: text/plain
.. :extend:


.. :comments:
.. :comment id: 2005-11-28.4927198623
.. :title: Re: サーバー移行、失敗
.. :author: 清水川
.. :date: 2005-04-18 00:14:50
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. 今日は曇り。今日は曇り。

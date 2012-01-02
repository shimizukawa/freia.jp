:date: 2007-07-07 19:50:19
:categories: ['Zope', 'Plone']
:body type: text/x-rst

=====================================
2007/07/07 Plone2.5のRadius認証Plugin
=====================================

PASRadius - Radius authentication plugin for PluggableAuthService ver 0.1 七夕リリース。

- `PASRadius-0.1.tgz`_　

Plone-JP のMLでPASのradius認証プラグイン無いねー、という話が出ていたので、PluggableAuthServiceの勉強がてらに作ってみました。

PluggableAuthServiceのコードはそれなりにzope3化されているので、Zope3を知っていればとても簡単、知らなくてもわかりやすいフレームワークに仕上がってる感じです。逆に、Zope2なコードを書くのは結構久しぶりだったので変なところではまりまくりました。どうして公開メソッドにはDocStringが必須なんだっけ‥‥（1時間くらい悩んだ）。

それにしても、PAS用RADIUSプラグインなんてもうあるんじゃないの？と思って検索してみても、ヒットするのは

1. PASを使うと簡単に認証を拡張できる
2. でもRADIUS用のpluginは今のところ無い
3. しょうがないからPlone2.1系を使う

という流ればっかりでした。RADIUSの需要が無いのか、認証系はバグがあるとアブナイのでだれも作りたがらないのか‥‥。需要という意味では、自宅のRADIUSサーバーも実際はLDAPに問い合わせしてるだけ。mpdというVPNサーバーがLDAP認証できないけどRADIUS認証出来るので、そのために立ち上げてるだけ。そういう意味ではPASRadiusを作ったものの、常用はしないだろうなあ‥‥。

参考: `PlonePASとPluggableAuthService — Garage with Blue Sky`_

.. _`PASRadius-0.1.tgz`: http://www.zope.org/Members/shimizukawa/PASRadius
.. _`PlonePASとPluggableAuthService — Garage with Blue Sky`: http://www.wedgeshape.com/wedge/gwbs/plonepas-pluggableauthservice


.. :extend type: text/html
.. :extend:

:date: 2005-01-27 21:38:57
:tags: Zope, Memo
:body type: text/x-rst

===============================
2005/01/27 _SUPPRESS_ACCESSRULE
===============================

Zope上で設定や開発をしていてよくはまった罠が二つある。

- Site Rootの設定を間違えた
- Set Access Ruleを設定したPythonScriptが例外を出す状態で保存してしまった

どちらも大抵はサブフォルダ以下にアクセスできなくなってしまう。回避方法の一つにFTP接続で対象オブジェクトを削除してしまうというのがあるけど、もう一つの方法が以下のように対象のURLに回避指定を入れる方法::

  Site Rootの場合は
    http://www.freia.jp/target/_SUPPRESS_SITEROOT/manage
  Set Access Ruleの場合は
    http://www.freia.jp/target/_SUPPRESS_ACCESSRULE/manage

Site Rootの方は `Zopeガイド`_ に載っていたけど、AccessRuleは載っていなかったのでメモ。

.. _`Zopeガイド`: http://www.amazon.co.jp/exec/obidos/ASIN/4839907900



.. :extend type: text/plain
.. :extend:


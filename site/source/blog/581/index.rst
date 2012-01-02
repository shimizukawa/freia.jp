:date: 2008-06-22 00:56:26
:categories: ['Zope']
:body type: text/x-rst

===========================================
2008/06/22 Zope-2.11.0 がリリースされました
===========================================

*Category: 'Zope'*

zope-usersとplone-usersの日本のMLに流した文面をこちらにも掲載しておきます。

- http://ml.zope.jp/pipermail/zope-users/2008-June/006121.html
- http://ml.plone.jp/pipermail/plone-users/2008-June/001341.html

------------------------

6月21日にZope-2.11.0がリリースされました。
様々な機能追加・バグ修正などが行われていますが、同時に古い実装コードの
整理やzope3パッケージ化の進行などによるプロダクトや日本語まわりへの
影響も懸念されます。


目立つ変更点としては、

1. 最新のZopeコンポーネント(Zope-3.4.0)を組み込み
2. BLOB(binary large objects)に対応したZODB 3.8にアップデート
3. トランザクション対応のMailHost実装に対応し、非同期でメール送信
4. Windowsでzopectlを使えるようになった
5. Script(Python)でsetsモジュールを使えるようになった

個人的にはWindowsでzopectlを使えるのがうれしいですね。
あと、MailHostの実装変更でjaMailHostに影響がある気がします。


削除された機能として目立つのは、

1. ZGadflyDA が削除された (Productのコードは入手可能)
2. ``OFS.content_types``, ``__ac_permissions__``, ``meta_types`` を削除

このあたりを使っているプロダクトが起動しなくなるトラブルが起きそうです。


日本語周りで気になるのは、

1. ZopePageTemplate の内部実装にunicodeを使用するようになった
   (utf-8かISO-8859-15以外で使う場合は環境変数 ``ZPT_REFERRED_ENCODING`` の設定が必要)

これは環境変数設定が必要なので、起動スクリプトへの仕込みをしておく
のがよさそうです。(zope.confに入れて欲しかったところですが...)


CHANGESの翻訳を以下に掲載しています。

- http://zope.jp/download/zope/releases/2.11.0


.. :extend type: text/html
.. :extend:


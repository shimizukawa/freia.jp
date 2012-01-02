:date: 2009-12-27 19:24:35
:categories: ['Zope']
:body type: text/x-rst

===========================================================
2009/12/27 Zope-2.12.2 リリース & buildout での環境構築メモ
===========================================================

Zope 2.12.2 が先週12/22にリリースされました。リリースされるのは、その１週間も前から分かっていたんだけど、ぼーっと過ごしていたら翻訳が遅れました＞＜

* 翻訳: http://docs.zope.jp/zope2/releases/2.12/CHANGES.html#zope-2-12-2-2009-12-22

同日、2.10.10, 2.11.5 もリリースされたけどこれはまあいいや。

Zope 2.12.2 ではついに management_page_charset のデフォルト値がiso-8859-1 から utf-8 に変更になって、これで日本語を使う際の必須TIPSが1つ不要になりました。また、Python-2.4 は完全にサポート外なり、正式サポートはPython 2.6のみになっています。2.5のサポートも非公式になっちゃったけど、Zope使ってる人は今まで2.4しか使えなかったわけだし、2.5はまあサポート無くてもあんまり困らなそうね。


buildoutでの環境構築
-----------------------

http://docs.zope.jp/zope2/releases/2.12/INSTALL.html に書かれている方法でも良いんですが、その方法ではZope2のソースコードが環境に残ってしまうので、もうすこしクリーンな感じにするためにbuildout.cfgを書いてみました。

::

  $ mkdir zope-env
  $ cd zope-env
  $ wget "http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py"
  $ python-2.6 bootstrap.py init

生成された buildout.cfg に以下を記載

buildout.cfg::

  [buildout]
  parts = zope2 zopepy
  
  extends = http://download.zope.org/Zope2/index/2.12.2/versions.cfg
  versions = versions
  eggs = Zope2 
  
  [zope2]
  recipe = zc.recipe.egg
  eggs = ${buildout:eggs}
  
  [zopepy]
  recipe = zc.recipe.egg
  eggs = ${zope2:eggs}
  interpreter = zopepy
  scripts = zopepy

そして環境をビルドします::

  $ bin/buildout

最後にZopeのインスタンスを作成します::

  $ bin/mkzopeinstance -d inst2 -u admin:admin

あとは実行するだけです::

  $ cd inst2
  $ cd bin/runzope


.. :extend type: text/x-rst
.. :extend:

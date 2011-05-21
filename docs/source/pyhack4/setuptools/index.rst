setuptools
===========


setuptoolsの目的
-----------------

setuptoolsはPython 標準の distutils を拡張しています。
この拡張によってeggを作ったり使ったりできるようになります。
一番有名な利用方法は、easy_installコマンドでしょう。

easy_install を使うために ez_setup.py を実行したことがある人も多いはず。
ez_setup.py を行うと、Pythonのsite-packagesに setuptools がインストール
されます。

easy_install コマンドは ``easy_install aodag.util`` 等と書くと、
PyPI(Python Package Index)から自動的に aodag.util パッケージを探してきて
site-packages にインストールしてくれます。


distribute
-----------
setuptoolsはほとんどメンテナンスされていないため、Distributeという互換
パッケージが開発されています。基本的にsetuptoolsとdistributeどちらを使っても
かまいませんが、distributeの方が安定しています。
安定というのは、最新のPythonで動作する、環境依存が少ない、エラーが分かりやすい、などです。


setuptoolsをインストール
------------------------

virtualenvを使っていれば既にインストールされているはずです。
Python本体にインストールするには以下の方法で行います。

1. http://peak.telecommunity.com/dist/ez_setup.py をダウンロード
2. ez_setup.pyをどこか(仮に/tmpとする)に置いておく。
3. インストールする

::

   $ python /tmp/ez_setup.py


distributeをインストール
-------------------------

virtualenv で --distribute オプションを付けるとdistributeが使われます。
後からdistributeに変えたくなったり、Python本体にインストルするには以下
を行います。


1. http://python-distribute.org/distribute_setup.py をダウンロード
2. distribute_setup.pyをどこか(仮に/tmpとする)に置いておく。
3. インストールする

::

   $ python /tmp/distribute_setup.py


これで既存にsetuptoolsがあればそれが使われないように調整してくれます。
使うときはsetuptoolsというライブラリ名で使うことになるので、これ以降は
setuptoolsだと思って使って下さい。


.. toctree::

   quickstart
   setuptools-plugin1
   setuptools-plugin2


Virtualenv
===========


Virtualenvの目的
-----------------

VirtualEnv_ はPythonの仮想環境を作ります。それだけですが、非常に便利です。
virtualenvwrapper も合わせて使うと便利らしいです。 workingenv や
virtual-python の後継という位置づけのようです。

今回はPython環境を一切変更せずに導入する方法で進めます。


virtualenvをゲット
-------------------

1. http://pypi.python.org/pypi/virtualenv から virtualenv-1.4.9.tar.gz を取得
2. 中身から virtualenv.py をゲット, どこか(仮に/tmpとする)に置いておく。


virtualenv環境を作成
---------------------

``python /tmp/virtualenv.py env1`` のようにして環境を作ります。
複数のPythonがインストールされている人は今回使いたいPythonを使ってください。
以降、そのPythonのバージョンに環境が固定されます。

::

   $ python /tmp/virtualenv.py --no-site-package env1
   $ cd env1
   $ source bin/activate
   (env1)$

これで専用環境ができました。

.. note::
   Windowsの人は source bin/activate の代わりに Scripts/activate.bat です。

.. _mac-virtualenv:

.. warning::
   Macでvirtualenvがうまくいかない場合があります。問題になるのはMac標準の
   Pythonを使用している(MacPortsのPythonを使用していない)場合や、Macで複数
   のPythonをsymlinkで切り替えている場合です。

   こういった環境の場合、virtualenv環境下でeasy_installを行うと、Mac標準の
   Python環境下のsite-packagesにインストールされてしまう問題が発生します。

   これに該当する場合、virtualenvの環境作成時に
   ``virtualenv -p [python-interpreter] env1`` のように-pオプションで実際に
   使用するPythonインタプリタを指定するとうまくいく場合があるようです。

   これでもうまくいかない場合は内部で利用するモジュールをeasy_installでは
   なくdistributeを使うように ``virtualenv --distribute env1`` のように
   オプション指定すると解消される場合があるようです。

   参考: `virtualenv not working with default Python on Mac OS 10.6 <https://bitbucket.org/ianb/virtualenv/issue/17/virtualenv-not-working-with-default-python-on-mac-os>`_


easy_installしてみる
---------------------
virtualenvで環境を作ると、easy_installコマンドが自動的に使えるようになります。
試しに本体のPythonにインストールしていない何かをeasy_installしてみてください。
例えば ``aodag.util`` とか::

   (env1)$ easy_install aodag.util
   (env1)$ mkpkg foo.bar

インストールされたmkpkgはこのenv1環境でしか使えません。
また、 --no-site-package オプションを付けたので、Python本体にeasy_install
などでインストールしているものがあっても使うことは出来ません。


まとめ
-------
VirtualenvはPython環境から独立して好きなようにeasy_installできる環境です。
要らなくなったらディレクトリごと削除してしまえます。
その代わりに、Virtualenv環境毎にインストールパッケージが独立してしまうので
あまり作りすぎるとDISKを圧迫します。インストールのたびにダウンロードするし。


おまけ
-------
* `--distribute` オプションを付けるとsetuptoolsの代わりにdistributeを使います。
* pipも自動的に入っています
* virtualenv.py のコード内に上記がこっそり同梱されています



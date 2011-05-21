================================
The BuildBot setup for CentOS-5
================================

.. contents::
    :depth: 2

開発環境のCentOSセットアップ
==============================


OSのインストール
------------------
インストールしてください。


yumの設定更新
--------------

OSインストール後にyumのリポジトリ設定を行います。これはgitやmercurialをインストールするために必要な設定です。
``/etc/yum.repos.d/CentOS-Base.repo`` の末尾に以下の内容を追記してください::

    [dag]
    name=Dag RPM Repository for Redhat EL5
    baseurl=http://apt.sw.be/redhat/el$releasever/en/$basearch/dag
    gpgcheck=1
    enabled=1
    gpgkey=http://dag.wieers.com/packages/RPM-GPG-KEY.dag.txt


ツールとライブラリのインストール
---------------------------------
yumコマンドを用いて以下のツール・ライブラリをインストールしてください::

    gcc               x86_64     4.1.2-48.el5
    zlib-devel        x86_64     1.2.3-3
    openssl-devel     x86_64     0.9.8e-12.el5_5.7
    sqlite-devel      x86_64     3.3.6-5
    libxml2-devel     x86_64     2.6.26-2.1.2.8.el5_5.1
    libxslt-devel     x86_64     1.1.17-2.el5_2.2
    python-devel      x86_64     2.4.3-27.el5_5.3
    libjpeg-devel     x86_64     6b-37
    freetype-devel    x86_64     2.2.1-28.el5_5.1
    python-imaging    x86_64     1.1.5-7.el5
    fonts-japanese    noarch     0.20061016-4.el5


補助ツールのインストール
-------------------------
yumコマンドを用いて以下のライブラリをインストールしてください::

    screen           x86_64     4.0.3-1.el5_4.1
    readline-devel   x86_64     5.1-3.el5


開発ツールのインストール
-------------------------
yumコマンドを用いて以下のライブラリをインストールしてください::

    git              x86_64     1.7.3-1.el5.rf
    mercurial        x86_64     1.7.2-1.el5.rf


BuildBot Master のインストール
-------------------------------

インストール手順
~~~~~~~~~~~~~~~~~~
環境設定

.. code-block:: bash

    $ mkdir /tmp/master
    $ cd /tmp/master
    $ wget http://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/bootstrap.py
    $ python bootstrap.py -d init
    $ vi buildout.cfg

buildout.cfg:

.. code-block:: ini

    [buildout]
    parts = master

    [master]
    recipe = zc.recipe.egg
    eggs = buildbot
    interpreter = python
    entry-points = buildbot=buildbot.scripts.runner:run

buildout実行

.. code-block:: bash

    $ bin/buildoiut
    $ ls bin
    buildbot  buildout  python

非常に紛らわしいですが、buildbotコマンドが作成されました。

buildbot設定作成
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ bin/buildbot create-master var
    updating existing installation
    chdir /tmp/master
    creating master.cfg.sample
    populating public_html/
    creating Makefile.sample
    creating database
    buildmaster configured in /tmp/master/buildbot_master

    $ ls var
    buildbot.tac  Makefile.sample  master.cfg.sample  public_html  state.sqlite


.. todo:: めんどくさくなってきた


BuildBot Slave のインストール
-------------------------------

インストール手順
~~~~~~~~~~~~~~~~~~
環境設定(BuildBot Masterとディレクトリ以外同じ)

.. code-block:: bash

    $ mkdir /tmp/master
    $ cd /tmp/master
    $ wget http://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/bootstrap.py
    $ python bootstrap.py -d init
    $ vi buildout.cfg

buildout.cfg (細かく異なる):

.. code-block:: ini

    [buildout]
    parts = slave

    [slave]
    recipe = zc.recipe.egg
    eggs = buildbot_slave
    interpreter = python
    entry-points = buildslave=buildslave.scripts.runner:run

buildout実行

.. code-block:: bash

    $ bin/buildoiut
    $ ls bin
    buildout  buildslave  python

buildslaveコマンドが作成されました。




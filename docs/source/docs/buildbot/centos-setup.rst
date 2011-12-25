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
    python-setuptools noarch     0.6c5-2.el5


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
    subversion       i386       1.6.11-7.el5_6.3


setuptoolsの更新
-----------------
yumコマンドを用いてインストールしたsetuptoolsは古いため、以下のコマンドで
新しいバージョンに更新します。

.. code-block:: bash

    $ sudo easy_install distribute


その他のPythonパッケージのインストール
---------------------------------------

.. code-block:: bash

    $ sudo easy_install pip
    $ sudo pip install virtualenv


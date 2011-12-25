=================
zc.buildout メモ
=================

buildoutの目的
-----------------
`buildout` はPythonベースのビルドシステムです。パーツという単位で
アプリケーションを作成、組み立て、配置などを行い、非Pythonベースのものも
構築可能です。

virtualenvはPython本体とは別の箱庭を作りますが、箱庭に何をどう置くかは
virtualenv環境毎に人間の手で行う必要があります。例えばSphinxをeasy_install
すれば関連パッケージ類(Pygmentsやdocutils)は自動的にインストールされますが、
Sphinx拡張パッケージなどは別途easy_installする必要があります。

buildoutはそういった任意のパッケージインストールや、recipeを使って
様々な環境を作る事が出来ます。

このページの目的
-----------------

buildoutのサンプルをいくつか用意しました。


コンテンツ
----------

.. toctree::
    :maxdepth: 2

    sphinx
    gae
    paste-wsgi



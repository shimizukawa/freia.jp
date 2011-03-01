Sphinxの実行環境をつくる
=========================

シンプルに環境を作る
---------------------

buildout.cfg:

.. literalinclude:: code/sphinx/buildout_step1.cfg
    :language: ini

実行すると以下のようになります:

.. code-block:: bash

    $ python bootstrap.py -d init
    $ bin/buildout

    $ ls bin
    bin/buildout          bin/sphinx-build
    bin/seqdiag           bin/sphinx-py
    bin/sphinx-autogen    bin/sphinx-quickstart

    $ bin/sphinx-quickstart
    Welcome to the Sphinx 1.0.7 quickstart utility.

バージョンが勝手に上がらないように制御する
-------------------------------------------

buildoutで使用するeggのバージョンを指定する方法として、 `version=`
オプションがあります。 `[buildout]` セクションに ``versions=セクション名``
という風に、セクション名を指定して、そのセクションに
eggパッケージ名とバージョンを列挙します。たとえば以下のように書きます:

buildout.cfg:

.. code-block:: ini

    [buildout]
    parts = ....
    versions = versions

    [versions]
    spam = 1.0
    ham = 0.9

しかし多くの依存パッケージがある場合にこれを手動で書いていくのは大変なので、
buildout拡張 ``buildout.dumppickedversions`` を使用します。buildout拡張は
`extensions=` オプションを使って以下のように書きます:


.. code-block:: ini

    [buildout]
    parts = app docutils
    versions = versions

    extensions = buildout.dumppickedversions
    dump-picked-versions-file = versions.cfg

    extends = versions.cfg

これは、extensions=でdumppickedversionsを使うことを指定し、さらに
dumppickedversionsが参照するオプション `dump-picked-versions-file=`
にファイル名を指定しています。これでbuiltoutを実行したときにversions.cfg
に各eggのバージョンを書き出してくれるようになります。

書き出されたversions.cfgを `extends=` に指定することで、内容を読み込んで
利用しているので、これ以降はbuildout実行時に勝手に利用パッケージのバージョンが
更新されることは無くなります。

最終的にbuildout.cfgは以下のようになります。

buildout.cfg:

.. literalinclude:: code/sphinx/buildout_step2.cfg
    :language: ini

実行すると以下のようになります:

.. code-block:: bash

    $ touch version.cfg
    $ bin/buildout
    Updating app.
    Updating docutils.
    *********************************************
    Overwriting versions.cfg
    *********************************************

    $ cat versions.cfg
    [versions]
    jinja2 = 2.5.5
    pil = 1.1.7
    pygments = 1.4
    sphinx = 1.0.7


Sphinxのtrunk版を利用する
--------------------------

buildout.cfg:

.. literalinclude:: code/sphinx/buildout_step3.cfg
    :language: ini

trunk.cfg

.. literalinclude:: code/sphinx/buildout_step3_trunk.cfg
    :language: ini

実行すると以下のようになります:

.. code-block:: bash

    $ bin/buildout -c trunk.cfg
    $ bin/sphinx-quickstart
    Welcome to the Sphinx 1.1pre/ce4bb37a1409 quickstart utility.


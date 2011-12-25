Google App Engine (GAE/py) の開発環境をつくる
==============================================

appfy.recipe.gae のサンプル
----------------------------

buildout.cfg:

.. literalinclude:: code/gae/buildout_step0.cfg
    :language: ini

実行すると以下のようになります:

.. code-block:: bash

    $ python bootstrap.py -d init
    $ bin/buildout

    $ ls bin
    bin/appcfg           bin/bulkloader       bin/remote_api_shell
    bin/buildout         bin/dev_appserver
    bin/bulkload_client  bin/python


アプリのスケルトンを自動生成する設定を追加
-------------------------------------------

buildout.cfg:

.. literalinclude:: code/gae/buildout_step1.cfg
    :language: ini

実行すると以下のようになります:

.. code-block:: bash

    $ bin/buildout

    $ ls bin
    bin/appcfg           bin/bulkloader       bin/remote_api_shell
    bin/buildout         bin/dev_appserver
    bin/bulkload_client  bin/python

    $ ls app
    app.yml     distlib/    distlib.zip main.py

    $ bin/dev_appserver app


アプリ名などを設定出来るようにする
-----------------------------------

buildout.cfg:

.. literalinclude:: code/gae/buildout_step2.cfg
    :language: ini


デバッグ用の対話コンソール用スクリプトを追加する
-------------------------------------------------

buildout.cfg:

.. literalinclude:: code/gae/buildout_step3.cfg
    :language: ini


NoseとNoseGAEを使って自動テストの設定を追加する
------------------------------------------------


buildout.cfg:

.. literalinclude:: code/gae/buildout_step4.cfg
    :language: ini

実行すると以下のようになります:

.. code-block:: bash

    $ bin/buildout

    $ ls bin
    bin/appcfg           bin/ipcontroller     bin/pycolor
    bin/buildout         bin/ipengine         bin/python
    bin/bulkload_client  bin/iptest           bin/remote_api_shell
    bin/bulkloader       bin/ipython          bin/test
    bin/dev_appserver    bin/ipythonx         bin/twitter
    bin/ipcluster        bin/py               bin/twitterbot

    $ bin/test
    ----------------------------------------------------------------------
    Ran 0 tests in 0.005s


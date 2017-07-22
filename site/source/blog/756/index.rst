:date: 2011-05-01 18:20:00
:tags: python
:body type: text/x-rst

======================================================
2011/05/01 Python3でzc.buildout-2.0.0a1 を動かしてみた
======================================================

昨夜、4/30の夜に `zc.buildout-2.0.0a1`_ がリリースされたので早速試してみました。

.. _`zc.buildout-2.0.0a1`: http://pypi.python.org/pypi/zc.buildout/2.0.0a1

.. topic:: bootstrap.py
    :class: dos

    | $ mkdir bo2
    | $ cd bo2
    | $ wget http://svn.zope.org/repos/main/zc.buildout/branches/2/bootstrap/bootstrap.py
    | $ python-3.2 bootstrap.py init

これで動いてくれれば話は早かったんですが、自分の環境ではなぜかzc.buildout-1.5.2がセットアップされてしまい、当然Python3では動きません。そこで、先にbuildout.cfgを作ってversions指定しておきました。

buildout.cfg::

    [buildout]
    parts =
    versions = versions
    
    [versions]
    zc.buildout = 2.0.0a1
    zc.recipe.egg = 2.0.0a1

改めてbootstrapを実行。 Python3では -d オプションはdefaultでonになりました。

.. topic:: bootstrap.py
    :class: dos

    | $ python-3.2 bootstrap.py init
    | ...
    | Generated script '/tmp/bo2/bin/buildout'.

次にbuildout.cfgにPython3アプリを使えるようにappセクションを追加します。

buildout.cfg::

    [buildout]
    parts = app
    versions = versions
    
    [app]
    recipe = zc.recipe.egg
    eggs = bucho
    interpreter = py
    
    [versions]
    zc.buildout = 2.0.0a1
    zc.recipe.egg = 2.0.0a1

.. topic:: bin/buildout
    :class: dos

    | $ bin/buildout
    | ...
    | Generated script '/tmp/bo2/bin/bucho'.
    | Generated interpreter '/tmp/bo2/bin/py'.

セットアップできました！ Python3でも zc.buildout が使えるようになりましたね。

.. topic:: bin/buildout
    :class: dos

    | $ bin/py -c "import sys;print(sys.version)"
    | 3.2 (r32:88445, Feb 20 2011, 21:30:00) [MSC v.1500 64 bit (AMD64)]
    |
    | $ bin/bucho latest_status
    | 雨降ってきまけど、池袋に飲みにいく。

雨の中のみに行くそうです。さすがbuchoですね。


.. :extend type: text/x-rst
.. :extend:


:date: 2010-06-22 23:05:00
:categories: ['python']
:body type: text/x-rst

==================================================
2010/06/22 setuptoolsを使ったpluginサンプル(egg編)
==================================================

*Category: 'python'*

`setuptoolsを使ったpluginサンプル`_ で作ったpluginの仕組みを
ちょっとだけ変更して、plugin用フォルダにファイルを追加したら
pluginとして認識されるようにしてみます。

ここで、pluginファイルの形式としてeggファイルを使うことにします。


前準備
------

Python環境にsetuptoolsをインストールしておきます。
手順は前のエントリ `setuptoolsを使ったpluginサンプル`_ を参照のこと。

次に `plugins_egg.zip`_ を展開します::

  plugins_egg/
     +-- README.txt
     +---p1/
     |   +-- foo_plugin.py
     |   +-- setup.py
     |
     +---p2/
     |   +-- bar_plugin.py
     |   +-- setup.py
     |
     +---server/
         +-- server.py
         +-- plugins/


pluginをegg化して追加
----------------------

p1フォルダでpluginをegg化します。

.. topic:: bdist_egg
  :class: dos

  | $ cd ../p1
  | $ python setup.py bdist_egg
  | running bdist_egg
  | running egg_info
  | ...
  | ...
  | creating dist
  | creating 'dist/foo_plugin-0.0.0-py2.6.egg' ...
  | removing 'build/bdist.xxx/egg' (and everything under it)
  | 
  | $

これでdistフォルダにeggファイルが生成されるので、この
foo_plugin-0.0.0-py2.6.egg をserver/pluginsフォルダに移動します。

.. topic:: install
  :class: dos

  | $ ls dist
  | foo_plugin-0.0.0-py2.6.egg
  | $ mv dist/* ../server/plugins


serverを実行
------------

'server' フォルダに移動して以下のように実行します。

.. topic:: run
  :class: dos

  | $ cd ../server
  | $ python server.py
  | ## call plugin: plugin:plugin_name1
  | Hello SERVER (by foo_plugin)
  | 
  | ## plugins call finished
  |
  | $


pluginの仕組み
---------------

plugin側のコードは前回の `setuptoolsを使ったpluginサンプル`_ で用意したものと
完全に同じで、pluginを使うserver.py側のコードをちょっとだけ変更しました。

server.pyでは以下のコードの例のように、pluginsフォルダの中身を自動的に
sys.pathに追加してからpkg_resourcesを使っています。

.. code-block:: python

  import sys
  from glob import glob

  sys.path[0:0] = glob('plugins/*.egg')

  import pkg_resources
  for plugin in pkg_resources.iter_entry_points('plugin_example'):
      ...

上記は `import pkg_resources` すると内部でsys.pathを走査する作りになっているためにこのような手順になっていますが、あるいは以下のように書くこともできます。

.. code-block:: python

  import sys
  from glob import glob
  import pkg_resources

  for p in glob('plugins/*.egg'):
      pkg_resources.working_set.add_entry(p)

  for plugin in pkg_resources.iter_entry_points('plugin_example'):
      ...


（6/26追記）さらにpkg_resources.pyに書かれているサンプルとして以下のコードもあります。

.. code-block:: python

  import sys
  import pkg_resources

  distributions, errors = pkg_resources.working_set.find_plugins(
      pkg_resources.Environment(['plugins'])
  )
  map(pkg_resources.working_set.add, distributions)

  for plugin in pkg_resources.iter_entry_points('plugin_example'):
      ...


これならsys.pathも汚さないですね。



後始末
-------

今回はpluginをシステムにインストールした訳ではないので、後始末は
特に必要ありません。


まとめ
-------
`setuptoolsを使ったpluginサンプル`_ で説明した方法と比べて、pluginsフォルダ
にeggファイルを置いたりプログラムでpluginsフォルダをsys.pathに追加したりと
手動での管理が増えており、easy_installで自動的にプラグインを追加するなど
の方法は使えなくなってしまいました。しかしこれはこれで使い方によっては
メリットになるかもしれません。

ちなみに、eggファイルは実はzipファイルだとか、pythonはzip圧縮されたパッケージ
をsys.pathに追加しておけばimportできるようになるとか、色々なバックグラウンド
の上でこの仕組みは動作しています。

なお、buildoutを使うことで、buildout.cfgの設定を書き換えるだけでplugin
となるeggを自動的にPyPIから取ってきてシステムに組み込むと言うような
仕組みを作ることも簡単にできるようになります。



参考文献:
 * [Python] setuptools - SumiTomohikoの日記
    * http://d.hatena.ne.jp/SumiTomohiko/20070622
    * http://d.hatena.ne.jp/SumiTomohiko/20070623
    * http://d.hatena.ne.jp/SumiTomohiko/20070624
 * `エキスパートPythonプログラミング`_

.. _`エキスパートPythonプログラミング`: http://astore.amazon.co.jp/freiaweb-22/detail/4048686291

.. _`plugins_egg.zip`: http://www.freia.jp/taka/blog/stuff/plugins_egg.zip/download
.. _`setuptoolsを使ったpluginサンプル`: http://www.freia.jp/taka/blog/721


.. :extend type: text/x-rst
.. :extend:

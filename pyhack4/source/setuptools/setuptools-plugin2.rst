setuptoolsを使ったpluginサンプル egg編
=======================================

`setuptoolsを使ったpluginサンプル <setuptools-plugin1.html>`_
で作ったpluginの仕組みをちょっとだけ変更して、plugin用フォルダにファイル
を追加したらpluginとして認識されるようにしてみます。

ここで、pluginファイルの形式としてeggファイルを使うことにします。


前準備
------

`plugins_egg.zip <../_static/plugins_egg.zip>`_ を展開します::

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

p1フォルダでpluginをegg化します::

   $ cd ../p1
   $ python setup.py bdist_egg
   running bdist_egg
   running egg_info
   ...
   ...
   creating dist
   creating 'dist/foo_plugin-0.0.0-py2.6.egg' ...
   removing 'build/bdist.xxx/egg' (and everything under it)
   
   $

これでdistフォルダにeggファイルが生成されるので、この
foo_plugin-0.0.0-py2.6.egg をserver/pluginsフォルダに移動します。

::

   $ ls dist
   foo_plugin-0.0.0-py2.6.egg
   $ mv dist/* ../server/plugins


serverを実行
------------

'server' フォルダに移動して以下のように実行します::

   $ cd ../server
   $ python server.py
   ## call plugin: plugin:plugin_name1
   Hello SERVER (by foo_plugin)
   
   ## plugins call finished
  
   $


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


さらにpkg_resources.pyに書かれているサンプルとして以下のコードもあります。

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



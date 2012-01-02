:date: 2010-06-22 00:55:00
:categories: ['python']
:body type: text/x-rst

================================
setuptoolsを使ったpluginサンプル
================================

Pythonでplugin的な仕組みを作るとしたら__import__やimpを使う方法が
ありますが、今の流れ的にはsetuptools対応して簡単にパッケージング
や配布、PyPIでの公開、buildoutへの対応など行うことも視野に入れて
いきたいところです。

と言ってもやらないと行けないことは少ないので、__import__の使い方
を調べて試行錯誤するよりも簡単かもしれません。


前準備
------

Python環境にsetuptoolsをインストールしておきます。

.. topic:: wget
  :class: dos

  | $ wget http://peak.telecommunity.com/dist/ez_setup.py
  | $ sodo python ez_setup.py

OSの構成管理ツール(apt,yum,portsなど)でインストールしておいても可。
あるいはvirtualenvを使っても可です。

インストール出来ていれば `easy_install` コマンドが使えるように
なっているはずです。

.. topic:: check
  :class: dos

  | $ easy_install
  | error: No urls, filenames, or requirements specified (see --help)


次に `plugins.zip`_ を展開します::

  plugins/
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


pluginの無い状態での実行
------------------------

'server' フォルダで以下のように実行します。

.. topic:: server
  :class: dos

  | $ cd server
  | $ python server.py
  | ## plugins call finished
  | 
  | $

pluginが無い状態のため、プラグイン呼び出し終了のメッセージのみ表示
されてプログラムが終了します。


pluginを追加
------------

p1というフォルダに入っているpluginを環境に追加します。

.. topic:: develop
  :class: dos

  | $ cd ../p1
  | $ python setup.py develop
  | running develop
  | running egg_info
  | ...
  | ...
  | Installed .../p1
  | Processing dependencies for foo-plugin==0.0.0
  | Finished processing dependencies for foo-plugin==0.0.0
  | 
  | $


今回は実験目的のため `python setup.py develop` でインストールして、あとで
アンインストールしやすいようにしていますが `python setup.py install` としても同じように動作します。


serverを再実行
--------------

'server' フォルダに移動してもう一度以下のように実行します。

.. topic:: server
  :class: dos

  | $ cd ../server
  | $ python server.py
  | ## call plugin: plugin:plugin_name1
  | Hello SERVER (by foo_plugin)
  | 
  | ## plugins call finished
  | 
  | $


pluginをもう一つ追加して再実行
------------------------------

plugin2つめを追加。

.. topic:: p2
  :class: dos

  | $ cd ../p2
  | $ python setup.py develop
  | ...
  | ...
  | Installed .../p2
  | Processing dependencies for bar-plugin==0.0.0
  | Finished processing dependencies for bar-plugin==0.0.0
  | 
  | $

serverを実行。

.. topic:: server
  :class: dos

  | $ cd ../server
  | $ python server.py WORLD
  | ## call plugin: foo_plugin:plugin_name1
  | Hello WORLD (by foo_plugin)
  | 
  | ## call plugin: bar_plugin:plugin_name2
  | Hello WORLD (by bar_plugin)
  | 
  | ## plugins call finished
  | 
  | $


pluginの仕組み
---------------

p1/setup.py のコードはsetuptoolsで拡張されたdistutilsのsetup関数です。

.. code-block:: python

  setup(
      name="foo_plugin",
      py_modules=['foo_plugin'],
      entry_points="""
         [plugin_example]
         plugin_name1 = foo_plugin:func
      """,
  )

ここでentry_pointsに記載している 'plugin_example' というのがポイントで、
このように書いておくと別のプログラムから以下のようにして関数を取り出す
事ができるようになります。

.. code-block:: python

  import pkg_resources
  for plugin in pkg_resources.iter_entry_points('plugin_example'):
      ...


後始末
-------

今回実験用にインストールしたプラグインパッケージをアンインストール
しておきましょう。

.. topic:: cleanup
  :class: dos

  | $ cd ../p1
  | $ python setup.py develop -u
  | running develop
  | Removing ../python26/lib/site-packages/foo-plugin.egg-link (link to .)
  | Removing foo-plugin 0.0.0 from easy-install.pth file
  | 
  | $ cd ../p2
  | $ python setup.py develop -u
  | running develop
  | Removing ../python26/lib/site-packages/bar-plugin.egg-link (link to .)
  | Removing bar-plugin 0.0.0 from easy-install.pth file
  | 
  | $


まとめ
-------
ここで説明した方法ではpluginを使えるようにするためには `python setup.py install`
等する必要があります。これはpluginをどこか(PyPI等)に公開しておけば `easy_install`
コマンド一発でpluginを使えるようになる、ということになります。

しかし、場合によってはpluginフォルダにファイルを置くだけで動作するようにしたい
と考えるかも知れません。その方法は次のエントリで書きたいと思います。


参考文献:
 * [Python] setuptools - SumiTomohikoの日記
    * http://d.hatena.ne.jp/SumiTomohiko/20070622
    * http://d.hatena.ne.jp/SumiTomohiko/20070623
    * http://d.hatena.ne.jp/SumiTomohiko/20070624
 * `エキスパートPythonプログラミング`_

.. _`エキスパートPythonプログラミング`: http://astore.amazon.co.jp/freiaweb-22/detail/4048686291
.. _`plugins.zip`: stuff/plugins.zip/download


.. :extend type: text/x-rst
.. :extend:


.. :comments:
.. :comment id: 2010-06-22.7583323027
.. :title: Re:setuptoolsを使ったpluginサンプル
.. :author: nakagami
.. :date: 2010-06-22 15:22:40
.. :email: 
.. :url: 
.. :body:
.. PyPI への道（続編）も期待します！
.. 
.. :comments:
.. :comment id: 2010-06-22.0619591066
.. :title: Re:setuptoolsを使ったpluginサンプル
.. :author: jhotta
.. :date: 2010-06-22 16:51:02
.. :email: 
.. :url: 
.. :body:
.. 参考に成ります。また教えてください。
.. 

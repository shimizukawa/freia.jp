:date: 2011-04-23 12:45:00
:tags: python

==================================================================================
2011/04/23 Python-3.3 に標準搭載されるpackaging(Python3.3未満ではDistutils2)を試す
==================================================================================

`(第7回)Python mini Hack-a-thon 午前の部`_

.. _`(第7回)Python mini Hack-a-thon 午前の部`: http://atnd.org/events/14178

pysetupきたー

  "distutils2 には pipやeasy_installと同じような "pysetup" コマンドが搭載され、インストール時の依存関係を解決してくれます。"

  "distutils2 will come with a "pysetup" command similar to pip/easy_install that will handle dependencies." 

`Distutils ML`_ で上記のようなメールを見かけて、Python標準で ``pysetup`` コマンドが搭載されるんだなーと言うことを知ったのでさっそくインストールしてみた。

https://bitbucket.org/tarek/distutils2/wiki/Home を見ると、以下のように書かれている。

* distutils2 はPython 2.4-3.2 では "Distutils2" というサードパーティーパッケージとして配布されます
* distutils2 はPython 3.3に "packaging" という名前で統合されます

なるほど。

最新はまだpypiに上がってないので、リポジトリから取ってきて実験。

.. topic:: Installing distutils2
  :class: dos

  | $ virtualenv du2
  | $ cd du2
  | $ source bin/activate
  | $ hg clone https://bitbucket.org/tarek/distutils2
  | $ python-2.7 setup.py install
  | $ bin/pysetup
  | Usage: pysetup [options] action [action_options]
  | 
  | Actions:
  |     run: Run one or several commands
  |     metadata: Display the metadata of a project
  |     install: Install a project
  |     remove: Remove a project
  |     search: Search for a project
  |     graph: Display a graph
  |     create: Create a Project
  | 
  | To get more help on an action, use:
  | 
  |     pysetup action --help
  | 
  | Global options:
  |   --verbose (-v)  run verbosely (default)
  |   --quiet (-q)    run quietly (turns verbosity off)
  |   --dry-run (-n)  don't actually do anything
  |   --help (-h)     show detailed help message
  |   --no-user-cfg   ignore pydistutils.cfg in your home directory
  |   --version       Display the version
  |
  | $

ふむふむ、動いた動いた。さっそく bucho をインストールしてみるか

.. topic:: pysetup commands
  :class: dos

  | $ bin/pysetup install bucho
  |
  | $

残念、ダメだった。何も起こらない。深くは追ってないけど。

runのサブコマンドはどんなのがあるのかな？

.. topic:: pysetup commands
  :class: dos

  | $ bin/pysetup run --list-commands
  | List of available commands:
  |   bdist: create a built (binary) distribution
  |   bdist_dumb: create a "dumb" built distribution
  |   bdist_wininst: create an executable installer for MS Windows
  |   build: build everything needed to install
  |   build_clib: build C/C++ libraries used by Python extensions
  |   build_ext: build C/C++ extensions (compile/link to build directory)
  |   build_py: "build" pure Python modules (copy to build directory)
  |   build_scripts: "build" scripts (copy and fixup #! line)
  |   check: perform some checks on the package
  |   clean: clean up temporary files from 'build' command
  |   install_data: install data files
  |   install_dist: install everything from build directory
  |   install_distinfo: create a .dist-info directory for the distribution
  |   install_headers: install C/C++ header files
  |   install_lib: install all Python modules (extensions and pure Python)
  |   install_scripts: install scripts (Python or otherwise)
  |   register: register the distribution with the Python package index
  |   sdist: create a source distribution (tarball, zip file, etc.)
  |   test: run the distribution's test suite
  |   upload: upload distribution to PyPI
  |   upload_docs: (no description available)

runはsetup.py相当のコマンドっぽい。なるほど。

.. _`Distutils ML`: http://mail.python.org/pipermail/distutils-sig/2011-April/017735.html


.. :extend type: text/x-rst
.. :extend:


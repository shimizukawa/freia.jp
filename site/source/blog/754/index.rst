:date: 2011-04-23 18:10:00
:categories: ['python']
:body type: text/x-rst

======================================================
2011/04/23 packaging (aka Distutils2) のcreateコマンド
======================================================

*Category: 'python'*

`(第7回)Python mini Hack-a-thon`_ 夕方の部

.. _`(第7回)Python mini Hack-a-thon`: http://atnd.org/events/14178

`Python-3.3 に標準搭載されるpackaging(Python3.3未満ではDistutils2)を試す`_ で `pysetup` を使えるようになったので、コマンドを少しずつ見ていきます。

.. _`Python-3.3 に標準搭載されるpackaging(Python3.3未満ではDistutils2)を試す`: http://www.freia.jp/taka/blog/752 

.. topic:: pysetup commands
  :class: dos

  | $ python bin/pysetup
  | Usage: pysetup [options] action [action_options]
  | 
  | Actions:
  | .   run: Run one or several commands
  | .   metadata: Display the metadata of a project
  | .   install: Install a project
  | .   remove: Remove a project
  | .   search: Search for a project
  | .   graph: Display a graph
  | .   create: Create a Project

* run: 1つまたは複数のコマンドを実行
* metadata: プロジェクトのメタデータを表示
* install: プロジェクトをインストール
* remove: プロジェクトを削除
* search: プロジェクトを検索
* graph: グラフを表示
* create: プロジェクトを作成


まずはプロジェクト作成のための ``create`` コマンドをたたいてみます。

.. topic:: pysetup create
  :class: dos

  | $ python bin/pysetup create
  | Project name [du2]: spam
  | Current version number: 0.5
  | Package summary:
  |    > ham ham ham
  | Author name: shimizukawa
  | Author e-mail address: shimizukawa
  | Project Home Page: none
  | Do you want me to automatically build the file list with everything I can find
  | in the current directory ? If you say no, you will have to define them manually
  | . (y/n): y
  | Do you want to set Trove classifiers? (y/n): y
  | Please select the project status:
  | 
  | 1 - Planning
  | 2 - Pre-Alpha
  | 3 - Alpha
  | 4 - Beta
  | 5 - Production/Stable
  | 6 - Mature
  | 7 - Inactive
  | 
  | Status: 4
  | What license do you use: BSD
  | Matching licenses:
  | 
  |    1) License :: OSI Approved :: BSD License
  | 
  | Type the number of the license you wish to use or ? to try again:: 1
  | Do you want to set other trove identifiers (y/n) [n]: n
  | Wrote "setup.cfg".
  | 
  | $ ls
  | bin  lib  setup.cfg

上記のように、対話型で実行され、最終的には ``setup.cfg`` が生成されました。
setup.cfgの中身はこんな感じ::

    [metadata]
    name = spam
    version = 0.5
    summary = ham ham ham
    download_url = UNKNOWN
    home_page = none
    author = shimizukawa
    author_email = shimizukawa
    classifier = License :: OSI Approved :: BSD License
        Development Status :: 4 - Beta

    [files]
    packages =
    modules =
    resources =

なるほど、でもsetup.pyは作ってくれないんですね.. その辺りの仕組みも違うのかな？

ちなみに、既存のプロジェクトディレクトリで ``pysetup create`` を実行すると、以下のように setup.py から自動変換してくれるようです。便利ですね。

.. topic:: pysetup create
  :class: dos

  | $ pysetup create
  | A legacy setup.py has been found.
  | Would you like to convert it to a setup.cfg ? (y/n)



.. :extend type: text/x-rst
.. :extend:

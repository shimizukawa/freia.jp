zc.buildout
===========


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
様々な環境を作る事が出来ます。例えばTracやBuildBot環境も作成出来ます。


ただし、buildoutでは Python 本体の site-packages を切り離せないので
(1.5.0正式版で対応される予定)、その必要がある場合は virtualenv 環境下
buildoutを使うという組み合わせも必要になります。
その必要が無い場合はvirtualenv無しでOKです。


buildout環境を作成
-------------------

1. http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py を取得
2. bootstrap.py をどこか(仮に/tmpとする)に置いておく。
3. 任意の環境名でフォルダを作成して(例:testdir), python /tmp/bootstrap.py init を実行

このとき使用したpythonがこれ以降使用されるpythonのインタプリタになります。このあたりの仕組みはvirtualenvとそっくりですね::

  $ cd /tmp
  $ wget "http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py"
  $ mkdir testdir
  $ cd testdir
  $ python-2.6 /tmp/bootstrap.py init

この時点でディレクトリ構成が以下のようになります::

  /tmp
   +-- testdir
       +-- buildout.cfg
       +-- bin/
       +-- develop-eggs/
       +-- eggs/
       +-- parts/


buildout環境を使ってみる
-------------------------

testdir作成された buildout.cfg ファイルが出来ているので以下の内容で更新します::

  [buildout]
  parts = env
  
  [env]
  recipe = zc.recipe.egg
  eggs =
      sphinx
      PIL
      aodag.util
  interpreter = py

最後に環境をビルドします::

  $ bin/buildout

この時点でディレクトリ構成が以下のようになりました::

  r:/
   +-- testdir
       +-- .installed.cfg
       +-- buildout.cfg
       +-- bin
       |   +-- buildout
       |   +-- mkpkg
       |   +-- py
       |   +-- sphinx-autogen
       |   +-- sphinx-build
       |   +-- sphinx-quickstart
       +-- develop-eggs/
       +-- eggs/
       |   +-- aodag.util-0.0-py2.6.egg/
       |   +-- docutils-0.6-py2.6.egg/
       |   +-- jinja2-2.2.1-py2.6.egg/
       |   +-- pil-1.1.7b1-py2.6-win32.egg/
       |   +-- Pygments-1.1.1-py2.6.egg/
       |   +-- Sphinx-0.6.3-py2.6.egg/
       |   +-- zc.buildout-1.4.1-py2.6.egg/
       |   +-- zc.recipe.egg-1.2.2-py2.6.egg/
       |   +-- setuptools-0.6c11-py2.6.egg
       +-- parts/

これでsphinx,PIL,aodag.utilがインストールされたPyhton環境が出来ました。 ``bin/py`` を使えば、sphinx,PIL,aodag.utilその他これらが依存しているパッケージをimportできる環境でインタプリタが起動します。

ということで、 ``bin/py`` でインタプリタを起動すると以下のようになります::

  $ bin/python.exe
  
  >>> import sys
  >>> from pprint import pprint
  >>> pprint(sys.path)
  ['r:\\testdir\\eggs\\aodag.util-0.0-py2.6.egg',
   'r:\\testdir\\eggs\\docutils-0.6-py2.6.egg',
   'r:\\testdir\\eggs\\sphinx-0.6.3-py2.6.egg',
   'r:\\testdir\\eggs\\pil-1.1.7b1-py2.6-win32.egg',
   'r:\\testdir\\eggs\\jinja2-2.2.1-py2.6.egg',
   'r:\\testdir\\eggs\\pygments-1.1.1-py2.6.egg',
   'c:\\Develop\\Python26\\lib\\site-packages\\virtualenv-1.3.3-py2.6.egg',
   'c:\\Develop\\Python26\\lib\\site-packages\\setuptools-0.6c9-py2.6.egg',
   ...
   ...
   ...
  >>>

ここではvirtualenvを使っていなかったため、Python本体のsite-packagesもsys.pathに含まれています。


VirtualEnvとの比較
-------------------

VirtualEnvは基本環境の複製を作って、そこにpythonインタプリタやsite-packageなどを複製します。VirtualEnvで環境を作る時に、元のsite-packagesを含めないように出来ます。buildoutでは元の環境を含めない仮想環境を作ることは今のところ出来ません。あくまで基本環境への追加という形式になります。

以下のように言い表せます.

  buildout = VirtualEnv + easy_install + その他手作業 - 仮想環境化

自分は構築手順を覚えておくのが苦手だし、手順に従って１ステップずつ環境を作るのも面倒なタチなのでbuildoutは非常に便利だと思っています。

しかし、VirtualEnvのactivate等で環境を切り替える概念はbuildoutには無いので、その機能が欲しい場合にはVirtualEnv環境上でbuildoutを使えば良いと思います。


その他
------

buildoutは内部的にeasy_installを使用しますが、代わりに `pip` や `distribute` を使うことも出来ます。また、簡単なrecipeを作ればその他のパッケージングシステムを使うことも出来ると思います。


.. toctree::

   plugin3
   recipe
   gae


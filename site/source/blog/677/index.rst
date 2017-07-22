:date: 2009-10-24 14:06:37
:tags: python
:body type: text/x-rst

====================================================
2009/10/24 buildoutで開発0: zc.buildout で環境を作る
====================================================

.. highlights::

  buildout_ はPythonベースのビルドシステムです。パーツという単位でアプリケーションを
  作成、組み立て、配置などを行い、非Pythonベースのものも構築は可能です。

  -- http://www.buildout.org/

ということで、これまでbuildoutに関するいくつかのエントリを書いて来ましたが、そもそもbuildoutって何？ということについて書きます。

仮想環境、またはサンドボックス(SandBox)としては VirtualEnv_ が有名ですが、 buildout (正式には zc.buildout)は冒頭に書いたように、ビルドシステムと言う方が適切です。buildoutはVirtualEnvと組み合わせて使うことも出来ますが、buildout単体で使用しても、既存のPython環境を汚さずにegg類をインストールして使うことが出来ます。

はじめよう
----------

まずは仮想環境的に使う例です。bootstrap.pyというのを取ってきて、init引数を付けて実行しています。このとき使用したpythonがこれ以降使用されるpythonのインタプリタになります::

  $ mkdir testdir
  $ cd testdir
  $ wget "http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py"
  $ python-2.6 bootstrap.py init

この時点でディレクトリ構成が以下のようになります::

  /tmp
   +-- testdir
       +-- bootstrap.py
       +-- buildout.cfg
       +-- bin/
       +-- develop-eggs/
       +-- eggs/
       +-- parts/


同じディレクトリに buildout.cfg ファイルが出来ているので以下の内容で更新します::

  [buildout]
  parts = env
  
  [env]
  recipe = zc.recipe.egg
  eggs =
      docutils  
      sphinx
      PIL
  interpreter = python

最後に環境をビルドします::

  $ bin/buildout

この時点でディレクトリ構成が以下のようになりました::

  r:/
   +-- testdir
       +-- .installed.cfg
       +-- bootstrap.py
       +-- buildout.cfg
       +-- bin
       |   +-- buildout
       |   +-- python
       |   +-- sphinx-autogen
       |   +-- sphinx-build
       |   +-- sphinx-quickstart
       +-- develop-eggs/
       +-- eggs/
       |   +-- docutils-0.6-py2.6.egg/
       |   +-- jinja2-2.2.1-py2.6.egg/
       |   +-- pil-1.1.7b1-py2.6-win32.egg/
       |   +-- Pygments-1.1.1-py2.6.egg/
       |   +-- Sphinx-0.6.3-py2.6.egg/
       |   +-- zc.buildout-1.4.1-py2.6.egg/
       |   +-- zc.recipe.egg-1.2.2-py2.6.egg/
       |   +-- setuptools-0.6c11-py2.6.egg
       +-- parts/

これでdocutils,sphinx,PILがインストールされたPyhton環境が出来ました。 ``bin/python`` を使えば、docutils,sphinx,PIL,その他これらが依存しているパッケージが使用できる環境で起動します。

ということで、 ``bin/python`` でインタプリタを起動すると以下のようになります::

  $ bin/python.exe
  
  >>> import sys
  >>> from pprint import pprint
  >>> pprint(sys.path)
  ['r:\\testdir\\eggs\\docutils-0.6-py2.6.egg',
   'r:\\testdir\\eggs\\sphinx-0.6.3-py2.6.egg',
   'r:\\testdir\\eggs\\pil-1.1.7b1-py2.6-win32.egg',
   'r:\\testdir\\eggs\\jinja2-2.2.1-py2.6.egg',
   'r:\\testdir\\eggs\\pygments-1.1.1-py2.6.egg',
   'R:\\testdir\\bin',
   'c:\\Develop\\Python26\\lib\\site-packages\\virtualenv-1.3.3-py2.6.egg',
   'c:\\Develop\\Python26\\lib\\site-packages\\setuptools-0.6c9-py2.6.egg',
   'c:\\Develop\\Python26\\lib\\site-packages\\ipython-0.10-py2.6.egg',
   'c:\\Develop\\Python26\\python26.zip',
   'c:\\Develop\\Python26\\DLLs',
   'c:\\Develop\\Python26\\lib',
   'c:\\Develop\\Python26\\lib\\plat-win',
   'c:\\Develop\\Python26\\lib\\lib-tk',
   'c:\\Develop\\Python26',
   'c:\\Develop\\Python26\\lib\\site-packages',
   'c:\\Develop\\Python26\\lib\\site-packages\\win32',
   'c:\\Develop\\Python26\\lib\\site-packages\\win32\\lib',
   'c:\\Develop\\Python26\\lib\\site-packages\\Pythonwin']
  >>>


VirtualEnvとの比較
-------------------

VirtualEnvは基本環境の複製を作って、そこにpythonインタプリタやsite-packageなどを複製します。VirtualEnvで環境を作る時に、元のsite-packagesを含めないように出来ます。buildoutでは元の環境を含めない仮想環境を作ることは(多分)出来ません。あくまで基本環境への追加という形式になります(多分)。

以下のように言いたいところですが言い過ぎ？

  buildout = VirtualEnv + easy_install + その他手作業 - 仮想環境化

自分は構築手順を覚えておくのが苦手だし、手順に従って１ステップずつ環境を作るのも面倒なタチなのでbuildoutは非常に便利だと思っています。

しかし、VirtualEnvのactivate等で環境を切り替える概念はbuildoutには無いので、その機能が欲しい場合にはVirtualEnv環境上でbuildoutを使えば良いと思います。


その他
------

buildoutは内部的にeasy_installを使用しますが、代わりに `pip` や `distribute` を使うことも出来ます。また、簡単なrecipeを作ればその他のパッケージングシステムを使うことも出来ると思います。


.. _buildout: http://www.buildout.org/
.. _VirtualEnv: http://pypi.python.org/pypi/virtualenv


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2009-10-25.3955164934
.. :title: Re:buildoutで開発0: zc.buildout で環境を作る
.. :author: okuji
.. :date: 2009-10-25 11:23:20
.. :email: 
.. :url: 
.. :body:
.. python -Sすれば含めないように作ることはできます。
.. 但し、-Sは生成されるスクリプトには引き継がれないので、毎回指定しないといけなくなり、実用上とっても不便です。
.. ですから、virtualenvは必須だと考えておいた方が楽です。
.. buildoutはパッケージの追加のために別環境を作る程度には分離できるので、複数のbuildoutで同じvirtualenv環境を使い回すのは構わないです。
.. 
.. :comments:
.. :comment id: 2009-10-25.8352983829
.. :title: Re:buildoutで開発0: zc.buildout で環境を作る
.. :author: しみずかわ
.. :date: 2009-10-25 11:30:38
.. :email: 
.. :url: 
.. :body:
.. おお、補足ありがとうございます。-S なんてあったんですね。
.. 結果的には、VirtualEnv使っとけ、と。VirtualEnvは色々考えなくて良くなるので楽ですよね。
.. 

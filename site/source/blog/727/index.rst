:date: 2010-07-19 21:12:22
:tags: python
:body type: text/x-rst

===========================================================================
2010/07/19 Pythonで入れ子Zip内のファイルを透過的に開く方法 - zip_openを使う
===========================================================================

Pythonは標準で、パッケージをzip圧縮しておいてこの中身を直接importすることができます。
例えば::

 packages.zip
  + foo.py
  + bar.py

このようなzipファイルを /path/to/packages.zip に置いて、Pythonインタプリタで以下のように実行することが出来ます。

.. code-block:: python

  import sys
  sys.path.insert(0,'/path/to/packages.zip')

  import foo, bar
  foo.func()

この方法を使えば、 Google App Engine のような配置出来るファイル数に上限のある環境や、たくさんのファイルをベタに展開したくない状況（Pythonで作ったアプリを人にあげるとき）などに単純にファイル数を減らすことが出来ます。

このようなzip圧縮して配布する方法は、py2exe(-bオプション)やsetuptools(zip_safeオプション)などでも使われています。

しかし、対象パッケージが静的ファイル(htmlテンプレートやiniファイルなど)が含まれている場合にzip圧縮パッケージは問題になります。例えばpackages.zipが以下のようになっているとします::

 /path/to/packages.zip
  + foo.py
  + bar.py
  + setting.ini


そして、前述のfoo.pyのプログラム中で ``open(os.path.join(os.path.dirname(__file__)),'setting.ini'))`` などと書いていてると、ここでopenしようとするファイルは '/path/to/packages.zip/setting.ini' になります。このようなpathはopenで開くことが出来ないのでエラーになります。

このような理由でzip_safeでないeggファイルはかなりたくさんあり、これを解決するopen関数があれば割と嬉しい人がいるんじゃないかと思うわけです。Python標準のzipimport.zipimporterを使えば似たようなことは出来ますが、このモジュールでは入れ子のZipファイルを扱うことが出来ません。

作ってみました
--------------------

あったらうれしい、ということで `zip_open`_ パッケージを作ってみました。このパッケージは以下の機能を提供しています。

.. _`zip_open`: http://pypi.python.org/pypi/zip_open


インストール方法
~~~~~~~~~~~~~~~~~~~~~
::

  $ easy_install zip_open


利用例1: zipファイル内のファイルを開く
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

packages1.zip の例::

   packages1.zip
     + file1.txt

file1.txt を開きます::

   >>> from zip_open import zopen
   >>> fobj = zopen('packages1.zip/file1.txt')
   >>> data = fobj.read()
   >>> print data
   I am file1.txt, ok.

上記のコードは以下のコードと等価です::

   >>> from zipfile import ZipFile
   >>> zipobj = ZipFile('packages1.zip')
   >>> data = zipobj.read('file1.txt')
   >>> print data
   I am file1.txt, ok.


利用例2: 入れ子になったzipファイル内のファイルを開く
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

packages2.zip の例::

   packages2.zip
     + data2.zip
        + file2.txt

file2.txt を開きます::

   >>> from zip_open import zopen
   >>> fobj = zopen('packages2.zip/data2.zip/file2.txt')
   >>> print fobj.read()
   I am file2.txt, ok.


利用例3: zip圧縮されたパッケージ内のモジュールからファイルを開く
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

packages3.zip の例::

   packages3.zip
     + foo.py
     + file1.txt
     + data3.zip
        + file3.txt

foo.py のコード例::

   import os
   from zip_open import zopen

   def loader(filename):
       fobj = zopen(os.path.join(os.path.dirname(__file__), filename))
       return fobj

foo.pyのloader()をインタラクティブシェルから呼び出してファイルを開きます::

   >>> import sys
   >>> sys.path.insert(0, 'packages3.zip')
   >>> import foo
   >>> fobj = foo.loader('file1.txt')
   >>> print fobj.read()
   I am file1.txt, ok.
   >>> fobj = foo.loader('data3.zip/file3.txt')
   >>> print fobj.read()
   I am file3.txt, ok.


次の目標
---------
実際にこの仕組みを使うと嬉しいパッケージ(jinja2を使った自分のアプリ等)を調べて、この仕様で機能に過不足がないか検証する。あと入れ子になったzip内のモジュールをimport出来ると嬉しいかな。

元々は gaepytz_ を使っているGoogle App Engineアプリをzc.buildoutのappfy.recipe.gaeで環境管理しようとしたところ、zoneinfo.zipが入れ子zipの中に入ってしまってファイルを開けなくなってしまったため、なんとかできないかなーと思ったのが `zip_open`_ を作成した動機でした。 gaepytz_ の作者に入れ子zipでも動作するようにパッチを作って送ったはずみで、勢いでPyPIに登録してしまったという。。他に色々やることあったんだけど、これ作るのに半日使っちゃったよ。

.. _gaepytz: http://pypi.python.org/pypi/gaepytz


.. :extend type: text/x-rst
.. :extend:


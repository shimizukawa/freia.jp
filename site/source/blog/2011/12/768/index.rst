:date: 2011-12-07 18:45:00
:categories: python, python3

===============================================
ライブラリをPython3対応に書き換える
===============================================

Python-3.3が来年中盤にリリース予定ということで、そろそろ自作ライブラリをPython2/3両対応していかないとなあ、と思いつつここ半年ほどいろいろあって手が回っていません。結婚式レポートも全然書けてません。

ということで、 `2011 Pythonアドベントカレンダー(Python3)`_ 7日目担当の、中神さんに `新婚で幸せいっぱいの @shimizukawa` と紹介された清水川です。

.. _`2011 Pythonアドベントカレンダー(Python3)`: https://connpass.com/event/142/

前提条件
===========

以前作成した `zip_open`_ ライブラリをPython3対応に書き換えてみたいと思います。可能な箇所は2.7でも動作するように気をつけて記述します。
今回使用した環境は以下の通りです。

.. _`zip_open`: http://pypi.python.org/pypi/zip_open/0.2.0

:Python: 2.7.2, 3.2.2
:OS: Windows7 64bit, Mac OS X (Lion)
:対象: zip_open 0.2.0


zip_openはREADME.txtでdoctestを書いているので、まずこれがPython2.7で動作することを確認します::

   $ hg clone https://bitbucket.org/shimizukawa/zip_open
   $ cd zip_open
   $ python2.7 setup.py test

   running test
   running egg_info
   writing zip_open.egg-info/PKG-INFO
   writing top-level names to zip_open.egg-info/top_level.txt
   writing dependency_links to zip_open.egg-info/dependency_links.txt
   reading manifest file 'zip_open.egg-info/SOURCES.txt'
   reading manifest template 'MANIFEST.in'
   warning: no files found matching '*.py' under directory 'src'
   writing manifest file 'zip_open.egg-info/SOURCES.txt'
   running build_ext
   /Users/shimizukawa/zip_open/tests/../README.txt
   Doctest: README.txt ... ok

   ----------------------------------------------------------------------
   Ran 1 test in 0.015s

   OK
   $


これをPython3で同じように実行して、すべてのエラーをstep by stepで修正していこう、というのが今回の記事の趣旨です。

なお、2to3を用いて、Python2/3両対応ではなく、2->3自動変換によってPython3対応する方法もあります。これについては以下の記事を参照してください。

* `Python 2からPython 3への移行 - YAMAGUCHI::weblog`__

.. __: http://d.hatena.ne.jp/ymotongpoo/20110406/1302061408

* `pyreadline を2to3でPython2/3両対応にするメモ - 清水川Web`__

.. __: http://www.freia.jp/taka/blog/753

* `buchoを2to3でPython2/3両対応にするメモ - 清水川Web`__

.. __: http://www.freia.jp/taka/blog/755

他にも以下のドキュメントも見ておきましょう。

* `Porting Python 2 Code to Python 3 - Python v3.3a0 documentation`__

.. __: http://docs.python.org/dev/howto/pyporting.html

* `Six: Python 2 and 3 Compatibility Library - six 1.1.0 documentation`__

.. __: http://packages.python.org/six/

Python3の順次対応
===================

import関連の調整
------------------

-Sオプション付きでPython3で実行してみます。-SはPython起動時にimport siteしない(site-packagesなどを利用しない)モードです::

   $ python3.2 -S setup.py test
   Traceback (most recent call last):
     File "setup.py", line 2, in <module>
       from setuptools import setup, find_packages
   ImportError: No module named setuptools

まずはsetuptoolsが無いといわれました。アドベントカレンダーのrudiさんの記事 `pysetup3のご紹介`_ でも紹介されているように、Python3.3からはpackagingが同梱されます。このため、setuptools (Distribute)が必須というデファクトスタンダードな作法は変わっていくと思われます。ということで、以下のように修正しました::

   diff -r 967faaa489bd setup.py
   --- a/setup.py  Tue Nov 29 15:50:49 2011 +0900
   +++ b/setup.py  Wed Dec 07 00:28:04 2011 +0900
   @@ -1,6 +1,9 @@
    # -*- coding: utf-8 -*-
   -from setuptools import setup
    import os
   +try:
   +    from setuptools import setup
   +except ImportError:
   +    from distutils import setup

.. _`pysetup3のご紹介`: http://d.hatena.ne.jp/rudi/20111204/1323003603


再度実行::

   $ python3.2 setup.py  test
   ...
   error: invalid command 'test'
   $


setup.py の test コマンドはsetuptoolsの拡張機能でしたね‥。
ではtestsディレクトリのtest_zip_open.pyを直接実行します。

::

   $ python3.2 tests/test_zip_open.py
   ...


大量のエラーが出ました（多すぎるので掲載はしません）。DocTestの場合、エラーが発生してもテストを止めてくれないので、変数代入でエラーになっていると後の方で未定義の変数アクセスのエラーが連鎖的に発生したりします。ということで、先頭から順に解決して行けばそれほど大量に修正せずにすむ・・はず。

ということで、先頭から順番にPython3対応(出来ればPython2/3両対応)に書き換えていきましょう。

StringIO -> io.BytesIO
------------------------

::

   ----------------------------------------------------------------------
   File "tests/../README.txt", line 35, in README.txt
   Failed example:
       from zip_open import zopen
   Exception raised:
       Traceback (most recent call last):
         File "zip_open.py", line 5, in <module>
           from cStringIO import StringIO
       ImportError: No module named cStringIO


StringIOはioモジュールに移動しました。以下のように変更します::

   diff a/zip_open.py b/zip_open.py
   --- a/zip_open.py
   +++ b/zip_open.py
   @@ -1,10 +1,7 @@
    import os
    from zipimport import zipimporter
    from zipfile import ZipFile
   -try:
   -    from cStringIO import StringIO
   -except:
   -    from StringIO import StringIO
   +import io

    __version__ = '0.2.0'
    __all__ = ['zopen', 'zip_open']
   @@ -46,7 +43,7 @@
                          os.path.join(zipobj.filename, subpath))

        prefix = prefixes[0] # select first file
   -    fileobj = StringIO(zipobj.read(prefix))
   +    fileobj = io.BytesIO(zipobj.read(prefix))
        new_subpath = subpath[len(prefix):]

        if new_subpath:


basestring -> str
---------------------------

::

   ----------------------------------------------------------------------
   File "tests/../README.txt", line 35, in README.txt
   Failed example:
       fobj = zopen('packages1.zip/file1.txt')
   Exception raised:
       Traceback (most recent call last):
         File "/Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/doctest.py", line 1253, in __run
           compileflags, 1), test.globs)
         File "<doctest README.txt[1]>", line 1, in <module>
           fobj = zopen('packages1.zip/file1.txt')
         File "/Users/shimizukawa/zip_open/tests/../zip_open.py", line 10, in zopen
           if isinstance(path_or_fobj, basestring):
       NameError: global name 'basestring' is not defined

basestring は無くなり、strとbytesになりました。
ここではpath文字列を扱っているのでbytesではなくstrに変更します::

   diff a/zip_open.py b/zip_open.py
   --- a/zip_open.py
   +++ b/zip_open.py
   @@ -11,16 +11,13 @@
    __all__ = ['zopen', 'zip_open']
    
    def zopen(path_or_fobj, subpath=''):
   -    if isinstance(path_or_fobj, basestring):
   +    if isinstance(path_or_fobj, str):
            path = os.path.join(path_or_fobj, subpath)
            if os.path.exists(path):
                return open(path, 'rb')

Python2/3両対応にするにはPython2のunicodeオブジェクトが考慮から漏れていますね。このへんは、あとでちゃんと実装しようとおもいます。zip_openパッケージはunicode（日本語）の扱いが甘いですね！orz


filterがlistではなくgeneratorを返す
-------------------------------------------

::

   File "tests/../README.txt", line 35, in README.txt
   Failed example:
       fobj = zopen('packages1.zip/file1.txt')
   Exception raised:
       Traceback (most recent call last):
         File "/Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/doctest.py", line 1253, in __run
           compileflags, 1), test.globs)
         File "<doctest README.txt[1]>", line 1, in <module>
           fobj = zopen('packages1.zip/file1.txt')
         File "/Users/shimizukawa/zip_open/tests/../zip_open.py", line 18, in zopen
           return zip_open(zipobj, path)
         File "/Users/shimizukawa/zip_open/tests/../zip_open.py", line 45, in zip_open
           prefix = prefixes[0] # select first file
       TypeError: 'filter' object is not subscriptable

filter()の結果がgeneratorになりました(他にもPython2ではlistを返していてた色々な関数がPython3ではgeneratorを返すようになっています)。なので、prefixes[0]という書き方が出来なくなりました。ここでは最初の1個が取り出せればいいのでnext(prefixes)に変更します。

::

   diff a/zip_open.py b/zip_open.py
   --- a/zip_open.py
   +++ b/zip_open.py
   @@ -41,12 +38,13 @@
        subpath = subpath.replace(os.path.sep, '/').strip('/')
        prefixes = filter(path_finder(subpath), zipobj.namelist())

   -    if not prefixes:
   +    try:
   +        prefix = next(prefixes)  # select first file
   +    except StopIteration:
            raise IOError(2, 'No such file or directory',
                          os.path.join(zipobj.filename, subpath))

   -    prefix = prefixes[0] # select first file
        fileobj = io.BytesIO(zipobj.read(prefix))
        new_subpath = subpath[len(prefix):]



printは関数に変更
--------------------

次は `print data` が大量にエラーになっています。Python3からprintは関数になりました。

::

   ----------------------------------------------------------------------
   File "tests/../README.txt", line 37, in README.txt
   Failed example:
       print data
   Exception raised:
       Traceback (most recent call last):
         File "/Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/doctest.py", line 1253, in __run
           compileflags, 1), test.globs)
         File "<doctest README.txt[3]>", line 1
           print data
                    ^
       SyntaxError: invalid syntax

数が多いので全部は書きませんが、以下のように修正しました::

   diff a/README.txt b/README.txt
   --- a/README.txt
   +++ b/README.txt
   @@ -34,13 +34,13 @@
       >>> from zip_open import zopen
       >>> fobj = zopen('packages1.zip/file1.txt')
       >>> data = fobj.read()
   -   >>> print data
   +   >>> print(data)
       I am file1.txt, ok.


再度実行すると・・・まだエラーが出ます::

   ----------------------------------------------------------------------
   File "tests/../README.txt", line 37, in README.txt
   Failed example:
       print(data)
   Expected:
       I am file1.txt, ok.
   Got:
       b'I am file1.txt, ok.\r\n'

なるほど、zopenで開くファイルの種類としてtextを想定していなかったので、bytes型でデータを保持してしまっています。これだとprintしたときに上記のように `print(repr(data))` した値が出力されています。zopenに読み取りモード指定オプションを付けるべきでしたが、今回はテストを書き換えてしまいます::

   diff a/README.txt b/README.txt
   --- a/README.txt
   +++ b/README.txt
   @@ -34,13 +34,13 @@
       >>> from zip_open import zopen
       >>> fobj = zopen('packages1.zip/file1.txt')
       >>> data = fobj.read()
   -   >>> print data
   +   >>> print(data.decode('ascii'))
       I am file1.txt, ok.

これでprint周りのエラーは無くなりました。

が。

こんなのがPyPIに掲載されるのはとても恥ずかしい。利用サンプルにこのように書かれていると使う気が無くなりますね。ということで、このあたりを修正するまでPython3対応版をリリースするのはやめることにします。

この記事としては、とりあえず、今の実装のPython3化ということで、残りのエラーも解消してしまいます。

open読み取りモード指定のバグ修正
-----------------------------------

::

   ----------------------------------------------------------------------
   File "tests/../README.txt", line 75, in README.txt
   Failed example:
       fobj = zopen(zip_fileobj, 'data2.zip/file2.txt')
   Exception raised:
       Traceback (most recent call last):
         File "/Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/doctest.py", line 1253, in __run
           compileflags, 1), test.globs)
         File "<doctest README.txt[14]>", line 1, in <module>
           fobj = zopen(zip_fileobj, 'data2.zip/file2.txt')
         File "/Users/shimizukawa/zip_open/tests/../zip_open.py", line 23, in zopen
           zipobj = ZipFile(fobj)
         File "/Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/zipfile.py", line 719, in __init__
           self._GetContents()
         File "/Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/zipfile.py", line 753, in _GetContents
           self._RealGetContents()
         File "/Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/zipfile.py", line 768, in _RealGetContents
           raise BadZipFile("File is not a zip file")
       zipfile.BadZipFile: File is not a zip file

なにやらBadZipFile例外が発生したようです。README.txtの該当箇所を見ると、以下のように書かれていました::

   >>> zip_fileobj = open('packages2.zip')

open関数は読み取りモードを指定しないと、Python2でも3でもデフォルトでテキスト読み取りを行います。

Python2ではどちらのモードで読み込んでも、改行コード変換などが発生しないなら結果は同じで、続く処理に影響はありませんでした（もちろんbinaryで読み込むべきものをtextで読み込んでしまうという動作は、「与えるファイルによってエラーが再現する」という嫌なバグの原因になるわけですが・・）。

Python3ではテキストモードで読み込んだらstr型、バイナリモードで読み込んだらbytes型が返されます。この違いによって、Python2ではエラーになっていなかった潜在的バグがPython3で実行したために出現したようです。

Python3で文字列とデータ列が厳密に区別されるようになったおかげで、zip_openの不具合が明らかになったわけですね...。

ということで、2カ所ほど以下のように明示的にバイナリモードで読み込むように修正しました::

   >>> zip_fileobj = open('packages2.zip', 'rb')

これでテストを実行すると以下のようになりました::

   $ python3.2 tests/test_zip_open.py
   .
   ----------------------------------------------------------------------
   Ran 1 test in 0.019s

   OK


まとめ
===========

自分のコードにバグが多くて泣きそうです。


次の8日目は `@hideaki_t`_ にバトンを渡そうと思います。よろしくお願いします。

.. _`@hideaki_t`: http://twitter.com/#!/hideaki_t


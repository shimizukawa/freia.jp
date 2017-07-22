:date: 2007-01-18 23:52:02
:categories: ['python', 'Windows']
:body type: text/x-rst

===========================================================
2007/01/18 WindowsでPython Imaging Library(PIL)をビルドする
===========================================================

python.jpのMLで出た話題。だいぶ前にビルドがうまくいったときにメモっておいたのを、思い出したかのようにBlogに書いてみる。

環境： `WindowsでFreeなCモジュールビルド環境`_ 

- 以下のパッケージを入手

  ::

    Imaging-1.1.6.tar.gz
    jpegsrc.v6b.tar.gz
    zlib-1.2.3.tar.gz

- 以下のように展開

  ::

    Imaging-1.1.6/
      + jpeg-6b
      + zlib-1.2.3

- setup.py を修正

  ::

    JPEG_ROOT = 'jpeg-6b'
    ZLIB_ROOT = 'zlib-1.2.3'

- JPEG_ROOTでビルド

  ::

    ren jconfig.vc jconfig.h
    nmake -f makefile.vc

- ZLIB_ROOTでビルド

  ::

    nmake -f win32\Makefile.msc

- Imaging-1.1.6でビルド

  ::

    python setup.py bulild

  以下のように出力されればOK::

    *** TKINTER support not available (Tcl/Tk 8.4 libraries needed)
    --- JPEG support ok
    --- ZLIB (PNG/ZIP) support ok
    *** FREETYPE2 support not available

- 作成された \*.pyd (.so) を Imaging-1.1.6へコピー
- Imaging-1.1.6をテスト

  ::

    python selftest.py

  以下のように出力されればOK::

    57 tests passed.


.. _`WindowsでFreeなCモジュールビルド環境`: http://www.freia.jp/taka/memo/freevcbuild

.. :extend type: text/html
.. :extend:


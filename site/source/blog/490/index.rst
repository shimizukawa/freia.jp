:date: 2007-10-28 09:09:46
:tags: misc, python, Windows
:body type: text/x-rst

============================================
2007/10/28 WindowsXPのハードリンクは不安定？
============================================

Python温泉の成果（文面だけ）。

Pythonにはファイルシステム操作関連機能としてハードリンクやシンボリックリンクを扱う機能があるが、この機能はプラットフォーム依存機能のため、利用できる環境はUnix系に限定されている。しかし、Windowsでも実はハードリンクを扱う機能は以前からAPI的には提供されていて、WindowsXPではコマンドラインでハードリンクを作成する機能が提供されている。

`＠IT：Windows XPの正体 強化されたコマンドライン・ツール（中編） 2．ディスク／ファイル関連ツール（2）`_ に載っているように、 ``fsutil hardlink create DEST SRC`` でファイルのハードリンクを作ることが出来る。

これをPythonで扱えるように以下のように書いてみた。

.. code-block:: python

  # -*- coding: utf-8 -*-
  
  import os, sys, shutil
  
  WIN32_USE_HARDLINK = True
  
  if sys.platform == 'win32':
      def win32_hardlink(src, dest):
          args = [
              'fsutil',
              'hardlink',
              'create',
              dest,
              src,
          ]
          r = os.system(' '.join(args))
          if r:
              raise os.error(r, str(args), '%s -> %s' % (src, dest))
      if WIN32_USE_HARDLINK:
          link = win32_hardlink
      else:
          link = shutil.copyfile
  
  else:
      link = os.link
  

ついでにディレクトリをハードリンク的に扱う関数。

.. code-block:: python
  
  def makedirs(d):
      if not os.path.exists(d):
          return os.makedirs(d)

  
  def lndir(srcdir, destdir):
      makedirs(destdir)
  
      for name in os.listdir(srcdir):
          srcpath = os.path.join(srcdir, name)
          destpath = os.path.join(destdir, name)
          if os.path.isdir(srcpath):
              lndir(srcpath, destpath)
          else:
              if os.path.exists(destpath):
                  os.remove(destpath)
              link(srcpath, destpath)
  

こんな感じで作って動かしてみたところ、なぜか安定動作してくれない。時々ハードリンクの作成に失敗してパーミッションエラーのコードが返ってくる。しょうがないのでWIN32_USE_HARDLINK=Falseにして使うことに。すごくイケテナイ。pyd作ったら安定動作するだろうか？


.. _`＠IT：Windows XPの正体 強化されたコマンドライン・ツール（中編） 2．ディスク／ファイル関連ツール（2）`: http://www.atmarkit.co.jp/fwin2k/xp_feature/013commandtool/commandtool3.html


.. :extend type: text/html
.. :extend:


:date: 2004-09-06 23:13:48
:tags: python, Programming

=============================
pyuiをいじってみる
=============================

久しぶりのpythonです。今回は pyui_ をいじってみます。 pyui_ はGUI系のライブ
ラリなので、Xを設定していないFreeBSDではなくWindows上で動かすために、
pythonのインストールから行いました。

.. _pyui: http://pyui.sourceforge.net/



.. :extend type: text/x-rst
.. :extend:

1. Python日本語環境用インストーラ_ (python23jp-20030906.exe)
2. PyGame_ (pygame-1.6.win32-py2.3.exe)
3. PyOpenGL_ (PyOpenGL-2.0.1.08.py2.3-numpy23.exe)
4. PIL_ (PIL-1.1.4.win32-py2.3.exe)
5. GLUT_ (glut-3.7.6-bin.zip)
6. pyui_ (pyui095.zip)

GLUT_ と pyui_ 以外はインストーラで簡単にインストールすることが出来ました。
GLUT_ はOpenGLを手抜き利用するためのものらしいですがよく知りません。入手し
たパッケージに入っているglut32.dllを\\Windows\\system32に入れました。

pyui_ は最新版の1.00があるのですが、間違って0.95を使用しました。0.95のパッ
ケージにはWindows専用インストーラは含まれていませんでしたので、展開してコマ
ンドラインから以下のコマンドを入力してインストールしました::

  c:\pyui95＞ python setup.py install

準備が整ったので、早速実験です。まずは pyui_ のサイトにあるサンプルを入力し
て、以下の最小のサンプルに行き着きました::

  import pyui
  pyui.init(400,300)
  pyui.run()

真っ黒なWindowが表示されて、あとはコンソールにFPSが流れていきます。さすがに
意味のあるサンプルにしたいので、もう一行追加::

  import pyui
  pyui.init(400,300)
  pyui.widgets.Frame(10,10,100,100,"test")
  pyui.run()

無事Windowが表示されたところで、今日はここまで::

  pyui.quit()

おまけ： pyui.widgets.Frame() を３つ出してみる
----------------------------------------------
|pyuitest1|


.. _pyui: http://pyui.sourceforge.net/
.. _Python日本語環境用インストーラ: http://www.python.jp/Zope/download/pythonjpdist
.. _PyGame: http://www.pygame.org/download.shtml
.. _PyOpenGL: http://sourceforge.net/project/showfiles.php?group_id=5988
.. _PIL: http://www.pythonware.com/products/pil/
.. _GLUT: http://www.xmission.com/~nate/glut.html
.. |pyuitest1| image:: pyuitest1



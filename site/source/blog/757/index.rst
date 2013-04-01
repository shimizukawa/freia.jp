:date: 2011-05-04 01:45:53
:categories: ['python']
:body type: text/x-rst

===============================================
2011/05/04 PILをWindowsで使う場合の問題への対策
===============================================

*Category: 'python'*

WindowsでPIL-1.1.7を使う場合につまらない対策をする必要が有るらしいので、状況を調べてみた。

PIL配布元
http://www.pythonware.com/products/pil/

64bit Pythonだとインストール出来ない
-----------------------------------------------
情報元: http://www.flotsam-fareast.com/2011/02/64bit-windows-python-image-library-20110212.html

* インストーラがPythonを認識できない問題。
* 解決方法
    * Zip展開して手動でインストールする
    * distributeのeasy_installか、buildoutを使う
    * 根本的には配布元で64bit版インストーラを用意する必要がある。


1.1.7-py26,27ではDLL書き換えが必要
-----------------------------------------------
情報元: http://99blues.dyndns.org/blog/2011/01/blockdiag_for_win/

* 解決方法
    * DLLを書き換える
    * デバッグ版のDLLをインストールする(VC++9.0Express)

* 対象バージョン
    * 1.1.6 py24 OK
    * 1.1.6 py25 OK
    * 1.1.6 py26 OK
    * 1.1.7 py24 OK
    * 1.1.7 py25 OK
    * 1.1.7 py26 NG
    * 1.1.7 py27 NG


.. :extend type: text/x-rst
.. :extend:



.. :comments:
.. :comment id: 2011-05-04.5743150465
.. :title: Re:PILをWindowsで使う場合の問題への対策
.. :author: KATO Kanryu
.. :date: 2011-05-04 02:09:34
.. :email: k.kanryu@gmail.com
.. :url: 
.. :body:
.. 記事ありがとうございます。
.. 64bit対応は今後行う可能性があるので
.. その時に改めてこの記事を参照したいと思います。
.. 
.. ですがPILのWindows版の対応については、
.. PythonのWindows版がVisual Studio 2008によるビルドが標準になっているにもかかわらず、
.. 一部のディストリ(要するにPython公式のWindows版)で
.. msvcr90.dll等がバンドルされていないという可能性があるような気がします。
.. Windowsへの対策が十分に考えられているActivePythonや
.. PortablePythonを利用すれば、こういった問題は発生しないでしょう。
.. 
.. あと、PIL公式配布のバイナリの方がまずい可能性もありますね。

.. note::

   2013/4/1 追記:

   PILの後継のPillowを使いましょう。

   * Python-2.6, 2.7, 3.2, 3.3: https://pypi.python.org/pypi/Pillow/2.0.0
   * Python-2.4, 2.5, 2.6, 2.7: https://pypi.python.org/pypi/Pillow/1.7.8


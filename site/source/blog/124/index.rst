:date: 2005-01-25 01:00:24
:categories: ['python', 'Programming']
:body type: text/x-rst

========================================
2005/01/25 Pythonを利用するDLLのデバッグ
========================================

デバッグ版Python32_d.libは標準のパッケージ 1_ には同梱されていない。そしてpython.hをincludeすると内部的に以下のようにかかれているので、Debugだとpython23_d.libを自動的にリンクしようとして失敗してしまう。::

  #ifdef _DEBUG
      #pragma comment(lib,"python23_d.lib")
  #else
      #pragma comment(lib,"python23.lib")
  #endif /* _DEBUG */

なので、Pythonを使うC++アプリをVS.NETで作ってもReleaseでしかコンパイルできないのでデバッグが大変。というかDebug版無しに開発するのはIDEに慣れてしまった身としては苦痛。いや、苦痛とか言ってないでUnitTestすればいいんだけど。

どっかにコンパイル済みのpython23_d.libがあるだろ！と思って調べてみたら、 `もっと簡単な方法`__ が::

	So if you want you should be able to change your source to something
	like this:
	
	#undef _DEBUG
	#include <python.h>
	#define _DEBUG

__ http://mail.python.org/pipermail/python-list/2004-June/226167.html


あー、なるほどー。

.. [1] Python 2.3.4 日本語環境用インストーラ(Win32)を使ってます。 http://www.python.jp/Zope/download/pythonjpdist


.. :extend type: text/plain
.. :extend:

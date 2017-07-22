:date: 2007-03-24 12:03:32
:tags: python
:body type: text/x-rst

=========================
2007/03/24 inspect.getmro
=========================

Pythonでクラスにクラス変数を定義する。そのクラスを継承してそこでクラス変数をoverrideする。

.. code-block:: python

  # a.py
  class A(object):
      path = 'foo'

  # b.py
  class B(A)
      path = 'bar'

  # c.py
  class C(A)
      pass

  a = A()
  b = B()
  c = C()

このとき、b.pathはもちろん'bar'になるがpathが宣言されているクラス名も欲しくて'B.bar'みたいに文字列を作りたい。

.. code-block:: python

  import inspect
  def makepath(o):
      objs = inspect.getmro(b.__class__)
      for x in objs:
        if 'path' in x.__dict__:
            return '.'.join(x.__name__, x.path)

  print makepath(a)
  print makepath(b)
  print makepath(c)

これで、 ``A.foo``, ``B.bar``, ``A.foo`` という文字列が取得できる。問題。c.path='moo'が設定された場合、 ``C.moo`` と出力するにはどうすればいいか。ヒント: c.__dict__


うーん、用途を書かないと意味不明だｗ


.. :extend type: text/html
.. :extend:


:date: 2017-11-12 1:00
:tags: Python, pyhack

========================================
Pythonで循環インポートするとどうなるのか
========================================

Pythonのインポート処理周りで、普段知られていないネタを集めました。

なお、ここで紹介するネタは知っておいて損はないけど、使うと危険です。使ってしまっても責任は持てません。

使った環境:

.. code-block:: bash

   [taka ~/py]$ python3
   Python 3.5.2 (default, Sep 14 2017, 22:51:06)
   [GCC 5.4.0 20160609] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

ケース1: aがimport aする
==========================

.. code-block:: python
   :caption: a1.py

   import a
   a.foo = 1
   print('foo =', foo)

.. code-block:: pycon

   [taka ~/py]$ python3 -q
   >>> import a
   foo = 1

2007年頃に田原さんから教えてもらったワザ。

どうしてもやりたいならこう書けるけど、アーキテクチャを見直した方がよい。


ケース2: モジュール b1, b2 が相互にimport
==========================================

``b1`` が ``b2`` をimportする。 ``b2`` が ``b1`` をimportしたあと何かのエラーでraiseする。

.. code-block:: python
   :caption: b1.py

   import sys
   print('b1 in sys.modules?', 'b1' in sys.modules)
   import b2


.. code-block:: python
   :caption: b2.py

   import sys
   print('b1 in sys.modules?', 'b1' in sys.modules)
   import b1
   raise ImportError('hoge')


.. code-block:: pycon

   [taka ~/py]$ python3 -q
   >>> import sys
   >>> import b1
   b1 in sys.modules? True
   b1 in sys.modules? True
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "/home/taka/py/b1.py", line 3, in <module>
       import b2
     File "/home/taka/py/b2.py", line 5, in <module>
       raise ImportError('hoge')
   ImportError: hoge
   >>> 'b1' in sys.modules
   False
   >>> 'b2' in sys.modules
   False


``b1``, ``b2`` とも ``sys.modules`` から消えた。importの連鎖中に存在していてもエラーが起きると消えるようになっている。 ``sys.modules`` に残っていたらなぜだめなのか？ ``b2`` のエラー解消後に対話コンソールで再度importできるようにするため。失敗したimportの残骸を残さないため。


ケース3: sys.modulesのobjectをimportする
========================================

``sys.modules`` ってなんなの？

.. code-block:: python
   :caption: aodag.py

   print('しゅーくりーむたべたいです')

.. code-block:: pycon

   [taka ~/py]$ python3 -q
   >>> import sys
   >>> sys.modules['aodag'] = 'わんわん'
   >>> import aodag
   >>> aodag
   'わんわん'

``aodag.py`` はロードされない。わんわん。

ケース4: サブモジュールのインポートエラー後の動き
=================================================

``d.py`` は ``d1.d2`` をインポートする。 ``d1/__init__.py`` は ``d2`` をインポートした後で例外を起こす。

.. code-block:: python
   :caption: d.py

   import sys
   print('Hello d:', [m for m in sys.modules if m.startswith('d1')])
   try:
       import d1.d2
   except ImportError as e:
       print(e)
       pass
   print('d1.d2 exists:', [m for m in sys.modules if m.startswith('d1')])
   print(sys.modules['d1.d2'])
   try:
       import d1.d2
   except ImportError as e:
       print(e)
       pass
   print('Goodbye d:', [m for m in sys.modules if m.startswith('d1')])

.. code-block:: python
   :caption: d1/__init__.py

   import sys
   print('Hello d1:', [m for m in sys.modules if m.startswith('d1')])
   from . import d2
   raise ImportError('Some Error on d1/__init__.py')
   print('Goodbye d1:', [m for m in sys.modules if m.startswith('d1')])


.. code-block:: python
   :caption: d1/d2.py

   import sys
   print('Hello d2', [m for m in sys.modules if m.startswith('d1')])

.. code-block:: bash

   [taka ~/py]$ python3 d.py
   Hello d: []
   Hello d1: ['d1']
   Hello d2 ['d1.d2', 'd1']
   Some Error on d1/__init__.py
   d1.d2 exists: ['d1.d2']
   <module 'd1.d2' from '/home/taka/py/d1/d2.py'>
   Hello d1: ['d1.d2', 'd1']
   Some Error on d1/__init__.py
   Goodbye d: ['d1.d2']

``sys.modules`` に ``d1.d2`` が残ってしまったけど、名前空間に ``d1.d2`` はロードされていないので使えない。 ``sys.modules`` にあればキャッシュとして単純に再利用されるわけではない。

ケース5: 循環インポート中に属性を読む
=====================================

``e1`` が ``e2`` をインポートし、 ``e2`` が ``e1`` をインポートしてすぐに ``e1.VALUE`` にアクセスする。

.. code-block:: python
   :caption: e1.py

   print('start e1')
   import e2
   print('e1 define VALUE')
   VALUE = 1
   print('e1 finished')


.. code-block:: python
   :caption: e2.py

   print('e2 start')
   print('e2 imports e1')
   import e1
   print('e2 prints e1.VALUE =', e1.VALUE)

.. code-block:: pycon

   [taka ~/py]$ python3 -q
   >>> import e1
   start e1
   e2 start
   e2 imports e1
   Traceback (most recent call last):
     File "b.py", line 1, in <module>
       import e1
     File "/home/taka/py/e1.py", line 2, in <module>
       import e2
     File "/home/taka/py/e2.py", line 4, in <module>
       print('e2 prints e1.VALUE =', e1.VALUE)
   AttributeError: module 'e1' has no attribute 'VALUE'

``e1.VALUE`` はまだない。

問い
====

Pythonで循環インポートのエラーを発生させよう。

自分も一時期循環インポートに苦しめられたけど、いざ起こそうと思ったら循環インポートできませんでした。Pythonでの循環インポートの起こし方、募集中です。



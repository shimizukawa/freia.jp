:date: 2018-05-22 23:10
:tags: birthday

=======================================
43歳 - Pythonで自分と息子の日齢比を計算
=======================================

43歳です。ふと、自分は生後何日目なんだろうと思ったので、Pythonで計算してみました。

.. code-block:: pycon

   >>> from datetime import date
   >>> today = date.today()
   >>> today - date(1975,5,22)
   datetime.timedelta(15706)

自分は、生後15706日目みたいです。


.. code-block:: pycon

   >>> today - date(2018,1,31)
   datetime.timedelta(111)

息子は111日目。

.. code-block:: pycon

   >>> (today - date(2018,1,31)) / (today - date(1975,5,22))
   0.007067362791289953

まだ自分の1%にも満たなかった。

ここで問題です。息子の日齢が私の日齢の1%に達するのは生後何日目でしょう？回答はPythonで解いてください。ライブラリの利用制限はありません。


答えは画像のあとで！

----------

.. figure:: happybirthday.*
   :width: 80%

   体重計（ `Nokia Body Cardio`_ ）にお祝いされた

.. _Nokia Body Cardio: https://health.nokia.com/jp/ja/body-cardio

----------

では回答です。2つ書いてみたけど、他にも書き方はたくさんあると思います。

1つ目。for文で解くとこんな感じ:

.. code-block:: pycon

   >>> for x in range(10000):
   ...     if x/(x+15595) >=  0.01:
   ...         print(x)
   ...         break
   ...
   158

2つ目。 Sympy_ で解くとこんな感じ:

.. code-block:: pycon

   >>> import sympy
   >>> x = sympy.Symbol('x')
   >>> f = x/(x+15595)
   >>> sympy.solve(sympy.Eq(f,0.01))
   [157.525252525253]

158日目だと分かりました。

日齢比をyとした式で定義して、変形してみます。

.. code-block:: pycon

   >>> y = sympy.Symbol('y')
   >>> f2 = sympy.Eq(f, y)
   >>> sympy.solve(f2, x)
   [-15595*y/(y - 1)]

はい、これでy（日齢比）に好きな値を入れれば、日齢何日目にその比率になるか計算できますね。

``y=0.1`` だとxはいくつになる？

.. code-block:: pycon

   >>> sympy.solve(f2, x)[0].subs(y, 0.1)
   1732.77777777778

Sympy_ 便利。

.. _Sympy: http://www.sympy.org/

:date: 2010-09-13 23:55:00
:categories: ['python']
:body type: text/x-rst

=============================================================
2010/09/13 Pythonの動的クラス生成と特殊メソッドとフレームの謎
=============================================================

先日、とある事情からクラス定義を動的に生成する必要があったのですが、そこでおかしな現象にはまってしまい、今もまだ解決出来ていません。

.. note::

  9/14 2:00 追記: この投稿の内容はWindowsのPython2.6.4, 2.7, FreeBSDのPython2.4.4で試しました。

  9/14 12:20 追記: 解決しました.... 勘違いした部分に追記入れておきます


動的なクラス生成
------------------

クラス定義を動的に生成するのは結構簡単にできます。例えば以下のように静的に定義して使う例があるとして、

.. code-block:: python

    >>> class Foo(object):
    ...     def foo(self, a):
    ...         return a
    ...
    >>> f = Foo()
    >>> f.foo('hoge')
    'hoge'

これと同じことを以下のように書けます。

.. code-block:: python

    >>> attrs = {
    ...     'foo': lambda self, a: a
    ... }
    >>> Foo = type('Foo', (object,), attrs)
    >>> f = Foo()
    >>> f.foo('hoge')
    'hoge'


ここまではtype()の使い方の一つとして知っていれば、詳しい原理などを知らなくても、まあ問題無く使える気がします。

特殊メソッド
--------------

もう一つ、本題に入る前に特殊メソッドの使い方の例。例えばあるクラスに__len__というメソッドを実装してその動きを見てみます。

.. code-block:: python

    >>> class Bar(object):
    ...     def __len__(self):
    ...         return 10
    ...
    >>> b = Bar()
    >>> len(b)
    10
    >>> b.__len__()
    10

len(b)で10という値が返ってきているし、__len__()を直接呼び出しても10が返ってきます。でも、len()関数がオブジェクトの__len__()メソッドを呼んでる、のでは無いところには注意。表現としては「len()アダプタはその内部で、対象オブジェクトと__len__プロトコルで通信して10という結果を返している」と書いた方が良いと思います。

ちょっと脱線ですが、試しに以下のように書いてみます。

.. code-block:: python

    >>> class Bar2(object): pass
    ...
    >>> b2 = Bar2()
    >>> b2.__len__ = lambda: 10
    >>> b2.__len__()
    10
    >>> len(b2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'Bar2' has no len()

上記エラーメッセージを見ると、Bar2という型はlen()を持っていないというエラーが出ているので、インスタンスではなくクラスに__len__を後付けしてみます。

.. code-block:: python

    >>> class Bar3(object): pass
    ...
    >>> b3 = Bar3()
    >>> len(b3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'Bar3' has no len()

    >>> Bar3.__len__ = lambda self: 10
    >>> len(b3)
    10

クラスに特殊メソッドを後付けしてもちゃんと動作する事が分かりました。


ここからが本題
----------------

先の2つの話を組み合わせて、以下のように動的に特殊メソッドを持つクラスを生成します。これはうまく動くので、クラス生成する関数をgen_safe()という名前にしました。

.. code-block:: python

    >>> d = {
    ...     '__len__': 10,
    ...     '__str__': 'va-',
    ... }
    ...
    >>> def gen_safe():
    ...     attrs = {}
    ...     attrs['__len__'] = lambda self: d['__len__']
    ...     attrs['__str__'] = lambda self: d['__str__']
    ...     return type('Gen', (object,), attrs)
    ...
    >>> Gen = gen_safe()
    >>> g = Gen()
    >>> str(g)
    'va-'
    >>> len(g)
    10

期待通りに動作したので、次に冗長なコードを最適化してみます。でもうまく動かなくなってしまったので、クラス生成関数をgen_fail()という名前にしました。

.. code-block:: python

    >>> d = {
    ...     '__len__': 10,
    ...     '__str__': 'va-',
    ... }
    ...
    >>> def gen_fail():
    ...     attrs = {}
    ...     for name in ('__len__', '__str__'):
    ...         attrs[name] = lambda self: d[name]
    ...     return type('Gen', (object,), attrs)
    ...
    >>> Gen = gen_fail()
    >>> g = Gen()
    >>> str(g)
    'va-'
    >>> len(g)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: an integer is required

``attrs`` を作成する処理をforループに書き換えたら動かなくなってしまいました。ここで内部的にはlen(g)した時点でgと__len__プロトコルで通信しているわけですが、その結果len()内部で ``'va-'`` という文字列を受け取ってしまい、__len__プロトコルで受け取る値は数値型であるという条件チェックにひっかかって ``TypeError: an integer is required`` エラーになっている事が分かりました。でも,,,

.. code-block:: python

    >>> g.__len__()
    10

上記のコードはエラーにならないんですよね。謎は深まるばかりです。

.. note::

  9/14 12:20 追記: 上記は勘違いです。g.__len__()は'va-'を返します。
  色々やっているうちに混乱していたようで… 謎は深まりませんでした。
%%%%%%%%%----------------

ところで、先日の `エキスパートPythonプログラミング読書会02`_ で、内包表記で閉じ込められた変数が属しているスタックはどこまで持って行かれるのか、という話が出ていたのに対して、@atsuoishimoto さんが `「スタックってか、フレームオブジェクトが保存される。」`_ とコメントしてくれていたことから、以下のように書き換えることを思いつきました。

.. _`エキスパートPythonプログラミング読書会02`: http://atnd.org/events/6954
.. _`「スタックってか、フレームオブジェクトが保存される。」`: http://twitter.com/atsuoishimoto/status/23230187180

.. code-block:: python

    ...     for name in ('__len__', '__str__'):
    ...         attrs[name] = lambda self, __name=name: d[__name]

nameの値をlambda定義の外から渡すことでフレームオブジェクトを保存しないようにしてみようと思ったわけですが……、なんと！これで期待通りに動いてくれました！

いやー、これで無事解決です。よかったー！%%%%%%%%%-----------------

……解決なわけ無いですね。引数有りのメソッドに対応出来ないし、そもそも根本解決してない。

と言うことで解決してません。解決するにはフレームオブジェクトを色々操作して頑張るしかないの？やだなー。

.. note::

  9/14 12:20 追記: コメントの方で「もう一段,関数でwrapすればよい」という指摘のもと、
  解決することが出来ました。結局の所、以下の挙動を理解していればこの問題にはまることも
  無かったと思います。

  .. code-block:: python

      >>> funcs = {}
      >>> for name in ('foo', 'bar', 'baz'):
      ...     funcs[name] = lambda: name
      ...
      >>> for n,f in funcs.items():
      ...     print n, f()
      ...
      baz baz
      foo baz
      bar baz


.. :extend type: text/x-rst
.. :extend:


.. :comments:
.. :comment id: 2010-09-14.0326482676
.. :title: Re:Pythonの動的クラス生成と特殊メソッドとフレームの謎
.. :author: atsuoishimoto
.. :date: 2010-09-14 01:23:54
.. :email: 
.. :url: 
.. :body:
.. attrs[name] = lambda self: d[name]
.. 
..  は、
.. 
.. attrs[name] = lambda self, name=name: d[name]
.. 
.. としないと駄目なんじゃないかと思います
.. 
.. :comments:
.. :comment id: 2010-09-14.5779225607
.. :title: name=name
.. :author: しみずかわ
.. :date: 2010-09-14 01:32:58
.. :email: 
.. :url: 
.. :body:
.. や、そこは __name で大丈夫でした。
.. 
.. 
.. :comments:
.. :comment id: 2010-09-14.6206704434
.. :title: Re:Pythonの動的クラス生成と特殊メソッドとフレームの謎
.. :author: atsuoishimoto
.. :date: 2010-09-14 01:33:40
.. :email: 
.. :url: 
.. :body:
.. すいません、最後まで読んでませんでした。
.. 
.. この形でご要望通りにする方法は思いつかないですねぇ。eval()使ってlambda式を動的コンパイルするぐらいでしょうか。
.. 
.. :comments:
.. :comment id: 2010-09-14.9909940206
.. :title: Re:Pythonの動的クラス生成と特殊メソッドとフレームの謎
.. :author: atsuoishimoto
.. :date: 2010-09-14 01:39:51
.. :email: 
.. :url: 
.. :body:
.. あ、関数をもう一枚かませば良いのか
.. 
.. def gen():
..     attrs = {}
..     def gen_lambda(name):
..         return lambda self: d[name]
..         
..     for name in ('__len__', '__str__'):
..         attrs[name] = gen_lambda(name)
..     return type('Gen', (object,), attrs)
.. 
.. でどうでしょ？
.. 
.. :comments:
.. :comment id: 2010-09-14.2712014002
.. :title: eval!?
.. :author: しみずかわ
.. :date: 2010-09-14 01:44:31
.. :email: 
.. :url: 
.. :body:
.. classの__dict__にはちゃんと入っていてg.__len__()やg.__str__()では正しく動作するのに、len(g)やstr(g)ではうまくいかない、というのが納得できないんです。len()を使った場合、フレーム処理まわりで g.__len__() したときとは何か違うんだとは想像してるんですが…。classobject.cやtypeobject.cを読んでるんですが、まだ追い切れていません＞＜
.. 
.. :comments:
.. :comment id: 2010-09-14.6980440469
.. :title: Re: 関数をもう一枚
.. :author: taka
.. :date: 2010-09-14 01:51:38
.. :email: 
.. :url: 
.. :body:
.. 関数をもう一枚挟んだらいけました！
.. 
.. とりあえずやりたいことはできるようになりましたが、しかし、、フレームが保存されるとなぜ問題が出てしまったのか、これはこれで理解しておきたいですね（バグなのか仕様なのかも含めて）。追々調べてみます。
.. 
.. :comments:
.. :comment id: 2010-09-14.8462931789
.. :title: Re:Pythonの動的クラス生成と特殊メソッドとフレームの謎
.. :author: atsuoishimoto
.. :date: 2010-09-14 01:54:06
.. :email: 
.. :url: 
.. :body:
.. 私の環境だと、 g.__len__()で 'va-'が返ってきますんで、何かの間違いじゃないかなぁと思うんですが。私の知る限りでは呼び出し方法が違うと言うことはありません。
.. 
.. :comments:
.. :comment id: 2010-09-14.7383183210
.. :title: Re: g.__len__()で 'va-'が返ってきます
.. :author: しみずかわ
.. :date: 2010-09-14 12:25:38
.. :email: 
.. :url: 
.. :body:
.. > 私の環境だと、g.__len__()で 'va-'が返ってきますんで、
.. 
.. うあー、確かに！このblogエントリを書こうと思ったきっかけの方のコードに別の要因が入ってました。切り分け不足でした＞＜
.. 
.. はずかしいエントリ書いちゃったなぁ… けど理解が深まったので良しとします。ありがとうございました。
.. 
.. :comments:
.. :comment id: 2010-09-21.3341715479
.. :title: Re:Pythonの動的クラス生成と特殊メソッドとフレームの謎
.. :author: Anonymous User
.. :date: 2010-09-21 09:52:43
.. :email: 
.. :url: 
.. :body:
.. クロージャの話ですよね？
.. 
.. :comments:
.. :comment id: 2010-09-21.5669440367
.. :title: Re:クロージャの話ですよね？
.. :author: しみずかわ
.. :date: 2010-09-21 09:56:07
.. :email: 
.. :url: 
.. :body:
.. クロージャの話です。クロージャの話だと言うことをatsuoishimotoさんに指摘されて理解しました＞＜
.. 

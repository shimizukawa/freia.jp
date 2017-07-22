:date: 2017-03-19 23:55
:tags: Python

===================================================================================
2017/03/19 Python3.6のdictキー順維持と、hash randomizeによるDoS回避の関係について
===================================================================================

.. note::  `3/20 修正`_ で、DDoS -> DoS に修正しました


Python-3.3で導入された、Hash Randomizeについて間違って理解していたようなので、考えを整理してそれの理解が正しいかTeratailに質問をしたところ、的確な回答をもらえて解決できました。

`Python - Python3.6でのdictのキー順維持と、hash randomizeによるDDoS回避の関係について(69286)｜teratail`_

（Teratailで質問したいと思えることが今までなくて、今回やっと質問できました。Q&Aサイトで質問すると流れずに残るのが良いですね）

.. contents::
   :local:


Python3.6でのdictのキー順維持と、hash randomizeによるDDoS回避の関係について
============================================================================

.. note:: 質問サイトにDDoSって書いちゃったのでそのまま引用しますが、実際には **DoS** です

以下、質問を引用します。

   **前提**

   Pythonは以前からdictのキーの順番は不定、とされてきました。
   しかし、見た目上は何らかの固定の順番でdictのキーを取り出せていました。（不定だけど一定） **--(A)**

   Python3.3では、 `hash randomizeが導入されました`_ 。
   導入された目的は、 `object.__hash__のドキュメント`_ に書いてあったので以下に引用します::

   > この目的は、慎重に選ばれた入力で辞書挿入の最悪性能 O(n^2) 計算量を悪用することで引き起こされるサービス妨害 (denial-of-service, DoS) に対する保護です。 詳細は http://www.ocert.org/advisories/ocert-2011-003.html を参照してください。

   この導入によって、dictのキーの順番がインタプリタ起動毎に不定になりました。 **--(B)**

   そしてPython3.6でdictの実装が変わり、dictが省メモリになり、キーの順番が維持されるようになりました。 ref: `Python 3.6 の（個人的に）注目の変更点 - methaneのブログ`_ **--(C)**

   **検証したこと**

   Python\ **2.7.13** で文字列のhash値を取得(**(B)** の確認)::

      $ python2.7 -c "print(hex(hash('abc')))"
      0x142a6050a093d0a3
      $ python2.7 -c "print(hex(hash('abc')))"
      0x142a6050a093d0a3
      $ python2.7 -c "print(hex(hash('abc')))"
      0x142a6050a093d0a3


   Python\ **3.5.2** で文字列のhash値を取得(**(B)** の確認)::

      $ python3.5 -c "print(hex(hash('abc')))"
      0x53a97f418e279642
      $ python3.5 -c "print(hex(hash('abc')))"
      -0x745a06d34cd5d4ed
      $ python3.5 -c "print(hex(hash('abc')))"
      0x29736bbb038652f5

   Python\ **3.6.0** で文字列のhash値を取得(**(B)** の確認)::

      $ python3.6 -c "print(hex(hash('abc')))"
      0x11108253ed4a023b
      $ python3.6 -c "print(hex(hash('abc')))"
      -0x5dc778080cb917cd
      $ python3.6 -c "print(hex(hash('abc')))"
      -0x687164debf8ee240

   Python\ **2.7.13** で辞書のキー順を取得(**(A)** の確認)::

      $ python2.7 -c "print(list(dict.fromkeys(list('abcdefg'))))"
      ['a', 'c', 'b', 'e', 'd', 'g', 'f']
      $ python2.7 -c "print(list(dict.fromkeys(list('abcdefg'))))"
      ['a', 'c', 'b', 'e', 'd', 'g', 'f']
      $ python2.7 -c "print(list(dict.fromkeys(list('abcdefg'))))"
      ['a', 'c', 'b', 'e', 'd', 'g', 'f']


   Python\ **3.5.2** で辞書のキー順を取得(**(B)** の確認)::

      $ python3.5 -c "print(list(dict.fromkeys(list('abcdefg'))))"
      ['e', 'd', 'f', 'a', 'b', 'c', 'g']
      $ python3.5 -c "print(list(dict.fromkeys(list('abcdefg'))))"
      ['e', 'f', 'g', 'b', 'a', 'c', 'd']
      $ python3.5 -c "print(list(dict.fromkeys(list('abcdefg'))))"
      ['d', 'e', 'a', 'g', 'b', 'f', 'c']

   Python\ **3.6.0** で辞書のキー順を取得(**(C)** の確認)::

      $ python3.6 -c "print(list(dict.fromkeys(list('abcdefg'))))"
      ['a', 'b', 'c', 'd', 'e', 'f', 'g']
      $ python3.6 -c "print(list(dict.fromkeys(list('abcdefg'))))"
      ['a', 'b', 'c', 'd', 'e', 'f', 'g']
      $ python3.6 -c "print(list(dict.fromkeys(list('abcdefg'))))"
      ['a', 'b', 'c', 'd', 'e', 'f', 'g']


   **質問**

   Python3.6では、セキュリティ上安全で、これまでOrderedDictを使っていたプログラムをdictで一部置き換え可能と考えてよいでしょうか？
   複数の要素が絡み合っていそうなので、質問を以下の3つに分けます。

   1. **(B)** で、DDoS回避のためにdictキー順をランダム化したかった訳ではなく、 `object.__hash__` がランダム化された副作用でdictキー順が起動毎にランダムになった、という理解であってますか？

   2. Python3.6未満でも、 `PYTHONHASHSEED環境変数`_ を指定すれば、起動毎には変化しない以前の挙動を復活させる方法がありますが、これをやるとDDoS回避の実装を無効化することになるという理解であってますか？

   3. **(C)** で、dictのキー順が維持されるようになりましたが、これはキー順が `object.__hash__` の結果に依存しなくなった、という理解で合っていますか？ `DSAS開発者の部屋:Python に現在実装中の Compact dict の紹介`_ からそのように読み解きました。



質問1にあるように、当初「DoS回避のためにdictキー順をランダム化したかった」のだと理解していましたが、そうではなかった、というのが回答をもらって確認できました。

回答全文は質問したサイト(teratail)で確認できます。 https://teratail.com/questions/69286#reply-109601
ここでは、教えてもらったリンクについてちょっとだけ紹介します。

python - Why is the order in dictionaries and sets arbitrary? - Stack Overflow
=====================================================================================

`Why is the order in dictionaries and sets arbitrary?`_ での質問は、なぜdictとsetのキー順が不定なのか？というものです。
その回答がとても丁寧で分かりやすく書かれていました。

hashの仕組みが実際にどのようにPythonのdictに対して作用しているかを実際のコードを通して説明しています。
実際のコードの部分を自分でもPython3.5でやってみました。

まず、'foo', 'bar', 'baz' の3つの文字列それぞれのhash値を確認します。 

.. code-block:: pycon

   >>> hash('foo')
   4779196005625627760
   >>> hash('bar')
   -7134697388611392496
   >>> hash('baz')
   -5250136657472905660

上記の数値を8で割ったあまりは以下のようになります（Python3.5のhashテーブルサイズは初期は8、という前提がありそうです（未確認））

.. code-block:: pycon

   >>> hash('foo') % 8
   0
   >>> hash('bar') % 8
   0
   >>> hash('baz') % 8
   4

これを見ると、'foo'と'bar'は8の剰余(mod 8)が0で一緒です。つまりhashテーブルが8つの状況では'foo'と'bar'とでhash collisionが発生していることになります。
StackOverflowの回答には、CPythonでの実装はオープンアドレス法だと書かれているので、hash collisionが起きた場合、hashテーブルの当該エントリは早い者勝ちで決まり、collisionを起こしたキーは次のテーブルの空きを探して再計算されます。
（collisionによる再計算が大量に発生すると計算負荷が上がってDoSが可能になります）

実際にPythonの辞書のキー順でみてみます。まず、mod 8が異なる'foo'と'baz'で確認します。

.. code-block:: pycon

   >>> {'foo': None, 'baz': None}
   {'foo': None, 'baz': None}
   >>> {'baz': None, 'foo': None}
   {'foo': None, 'baz': None}

dict定義としてfooとbazの順番を変えて2パターン書いてみましたが、結果は常にfooが先に表示されました。
（mod 8の値が小さい順に並んでいるという訳ではなさそうです）

次に、mod 8が同じ、'foo'と'bar'で確認します。

.. code-block:: pycon

   >>> {'foo': None, 'bar': None}
   {'foo': None, 'bar': None}
   >>> {'bar': None, 'foo': None}
   {'bar': None, 'foo': None}

先ほどのfoo,bazと異なり、今回は定義した順に表示されました。

'foo'と'baz'の場合、fooが常に先にきたのは ``hash('foo')  % 8`` が0で ``hash('baz') % 8`` の4よりも小さいから、・・・ということではなさそうです。実際に mod 8 の結果が異なる8つのキーで試してみました::

   >>> import string
   >>> d = dict(zip([hash(c)%8 for c in string.ascii_letters], string.ascii_letters))
   >>> d
   {0: 'X', 1: 'R', 2: 'Y', 3: 'U', 4: 'N', 5: 't', 6: 'Z', 7: 'S'}
   >>> dict([(v,k) for k, v in d.items()])
   {'X': 0, 'Y': 2, 'Z': 6, 'R': 1, 'U': 3, 'N': 4, 't': 5, 'S': 7}

なるほどー。

なおPython3.6では、辞書のキー順を維持するので、hash値がどうであっても結果は固定化されます。

まとめ
=======

teratailで回答をもらったことと、上記のStackOverflowの回答を読んだことで、自分の理解は次ようになりました。


1. `object.__hash__` のhash collisionによるDoS攻撃を回避するために、Python3.3で起動毎にhashをランダム化した

2. これによって、hashテーブルの順番で並んでいた特定のdictキー列も、起動毎にランダム化された（副作用）

3. Python3.6の **CPython実装** で、dictキーを挿入順で維持するキー列をhashテーブルtとは別に持つようになったため、キー順が `object.__hash__` の結果に依存しなくなった（これは1のDoS回避と反しない）

4. Pythonの言語仕様は変わっていないので、dictキーを挿入順で維持するかどうかはPython実装に依存している


.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/python3?src=hash">#python3</a>.6 news:  OrderedDict is dead. Long live dicts that are ordered.<br>Regular dicts are ordered and more compact: <a href="https://t.co/du4P4M4LFN">https://t.co/du4P4M4LFN</a></p>&mdash; Raymond Hettinger (@raymondh) <a href="https://twitter.com/raymondh/status/773978885092323328">2016年9月8日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Pythonコアデベロッパーが **"OrdereDictは死んだ"** って言ってるけど、CPython3.6以外だとやっぱりOrderedDict使わなきゃだめなんじゃね？


.. _Python - Python3.6でのdictのキー順維持と、hash randomizeによるDDoS回避の関係について(69286)｜teratail: https://teratail.com/questions/69286?sip=n0070000_019&uid=36122
.. _hash randomizeが導入されました: https://docs.python.jp/3/whatsnew/3.3.html#builtin-functions-and-types
.. _object.__hash__のドキュメント: https://docs.python.jp/3/reference/datamodel.html#object.__hash__
.. _Python 3.6 の（個人的に）注目の変更点 - methaneのブログ: http://methane.hatenablog.jp/entry/2016-09-12/Python3.6b1
.. _PYTHONHASHSEED環境変数: https://docs.python.jp/3/using/cmdline.html#envvar-PYTHONHASHSEED
.. _`DSAS開発者の部屋:Python に現在実装中の Compact dict の紹介`: http://dsas.blog.klab.org/archives/python-compact-dict.html
.. _Why is the order in dictionaries and sets arbitrary?: http://stackoverflow.com/questions/15479928/why-is-the-order-in-dictionaries-and-sets-arbitrary


3/20 修正
==============

@methane からツッコミをもらいました。ありがとうございます！

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/shimizukawa">@shimizukawa</a> まず、hashdosはDDoSじゃなくて単なるDoSですね。少数のリクエストで攻撃できるので。<br>（もちろん分散させてもいいですが。）</p>&mdash; INADA Naoki (@methane) <a href="https://twitter.com/methane/status/843623765393125376">2017年3月20日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

はい。 分散(Distributed)じゃなくても攻撃できるということで、DDoSじゃなくてDoSでした。

----------------------------------

.. raw:: html

   <blockquote class="twitter-tweet" data-conversation="none" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/shimizukawa">@shimizukawa</a> あと、他のPython実装が効率やスレッド対応のために別の方法でdict実装できるように、言語仕様としてはキーワード引数と名前空間だけが順序維持でそれ以外は不定です。</p>&mdash; INADA Naoki (@methane) <a href="https://twitter.com/methane/status/843624796038422528">2017年3月20日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

「言語仕様としてはキーワード引数と名前空間だけが順序維持」

キーワード引数の順序維持

.. code-block:: python

   > docker run -it --rm python:3.5.2
   Python 3.5.2 (default, Aug 31 2016, 03:01:41)
   [GCC 4.9.2] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> def func(**kwargs):
   ...     return kwargs
   ...
   >>> func(a=1, b=2, c=3)
   {'c': 3, 'b': 2, 'a': 1}

3.5まではキーワード引数は順序が不定(hash値依存)だった。

.. code-block:: python

   > docker run -it --rm python:3.6
   Python 3.6.0 (default, Jan 18 2017, 02:51:38)
   [GCC 4.9.2] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> def func(**kwargs):
   ...     return kwargs
   ...
   >>> func(a=1, b=2, c=3)
   {'a': 1, 'b': 2, 'c': 3}

3.6では言語仕様として、キーワード引数の順序が維持される。

---------------------

言語仕様で保障される、Python名前空間の順序維持

.. code-block:: python

   > docker run -it --rm python:3.5.2
   Python 3.5.2 (default, Aug 31 2016, 03:01:41)
   [GCC 4.9.2] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> class C:
   ...     a = 1
   ...     b = 2
   ...     c = 3
   ...
   >>> C.__dict__.keys()
   dict_keys(['__dict__', '__doc__', 'b', 'c', '__module__', 'a', '__weakref__'])

3.5までは名前空間（この例ではクラス属性）の順序が不定(hash値依存)だった。

.. code-block:: python

   > docker run -it --rm python:3.6
   Python 3.6.0 (default, Jan 18 2017, 02:51:38)
   [GCC 4.9.2] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> class C:
   ...     a = 1
   ...     b = 2
   ...     c = 3
   ...
   >>> C.__dict__.keys()
   dict_keys(['__module__', 'a', 'b', 'c', '__dict__', '__weakref__', '__doc__'])

3.6では言語仕様として、名前空間の順序が維持される。

モジュールの場合も同様.

3.5の場合::

   > docker run -it --rm python:3.5.2 python -c "import os; print(list(os.__dict__.keys())[-5:])"
   ['ttyname', 'system', 'minor', 'read', '_Environ']
   > docker run -it --rm python:3.5.2 python -c "import os; print(list(os.__dict__.keys())[-5:])"
   ['SEEK_HOLE', 'O_NOCTTY', 'umask', 'fchdir', 'SCHED_OTHER']

3.6の場合::

   > docker run -it --rm python:3.6 python -c "import os; print(list(os.__dict__.keys())[-5:])"
   ['popen', '_wrap_close', 'fdopen', '_fspath', 'PathLike']
   > docker run -it --rm python:3.6 python -c "import os; print(list(os.__dict__.keys())[-5:])"
   ['popen', '_wrap_close', 'fdopen', '_fspath', 'PathLike']



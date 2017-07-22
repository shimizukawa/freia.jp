:date: 2011-04-23 16:00:00
:categories: ['python']
:body type: text/x-rst

=======================================================
2011/04/23 pyreadline を2to3でPython2/3両対応にするメモ
=======================================================

`(第7回)Python mini Hack-a-thon`_ 午後の部の成果です。

.. _`(第7回)Python mini Hack-a-thon`: http://atnd.org/events/14178

`Python 2からPython 3への移行 - YAMAGUCHI::weblog`_ を読みながら、python readline のWindows用パッケージ pyreadline_ を2to3を使ってPyhton2,3両対応にしてみました。


Python3対応メモ
-----------------

`2to3` 変換は ``python32 c:\Develop\Python32\Tools\Scripts\2to3.py -w --no-diffs target_dir`` という感じで実行。バックアップファイルが要らない場合は `-wn` みたいにオプションに n を付ける。

あとはひたすら Python2 でのテスト実行と 2to3.py での変換、Python3 でのテスト実行を繰り返す感じ。


以下、はまったところをメモ。

ctypes でwin32関数を取得出来なくなった
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pyreadlineはWindowsで動作するために、Python本体が持っているHook関数のポインタを取得してゴニョゴニョしている。そのために以下のようにして関数ポインタを取得していた(Python2):

.. code-block:: python

    import sys
    from ctypes import windll
    handler = windll.kernel32.GetProcAddress(
                    sys.dllhandle,
                    "PyOS_ReadlineFunctionPointer")

でもこれだとPython3では動作しなくて、PyOS_ReadlineFunctionPointer と言う名前が変わったのか？とか思ってPython2と3のソースコード(C言語)を読んだり、ctypesの仕様が変わった？とか色々やってみて、最終的には以下のようにしたら動作した(Python3):

.. code-block:: python

    import sys
    from ctypes import windll
    handler = windll.kernel32.GetProcAddress(
                    sys.dllhandle,
                    b"PyOS_ReadlineFunctionPointer")

文字列の頭に ``b`` 付けただけ。あ゛ー、自動変換とか便利なものはPython3には無いんだっけなー‥


Python3でbytesになって欲しい文字列をPython2.5未満で表現出来ない
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python3では ``b'spam'`` となって欲しい文字列があったとして、Python2.6であれば素直に b'spam' と書いておけば `2to3.py` で変換した後も b'spam' が維持される。

変換前(`Python2.6`):

.. code-block:: python

    spam = b'spam'
    ham = u'ham'
    egg = 'egg'

2to3変換後(`Python3.2`):

.. code-block:: python

    spam = b'spam'
    ham = 'ham'
    egg = 'egg'


しかし、Python2.6未満もサポートしているパッケージの場合、Python2.6未満では b'spam' とは書けないのでこの方法が使えない。どうするか？

変換前(`Python2.4`):

.. code-block:: python

    spam = 'spam'.encode('latin-1')
    ham = u'ham'
    egg = 'egg'

2to3変換後(`Python3.2`):

.. code-block:: python

    spam = 'spam'.encode('latin-1')
    ham = 'ham'
    egg = 'egg'

なんだかなー...

もう少しマシな方法としては `@mopemope`_ さんにアドバイス `(1)`_, `(2)`_ をもらった six_ の実装をまねて以下のように書くくらいか。

以下のコードをどこかに実装しておいて...

.. code-block:: python

    import sys
    PY3 = (sys.version_info >= (3, 0))

    if PY3:
        b = lambda s: s.encode('latin-1')
        u = lambda s: s
    else:
        b = lambda s: s
        u = lambda s: unicode(s, "unicode_escape")

変換前(`Python2.4`):

.. code-block:: python

    spam = b('spam')
    ham = u'ham'
    egg = 'egg'

2to3変換後(`Python3.2`):

.. code-block:: python

    spam = b('spam')
    ham = 'ham'
    egg = 'egg'


文字列から1文字ずつ取り出す処理をbytesに行うと"文字は取り出されない
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pyreadline はPythonのInteractiveShell上でカーソル移動や編集を行う関係上、外界と内界の境界上で str / unicode 変換 (Python3なら bytes / str 変換)を行う必要があるし、カーソル位置やなんかを保持したりいじったりする。

そんな処理の一部にこんなコードがあった(Python2):

.. code-block:: python

    for c in text:
        self.line_buffer[self.point] = c
        self.point += 1
    ...
    line = ''.join.(self.line_buffer)

これはPython2時代なら文字列を1文字ずつ取り出して配列に突っ込んでいく処理なので、コードの文脈を無視して書き換えると以下のような処理をやっている(`Python2`):

.. code-block:: python

    >>> text = b('spam')
    >>> buffer = [c for c in text]
    >>> buffer
    ['s', 'p', 'a', 'm']
    >>> line = ''.join.(buffer)
    >>> line
    'spam'

これを `Python3` に置き換えて実行すると...

.. code-block:: python

    >>> text = b'spam'
    >>> buffer = [c for c in text]
    >>> buffer
    [115, 112, 97, 109]
    >>> line = b''.join.(buffer)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: sequence item 0: expected bytes, int found

buffer はintの配列なので b'' でjoinすることは出来ません、という事になってしまった。じゃあbytesに対して1文字ずつ処理するにはどうすれば良いのか‥ Python3.2のリファレンスを読んでも分からなかったので `@atsuoishimoto`_ 先生に助けを求めてみたところ、bytesはintの配列だから動作としては正しい、という趣旨のコメントを頂いた。うーん、、、 残念ながら標準的な解決法は今のところ無さそう。

intの配列から **文字列を** 取り出そうという考え方が良くないのかもしれないけど、2to3.pyでやろうとしている以上なんとかしないといけないので、以下のような互換レイヤーを挟んで解決を図ってみた。

.. code-block:: python

    def biter(text):
        if PY3 and isinstance(text, bytes):
            return (s.to_bytes(1,'big') for s in text)
        else:
            return iter(text)

``s.to_bytes`` が気持ち悪いけどまあ仕方が無いということで。これでこんな感じに動くようになった。

`Python2` で実行:

.. code-block:: python

    >>> text = b('spam')
    >>> [c for c in biter(text)]
    ['s', 'p', 'a', 'm']

`Python3` で実行:

.. code-block:: python

    >>> text = b'spam'
    >>> [c for c in biter(text)]
    [b's', b'p', b'a', b'm']


とりあえず今日のまとめ
-----------------------
感想

* pyreadlineはsyntaxやモジュールの両対応は比較的簡単だった
* pyreadlineはコンソール操作を扱うので str / unicode / bytes 変換が多くて地獄

成果

* 実装コード: https://code.launchpad.net/~shimizukawa/pyreadline/python3
* 本家へのmergeリクエスト: https://code.launchpad.net/~shimizukawa/pyreadline/python3/+merge/57057

使い方

* `Python 2からPython 3への移行 - YAMAGUCHI::weblog`_ に書かれている方法でsetup.pyを調整してあるので、前述のlaunchpadからコードを取得して、 ``python setup.py install`` でPython2/3どちらでもインストール出来ます。


.. _`Python 2からPython 3への移行 - YAMAGUCHI::weblog`: http://d.hatena.ne.jp/ymotongpoo/20110406/1302061408

.. _pyreadline: http://pypi.python.org/pypi/pyreadline

.. _`@atsuoishimoto`: http://twitter.com/atsuoishimoto

.. _`@mopemope`: http://twitter.com/mopemope
.. _`(1)`: http://twitter.com/#!/mopemope/statuses/61236397843025921
.. _`(2)`: http://twitter.com/#!/mopemope/statuses/61237191485034496

.. _six: http://pypi.python.org./pypi/six


.. :extend type: text/x-rst
.. :extend:


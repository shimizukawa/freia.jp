DocTest Quickstart
===================

はじめのいっぽ
---------------

まずはDocTestの環境を作ります。以下のコードを code1.py というファイルに
文字コード utf-8 で保存して下さい。

::

    # -*- coding: utf-8 -*-

    def add(x, y):
        """
        関数 :func:`add` は引数2つをうけとり足した値を返します。

            >>> add(1, 2)
            3

        """

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

DocTestの核となるのは上記の """ """ で囲われた数行の部分です。これは
``docstring`` と呼ばれるPythonの記法で、モジュールヘルプや関数ヘルプとして
解釈され、上記の例では add.__doc__ に保持されます。

DocTestを書くには、上記のように日本語のような自然言語で書かれた「説明文」
と、Pythonのインタラクティブシェルでの入出力を貼り付けたような「対話コード」
をインデントや空行などで見分けが付くように ``docstring`` に記述します。
これをDocTestが認識して、対話コード部分のみを実行して、その結果が期待した
とおりの値かどうかをチェックします。上記の例では、 ``add(1, 2)``
が実行され、同じ事をインタラクティブシェルで行ったら ``3`` と表示される
ことが期待されています。

参考までに、同じ事をUnitTestで書くと以下のようになります::

    class AddTestCase(unittest.TestCase):

        def test_add(self):
            self.assertEqual(add(1, 2), 3)


ところで ``doctest.testmod()`` は自分自身のモジュール内（ファイル内）の
docstringを探してDocTestとして実行する関数です。

テストの実行は以下のように行います。

.. code-block:: bash

    $ python code1.py

うまく実行されると何も表示されずにプログラムは終了します。
本当に正しく実行されているか確認するために、verboseオプションを付けて
もう一度実行してみましょう。

.. code-block:: bash

    $ python code1.py -v
    Trying:
        add(1, 2)
    Expecting:
        3
    ok
    1 items had no tests:
        __main__
    1 items passed all tests:
       1 tests in __main__.add
    1 tests in 2 items.
    1 passed and 0 failed.
    Test passed.

テストがちゃんと実行されていることが分かりました。

DocTestはそのままへプルになる
------------------------------
ところでDocTestを書いている領域は本来であれば関数などの説明文を書くところ
です。と言うことは以下のようにしてヘルプとして表示することができます。

::

    $ python
    >>> import code1
    >>> help(code1.add)
    Help on function add in module code1:

    add(x, y)
        関数 :func:`add` は引数2つをうけとり足した値を返します。

            >>> add(1, 2)
            3

.. note::
    code1.pyをutf-8で書いたため、コンソールがutf-8でないと文字化けします。


また、この例では \:func:\`add\` のようにreStructureingTextという記法を
一部利用しています（ちょっと無理矢理な例ですが...）。
このように書いておくと、別途Sphinxで自動的に関数リファレンスマニュアル
を作る事が出来たりもします。


失敗する例
------------

では、わざと失敗するようなテストコードを追加してみます::

    def add(x, y):
        """
        関数 :func:`add` は引数2つをうけとり足した値を返します。

            >>> add(1, 2)
            3

        数値以外にも文字列も足すことが出来ます。

            >>> add('foo', 'bar')
            'foobar'

        """

これを実行すると以下のように当然エラーになります。

.. code-block:: bash

    $ python code1.py
    **********************************************************************
    File "code1.py", line 12, in __main__.add
    Failed example:
        add('foo', 'bar')
    Expected:
        'foobar'
    Got:
        3
    **********************************************************************
    1 items had failures:
       1 of   2 in __main__.add
    ***Test Failed*** 1 failures.

-vを付けなくても、エラーの場合にはこのようにコンソールにエラー箇所が表示
されます。この内容を読んでみると、 ``'foobar'`` を期待したのに ``3`` が
返されたため期待と異なっていることが分かります。そのエラー箇所は code1.py
の12行目にある __main__.add 関数内です。

課題
-----

1. エラーが起きないようにadd関数の実装を修正して下さい

2. 以下のコードはエラーになります::

       >>> from datetime import date
       >>> today = date(2011,11,13)
       >>> tomorrow = today + 1

   上記が動作するような date を継承したクラス DateEx を実装してください。
   日付の計算には datetime.timedelta を使用してもかまいません。
   + 演算子の動作を実装するには __add__ メソッドをクラスに実装します。
   ただし、実装する際にDocTestで動作を確認して下さい。

3. DocTestのどういった点が良いと思ったかを3つ書いてください。書き方や書きやすさ
   の他にUnitTest(unittest.TestCaseでのテスト)との比較など何でもかまいません。

4. 同様に、DocTestの使いにくいと思った点を3つ書いてください。


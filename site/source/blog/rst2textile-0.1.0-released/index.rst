:date: 2012-04-24 23:00:00
:tags: Python, docutils, textile, rst2textile

======================================================
2012/04/24 rst2textile-0.1.0 リリースと実装の裏話
======================================================

先日 `Sphinx + 翻訳 Hack-a-thon 2012.04`_ にて `rst2textile-0.1.0`_ をリリースしました。

rst2textileの紹介
==================

rst2textileは ``reStructuredText`` 形式のテキストを ``textile`` 形式に変換するためのツールです。例えば以下のように変換することが出来ます。

元になるsample.rstファイル:

.. literalinclude:: sample.rst
   :language: rst

以下のコマンドで変換実行:

.. code-block:: bash

   $ rst2textile.py sample.rst sample.txt


出力されたsample.txtファイル:

.. literalinclude:: sample.txt
   :language: textile


このrst2textileパッケージは内部にdocutils_textileというdocutilsのwriter実装を持っています。rstファイルをパースして中間形式のノードツリーにするところまではdocutilsがやってくれるので、docutils_textileが実装するべきことはそれほど難しくありません。 :doc:`../docutils-pseudo-xml/index` で紹介した方法でノードツリーの構造を確認しながら実装を進めていきます。ただこれがけっこう時間がかかります。textileのフォーマットに一つずつ対応していくので、ひたすら手がかかります。

そこで楽しく実装できるように、余計なこと...工夫をしてみました。

Distutils2でパッケージング
============================

パッケージを作成するためにDistutils2のpysetupコマンドを使ってsetup.cfgを作成し、後方互換性のためにsetup.pyも生成しました。

pysetupは :doc:`../distutils2-setup-cfg-interactive-creating/index` で紹介したように、以下のように実行しています。

.. code-block:: bash

   $ pysetup create
   (対話形式で入力、 setup.cfgが生成される)

   $ pysetup generate-setup
   (setup.pyが生成される)

その後、いくつかのDistutils2のバグに悩みながらsetup.pyをsetuptools対応に書き換えたり、一部のUnicode文字列をstrにencodeするようコードを書き換えたりしました。こういった課題がクリアされればパッケージングはかなり楽になると思いますが、今の Distutils2-1.0a4 ではまだ厳しいですね。みんなでバグレポート出して改善しましょう。

一応、rst2textileは setup.py / setup.cfg とも調整してあるので、以下のどちらでもインストール可能です。

pip::

   $ pip install rst2textile

pysetup::

   $ pysetup install rst2textile


README.rstにテスト可能な変換サンプルを用意
===========================================

README.rst にrst2textileの変換例として、以下のように記載しています。

.. code-block:: rst

   List items
   -----------
   .. container:: test, rst, textile

      rst::

         - An item in a bulleted (unordered) list

         - Another item in a bulleted list

           - Second Level

           * Second Level Items

             * Third level

      textile::

         * An item in a bulleted (unordered) list
         * Another item in a bulleted list
         ** Second Level
         ** Second Level Items
         *** Third level


この記述はテスト出来るように、docutils標準の containerディレクティブでマーキングしてあって、test.pyの中でこのcontainerノードを見つけてテストするようにしてあります。もし実装に間違いがある状態で実行すると、実行結果は以下のようになります。

.. code-block:: bash

   $ python test.py
   ......F......
   ======================================================================
   FAIL: runTest (__main__.ReSTTestCase)
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "test.py", line 42, in runTest
       self.assertEqual(self.expect, self.actual, message)
   AssertionError: Convertion Mismatch (rst -> docutils_textile)
   ##source:
   - An item in a bulleted (unordered) list

   - Another item in a bulleted list

     - Second Level

     * Second Level Items

       * Third level

   ##expect:
   * An item in a bulleted (unordered) list
   * Another item in a bulleted list
   ** Second Level
   ** Second Level Items
   *** Third level

   ##actual:
   * An item in a bulleted (unordered) list
   * Another item in a bulleted list
    * Second Level
    * Second Level Items
     * Third level

   ##node-tree:
   <document source="<string>">
       <bullet_list bullet="-">
           <list_item>
               <paragraph>
                   An item in a bulleted (unordered) list
           <list_item>
               <paragraph>
                   Another item in a bulleted list
               <bullet_list bullet="-">
                   <list_item>
                       <paragraph>
                           Second Level
               <bullet_list bullet="*">
                   <list_item>
                       <paragraph>
                           Second Level Items
                       <bullet_list bullet="*">
                           <list_item>
                               <paragraph>
                                   Third level


   ----------------------------------------------------------------------
   Ran 13 tests in 0.004s

   FAILED (failures=1)
   $


上記のように「source(入力)」「expect(期待)」「actual(実際)」「node-tree(疑似XML)」といった実装修正の手がかりを全て表示してくれます。この仕組みを用意するためにdocutilsのコードをけっこう読む羽目になりましたが、それ以降は実装がかなり楽になりました。

test.pyがどのように実装されているかについては https://bitbucket.org/shimizukawa/rst2textile/src/tip/test.py を参照して下さい。

テストとして見ると無駄に努力していますが、以下のようなことをやりたくてこの仕組みを用意しました。

* README.rst で変換サンプルを提示したい
* 変換サンプルはテキストのままでも読みたい(自動生成したくない)
* 実装時にnode-treeのpseudoxml出力が欲しい
* docutils標準外のdirective等は使用したくない(PyPI公開のため)
* 以下のフローで実装を進めたい

  1. フォーマット対応の対象とする rst, textile の対を README.rst に書く
  2. `python test.py` を実行してactualとnode-treeを確認する
  3. docutils_textileのwriter実装を行う
  4. テストが通るまで2,3を繰り返す
  5. リリースではサンプルとしてREADME.rstをそのまま利用する

上記フローならtextile仕様把握後にnode-treeを確認しながら実装できて楽だし、サンプルと実装とテストが乖離しないのでメンテも楽かなと思います。あくまで壊れてないサンプルを提示するのが主体なので、この方式上でフォーマットの組み合わせを細かくとかは考えない方向で。

まとめ
========

rst2textileって、自分は使う予定があんまりないので、今対応してないフォーマット部分は要望次第で実装ということにしたいなあ。


.. _`Sphinx + 翻訳 Hack-a-thon 2012.04`: http://connpass.com/event/379/
.. _`rst2textile-0.1.0`: http://pypi.python.org/pypi/rst2textile/0.1.0

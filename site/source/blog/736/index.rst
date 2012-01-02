:date: 2010-09-20 17:00:00
:categories: ['python', 'testing', 'epp']
:body type: text/x-rst

==============================================================
Pythonのコーディング規約pep8チェックをUnitTestに組み込んでみた
==============================================================

Pythonには PEP_ という仕組みがあり、そのなかの `PEP-0008`_ がPythonのコードを書く上でのコーディング規約を定義しています。

.. _PEP: http://sphinx-users.jp/articles/pep1.html
.. _`PEP-0008`: http://oldriver.org/python/pep-0008j.html

で、このPEP8の規約通りに書けているかどうかをチェックするツールがいくつか PyPI_ で公開されているので、それをUnitTestに組み込んでみたら良いんじゃない？と言うわけでさっそく組み込んでみました。今回はテストに組み込むパッケージとして、 `エキスパートPythonプログラミング`_ でも軽く紹介されている pep8_ というパッケージを選んでみました。

.. _PyPI: http://pypi.python.org/pypi/
.. _pep8: http://pypi.python.org/pypi/pep8/
.. _`エキスパートPythonプログラミング`: http://astore.amazon.co.jp/freiaweb-22/detail/4048686291

以下のように test_pep8.py を作成しました。このテストはnoseで動作するように書いています。

.. code-block:: python

    # -*- coding: utf-8 -*-

    import os
    import pep8

    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.dirname(CURRENT_DIR)


    def test_pep8():
        arglist = [
            '--statistics',
            '--filename=*.py',
            '--show-source',
            '--repeat',
            #'--show-pep8',
            #'-qq',
            #'-v',
            BASE_DIR,
        ]

        options, args = pep8.process_options(arglist)
        runner = pep8.input_file

        for path in args:
            if os.path.isdir(path):
                pep8.input_dir(path, runner=runner)
            elif not pep8.excluded(path):
                options.counters['files'] += 1
                runner(path)

        pep8.print_statistics()
        errors = pep8.get_count('E')
        warnings = pep8.get_count('W')
        message = 'pep8: %d errors / %d warnings' % (errors, warnings)
        print message
        assert errors + warnings == 0, message

これをテスト対象のファイル群があるディレクトリ下のtestsディレクトリに置いてテストを実行すると以下のように結果が出力されます。

::

    $ test
    F
    ======================================================================
    FAIL: test_pep8.test_pep8
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    ...
    ...
    ...
    AssertionError: pep8 test detect 2 errors / 2 warnings
    -------------------- >> begin captured stdout << ---------------------
    ./somepkg/__init__.py:4:1: W391 blank line at end of file
    
    ^
    ./somepkg/somepkg.py:30:37: W602 deprecated form of raising exception
                    raise AttributeError, msg
                                        ^
    ./somepkg/parser.py:18:11: E401 multiple imports onone line
    import sys, os
              ^
    ./somepkg/parser.py:131:24: E211 whitespace before
    '('
            elif isinstance (x, Pair):
                           ^
    ./somepkg/parser.py:177:1: W391 blank line at end of file
    
    ^
    1       E211 whitespace before '('
    1       E401 multiple imports on one line
    1       W391 blank line at end of file
    1       W602 deprecated form of raising exception
    pep8: 2 errors / 2 warnings

    --------------------- >> end captured stdout << ----------------------

    ----------------------------------------------------------------------
    Ran 1 test in 0.512s

    FAILED (failures=1)

これで五月蠅いくらいにPEP8違反を教えてくれるようになります。 **「さいきん結合サーバーに接続したパトランプが回らなくて寂しいな－」という人にお勧め** です。

というか、某プロジェクトに組み込んでみたらかなりの規約違反が検出されてしまって案の定、表示されすぎたので（違反しているのが悪いんですけど）、もっと早くから組み込んでおけば良かったと反省中です…。Python標準のUnitTestに書き換えて使うのも簡単なので、今後の自分のコードにはかならず組み込むようにしようかな。

あわせて読みたい
---------------------

* `テスト自動化 - Python Developers Camp 2008冬 in 松本`_
* `エキスパートPythonプログラミング`_

.. _`テスト自動化 - Python Developers Camp 2008冬 in 松本`: http://www.slideshare.net/shimizukawa/python-autotest-pdc2008w


.. :extend type: text/x-rst
.. :extend:

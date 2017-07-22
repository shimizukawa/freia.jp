:date: 2014-5-25 19:00
:tags: Python, Sphinx
:body type: text/x-rst

============================================================
2014/05/25 Sphinxメンテナ日記: 2to3やめてsixに切り換えました
============================================================

前置き: このエントリを読むと、既存のPython2実装の何かをPython3に移行する時の参考になるかもしれません。前置きおわり。


Sphinx-1.2のPython3対応
========================

Sphinxはバージョン1.1からPython3対応していました。しかしSphinx-1.1と1.2はPython2で書かれていて、インストール時に :ref:`2to3-reference` でコードを変換してPython3で動作させています。
しかし、2to3を使ったためにSphinxの機能以外のところでいくつかの問題が起きていました。

* インストールに時間がかかる

  インストール時に2to3が実行されますが、多くの変換を行うため、対象ソースのコード行数に比例して時間がかかります。
  Sphinx-1.2.2をローカルのソースからインストールした場合:

  * Python2.7: 7 秒
  * Python3.3: 41 秒

* Python3のテスト実行に時間がかかる

  Sphinxはtoxでテストを行っていますが、テスト対象パッケージはテスト毎にvirtualenv環境に再インストールされるため、前述のインストール時間がテスト毎に2回(py32,py33)かかります。

* Python3でのデバッグに手間がかかる

  Python3でのみ発生するバグの修正やPython3の新しいバージョンで動作しない場合、2to3変換後のコードに対して修正を行い、そのように変換されるように2to3変換前のリポジトリのコードを修正する必要があります。
  うまく書けたか確認するために2to3を何度も実行するため、前述の変換コストがかかります。


もちろん、2to3自体はPython2が主流だったこれまでは、Python3にも楽に対応したい場合の道具としてとても役立つ物でしたが、Python3.4もリリースされ `Python3が一般的になってきた`__ 現状では、開発やインストールに時間がかかる2to3は良い選択とは言えなくなりました。


.. __: http://python3wos.appspot.com/

Sphinx-1.3のPython3対応
=========================

Sphinx-1.3は現在開発中ですが、既に2to3を使わない実装に切り替えがほぼ終了しており、Sphinx-1.3からは2to3による変換なしでPython3で動作します。



Sphinxはどのようにして2to3から脱却したか
------------------------------------------

チケット `#1350`_ でいくつかの方法を検討しました。

* six_ を使う
* python-future_ を使う
* ピュアPythonコードで書く

これらのうち、Georgのコメントから、python-futureよりもsixを使う、出来ればsixも無しで実装する、という方針になり、最終的にはsixを使った実装を採用しました。
また、#1350のやりとりを通して、 Pygments_ もシングルソースでの実装に移行し、その結果、Pygments-2.0はPython-2.6, 2.7, Python-3.3+ で動作することになったようです (`PygmentsのCHANGESより`_)。

ちなみに、python-futureは `Comparing future.moves and six.moves`_ の中で「six.movesの実装のためにDjangoのオートリロードや、py2exeやcx_freezeなどのツールで問題がある」という事を指摘しています。Sphinxもsixを採用したことにより、こういった問題に遭遇する可能性はあります。


Sphinxのシングルソース移行
---------------------------

移行は以下の3つのPull Requestで行われました（3つめは現在レビュー中です）。

* `Pull Request #208`_ python-futureの ``futurize --stage1`` によるexcept文やprint文の変換
* `Pull Request #238`_ sixパッケージを採用し、Py2/3で移動したパッケージに対応、bytes/str/unicodeの調整、iterの調整
* `Pull Request #243`_ next()の調整、mapの調整、``ur""`` リテラルの調整、2to3の削除

3つめの `Pull Request #243`_ では、部分的に ``from __future__ import unicode_literals`` を使っていますが、全体的には ``u""`` リテラルを残してあります。
Sphinxで多く利用されている ``u""`` リテラルを ``unicode_literals`` で書き換えるのは多くの手間と気を遣う作業のため、やりませんでした。
しかし、 ``u""`` リテラルが復活したPython-3.3以降でも ``ur""`` リテラルは使用できないため、その部分についてだけunicode_literalsで対処してあります。

ところで、Python3.2では ``u""`` リテラルが使用できません。このため、Sphinx-1.3もPython-3.2では動作しなくなる予定です。

なお、Sphinx-1.2が依存している Pygments_ (Georg作)と snowballstemmer_ (shibu作)もPython-3.2では動作しません。今後はPython-3.2対応はどんどん厳しくなっていきそうですね。


インストール時間の改善
------------------------

Sphinx-1.3のソースからのインストール時間を計ってみました:

* Python2.7: 6 秒
* Python3.3: 6 秒

ところで最近のSphinxはwheelパッケージもリリースしているので、pip-1.5以降を使っていればwheelパッケージでインストールされるので、インストール時間はもっと短かったりします。
wheelがどのくらい速いかについては@aodagによる `pipとwheelでテスト環境構築をスピードアップ`_ が詳しいです。
Sphinxのテストにwheelを活用したらめちゃ速くなりました( https://drone.io/bitbucket.org/shimizukawa/sphinx-py3-native/18 )。@aodag、良い記事をありがとうー。


まとめ
========

* そろそろ 2to3 やめよう
* python-future_ のfuturizeは便利
* six_ と python-future_ どちらが良いか誰か調査して
* ``u""`` リテラルめんどくさい
* Python-3.2 はDropしよう
* wheel速いよ、開発に活用すると良いよ


参考
=====

* `Writing Forwards Compatible Python Code | Armin Ronacher's Thoughts and Writings`_
* `Python 2 から Python 3 への移植 &mdash; Python 3.3.3 ドキュメント`_
* `Language differences and workarounds &mdash; Porting to Python 3 - The Book Site`_
* `Six: Python 2 and 3 Compatibility Library &mdash; six 1.6.1 documentation`_
* https://bitbucket.org/gutworth/six/src/4420499da495/six.py

.. _#1350: https://bitbucket.org/birkenfeld/sphinx/issue/1350/drop-2to3-mechanism
.. _six: https://pypi.python.org/pypi/six
.. _python-future: https://pypi.python.org/pypi/future
.. _PygmentsのCHANGESより: https://bitbucket.org/birkenfeld/pygments-main/src/2ba9b53c/CHANGES#cl-13
.. _Comparing future.moves and six.moves: http://python-future.org/standard_library_imports.html#comparing-future-moves-and-six-moves
.. _Pull Request #208: https://bitbucket.org/birkenfeld/sphinx/pull-request/208/modernize-the-code-now-that-python-25-is
.. _Pull Request #238: https://bitbucket.org/birkenfeld/sphinx/pull-request/238/using-six-package-for-py2-3-compatibility
.. _Pull Request #243: https://bitbucket.org/birkenfeld/sphinx/pull-request/243/native-py2-py3-support-without-2to3-refs/diff
.. _pipとwheelでテスト環境構築をスピードアップ: http://pelican.aodag.jp/20140502-pip-wheel-speedup.html
.. _Pygments: https://pypi.python.org/pypi/Pygments
.. _snowballstemmer: https://pypi.python.org/pypi/snowballstemmer
.. _Writing Forwards Compatible Python Code | Armin Ronacher's Thoughts and Writings: http://lucumr.pocoo.org/2011/1/22/forwards-compatible-python/
.. _Python 2 から Python 3 への移植 &mdash; Python 3.3.3 ドキュメント: http://docs.python.jp/3.3/howto/pyporting.html
.. _Language differences and workarounds &mdash; Porting to Python 3 - The Book Site: http://python3porting.com/differences.html
.. _`Six: Python 2 and 3 Compatibility Library &mdash; six 1.6.1 documentation`: http://pythonhosted.org//six/


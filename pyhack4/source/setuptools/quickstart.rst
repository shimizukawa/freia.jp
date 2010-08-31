setuptools QuickStart
======================

setup.py
---------

てきとーなフォルダを作ってsetup.pyを以下のように作成してください::

   from distutils.core import setup

   setup(
      name='foo',
      version='0.0.1',
   )


次に配布ファイルを作成してみます。まずはソース配布用::

   $ python setup.py sdist

これでdistフォルダに配布ファイルが作成されました。
次にバイナリ配布用::

   $ python setup.py bdist

さきほどと同様にdistフォルダに配布物が作成されました。

しかしこのままではeggを作成する事は出来ません。eggを作成するには
``bdist_egg`` というコマンドが必要ですが、 ``python setup.py --help-commands``
と実行してもbdist_eggというパッケージは表示されません。

そこで先ほどのsetup.pyの先頭を以下のように書き換えます::

   #from distutils.core import setup
   from setuptools import setup


再度 ``python setup.py --help-commands`` を実行すると、先ほどまでは無かった
`Extra commands` という項目以下にいくつかのコマンドが増えています。
その中に ``bdist_egg`` もあるはずです。ということで実行します::

   $ python setup.py bdsit_egg

これでdistフォルダ以下に .egg ファイルが作成されました。




:date: 2011-05-04 16:20:29
:categories: ['python', 'Windows']
:body type: text/x-rst

==============================================
MeCab-0.98 python binding for Windows のビルド
==============================================

Pythonで MeCab_ を使用するには `MecCab-pythonバインディング`_ を使用しますが、バンディングはビルド済みのものが提供されていないので、自分でビルドする必要があります。Linuxや*BSDならそれほどはまらないと思いますが、Windowsではコンパイル環境があってもはまったので、バインディングビルド手順をメモしておきます(完成物はこちら: `mecab-python-0.98-win32-binary-20110504.zip`_)。

.. _MeCab: http://mecab.sourceforge.net/
.. _`MecCab-pythonバインディング`: http://sourceforge.net/projects/mecab/files/mecab-python/0.98/


バインディングをビルドする手順
-------------------------------

この記事で対象にしているバージョン

* Windows7 (95以降共通と思われる)
* Python-2.7
* MeCab-0.98
* mecab-python-0.98.tar.gz
* VisualC++ 2008 Express Edition (無料版)

環境の用意
~~~~~~~~~~~~
Windowsを用意します。そこにPython-2.7, MeCab-0.98, VisualC++ 2008 Express Editionをインストールしておきます。


mecab-python-0.98.tar.gz を展開してsetup.pyを書き換える
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mecab-python-0.98.tar.gz に同梱されているsetup.pyには以下のような行があります::

    version = cmd1("mecab-config --version"),

しかしWindowsではMeCabをインストールしてもmecab-configが無いのでこのままでは動きません。そこで以下のように書き換えます。

`元のsetup.py`::

    #!/usr/bin/env python

    from distutils.core import setup,Extension,os
    import string

    def cmd1(str):
        return os.popen(str).readlines()[0][:-1]

    def cmd2(str):
        return string.split (cmd1(str))

    setup(name = "mecab-python",
        version = cmd1("mecab-config --version"),
        py_modules=["MeCab"],
        ext_modules = [
            Extension("_MeCab",
                ["MeCab_wrap.cxx",],
                include_dirs=cmd2("mecab-config --inc-dir"),
                library_dirs=cmd2("mecab-config --libs-only-L"),
                libraries=cmd2("mecab-config --libs-only-l"))
                ])


`書き換えたsetup.py`::

    #!/usr/bin/env python

    from distutils.core import setup, Extension

    setup(name = "mecab-python",
        version = '0.98',
        py_modules=["MeCab"],
        ext_modules = [
            Extension("_MeCab",
                ["MeCab_wrap.cxx",],
                include_dirs=[r'C:\Develop\Mecab\sdk'],
                library_dirs=[r'C:\Develop\Mecab\sdk'],
                libraries=['libmecab'])
                ])

上記は、MeCabが ``C:\Develop\Mecab\`` にインストールされている場合です。それ以外にインストールしている場合は適宜パスを書き換えて使用してください。

そして ``python setup.py dist`` を実行してビルドします。

.. Topic:: python setup.py
    :class: dos

    | C:> python setup.py build
    | running build
    | running build_py
    | running build_ext
    | building '_MeCab' extension
    | ...
    | build\lib.win32-2.7\_MeCab.pyd : fatal error LNK1120: 外部参照 3 が未解決です

しかし、上記のようにエラーになってしまいます。


python setup.py bdistを実行するとビルドに失敗するのでコードを書き換える
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
既に同じようなbindingをRuby用に作っていた経験から、エラーになる原因はわかっています。そこで、Ruby版と同じように ``MeCab.Tagger.version`` と ``MeCab.Tagger.create`` をあきらめる方向で対策します。

`MeCab_wrap.cxx` の以下の2行を削除かコメントアウトします(5597行あたり)::

    { (char *)"Tagger_create", _wrap_Tagger_create, METH_VARARGS, NULL},
    { (char *)"Tagger_version", _wrap_Tagger_version, METH_VARARGS, NULL},


これでビルドが通るはず。


改めてpython setup.py bdist を実行してMeCab.pydを作成する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
正確には MeCab.py と _MeCab.pyd が作成されます。

.. Topic:: python setup.py
    :class: dos

    | C:> python setup.py bdist
    | ...
    | adding 'Develop\Python27\Lib\site-packages\MeCab.py'
    | adding 'Develop\Python27\Lib\site-packages\_MeCab.pyd'
    | ...
    |
    | C:> dir dist
    | ...
    | 2011/05/04  16:10            27,730 mecab-python-0.98.win32.zip

これでMeCabのPythonバインディングが作成出来ました。
python setup.py bdist の代わりに ``python setup.py install`` とすれば直接使用している環境にインストールすることもできます。

完成物(python2.7, 2.6用)と変更を加えたファイルを公開しておきます。ライセンスなどは元のMeCabのものに従います。egg化とかは要望があれば。

* `mecab-python-0.98-win32-binary-20110504.zip`_

.. _`mecab-python-0.98-win32-binary-20110504.zip`: stuff/mecab-python-0.98-win32-binary-20110504.zip


.. :extend type: text/x-rst
.. :extend:

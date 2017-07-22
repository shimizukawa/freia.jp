:date: 2012-07-24 23:58:00
:tags: python, python3, namespace-package

==========================================================
2012/07/24 Python 3.3b1 の名前空間パッケージを試してみた
==========================================================

*'python', 'python3', 'namespace-package'*

今日会社で `@IanMLewis`_ と話していて、Python3の名前空間パッケージの話になった。自分はてっきり名前空間パッケージは今後業界標準から消えていくのかと思っていたんだけど、実際には `PEP-0420`_ で提案されて Python-3.3 から標準化されている、というのを教えてもらった。 Ian++

.. _`@IanMLewis`: https://twitter.com/IanMLewis
.. _`PEP-0420`: http://www.python.org/dev/peps/pep-0420/

Python2の名前空間パッケージ
=============================

Pythonで名前空間パッケージを使うにはいくつか作法がある。そもそもPythonでディレクトリをimport可能にする(=パッケージにする)には、そのディレクトリに ``__init__.py`` を置く必要がある。中身は空でも良い。

::

   /tmp/
      +-- spam/
      |    +-- __init__.py
      +-- ham/

*(spam/ham逆だったのを直しました. thx* `@kyuwabara <https://twitter.com/kyuwabara/status/227793920799674369>`_ *!)*

この状態で以下のようになる:

.. code-block:: pycon

   $ cd /tmp
   $ python
   Python 2.7.2 ...(略)
   >>> import spam
   >>> import ham
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ImportError: No module named ham

``spam`` はimportできたけど ``ham`` はimport出来ない。

次に名前空間パッケージを作ってみる。名前空間パッケージとは、PYTHONPATHの通っている別々のディレクトリに同じPythonパッケージ構造をもっているもののこと。 ``parent.child1.one`` と ``parent.child2.two`` が同じディレクトリにあるのは名前空間パッケージとは言わない。

名前空間パッケージではない、普通のパッケージ::

   /tmp/
      +-- parent/
           +-- __init__.py
           +-- child1/
           |    +-- __init__.py
           |    +-- one.py
           +-- child2/
                +-- __init__.py
                +-- two.py

.. code-block:: pycon

   $ cd /tmp
   $ python
   Python 2.7.2 ...(略)
   >>> import parent.child1.one
   >>> import parent.child2.two


名前空間パッケージ::

   /tmp/
      +-- spam/
      |    +-- parent/
      |         +-- __init__.py     ... (1)
      |         +-- child1/
      |              +-- __init__.py
      |              +-- one.py
      +-- ham/
           +-- parent/
                +-- __init__.py     ... (1)
                +-- child2/
                     +-- __init__.py
                     +-- two.py

このとき ``(1)`` の__init__.pyには一般的に以下の内容を記載する:

.. code-block:: python

   try:
       __import__('pkg_resources').declare_namespace(__name__)
   except ImportError:
       __path__ = __import__('pkgutil').extend_path(__path__, __name__)


これで以下のようにspamとhamにPATHを通せば動作する(環境変数PYTHONPATHでもいい):

.. code-block:: pycon

   $ cd /tmp
   $ python
   Python 2.7.2 ...(略)
   >>> import sys
   >>> sys.path.insert(0, '/tmp/spam')
   >>> sys.path.insert(0, '/tmp/ham')
   >>> import parent.child1.one
   >>> import parent.child2.two

このとき、parentが名前空間パッケージという、実体が1つのPATHとは限らない特殊なパッケージと呼ばれる。

.. code-block:: pycon

   >>> parent.__path__
   ['/tmp/spam/parent', '/tmp/ham/parent']

Python3の名前空間パッケージ
=============================

`Python-3.3(b1)のリリースノート`_ に以下のように記載されている:

   Native support for package directories that don’t require __init__.py
   marker files and can automatically span multiple path segments
   (inspired by various third party approaches to namespace packages,
   as described in PEP 420)

   Python標準で、パッケージディレクトリに __init__.py マーカーファイルを
   置かなくてもパッケージとして使えるようになりました。また、複数のパス
   に同じパッケージ名が分散している場合に自動的に集約するようになりました
   (これらは、いくつかのサードパーティーのアプローチにインスパイアされ、
   `PEP-0420`_ で採用されました)。

.. _`Python-3.3(b1)のリリースノート`: http://docs.python.org/dev/whatsnew/3.3.html#pep-420-namespace-packages

ということで、もはや **パッケージディレクトリに__init__.pyは要らない** らしい。

さっそく試してみた::

   /tmp/
      +-- spam/
      |    +-- parent/
      |         +-- child/
      |              +-- one.py
      +-- ham/
           +-- parent/
                +-- child/
                     +-- two.py


__init__.py は無し。

.. code-block:: pycon

   $ python3.3
   Python 3.3.0b1 ...(省略)
   >>> import sys
   >>> sys.path.append('/tmp/spam')
   >>> import parent
   >>> parent.__path__                          #(1)
   _NamespacePath(['/tmp/spam/parent'])
   >>>
   >>> sys.path.append('/tmp/ham')
   >>> parent.__path__                          #(2)
   _NamespacePath(['/tmp/spam/parent'])
   >>>
   >>> import parent.child
   >>> parent.__path__                          #(3)
   _NamespacePath(['/tmp/spam/parent', '/tmp/ham/parent'])
   >>> parent.child.__path__
   _NamespacePath(['/tmp/spam/parent/child', '/tmp/ham/parent/child'])


ちゃんとimportできたし、実体が複数箇所にあることも認識された！
(1)の時点でparentがimport済みだったので、pathを追加しただけでは(2)ではparent.__path__は変化していないが、(3)でimportしたあとではparent.__path__が変化した。

次はsiteコマンドを使ってsite-packagesを追加する要領でディレクトリを追加:

.. code-block:: pycon

   >>> import site
   >>> site.addsitedir('/tmp/egg')
   >>> parent.__path__
   _NamespacePath(['/tmp/spam/parent', '/tmp/ham/parent'])
   >>>
   >>> import parent.child.three
   >>> parent.__path__
   _NamespacePath(['/tmp/spam/parent', '/tmp/ham/parent', '/tmp/egg/parent'])
   >>> parent.child.__path__
   _NamespacePath(['/tmp/spam/parent/child', '/tmp/ham/parent/child', '/tmp/egg/parent/child'])

sys.path.appendしたときと同じように、parentもparent.childもimport済みだったためpathを追加しただけでは変わらなかったけど、/tmp/eggにあるモジュールをimportしたらちゃんとparent.__path__が変化した。

すばらしい！これで __init__.py を置くべきか置かないべきかという話は不要になるね。


追記1
^^^^^^

.. code-block:: pycon

   $ cd /tmp
   $ mkdir foo
   $ mkdir bar
   $ touch foo/__init__.py
   $ python3.3
   Python 3.3.0b1 ...(省略)
   >>> import foo
   >>> import bar
   >>> foo
   <module 'foo' from './foo/__init__.py'>
   >>> bar
   <module 'bar' (namespace)>

__init__.py が無い場合 (namespace) と表示されている。

追記2
^^^^^^

.. code-block:: pycon

   C:\Users\taka> cd \
   C:\> python3.3
   Python 3.3.0b1 ...(省略)
   >>> import Users.taka.Dropbox.code.python.stdout
   >>> Users.taka.Dropbox.code.python.stdout
   <module 'Users.taka.Dropbox.code.python.stdout' (namespace)>
   >>> Users.taka.Dropbox.code.python.stdout.__path__
   _NamespacePath(['.\\Users\\taka\\Dropbox\\code\\python\\stdout'])

なんか気持ち悪いぞｗ


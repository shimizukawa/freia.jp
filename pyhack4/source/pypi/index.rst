PyPIデビュー
=============


PyPIの目的
-----------

PyPI (http://pypi.python.org/pypi) はだれでもPythonパッケージを
登録したりダウンロードしたりできるPython版CPANと言えるものです。
easy_install が登場してから一気に使い勝手がよくなり知名度が
あがりました。


PyPIへの登録
-------------

先ほど作成したfooのseutp.pyを使って登録してみましょう::

   $ python setup.py register

ここで初めて行う人はユーザーアカウントを聞かれると思います。
ちなみに、 ``foo`` というアプリケーションは既に登録されているため、
(http://pypi.python.org/pypi/foo) このまま進めても登録は失敗するので、
そのまま進めちゃってください。

アカウント登録は以下のように進みます::

   $ python setup.py register
   running register
   ...
   We need to know who you are, so please choose either:
   1. use your existing login,
   2. register as a new user,
   3. have the server generate a new password for you (and email it to you), or
   4. quit
   Your selection [default 1]:

アカウントを持っていない人はここで2番を選択してアカウント作成して下さい。
実際にPyPIにアカウントが作成されるのでID/PWはそれなりのものを入れて下さいね。

.. note::
   PyPIのサイト側の仕様変更によりユーザー登録できなくなっていましたが、
   この問題を報告し、2010/7/25頃に無事解決されました。

   原因は、PSFの法務担当からの要請でユーザー登録画面にagreementの
   チェックボックスを付けたためですが、このチェックボックスを登録画面
   から確認画面へ移動する修正を行い、setup.py register から登録した
   場合でもかならず登録者のagreeチェックを行うようになり、実装上も
   法務上も問題が無くなりました。

   議論の流れについては、以下のスレッドで確認して下さい。
   http://mail.python.org/pipermail/distutils-sig/2010-July/016643.html

で、最後にfooは登録されているので、失敗すると思います。


ところで、IDやパスワードは次からは聞かれません。これらは ~/.pypirc に
プレーンテキストで保存されています。ちょっとリスキーな感じです。
パスワードは保存せずに毎回入力したいところですが、保存していないと
uploadに失敗してしまうので、保存せずに運用するのは難しそうです。



PyPIへのアップロード
--------------------

::

   $ python setup.py sdist bdist bdist_egg upload

これでソース配布、バイナリ配布、egg配布それぞれのファイルがPyPIに登録されます。
fooパッケージは登録出来ませんが、もしfooのオーナーと連絡を取りあって、fooの
管理権限を共有設定してもらえば登録出来るようになります。


では、実際にアップロードしてしまうための準備をして、本当にやってみます。


ドキュメントを書く
-------------------

PyPIに登録するには、setup.pyで色々なドキュメント等を適切にする必要があります。
そうしてパっと見でも、これが何のためのパッケージかわかりやすい情報を提供
するわけです。

例えば以下のように書きます::

   from setuptools import setup
   
   version = '0.0.1'
   name = 'practice_bucho'
   short_description = '`practice_bucho` is a package for exercises.'
   long_description = """\
   `practice_bucho` is a package for exercises.
   
   Requirements
   ------------
   * Python 2.4 or later (not support 3.x)
   
   Features
   --------
   * nothing
   
   Setup
   -----
   ::

      $ easy_install svnpoller
   
   History
   -------
   0.0.4 (2010-7-10)
   ~~~~~~~~~~~~~~~~~~
   * first release

   """

   classifiers = [
      "Development Status :: 1 - Planning",
      "License :: OSI Approved :: Python Software Foundation License",
      "Programming Language :: Python",
      "Topic :: Software Development",
   ]
   
   setup(
       name=name,
       version=version,
       description=short_description,
       long_description=long_description,
       classifiers=classifiers,
       keywords=['practice',],
       author='PUT YOUR NAME HERE',
       author_email='name at example.com',
       url='http://bitbucket.org/foo/bar',
       license='PSL',
   )

classifiers には http://pypi.python.org/pypi?:action=list_classifiers
に書かれているものから適切な項目を列挙します。

long_description にはreSTでドキュメントを書くことが出来ます。
これがPyPIのページで表示されるものになります。

あとは実際に register や upload してみてください。
また、uploadしてあればeasy_installで取ってくることも出来ます。

.. _check:

.. note::
   (2011/1/23 `@t2yからの指摘 <http://twitter.com/t2y/status/28845059566731265>`_ で追加. ありがとう!)

   実際にアップロードしてPyPIのページを確認したときに、long_description
   の内容がHTMLに変換されずにそのままreSTのテキストで表示されてしまう場合、
   reSTの記述にエラーがある可能性があります。この場合、upload前にエラーが
   あるかどうかを確認しておくのがよいでしょう。

   docutils付属の :command:`rst2html` コマンドを使って以下のように実行して
   エラーが出るかどうか確認する方法があります。

   .. code-block:: bash

      $ python setup.py --long-description | rst2html > output.html

   または、Python2.7以降でdocutilsがインストールされている環境であれば、
   以下のコマンドのようにエラーを確認することも出来ます。問題がなければ
   `running check` だけ表示されますが、問題があれば以下のように表示されます。

   .. code-block:: bash

      $ python setup.py check -r
      running check
      warning: check: No directive entry for "foo" in module "docutils.parsers.rst.languages.en".
      Trying "foo" as canonical directive name. (line 19)

      warning: check: Could not finish the parsing.

   もう一つの方法として、 `haufe.releaser <http://pypi.python.org/pypi/haufe.releaser/>`_ をインストールするして :command:`python setup.py check_description` のように実行する方法もありそうです(未確認)。

.. warning::
   十分練習したら登録を削除した方が良いでしょう。
   PyPIのサイト上でログインして削除を行って下さい。


PyPIを眺める
-------------

PyPIにどんなパッケージがあるかは http://pypi.python.org/pypi ですこし
見ることが出来ますが、 http://pypi.python.org/simple を見ると全ての
パッケージ名が並んでいるのでブラウザの検索機能を使って目的のライブラリ
があるかどうかを名前ベースで探すことが出来ます。

例えばsphinx拡張は ``sphinxcontrib`` というキーワードで探したり、
後述するbuildoutのレシピは ``recipe`` というキーワードで色々見つけられます。

また、ある程度の命名規則や、探しやすい名前の特徴もみえてきます。
sphinx拡張は ``sphinxcontrib-拡張名`` buildoutのレシピは
``ベンダ名.recipe.目的`` といった感じです。

pdf や aws といった単語で検索すると思わぬパッケージが見つかるかも
しれません。気になるパッケージがあったらリンクを開いて、URLの
simpleをpypiに置き換えれば説明ページを見ることが出来ます。


ちなみに、インデックスサーバーは pypi.python.jp でも公開しています。
`easy_install -i http://pypi.python.jp sphinx` のように書くと、
高速にダウンロードすることが出来ますし、ブラウザで直接みることで
orgの/simpleと同じ結果を得られます。ただし詳細説明画面は.jpでは
見ることは出来ません。





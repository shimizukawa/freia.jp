distutils, setuptools, distribute, pip, virtualenv, buildout 再掲
==================================================================

http://www.freia.jp/taka/blog/691 (2010/12/5) の更新版。

各パッケージの用途と概要
-------------------------

distutils
~~~~~~~~~~
Python の標準パッケージです。eggは作れませんが、 ``python setup.py build`` したり、 ``python setup.py install`` したり、 ``python setup.py register ...`` でPyPIにパッケージを新規登録出来るようになったり、 ``python setup.py bdist sdist upload`` でパッケージファイルをアップロードしたり、といった機能が提供されています。

詳しくは `Pythonのマニュアル`_ を参照のこと...。

.. _`Pythonのマニュアル`: http://www.python.jp/doc/2.5/lib/module-distutils.html


setuptools
~~~~~~~~~~~
setuptools_ はPython 標準の distutils を拡張しています。

良く使われるのは easy_install コマンドで、 easy_install を使うために ez_setup.py を実行すると、陰でこっそり setuptools がインストールされます。 easy_install は ``easy_install Sphinx`` 等と書くと、PyPI(Python Package Index)から自動的に Sphinx パッケージを探してきて site-packages にインストールしてくれます。

開発向けには、setuptoolsをインストールすると setup.py に egg を作るための記述が出来るようになり、また、 ``python setup.py bdist_egg`` で egg を作れるようになったり。

現在の開発状況は、0.6c11 (2009-10-20) までリリースされていますが、 0.6c9 (2008-09-24) から 0.6c10 (2009-10-19) まで1年以上間が空いていて、6個のバグが修正されただけで、実質、開発が止まっているといえるかもしれません。2010-07-08にはPython2.7用のeggがアップロードされましたがコードは変わってないようです。

.. _setuptools: http://pypi.python.org/pypi/setuptools


distribute
~~~~~~~~~~~
distribute_ は setuptools から分岐したプロジェクトです（というかクローンです）。 distribute は将来的に setuptools から置き換えて使えるように設計しています。また、0.6.2までで既存の setuptools との後方互換性対応が完了し、同時に Python3 への対応を始めました。

distribute をインストールすると、 setuptools がインストール済みの場合、自動的にこれが使われないようにリネームします。インストールされた distribute-0.6.8-py2.6.egg の中には setuptools というパッケージ名が入っているので（と言うか名前なども全部互換なので）、これ以降 ``import setuptools`` 等と実行すると、distributeのコードがimportされるようになります。

bin/easy_install も distribute を使うように書き換わります。

Distributeがsetuptoolsより優れている点は、 Windowsのexeインストーラで提供されている場合（例えばMarkdown）でもeasy_install出来るとか、Mac標準のPythonだとeasy_installの問題でvirtualenvうまくいかない時にも大丈夫（これはwork-around）とか、エラーメッセージが分かりやすくなっているとか、コードが読みやすくなっているとか、まあ色々です。

Tarek の blog `virtualenv and zc.buildout now with Distribute included`_ から引用:

   Setuptools から Distribute に切り替えるとてもシンプルな理由:

   * Distribute 0.6.x は Setuptools の完全互換性を持っています
   * Distribute は活発にメンテナンスされており、10人以上のコミッターがいます
   * Distribute 0.6.x は Python3 をサポート!

合わせて読みたい: `Distutils and Distribute status (part #1)`_

.. _distribute: http://pypi.python.org/pypi/distribute
.. _`virtualenv and zc.buildout now with Distribute included`: http://tarekziade.wordpress.com/2009/11/07/virtualenv-and-zc-buildout-now-with-distribute-included/
.. _`Distutils and Distribute status (part #1)`: http://tarekziade.wordpress.com/2009/11/18/distutils-and-distribute-status-part-1/


pip
~~~~
pip_ は easy_install と同様の機能を提供します。 distribute は setuptools 全体を置き換えようとしていますが、 pip は easy_install コマンドを置き換えようとしています（distribute とは異なり、easy_installを削除したり書き換えたりはしません）。

pip は easy_install でインストール出来るものは同じようにインストールできます。パッケージ名を指定すれば自動的に PyPI から取ってきてくれたりします。ただし、 easy_install よりも良い動作をするよに設計されていて、複数パッケージを逐次インストールせずに、先にダウンロードしてからインストールを始めるとか、エラーメッセージが親切だとかが考慮されています

pip の方針として、複数バージョンの共存は行わない設計のため、 pip でインストールする場合は virtualenv の環境下で行うことが推奨されています。なお、 ``pip install -E new-env/ MyPackage`` と実行すれば任意の virtualenv 環境をインストール先に指定できます。また、間違って実環境下で pip install してしまわないように環境変数 ``PIP_REQUIRE_VIRTUALENV=true`` しておく方法も提供されています。

pip の便利な機能は, uninstall(パッケージのアンインストール), freeze(パッケージ名==Version番号、の羅列がstdoutに表示されます), bundle(対象パッケージがrequireしているパッケージを集めて1つの .pybundle ファイルに固めてくれる) などがあります。 .pybundle に固めたファイルは ``pip install foo.pybundle`` としてインストール出来ます。ソースが全て .pybundle に格納されているためこのとき通信出来なくても問題ありませんが、C拡張などはこの時点でビルドされるためコンパイラや関連ライブラリなどが必要になります。

現在の所、制限事項も多く、eggパッケージからのインストールは出来ず、ソース提供されているパッケージのみインストール出来るなどがあります（＝バイナリ配布出来ません）。Windowsではテストされておらず、ちょっとしたバグのためにbundleが動作しません。またWindowsでちょっと試してみたところ、C拡張のビルド時にコンパイルエラーになってもインストールが継続してしまうようです。詳しくは pip の `Differences From easy_install`_ の説明を確認して下さい。

非開発向けの視点からみると pip を使ったインストールはシンプルなので(単一バージョン,eggで固めず全て展開する,名前空間を結合する) 使いやすいという意見もあります。実際、setuptoolsの複数バージョン管理,egg化という複雑さや、jarっぽい設計よりも良いと評価している人もいるようです(`Why I like pip`_)。

.. _pip: http://pypi.python.org/pypi/pip
.. _`Differences From easy_install`: http://pypi.python.org/pypi/pip#differences-from-easy-install
.. _`Why I like pip`: http://www.b-list.org/weblog/2008/dec/15/pip/


virtualenv
~~~~~~~~~~~
VirtualEnv_ はPythonの仮想環境を作ります。それだけですが、非常に便利です。 virtualenvwrapper も合わせて使うと便利らしいです。 workingenv や virtual-python の後継という位置づけのようです。

virtualenv は標準で setuptools を取ってきてインストールしますが、 ``virtualenv --distribute envdir`` のようにして環境を作ると、 setuptools の代わりに distribute を使ってくれるようになります（環境を作ってから 'easy_install distribute` してもよいです）。

virtualenv を導入して困ることはほとんど無いと思います。 distribute, pip, buildout, どれもが virtualenv 下で問題無く動作します。ただし、 mod_python や mod_wsgi など、 virtualenv 環境下の bin/python 以外から virtualenv 下のモジュールを呼び出す場合、 `Using Virtualenv without bin/python`_ を参考に多少の設定を行う必要があります。

.. _VirtualEnv: http://pypi.python.org/pypi/virtualenv
.. _`Using Virtualenv without bin/python`: http://pypi.python.org/pypi/virtualenv#using-virtualenv-without-bin-python

zc.buildout
~~~~~~~~~~~~
`zc.buildout`_ は Python ベースのビルドシステムです。パーツという単位でアプリケーションを 作成、組み立て、配置などを行い、非Pythonベースのものも構築は可能です。

buildout 自体は buildout.cfg の設定を元に環境を構築してくれます。処理の実体は buildout 用の recipe と呼ばれるパッケージで実装されていて、PyPIからeggを取ってくる、svnからチェックアウトする、などいろいろなrecipeがあります。 Zope 用としては Zope のインスタンスを作成する、Ploneのサイトインスタンスを作ってProductsをインストールする、などの recipe もあります。

buildout では Python 本体の site-packages を切り離せないので、その必要がある場合は virtualenv 環境下で buildout を使うようにしましょう。ただし1.5.0正式リリースからこの機能が搭載される予定で開発を行っているようなので、「親Python環境のsite-packagesを完全に切り離したい」場合にvirtualenvを使わなくても良くなる日も近いでしょう。

buildout 自体は recipe を取ってくるために setuptools を使っていますが、代わりに distribute を使うようにも出来ます (``python bootstrap.py --distribute``)。

詳しい使い方については `本ドキュメントのzc.buildout <buildout/index.html>`_ を参照して下さい。

.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout


各パッケージの現状(2010/7/10)
-------------------------------

distutils
~~~~~~~~~~
:作者: Python コミュニティー
:PyPI: Python同梱です
:最新: Python-2.7 同梱 (2.6以前にももちろん同梱)

setuptools
~~~~~~~~~~~
:作者: Phillip J. Eby (PEAK)
:PyPI: http://pypi.python.org/pypi/setuptools
:最新: 0.6c11 (2010/7/10)
:更新頻度: 超低 (2010/7/8に-py2.7.eggが登録された)
:目的: distutilsの拡張, egg作成, PyPIからのインストール
:弱点: メンテが止まっているように見える、進化がない。

distribute
~~~~~~~~~~~
:作者: Tarek Ziade
:PyPI: http://pypi.python.org/pypi/distribute
:最新: 0.6.13 (2010/5/31)
:更新頻度: 高
:目的: distutils の拡張。 setuptools の完全置き換え、完全互換。Python3対応(今後)
:相性: setuptools を使っているのと変わらない使用感。 setuptools を排除する以外はとても良い。 virtualenv や buildout で最初から distribute を使うためのオプション(``--distribute``)が提供されている。

pip
~~~~
:作者: Ian Bicking
:PyPI: http://pypi.python.org/pypi/pip
:最新: 0.7.2 (2010/5/27)
:更新頻度: 高
:目的: easy_install コマンドの置き換え、uninstallサポート、bundleパッケージの作成。
:弱点: eggをインストール出来ない。ソースからのみ可能。
:相性: Windowsでは動作確認されてません(Maybe it doesn't work on Windows.)。実際、bundleコマンドはWindowsで動作せず。また、buildoutで構築した環境ではfreezeとuninstallも意味をなさないため、buildout使用時はpipの必要性が無いかも。

virtualenv
~~~~~~~~~~~
:作者: Ian Bicking
:PyPI: http://pypi.python.org/pypi/virtualenv
:最新: 1.4.9 (2010/5/28)
:更新頻度: 中
:目的: Pythonの仮想環境を作成。site-packagesの切り離し。
:相性: とくに競合するパッケージは無し。distributeをデフォルトにするオプション ``--distribute`` あり。Mac標準のPythonだとeasy_installの問題で導入できたように見えても実は導入できていないといった問題もあり。その場合はvirtualenv環境にdistributeを導入して回避できるという報告もあります。

zc.buildout
~~~~~~~~~~~~
:作者: Jim Fulton, Andreas Jung, Tarek, Tres Seaver, tlotze
:PyPI: http://pypi.python.org/pypi/zc.buildout
:最新: 1.5.0b2 (2010/4/30)
:更新頻度: 高
:目的: 環境やアプリケーションの構築を行う。egg取得、配置、設定、shellコマンド実行...等々。JavaならMavenに相当するらしい。
:相性: virtualenv 無しで独立した環境を構築するが、virtualenv環境下で使うとさらにクリーンに使える。1.5.0正式版でvirtualenv無しでの完全独立環境が作成出来る予定。とくに競合するパッケージは無し。distributeをデフォルトにするオプション ``--distribute`` あり。


主観的なまとめ
---------------

調べてみた感想として、個人的には virtualenv + distribute 環境下で buildout + distribute を使うのが良いように思います。pipはbuildout環境下では積極的に使う必要はなさそうな気がしますが積極的に使っていないので自分が利点を理解していないだけかも。pipにバイナリインストール機能が提供されてもうちょっと安定したら(開発以外の配布用途などで)使いたいシーンが出てくるかもしれません。



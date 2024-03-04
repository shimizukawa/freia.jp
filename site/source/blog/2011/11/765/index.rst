:date: 2011-11-02 21:18:26
:tags: python

============================================================================
PyPIで公開していないパッケージをeasy_installで手軽にインストール 
============================================================================

先日 @aodag と社内で話していたときにgithubやbitbucketの便利な使い方を聞いて、ナルホド！と思ったので、もうひと工夫してみた。

前置き
=======
easy_install はパッケージ名を指定すればネットワーク(PyPI)からそのパッケージを探してきて自動的にインストールしてくれる便利なツールだ。
例えば以下のように実行する::

   $ easy_install Pillow

   (venv2) D:\venv2>easy_install Pillow
   Searching for Pillow
   Reading http://pypi.python.org/simple/Pillow/
   Reading http://github.org/collective/pillow
   Reading http://github.org/collective/Pillow
   Reading http://github.com/Pillow
   Best match: Pillow 1.7.5
   Downloading http://pypi.python.org/packages/2.7/P/Pillow/Pillow-1.7.5-py2.7-win32.egg...

easy_installがPillow 1.7.5 を見つけたようだ。

既にインストールされていてアップデートする場合は以下のように実行する::

   $ easy_install -U Pillow


PyPIにリリースしていないパッケージのeasy_install
==================================================

先の例では、easy_installはPillowを標準のインデックスサーバー = PyPI( http://pypi.python.org/pypi/ )から自動的に探してインストールしてくれている。ではPyPIにパッケージがない、あるいは別の所にあるパッケージを指定してインストールするにはどうすればいいか。単にそのパッケージのURLを指定するだけで良い::

   $ easy_install https://bitbucket.org/shimizukawa/pillow/downloads/Pillow-1.7.5-py2.7-win32.egg

このeasy_installの機能と、githubやbitbucketで用意されているtag名やbranch名で自動的にzip/tgzを用意してくれる機能を組み合わせると、こんな事が出来るようになる。

自分がちょっとしたツールとして作った logfilter はPyPIに公開されていないので、easy_installは出来ない::

   $ easy_install logfilter
   Searching for logfilter
   Reading http://pypi.python.org/simple/logfilter/
   Couldn't find index page for 'logfilter' (maybe misspelled?)

しかし、先の例のようにURLを直接指定すれば任意のtagのパッケージを直接インストールすることが出来る。例えばgithubにあるWebDispatchの場合、tagを付けると https://github.com/aodag/WebDispatch/tags にあるように自動的にtag名でzipファイルが生成されるので、以下のようにeasy_installすることができるわけだ::

   $ easy_install https://github.com/aodag/WebDispatch/zipball/1.0a3
   Downloading https://github.com/aodag/WebDispatch/zipball/1.0a3
   Processing 1.0a3

同様のことはbitbucketでもちょっと前のアップデートでできるようになった。logfilterを置いている https://bitbucket.org/shimizukawa/logfilter/downloads を見ると、zipだけでなくtar.gzやbz2も提供されている。

ここまでが @aodag から教えてもらったこと。さすがaodagや！ヽ('∀`)ﾉ

easy_install -f の名前解決を使ってバージョンを自動認識
=======================================================

パッケージのURLを直接指定する方法には一つだけ難点があって、logfilter-0.9.2 の次のバージョンがリリースされたときに自動的に新しいバージョンを見つけてくれない。そこで、easy_installにある ``--find-links`` または ``-f`` オプションを使う方法を併用してみる。-fオプションに指定するのはパッケージへの ``リンク集`` があるページのURLだ::

   $ easy_install -f https://bitbucket.org/shimizukawa/logfilter/downloads logfilter
   Searching for logfilter
   Reading https://bitbucket.org/shimizukawa/logfilter/downloads
   Best match: logfilter 0.9.2
   Downloading https://bitbucket.org/shimizukawa/logfilter/get/logfilter-0.9.2.zip

このように -f オプションを指定すると、 ``ページ内にあるリンクをチェックして、パッケージ名を認識し、自動的に最新のバージョンを取得＆インストール`` してくれる。さらに、インデックスサーバー(PyPI等)を指定する-iオプションと異なり、複数指定もできてインデックスサーバーよりも優先されるので、独自のパッケージサーバーを利用しつつ、PyPIも使いたいといったシーンで活用できる。


* `Dependencies that aren't in PyPI - setuptools - The PEAK Developers' Center <http://peak.telecommunity.com/DevCenter/setuptools#dependencies-that-aren-t-in-pypi>`_

* `PyPIにない依存物 [Python] setuptools - SumiTomohikoの日記 <http://d.hatena.ne.jp/SumiTomohiko/20070622/1182537643>`_


ただし、パッケージ名に相当するリンクターゲット名は、easy_install(setuptools)の決めたルールに従って名前づけられていないとeasy_installがパッケージを見つけることが出来ない。名前は logfilter-0.9.2.zip を参考に説明すると、以下のようになっている::

   [パッケージ名]-[バージョン].[拡張子]

完全な名前付けのルールはもうすこし複雑で、プラットフォームやアーキテクチャが含まれる場合もある。そういったファイル名の例は http://docs.python.org/distutils/builtdist.html で参照することが出来る（仕様はPEPになってないのかな？）。

バージョン番号部分の付け方は、easy_installが導入したデファクトの名前付けルールについては以下のページを参照して欲しいが、 PEP386_ で正式に決められたバージョン番号体系に従うべきだ。

.. _PEP386: http://www.python.org/dev/peps/pep-0386/

* `Specifying Your Project's Version - setuptools - The PEAK Developers' Center <http://peak.telecommunity.com/DevCenter/setuptools#specifying-your-project-s-version>`_

* `プロジェクトのバージョンを指定する [Python] setuptools - SumiTomohikoの日記 <http://d.hatena.ne.jp/SumiTomohiko/20070622/1182537643>`_


ということで、bitbucketやgithubで自動生成されるzipファイルの名前を上記のルールに適合するようにタグ名を調整すれば、easy_installの-fオプションでインストール出来る様になる。 https://bitbucket.org/shimizukawa/logfilter の例でいうと、タグ名は以下のように設定した::

   logfilter-0.9.2
   logfilter-0.9.1
   logfilter-0.9

タグ名を ``0.9.2`` とかしてしまうと残念ながらPythonの配布パッケージとして認識されないので(先のWebDispatchの例のようにフルURL指定すればインストールは出来る)、パッケージ名付きでリポジトリにタグを設定するのがポイントだ。


まとめ
=======

タグ名を工夫すれば、PyPIで公開していないパッケージを自動名前解決&バージョン認識してeasy_installで手軽にインストールすることができる。

というか、0.9.2.zip とか tip.zip とかいう名前でダウンロード出来てもあとで何だか分からなくなるので、プロジェクト名も付けてzipファイルを生成してくださいよ、bitbucket & githubさん！


.. :extend type: text/x-rst
.. :extend:


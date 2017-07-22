:date: 2012-04-11 23:30:00
:categories: ['Python', 'make', 'Makefile', 'Library']
:body type: text/x-rst

=========================================
2012/04/11 MakefileをPythonで置き換える
=========================================

仕事でMakefileを書いていたのですが、ちょと複雑なことをしようとすると書き方を調べるのにやたらと時間を取られます。Pythonばっかり書いてるせいか、Makefileやshell scriptの書き方は毎回忘れますね。

**MakefileをPythonで書ければ良いのに！** とはいえ、ベタにPythonで書いて、ターゲット間の依存関係などを考え始めるとコードがめちゃくちゃ長くなってしまいます。ということでPythonでMakefileを置き換えるツールが無いか調べてみました。ざっと探して見つけたのが以下のツールです。

* http://pypi.python.org/pypi/Baker
* http://pypi.python.org/pypi/mk
* http://pypi.python.org/pypi/shovel
* http://pypi.python.org/pypi/Paver

この中では、多分欲しいのはPaver辺りだろうなあと思いつつ、自分が欲しいのはどういう使い方なのかを把握するためにコードを書いてみました。

以下のようなmake.pyを記述できると、書くのが楽そうです。

.. literalinclude:: make.py
   :language: python

これを動かすためのmk.pyをざざっと実装してみました。

.. literalinclude:: mk.py
   :language: python


なぜかclassmethodだらけ。使い方のわかりやすさ優先で実装したらなぜかこんなコードになりました。


これで以下のように実行できます。

.. code-block:: bash

   $ python make.py all
   ...
   $ python make.py pkg
   ...
   deploy package: maketest-20120406190450.tgz
   $

`make all` に比べると多少入力文字数が多くなりましたが、既存の手順を維持したいなら以下のようなMakefileを用意しておけば良いですね。

.. code-block:: make

   all:
       python make.py all

   pkg:
       python make.py pkg

   ...

あとは、先のコードに近い記述ができるツール(=自分が使いやすいと感じるツール)を前述の4つから探せば良いわけですが、とりあえずの目的は達成しちゃったので調べるのはまた今度にします。

ソースコード
------------
作ったコードは以下から取得出来ます。

* https://bitbucket.org/shimizukawa/freia.jp/src/tip/site/source/blog/replace-makefile-with-python

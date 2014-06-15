:date: 2014-6-15 17:30
:categories: ['Python', 'Sphinx']
:body type: text/x-rst

============================================================
2014/6/15 Sphinxメンテナ日記: チケットとメールの対応いろいろ
============================================================

*Category: 'Python', 'Sphinx'*

前置き: Sphinx本家のMLに返信したり、チケットに返信した内容のメモです。このエントリを読むと、Sphinxのこまかい機能を知ることが出来るかもしれません。前置きおわり。

.. contents::
   :local:

docs.python.org みたいなドキュメントバージョン切り替え
=======================================================

sphinx-users ML: `Different version drop-down like python.org`__

.. __: https://groups.google.com/d/msg/sphinx-users/t-USA30hQTY/t85h2Z1d80QJ

**Q.** docs.python.org のようにドキュメントのバージョンをドロップダウンで表示して切り換える機能はSphinxにありますか？

**A.** ありません。

Pythonのドキュメントチームがその機能を用意したぽいですね。
http://blog.python.org/2012/10/updates-to-docspythonorg.html 

他の例では、Read The Docs のシステムと専用テーマの組み合わせで
似たような機能を提供しています。
https://github.com/snide/sphinx_rtd_theme/


スペイン語の日付をPDF出力に表示したい
======================================

sphinx-users ML `How i can generate the date into Spanish with latexpdf?`__

.. __: https://groups.google.com/d/msg/sphinx-users/vBDx5_waC8g/-d70dT8tdR8J

**Q.** language='es' で ``make latexpdf`` したら日付が ``5 de june de 2014`` と表示されたんだけど、スペイン語としては ``5 de junio de 2014`` が正しい。conf.pyの ``today`` と ``today_fmt`` を設定してみたけどうまくいかない。どうすればいいだろう？

**A.**  Sphinxはtoday_fmtのスペイン語翻訳を持っています: 
https://bitbucket.org/birkenfeld/sphinx/src/6e61d8a5/sphinx/locale/es/LC_MESSAGES/sphinx.po#cl-47 しかしながら、Sphinxはlocaleを設定していないので、 "%B" を指定すると英語の月名を表示してしまいます。そこで、以下のように ``locale.setlocale`` をconf.pyで実行することで問題を回避できます::

   #today = '' 
   #today_fmt = '%B %d, %Y' 
   import locale 
   locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') 


%Bを指定すると月が英語表示になる、って、これはバグっぽい気もする。しかし、setlocaleの値はシステムによって異なるので、Windowsだと 'es_ES.UTF-8' じゃなくて 'spanish' を指定する必要がある。そういうconfig設定増やすのが良いのかなあ。


脚注マークを [] で囲わない方法は？
===================================

sphinx-users ML: `Can I have a footnote without []?`__

.. __: https://groups.google.com/d/msg/sphinx-users/vAgojGx4V-E/FSI0_38dneIJ

**Q.** 文中に脚注へのリンクがあると ``[1]`` のように表示されるけど、この角括弧を付けないHTML出力にして、CSSでsuperscript(上付き)表示にしたい。

**A.** それdocutils.confにオプション設定すれば出来るよ

Sphinx-1.2 以降では ``docutils.conf`` でdocutilsのオプションを設定できます。
http://sphinx-doc.org/changes.html#release-1-2-beta2-released-sep-17-2013

docutils.confをconf.pyと同じディレクトリに置いて（カレントディレクトリだったかな）、以下の内容を書いて下さい::

   [html4css1 writer]
   footnote_references = superscript

docutilsの設定値については以下も参照してください:
http://docutils.sourceforge.net/docs/user/config.html#footnote-references 


インスタンス属性のドキュメントが1行で複数設定した場合反映されない
==================================================================

sphinx-users ML: `autoattribute for parallel assignment`__

.. __: https://groups.google.com/d/msg/sphinx-users/kPlTpeMQNOE/OOdImIuCSsoJ


**Q.** 以下のように書いたらautodocでインスタンス属性のドキュメントとして反映されます::

   class Foo:
       def __init__(self):
           self.spam = 4
           """Docstring for instance attribute spam."""

でも以下のように書くと反映されません::

   class Foo:
       def __init__(self):
           self.spam, self.bar, self.moo = 4, 5, 6
           """Docstring for instance attribute spam."""

ドキュメントを反映する方法はありますか？


**A.** ありません。属性毎に別の行にしてドキュメントを書いて下さい。

技術的には、 ``sphinx.pycode.AttrDocVisitor.add_docstring`` 関数が属性ドキュメントを解釈しています。146行目のIFブロックはドキュメントコメントの前か後に `self.variable = value` といった形式の行がなければ属性ドキュメントとみなしません。
https://bitbucket.org/birkenfeld/sphinx/src/ba4b069e/sphinx/pycode/__init__.py#cl-146



@property デコレータを付けた属性にシグネチャが付く問題
=======================================================

Pull Request #157 `Remove spurious signatures from @property decorated attributes`__

.. __: https://bitbucket.org/birkenfeld/sphinx/pull-request/157/remove-spurious-signatures-from-property


以下のような属性 myattribute を書くと、cythonがdocstringの先頭に 'Bar.myattributes(self)' って付けるようになってしまったので、autodocでdocstring先頭のシグネチャをメソッドのときと同じように@propertyが付いている時も無視するようにしたい::

   # cython: embedsignature=True
   class Bar(object):
       def __init__(self):
           pass

       @property
       def myattribute(self):
           """my docstring"""


これの動作検証をして、テストコード書いてmergeした。
https://bitbucket.org/birkenfeld/sphinx/commits/679955b96d


Sphinxのautodoのための複雑なコードを簡略化
===========================================

Pull Request #246: `remove complex distinguishing method/classmethod/staticmethod approach for autodoc`

.. __: https://bitbucket.org/birkenfeld/sphinx/pull-request/246/remove-complex-distinguishing-method/diff


自分で提出したPR。あるメソッドがclassmethodか、staticmethodか、普通のmethodかを判別する実装が複雑だったので簡略化したい。

修正前:

* py2: メソッドオブジェクトを取得するために ``getattr(classobj, 'methname')`` してからいくつかの条件チェックを行う
* py3: メソッドオブジェクトを取得するために ``classobj.__dict__.get('methname')`` してからisinstance()でclassmethodかstaticmethodかのチェックを行う

修正後:

* 修正前のpy3用の実装に統一

この修正で既存の機能が壊れることはなさそうだけど、心配だったのでPR出してレビューしてもらった。たぶん大丈夫、ということでマージ。


非minify版のjquery.js, underscore.jsをmake htmlで選べるようにする
==================================================================

Issue #1434: `provide non-minified options for jquery.js, underscore.js, all others`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1434/provide-non-minified-options-for-jqueryjs#comment-10722895

Debianのlintianが、配布パッケージの内容物にライセンス違反がないかチェックを自動的に行っているが、それによって、Sphinxが同梱しているminified版のJSファイルがひっかかって、SQLAlchemyの配布物を作るために人間が毎回手動でJSファイルを入れ替えている。この問題を解決したい。


最終的に、選択出来るように、ではなく、非minified版を常にmake htmlの結果として同梱するようにしました。とりあえず反論はなさそうなので、Issueを一旦クローズ。


CIFSファイルシステム上でmake htmlするとエラー
==============================================

Issue #1490: `sphinx-build -b html . ./_build -> No such file or directory`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1490/sphinx-build-b-html-_build-no-such-file-or#comment-10722930


cifsでWindowsの共有ディレクトリUbuntuにマウントしてそこでmake htmlすると ``OSError: [Errno 2] No such file or directory`` というエラーが出る。


これは ``libc getcwd(3)`` の制限なので、Python/Sphinxではどうにもならなそう: http://bugs.python.org/issue17525

なので、make htmlしてから出力結果をcifsディレクトリにコピーする方法を進めておいた。


画像が次のページに表示されて、キャプションだけ前のページにある
===============================================================

Issue #1482: `Forcing images to be seen in the same page`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1482/forcing-images-to-be-seen-in-the-same-page#comment-10723168


PDF出力すると、ページ内に収まらない画像は次のページに送られてしまうけど、画像の次の行に書いた説明文は前のページに残るので、画像なしで説明文だけあると意味が分からなくなってしまう、という問題。

手元では再現しなかった。 figure ディレクティブと image ディレクティブ両方で試してみたけど再現せず。ソースを添付して、って依頼してHOLD状態へ。


使われてないimportとかPEP8的な修正とか
========================================

https://bitbucket.org/birkenfeld/sphinx/commits/ba4b069ed617a6479a7d701fb3cc8fd3544db25e

Sphinxのテストではpyflakesとかpep8とか実行していないけど、 `check_sources.py`__ というチェックスクリプトでチェックする運用になっている。なんでこういう仕組みにしたんだろう？flake8で検査してみたら大量にエラー出過ぎたので、そのうちflake8で通るようにして、flake8に切り換えよう・・・。

.. __: https://bitbucket.org/birkenfeld/sphinx/src/ba4b0/utils/check_sources.py



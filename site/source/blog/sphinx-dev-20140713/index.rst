:date: 2014-7-13 15:00
:categories: ['Python', 'Sphinx']
:body type: text/x-rst

====================================================================
2014/07/13 Sphinxメンテナ日記(7/7-7/13): IRC=Sphinxよろず相談所
====================================================================

*Category: 'Python', 'Sphinx'*

前置き: チケットとメールとIRCで対応した内容のメモです。


**先にまとめ**

今週ちょっと忙しかったのと、 sphinx-intl_ のPR取り込んだりしてたため、またSphinxのチケット残数が増えてきました。減らせないまでも、増やさないようにしたいなあ

.. _sphinx-intl: https://pypi.python.org/pypi/sphinx-intl


以下、各チケットとかの対応でやったこと。

.. contents::
   :local:


7/7 SphinxをMarkdownで書く方法知らない？
===========================================

IRCで、SphinxのMarkdown拡張ある？という質問。

remarkdown_ (docutilsのパーサープラグインで、Markdownからdoctreeにパースするもの)と sphinxcontrib_markdown.py_ (`@tk0miya`_ が作った、内部でpandoc呼び出してMarkdownをreSTに変換するもの)の存在を教えてみた。

反応はなかった。


IRCより::

   Monday, July 7th, 2014
   02:19 _AJ> Has anyone come across an extension that adds Markdown support?
   09:20 <shimizukawa> https://github.com/sgenoud/remarkdown is a docutils' markdown parser. I think it works with Sphinx but I've never tried.
   09:30 <shimizukawa> Another way https://gist.github.com/tk0miya/4336929 that call 'pandoc' command internally.

.. _remarkdown: https://github.com/sgenoud/remarkdown
.. _sphinxcontrib_markdown.py: https://gist.github.com/tk0miya/4336929
.. _@tk0miya: https://twitter.com/tk0miya


7/7 code-blockを使うとrst2htmlでエラーになる
===============================================

IRCでの質問。rst2htmlはdocutilsのコマンドであって、Sphinxのコマンドでは無いので、Sphinxが提供している :rst:dir:`code-block` を含むrstファイルを変換しようとするとエラーになる。docutils-0.9以降なら ``code`` ディレクティブが使えるようになるので、それを勧めておいた（しかし、パッケージのアップデートが出来なかったらしく、別の人がフォローしてた）。

ちなみに ``code`` ディレクティブはSphinxから逆移植されたもの。こうなってくると、どれがSphinxのものでどれがdocutilsのものか判別つかないだろうなあ。

Sphinx-1.3はdocutils-0.10以降しかサポートしてないので、code-blockの実装を落として、docutilsのcodeディレクティブへのエイリアスにしてもいいかもしれない。

あと、Sphinxが提供する、docutils単体でも使えそうなディレクティブなどは、docutilsの拡張として実装してあったらよかったのになあ、と思う。このへんもそのうち作り替えていこう。

IRCより::

   Monday, July 7th, 2014
   20:28 <Lionel__> hello
   20:28 <Lionel__> I've got a problem with Sphinx, using rst2html, it says " Unknown directive type "code-block". " Yet Pygments is installed, can someone help me? Thanks.
   20:33 <shimizukawa> rst2html is not a sphinx command
   20:34 <shimizukawa> If you want to use 'code-block' like directive under docutils (it means without sphinx), you can use 'code' directive that is provided from docutils-0.9.
   20:34 <shimizukawa> see also: http://docutils.sourceforge.net/docs/ref/rst/directives.html#code


7/8 Sphinx拡張作ったけど、ドキュメント間のリンクの解決をうまくやる方法は？
============================================================================

docutilsが提供する標準のreSTでは、ファイル間のリンクをサポートしていない。

Sphinxでは ``:ref:`link-label`` や ``:doc:`../other``` のように別のファイルへのリンクを生成する機能がある。これらは、ドキュメントの読み込みフェーズではリンク先ドキュメントはまだ読み込まれていない可能性があるため解決出来ない。そのため、読み込み時には :class:`sphinx.addnodes.pending_xref` というノードにしておいて、書き出すときに解決する仕組みを持っている。

この仕組みはSphinx拡張でも当然使えるものなので、それを紹介しておいた。無事使えたかどうかは分からないけど。

参考: :ref:`exttut` の "ビルド・フェーズ" のあたり。


IRCより::

   Tuesday, July 8th, 2014
   07:26 <harlowja> hi folks, qq, if i have a extension that wants to insert a node.reference to a refname, is that possible? i was trying this over the weekend and it seems like the refname is never resolved to the refuri (even though other refnames are resolved correctly), is the extension activation time or something stopping this from correctly occurring?
   07:27 <harlowja> i dropped some debug statements in the sphinx/docutils code, and it seems like it never gets resolved even though the extension produces a valid reference
   07:28 <harlowja> maybe extensions should just avoid using refname and only use refuri (which works, but makes people duplicate uris)
   13:06 <shimizukawa> harlowja: node.reference is not suitable to the purpose. In order to link to another reftarget by using refname, you should use sphinx.addnodes.pending_xref instead: http://sphinx-doc.org/extdev/nodes.html#sphinx.addnodes.pending_xref
   13:07 <harlowja> shimizukawa coool, is that useable from an extension without problems?
   13:07 <shimizukawa> And you need to resolve the pending_xref, you should hook missing-reference event http://sphinx-doc.org/extdev/appapi.html#event-missing-reference
   13:08 <shimizukawa> Yes > without problems
   13:08 <harlowja> cool, i will try that out
   13:08 <harlowja> i didn't find many extensions that were doing this as example, most seem to just set refuri
   13:11 <shimizukawa> yeah, for example, sphinx.ext.todo extension is not necessary to know a refname to link another reftarget.
   13:16 <shimizukawa> Sphinx itself is using pending_xref to resolve references because in reading stage, other reST files are not parsed yet and a document can't resolve target refurl in other reST file.
   13:40 <harlowja> shimizukawa thx, i'll try it out and see how it goes :)


7/10 autoflask拡張がうまくうごかない
========================================

`sphinxcontrib.autohttp.flask` ってなに？と思ったら sphinxcontrib-httpdomain_ に同梱されているらしい。


* `sphinxcontrib.autohttp.flask — Exporting API reference from Flask app`__

.. _sphinxcontrib-httpdomain: https://pythonhosted.org/sphinxcontrib-httpdomain/
.. __: https://pythonhosted.org/sphinxcontrib-httpdomain/#sphinxcontrib-autohttp-flask-exporting-api-reference-from-flask-app

手元では問題なく動いたので、うまく動かなかった理由は、たぶん ``PYTHONPATH`` の指定が1階層ずれてたためだと思う。という指摘をしておいたが、反応はなかった。IRC切断時間あるから、その間に返事が来ても見逃すんだよね。


IRCより::

   Thursday, July 10th, 2014
   06:40 <claudiop> Hi. How can i get documentation generated by sphinx to keep offline?
   06:41 <claudiop> For example, this project: https://lazka.github.io/pgi-docs/ It tells how it was generated, but i am being unable to, can i simply get the generated data from that spinx-based-cms?
   19:59 <shimizukawa> claudiop: I have no idea for the pgi-docgen :(
   21:49 <marscher> hi, is it possible to avoid showing the content of a documentated global variable of a module?
   Friday, July 11th, 2014
   18:20 <future-unicorn> Hi! I am new to Sphinx and am trying to build doc for my RestAPI made with flask. sphinxcontrib-httpdomain seems to have a nice generator for flask, but I can't produce any output from my docstrings
   18:22 <future-unicorn> using .. autoflask:: foo.api:app does not produces any output but a function declared in foo/api/__init__.py before building the Flask app
   19:36 <shimizukawa> future-unicorn: please let me see a small sample what did you create by using zip archive or gist or pastebin ...
   20:08 <future-unicorn> shimizukawa: https://gist.github.com/tszym/3f55e1e2755d4c58c1ba thanks for watching
   20:20 <shimizukawa> future-unicorn:    .. autoflask:: app.api:app is indented that is not correct.
   20:22 <future-unicorn> shimizukawa: should it never be indented?
   20:32 <shimizukawa> In this case, the statement means "   .. autoflask:: app.api:app" is a content  of "toctree" directive.
   20:32 <shimizukawa> However, toctree directive doesn't take other directive.
   20:45 <future-unicorn> ok thanks :)
   22:26 <future-unicorn> shimizukawa: Remove indentation just gave me errors because of missing docstring on some functions, but with these docstrings, the output just contains doc about de static path and sphinx-build does not give any error, so my functions are still undocumented
   22:26 <future-unicorn> I don't know where I could have missed something
   Saturday, July 12th, 2014
   10:04 <shimizukawa> future-unicorn: I think your 'sys.path.insert(...)' is not correct. you specified './app'. If you have a 'app' directory that contains  a 'api.py' in the document directory that include conf.py, I think '.' is correct.


7/12 sphinx_bootstrap_themeを使ったらエラー
===============================================

Issue #1507: `AttributeError: 'list' object has no attribute 'startswith'`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1507/attributeerror-list-object-has-no#comment-11200828


以下のように書いたら::

   html_theme_path = [sphinx_bootstrap_theme.get_html_theme_path()]


``AttributeError: 'list' object has no attribute 'startswith'`` というエラーになったので、以下のように書き換えた::

   html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

ドキュメントが間違ってるから更新してほしい、というチケットなんだけど、Sphinxのドキュメントにそのような説明をしているところは無いし、sphinx_bootstrap_themeにも前者のような記述は無かった。謎。ステータスを `修正しない` にしたけど、 `無効` にするべきだったな、ということで今 `無効` に変更した。



7/12 py:function ディレクティブにデフォルト引数 `[]` を渡すと壊れる問題
========================================================================

Issue #1503: `Default parameter with value an empty list ([]) parsed incorrectly.`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1503/default-parameter-with-value-an-empty-list

先週、パッチをもらったけどテストを書いたらちょっと問題があることが分かったので、パッチの更新依頼をしていたやつ (:doc:`../sphinx-dev-20140705/index`)。昨日更新版パッチをもらったので適用したら期待した結果になったので即取り込んだ。



7/13 日本語ファイル名を使うと make singlehtml でエラーになる
=================================================================

Issue #1508: `Non-ASCII filename raise exception when make singlehtml`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1508/non-ascii-filename-raise-exception-when

`Sphinx-users.jp ML でのバグ報告`__ がきっかけで直したバグ。

.. __: http://www.python.jp/pipermail/sphinx-users/2014-July/000997.html

Sphinxの日本語ファイル名対応を行った際に、文字列を ``str`` に変換しているところを全て ``unicode`` に変換するように修正したつもりだったけれど、1箇所漏れていたっぽい。それが、 `singlehtml`, `latex`, `man`, `texinfo` と言った1ファイルにまとめる系のビルダーで使われている関数に埋まっていた。

これを修正している際に、 `changes` ビルダーがlatin1でファイルを読み込んでlatin1で書き出す実装をしていて、日本語ファイル名を使っているとchangesの出力にファイル名も書き出すために、 ``codecs.open(..., encoding='latin1')`` で開いたファイルにUnicodeオブジェクトなファイル名を書き出そうとしてUnicodeEncodeErrorが起きていた。

日本語ファイル名を使う人は今まで make singlehtml とかやってなかったんだろうなあ。

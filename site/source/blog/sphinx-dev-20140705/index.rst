:date: 2014-7-5 17:40
:tags: Python, Sphinx
:body type: text/x-rst

====================================================================
2014/07/05 Sphinxメンテナ日記(6/22-7/5): なんか幅広い知識が要る感じ
====================================================================

前置き: チケットとメールとIRCで対応した内容のメモです。最近、英語のIRCチャットに抵抗がなくなりました。 IRCCloud_ 便利ですね。

.. _IRCCloud: https://www.irccloud.com/

**先にまとめ**

最近は、チケットやメールを「あとでやろう」と思うとそのまま1年以上放置しちゃってよくないということにやっと気づいたので、出来るだけその日のうちに手を付けるようにしてます。そのためか、この一週間でけっこう数は進めてたのにまとめてて気づいた。まとめも都度メモしていかないと思い出すのが大変なので、次からそうしよう。

処理の優先度としては、Pull Requestは最優先で確認。せっかくコントリビュートしてくれてるのに放置すると協力者減っちゃうし。とはいえ、だいたいテストコード付いてないので、動作確認してテストコード書くのはそれなりに時間がかかるので、大きな変更でテストコード付いてないのは、テストコード書いてねって返すことにします。

Pull Requestの次にIRCとメールだけど、誰かが返事してたら放置。次にチケット。新機能のリクエストはいつ対応するかだけ判断して放置になりがち。最後に次期リリースの作業。いつまでたっても次期リリースに到達しない感じがするのがつらいところ。

英語のメールを書くのは、ちょっとした文面でも1時間くらいかかるので敬遠してしまっていたのを意識して書くようにしてます。同じ理由で、英語のリアルタイムチャットは、返事に時間がかかるので、待たせちゃうどうしよう、とか思ってしまって苦手。ただ、ここ半年ほどコミュニケーションが英語の仕事をしていて、日々英語チャットしてたら慣れました。間違って書いても大体通じるし、頻出するちょっとした言い回しをマネできるようになったのが収穫。 "I'll take a look" とか "Please take a look if you have a chance" とか "not sure" とか。

SphinxのチャットはIRCの #sphinx-doc チャンネルで行われてるんだけど、IRCは接続してないときのログが失われるのもあって昔から苦手だったけど、最近は IRCCloud_ を使うことでその問題もちょっと解消。クライアントアプリを使わずにWeb画面をChromeのアプリ化(Windows)して使っているけど十分使いやすい。無料プランでもiPhoneアプリ使えるし、クライアントがオフラインでも2時間は接続維持してログ残してくれるし。$5/月 で24時間接続維持。まだそこまでは要らないかな。

メンテナ日記書き始めてから思ったのは、Sphinxのようなものをメンテするとコードやら環境やら知らないことばっかりで、サポートするのも想像付かないようなことばっかりで、これを一人でやってたGeorgすげー、って感じ。速度的にまったく追いついてないけど、実践で素振りできる環境でもあるので、素振りの質の向上につとめたい。


以下、各チケットとかの対応でやったこと。書いてみたら超長くなった。

.. contents::
   :local:



6/21 クラス内クラスがautodocで正しくドキュメント化されない問題
===============================================================

Sphinxはインナークラスをドキュメント化うまく出来ない、と思って回答してから調べてみたら、リリース当初から対応していたことが分かった。はやとちりスミマセンでした。

IRCより::

   Saturday, June 21st, 2014
   07:13 <patweb> Has anyone attempted to use autoclass to document a python subclass (2nd level down class) within a module? This does not look possible from what I see.
   08:23 <shimizukawa> patweb: hum.. please describe a detail or give me a small sample.
   08:25 <patweb> path of module is "this.is.my.module". Within the module is a class and a sub-class "this.is.my.module.Class.SubClass". Subclass does not get captured by the autoclass feature
   08:25 <patweb> Instead it gives an error stating that it cannot find the module Class (which is above SubClass in this case)
   08:30 <shimizukawa> ah, I got it. I think you means a Inner Class.
   08:32 <shimizukawa> IIUC, Sphinx autodoc doesn't support inner class.
   08:38 <patweb> Yeah an inner class. sorry
   08:38 <patweb> Bummer that it's not supported
   08:38 <shimizukawa> mmm.. maybe my understanding is not correct...
   08:38 <shimizukawa> https://groups.google.com/d/msg/sphinx-users/VYs9K4fzguI/IIGSga5BevcJ
   08:40 <patweb> great find shimizukawa! This is what i was looking for
   08:46 <shimizukawa> :)


6/25 docstring内に'0x00'と'0xFF'があるとhighlightingに失敗する問題
===================================================================

Issue #1497: `Exception occurred while 'make html'`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1497/exception-occurred-while-make-html

っていうかどうしてそんなdocstring作るんだ。再現方法わからなかったし。投稿者が匿名だし。

チケット作成者が匿名だと、再現手順聞きたくてもだいたい反応もらえないことが多い。再現手順待ちのときはステータスをHOLDにしてるけど、匿名のHOLDチケットはけっこう埋まってると思う。


6/26 docstring内の末尾バックスラッシュがドキュメントを壊す問題
===============================================================

サンプルコードが長いので末尾に\マークを置いて改行したら、ドキュメントが次の行と連結されちゃったらしい。

こんな感じに書いてた:

.. code-block:: python

   def search(self):

       """
           some description text

           >>> bugs = bugzilla.search_for\
           ...                .keywords("checkin-needed")\
           ...                .include_fields("flags")\
           ...                .search()
       """

ちょっと試してみて、docstringのパース時になにか壊してる？とか思ったけど、docstringの先頭に ``r`` を付けてエスケープすればよいことに気づいて解決。普段文字列リテラル内の行末尾に ``\`` を書くことがないので、一瞬悩んだ。

.. code-block:: python

   def search(self):

       r"""



IRCより::

   Wednesday, June 25th, 2014
   07:18 <AutomatedTester> Hi, is there a way to document something as multiline. I tried https://github.com/AutomatedTester/Bugsy/blob/master/bugsy/search.py#L67 but it comes up as 1 line.
   08:00 <rafaelmartins> AutomatedTester: this should help: http://sphinx-doc.org/markup/code.html
   08:01 <AutomatedTester> rafaelmartins: do those work with docstrings?
   08:01 <rafaelmartins> AutomatedTester: of course... docstrings are valid rst
   08:01 <rafaelmartins> afaik
   08:02 <AutomatedTester> hmmm
   08:15 <AutomatedTester> rafaelmartins: cant seem to make it work
   10:02 <rafaelmartins> AutomatedTester: can you paste your docstring somewhere?
   21:26 <AutomatedTester> rafaelmartins: https://github.com/AutomatedTester/Bugsy/blob/master/bugsy/search.py#L67 thats the docstring I want to be multiline
   22:20 <shimizukawa> AutomatedTester: the docstring need `r` prefix
   22:20 <shimizukawa> def search(self):
   22:20 <shimizukawa>      r"""
   22:20 <AutomatedTester> aha
   22:21 <AutomatedTester> shimizukawa: let me try that quickly
   22:21 <shimizukawa> sure :)
   22:22 <AutomatedTester> shimizukawa: that works a treat! THanks
   22:23 <shimizukawa> ;)


6/27 onlyディレクティブでセクション名が予期しないところにぶら下がる
====================================================================

Issue #1488: `Only Directive does not order text as expected`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1488/only-directive-does-not-order-text-as

:rst:dir:`only` ディレクティブ内にセクションを書いたら、親子関係のなさそうなところに子セクションがぶらさがってしまったという話。こんな感じ:

.. code-block:: rst

   ====
   top
   ====

   1.
   ====

   1.1.
   -----

   .. only:: flag2

      2.
      ===

   .. only:: flag21

      2.1.
      ------

flag2, flag21 両方とも真の状態で、 ``2.1.`` が 1. の子で 1.1. の兄弟になってしまった。

reST的には(docutils的には)、1.1. のコンテンツとして `.. only:: flag2` ディレクティブがあって、ディレクティブの中身のコンテンツも当然 1.1. の子要素になるけれど、 `2.` セクションが `1.1.` セクションの子になるのはおかしい。docutilsの実装としては、こういうのはエラーになる。

Sphinxのonlyディレクティブはこれをエラーにせずdoctree化する。その過程で、 `2.` が `1.1.` の子にならないように、内部のdoctreeを作る段階でツリー構造的に `2.` を同じレベルの  `1.` の兄弟として `top` にぶらさがるように調整する。HTML等に書き出すときにflagをチェックするので、onlyのノードはこの時点では残っている。ここまではこんな感じ::

   top
      1.
         1.1.
      <only flag2>
         2.

HTMLやPDFに書き出す際に、flagの真偽にかかわらず<only>ノードは消滅する。
偽の時は<only>ノードの子要素ごと消えるので以下のようになる::

   top
      1.
         1.1.

真のときは<only>ノードの子要素を残すので以下のようになる::

   top
      1.
         1.1.
      2.


`2.1.` も同様に、既に出現している同じレベルのセクション `1.1.` の兄弟として `1.` にぶらさがる。結果として、doctreeは以下のようになる::

   top
      1.
         1.1.
         <only flag21>
            2.1.
      <only flag2>
         2.

ここで、今の実装では `2.1.` は `2.1.` の下にはぶら下がれない。flag2が偽でflag21が真のときに困っちゃうから。代替案があるとすれば、以下のようなdoctreeを生成して、flag2が偽の場合は内包する子要素をまとめて消滅させる感じだろうか::

   top
      1.
         1.1.
      <only flag2>
         2.
            <only flag21>
               2.1.

その場合、後方互換性はなくなるので、変えるの面倒だなあ・・・。とはいえ、現状の実装が分かりやすいかというとそんなこともないので悩ましいところ。

この問題について言及したチケットとblog。

* `Issue #1115: 'only' directive exhibits strange behavior with headers`__
* `'ドキュメントを部分的に公開/非公開にしてビルドする'の実用例 - logiqboard`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1115/only-directive-exhibits-strange-behavior
.. __: http://feiz.hateblo.jp/entry/2012/12/18/153701

ということで、チケットにこのことを書いて、意見ちょーだいと書いて、 Hold。


6/29 UnicodeError問題、報告者が作ったSphinx拡張が原因だった
============================================================
Issue #1196: `Encoding clash when reading sources`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1196/encoding-clash-when-reading-sources


壱年前に一度、Sphinx-1.1.3 がPython3.3に対応してないせいで起きてる問題だと思って返事していたけど、Sphinx-1.2.xでも問題が出るというので再調査。よく見てみたら、トレースバックに、報告者が作った拡張のコードが入っていて、そのコードを見てみたらエンコーディングがdocutilsの期待と合っていなかった。ということで、Invalidにして終了。

気分の問題だけど、Invalidにするのはなんとなく心苦しい感じがする。


6/30 conf,py内で import setup するとmake htmlでエラーが出る問題
================================================================
Issue #1499: `Make "build_sphinx" error more user-friendly when importing setup.py from conf.py`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1499/make-build_sphinx-error-more-user-friendly

conf.py の中で、パッケージのsetup.pyをimportしてパッケージ情報などをドキュメントタイトルなどに利用使用としたようですが、make htmlすると ``module object is not callable`` というエラーが発生したとのこと。

SphinxはSphin拡張(プラグイン)の初期化のために、Sphinx起動時に各拡張のsetup()関数を呼び出す。conf.pyの中にsetup関数を用意すると、conf.py自体をSphinx拡張とみなしてsetup()を呼び出す。 という話が :confval:`extensions` にある。

conf.pyでsetupモジュールをimportしたために、SphinxがSphinx拡張のための関数と勘違いして関数呼び出ししたけど、関数じゃ無くてモジュールだったからエラーになった、という話でした。そこだけ聞くと、setup.pyをimportするなよって思うけど、エラーメッセージがらはヒントがなさ過ぎて自己解決出来なそうだったので、 **Sphinx拡張用のsetupがあったけど呼び出し出来なかったよ、拡張として動作させるためには呼び出し可能なオブジェクトにしてね** というメッセージを表示するように変更した。

今回はエラー停止するように実装したけど、Warning表示してビルド継続するのとどっちが良いかちょっと悩んだ。どうしてエラー停止の方を選んだか既に忘れているので、こういうメモはその日のうちにとらないとダメだな、と改めて思った。

この変更は Sphinx-1.2.3 に含まれます。


7/1 メソッドのデフォルト引数に `'\n'` を使用するとautodocで `'n'` に化ける問題
===============================================================================

Issue #1502: `'\n' in method default args gets munged in autodoc output`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1502/n-in-method-default-args-gets-munged-in

関数でも同じ問題があって、 Sphinx-0.6.6 で修正済みだったけど、メソッドの方で修正漏れてたという話。こういう仕様に関わる処理は2行程度であっても関数に切り出して共通化したほうがいいんだろうな。やってないけど。テストは書いたよ。

この変更は Sphinx-1.2.3 に含まれます。


7/2 コードハイライトを行番号付きで表示するとHTMLページが横に長くなる問題
=========================================================================

ML: `literalinclude and long lines`__

.. __: https://groups.google.com/d/msg/sphinx-users/dKCgqUJcp4M/F8PuLHndBdcJ


:rst:dir:`literalinclude` に ``:linenos:`` オプションを付けるとHTMLが行番号表示と内容表示のためにtableレイアウトになり、テーブルが中身の幅の分だけ広がってしまうという問題。CSSを追加すれば解決。


1. 以下の内容の _static/custom.css ファイルを追加::

    table.highlighttable {
        table-layout: fixed;
        width: 100%;
    }

    table.highlighttable td.linenos {
        width: 1em;
    }

    table.highlighttable td.linenos div.linenodiv {
        text-align: right;
    }

2. conf.py にsetup関数を追加::

    def setup(app):
        app.add_stylesheet('custom.css')

これ、Sphinxのバグっぽいよね。

4日遅れで回答。users ML に返事しても半分くらいは返事が返ってこないのが寂しいかぎり。返事したものをあつめてFAQ作れば質問減るんだろうか。減らないだろうなー。



7/2 py:function ディレクティブにデフォルト引数 `[]` を渡すと壊れる問題
=======================================================================

Issue #1503: `Default parameter with value an empty list ([]) parsed incorrectly.`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1503/default-parameter-with-value-an-empty-list

py:functionを使ってPythonの関数引数を表現する場合、 :ref:`signatures` で説明されているように、以下のように記載する。

.. code-block:: rst

   reST: .. py:function:: func(a, [b=None])
   HTML: func(a, [b=None])

上記は引数bが省略可能という意味。

.. code-block:: rst

   reST: .. py:function:: func(a[, b=None])
   HTML: func(a, [b=None])

これも最初の例と同じだけど角括弧の位置がちょっと違う。HTMLでは最初の例と同じ表示に揃えられている。

このチケットで指摘していたのは以下のパターン。

.. code-block:: rst

   reST: .. py:function:: func(a, [b=[], [c=None]])
   HTML: func(a, [b=, [], [c=None]])

確かにこれはバグっぽい。 `[]` が空リストなのか、省略可能なことを意味する記号なのかが混同されてしまっているっぽい。

チケットで提示してくれていたパッチを適用すると、以下のように修正された。

.. code-block:: rst

   reST: .. py:function:: func(a, [b=[], [c=None]])
   HTML: func(a, [b=[], [c=None]])

ところが、テスト書いてみたら惜しい結果になった。

.. code-block:: rst

   reST: .. py:function:: func(a[, b=[][, c=None]])
   HTML(期待): func(a, [b=[], [c=None]])
   HTML(実際): func(a[, b=[][, c=None]])

最初の1組の例と整合性とれてないけど、現状のバグっている状態よりはまあましかもしれない？

せっかくパッチ書いてくれたので、ついでにこれも直して欲しいと伝えて、Open状態。来週中に返事なかったら自分で直そう。



7/3 imageのscaleが効かない問題（PIL名前空間問題）
===================================================

Issue #883: `img "scale" option is broken for HTML output`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/883/img-scale-option-is-broken-for-html-output

Sphinxの image / figure ディレクティブの :scale: オプションは、PIL / Pillow がインストールされていないと、Warningも出さずにリサイズをあきらめる。 :width: はPILなしでも動作するけど、画像は元サイズのままHTMLで無理矢理縮ませる。

ということで、これは「PILインストールしてない問題」または「PILインストールしたけどSphinxがPILをimportできない問題」と言える。

2012年当時、PILのインストール方法によって、 ``import Image`` と ``from PIL import Image`` のどちらかだけがOK、あるいは両方OK、という状況があった。というか今もある。

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :widths: 2 1 1

   - -
     - import Image
     - from PIL import Image

   - - (A) PIL + pip等
     - ○
     - ○

   - - (B) PIL + buildout
     - ○
     - ×

   - - (C) Pillow + pip等
     - ×
     - ○

   - - (D) Pillow + buildout
     - ×
     - ○

(A)や(B)のときにbuildoutでPIL名前空間を扱えなかったのは、PILのパッケージングの仕方がよくなかった事と、buildoutがPIL.pthファイルを扱えなかった事の両方に問題があった、と思う。PILがPIL.pthというファイルで、あたかもPILという名前空間があるかのように調整を行っていたがbuildoutはpthファイルを参照しないため上記(B)のように「buldoutでPILをインストールするとPILがimportできない」という問題があった。

この頃、みんな以下のような対処方で回避していた。

.. code-block:: python

   try:
      import Image
   except ImportError:
      try:
         from PIL import Image
      except ImportError:
         Image = None


しかし、グローバルな名前空間に ``Image`` というモジュールを置くのはどうなの？という話もあり、PIL後継のPillowではPILという名前空間を省略できないように、ちゃんとパッケージングした。

その結果、(C), (D) のように、buildoutでもpipでもその他のインストール方法でも、PIL名前空間は省略できなくなった。ここで、「import Image でいいんだ」と思って実装していた、古いSphinxを含むサードパーティーライブラリはPillowで動作しなくなった。

最近はもうPillowでしょ、と思いつつも、PILのサイトもPyPIページも残っているので、本とか読んでPILをインストールする例はこれからもありつづけそう。

Pillowが後継だというなら、PILから権利を譲ってもらうなりして引き継げばいいんじゃないの？という話もあるけど、PILの開発元は企業なので、なかなか難しそうである。先日aodagがPillowの開発コミュニティーに意見を投下 (`Should I use Pillow or PIL?`__)したけど、まあ難しそう。

と言うことで、ライブラリとツールの組み合わせによって挙動が変わってくる「PILがimportできない問題」、同じチケットに環境情報なしに「おれもおれも」って書かれても解決しなかったりするので、「Sphinxの新しいバージョン使おう、Pillow使おう、だめなら別チケットよろ」って書いて、HOLDからClosedに変更した。

.. __: https://github.com/python-pillow/Pillow/issues/705


7/4 autodoc で setup モジュールをimportする問題
=================================================

* ML: `option -b not recognized?`__

.. __: https://groups.google.com/d/msg/sphinx-users/cOCOVCO9NbQ/zVXMbuqjNFkJ

2012年にSphinx-users MLに投稿された内容::

   sal@bobnit:~/workspace/jenkinsapi/doc$ sphinx-build -b html source build
   Running Sphinx v1.1.2
   usage: sphinx-build [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
      or: sphinx-build --help [cmd1 cmd2 ...]
      or: sphinx-build --help-commands
      or: sphinx-build cmd --help

   error: option -b not recognized

   なにが起きてるの？なにか壊れた？

当時は ``sphinx-build`` コマンドが壊れてなにか不思議な挙動をしているようにしか思えなかった。

これが昨日、IRCで質問を受けてreSTを眺めていたときに突然解決した。そのときのチャットの内容は同件問題のチケット #1226 に貼っておいた。

* Issue #1226: `Sphinx runs my code, then crashes`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1226

全ては、setup.pyをautodocでドキュメント化しようとして、パッケージのセットアッププロセスが実行されたためにおきていた。

1. setup.pyって以下のように書くじゃないですか::

      from setuptools import setup

      setup(
          name='spam',
          version='1.2.3',
          ...
      )

2. お行儀悪い慣習のために、いちいちsetup()を ``if __name__ == '__main__':`` ブロックには書かないじゃないですか。
3. そんなのをimportしたらsetup()関数実行されちゃうじゃないですか。
4. setup関数はsys.argv見て引数間違ってたらsys.exit()するじゃないですか。
5. error: option -b not recognized


ということで、setup.pyをimportするとかSphinxのautodocで自動ドキュメント化の対象にするとか考えてはいけない。

ところが、 sphinx-apidoc を使うと、指定ディレクトリの.pyファイルを見つけて自動的にautodoc用のrstファイルを生成してくれるので、setup.pyと同じ階層にソースコードがあるとsphinx-apidocコマンドの対象になってしまい、ドキュメント作者が意図せず setup.py をautodocの対象にしてしまう。たぶん、これが根本原因。

ということで、謎問題の再発を防止するためにSphinxの挙動を一部変更した。

Sphinxのautodocがドキュメント化のためにモジュールをimportしたときに、SystemExit例外が発生したら、「○○モジュールimportしたらsys.exit()呼ばれたっぽいよ」というWarningを表示して、そのとき発生したtracebackは握りつぶす（error: option -b not recognized とか表示されても混乱するだけなので）。

この変更は Sphinx-1.2.3 に含まれます。


7/4 Windowsでコンソールのカラー表示
====================================

* Issue #1291: `Color on Windows Cmd Prompt`__
* Pull Request #252: `Windows color support on cmd`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1291/color-on-windows-cmd-prompt#comment-11079197
.. __: https://bitbucket.org/birkenfeld/sphinx/pull-request/252/windows-color-support-on-cmd

colorama_ というライブラリを使えば、WindowsでもANSIカラーシーケンスで正しく文字色を変えられるよ。というチケットをもらっていたけど、新機能は後回しでいいや、と思ってたらPull Requestをもらったので速攻取り込んだ。待ってみるものである（違う）。

結局PR取り込む前に動作確認したり、実装を適切なものにしたりと色々やるのでPRはきっかけでしかないけど、気分的には使い方調べるところからやるよりだいぶ楽。

多分環境によらず正しく動作するはずだし、Windows以外では有効化されないように実装したのだけど、若干不安は残る。

この変更は Sphinx-1.3 に含まれます。

ところで、coloramaってコロラマって読むのね。バラの品種だったり色調整ツールの名前だったりするらしい。


.. _colorama: https://pypi.python.org/pypi/colorama


7/5 make coverage が無い問題
=============================
Pull Request #159: `Add coverage targets to quickstart generated Makefile and make.bat.`__

.. __: https://bitbucket.org/birkenfeld/sphinx/pull-request/159/add-coverage-targets-to-quickstart/diff

Makefileとmake.batに coverage ターゲットが無いので追加する変更のPR。sphinx.ext.coverage を有効化してないと使えないのでMakefileに入れるのをためらっていた。

PRにコメントを書いて、それへの反論が来てたのを1年放置しました。ごめんなさい。

Sphinxのmake-modeがcoverageも対象にしていることに、今朝ふと気づいたのでマージ。PR出してくれた人、あきれてるだろうなあ・・。

この変更は Sphinx-1.3 に含まれます。


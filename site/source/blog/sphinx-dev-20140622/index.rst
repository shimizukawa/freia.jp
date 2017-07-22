:date: 2014-6-22 19:00
:tags: Python, Sphinx

==============================================================================
2014/06/22 Sphinxメンテナ日記: 翻訳機能と、シンタックスハイライトと、 @tk0miya
==============================================================================

前置き: チケット対応した内容のメモです。Sphinxと関係ないけどdiff-highlight便利でした。

.. contents::
   :local:


Sphinxの国際化機能を使っても翻訳されないんだけど
=================================================

sphinx-users ML: `help with internationalization`__

.. __: https://groups.google.com/d/msg/sphinx-users/8DC7eyhYzEA/P3FWSnBfK3gJ


**Q.** http://sphinx-doc.org/intl.html#intl を見ながらSphinxの国際化機能を使ってみたけど、一部が翻訳されないんだけど？


**A.** 翻訳されていないのはSphinxが提供している部分の文字列だね。Sphinxが提供する文字列の翻訳はSphinx自体が翻訳カタログを持っているんだけど、 `ソース`__ を見ると ``el`` 言語のカタログは無いようだね。Sphinxのシステムが提供する文字列の翻訳は `Transifexというサービス`__ で行っていて、各言語の翻訳はSphinxの利用者たちが行ってくれているんだ。もし翻訳に興味があれば、Transifexで ``el`` 言語をリクエストして翻訳を行ってみてほしい。

.. __: https://bitbucket.org/birkenfeld/sphinx/src/ba4b069e/sphinx/locale/
.. __: https://www.transifex.com/projects/p/sphinx-1/


メールの送信者が ``sphinx el`` だったので、 ``el`` 言語というのが分かったけど、推理ゲームじゃないのでメールの文面に書いて欲しいところ。

SphinxはSphinx自体が持っている文字列の翻訳カタログ（HTMLのPrev, Nextなどのメニューなど）と、利用者が書くドキュメントの翻訳カタログの2つがあるので、初めて使う人はその違いが分からないという事例。ドキュメントにもそのあたりは触れていなかった。 メールの返信を書くためにドキュメント調べて初めて気づいた。どこかに書いた方が良いんだろうなー。


code-blockで書いたSQLのハイライトが、$書いたらハイライトされなくなった
=======================================================================

Issue #1494: `$-sign in code-block directive removes syntax highlighting`__

.. __: https://bitbucket.org/birkenfeld/sphinx/issue/1494/sign-in-code-block-directive-removes

SQLのシンタックスハイライトをしようとしたら、SQL文内に ``$`` サインがあるとシンタックスハイライト出来なかった。という話。

pygmentizeコマンドで実験してみたら ``$`` がエラー扱いになってた（以下の出力は見やすいように整形済み）:

.. code-block:: html

   $ echo SELECT * FROM v$sql; | pygmentize -f html -g
   <div class="highlight"><pre>
     <span class="n">SELECT</span>
     <span class="o">*</span>
     <span class="n">FROM</span>
     <span class="n">v</span>
     <span class="err">$</span>
     <span class="n">sql</span>
     <span class="p">;</span>
   </pre></div>


Sphinxは指定された言語でのpygmentizeに失敗すると、 'none' という言語(無変換?)でハイライトし直すので、 ``$`` があるとハイライトされなくなるというわけ。

ということで、pygmentsのissue trackerを案内して "保留"。"修正しない" ステータスでもよかったかな・・。チケットの閉じ方はいつも悩む。一応以下のように考えている。

* 保留 Hold
   追加の情報を出してもらいたい場合。bitbucketでは保留はCloseと同じ扱いなので、
   追加情報もらえなくてもそのまま忘れられるので便利。

* 解決済み Resolved
   修正した場合。Sphinxのコードを変更した場合はだいたいこれを使う。
   コミットメッセージに Closes #1234 とか書いてpushすると解決済みになる。

* 修正しない Won't Fix
   修正する気が無い。依存ライブラリの問題だった場合。Sphinx自体に問題はあるけど
   修正せず、ワークアラウンドで対処してもらう場合など。

* 無効 Invalid
   レポート自体が間違っている。依存ライブラリの問題の場合は「無効」なのかも
   しれないけど、Georgが無効を使わないのでそれに倣っている。

* 重複 Duplicated
   ほかのチケットと同件の場合。
   bitbucketの翻訳が間違ってて「複製する」って表示されるけど。
   ``Duplicate`` って翻訳難しいよね。

* Closed
   単に閉じたい時？使いどころが分からないけど、上記のどれにも当てはまらない
   場合はこれを使う。一度だけ使った。

いきなりCloseにされたらどう思うかなーと思って保留にしたけど、どう思おうがSphinxでなんとかする気は無いので、やっぱり ``修正しない`` でCloseしよう。


ドキュメントの、単語、文法、79文字改行の修正
=============================================

Pull request #251: `Spelling, grammar, and formatting fixes for docs`__

.. __: https://bitbucket.org/birkenfeld/sphinx/pull-request/251/spelling-grammar-and-formatting-fixes-for/diff


31ファイルの多数のスペルミスや文法ミス、80文字目までかいていた部分の79文字での改行への修正をPRいただきました。このPRの差分に、smartypantsに言及している部分に http://daringfireball.net/projects/smartypants/ へのリンクが追加されていたのですが、smartypantsの出自がLaTeX界隈だと思っていたけど、違うようだ、ということが分かりました。

ところで、このPRは文章の改行位置の変更と単語のスペルミス修正が行われているため、bitbucketのWeb上で差分を確認するのが大変でした。そこで、 `tk0miya作のdiff-highlight`__ をhgコマンドに組み込んで確認したらかなり楽でした。 @tk0miya さん、いつも役立つツールを作ってくれてありがとう！

.. __: http://tk0miya.hatenablog.com/entry/2013/12/22/155358


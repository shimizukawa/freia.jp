:date: 2004-08-16 12:09:23
:categories: ['Zope', 'python']
:body type: text/x-rst

=============================
2004/08/16 No module named ja
=============================

*Category: 'Zope', 'python'*

reST表示でZopeがリブートする問題_ は解決しました。

原因は、 StructuredText日本語問題_ に対応するために、DocumentClass.pyなど修正・コンパイルしたせいか、あるいはweather_pluginを入れるためにentry_bodyを修正したせいか、、、。

解決法としては、エラーメッセージから適当に当たりを付けて、jaモジュールをでっち上げてみました。

.. _reST表示でZopeがリブートする問題: http://www.freia.jp/taka/blog/61
.. _StructuredText日本語問題: http://www.freia.jp/taka/blog/4



.. :extend type: text/x-rst
.. :extend:

エラーメッセージは、以下のようなものがreStructuredTextのレンダリング時にコンソールに表示されていました::

  No module named ja
  Exiting due to error.  Use "--traceback" to diagnose.
  Please report errors to .
  Include "--traceback" output, Docutils version (0.3.4),
  Python version (2.3.4), your OS type &amp; version, and the
  command line used.

最初のうちは *Use "--traceback" to diagnose* に気を取られていたのですが、どうやってZopeからOptionを指定すればいいのかが分からなかったため、そもそもの問題である *No module named ja* に着目してみました。docutils/languages 以下を見てみると、en.pyと言うのはあるのですが、ja.pyは見あたらなかったため、とりあえずen.pyをja.pyにコピー&amp;コンパイルしてみたところ、問題が解消されたようです。

ちなみに、コンパイルには以前教えてもらった方法「pythonを起動して import ja などとする」を行いました。pythonのコマンドラインオプションでpycを作る方法よりもお手軽です。

それにしても、インストール当初は何ともなかったのに何が原因でdocutilsが異常動作するようになってしまったのかがわかりません。 象歩Blog_ によると「Zope で Locale の扱いに問題がある」ようですが、症状発生の原因はやはりよくわかりませんでした。

.. _象歩Blog: http://owa.as.wakwak.ne.jp/zope/coreblog/96




.. :trackbacks:
.. :trackback id: 2005-11-28.4461481004
.. :title: docutilsのUnitTest
.. :blog name: 象歩Blog
.. :url: http://owa.as.wakwak.ne.jp/zope/coreblog/98
.. :date: 2005-11-28 00:47:26
.. :body:
.. reStructuredText で落ちるのは、 docutils に ja.py
.. ファイルが無いためであることの再確認。 docutils-0.3.5.tar.gz
.. をダウンロードして試してみました。 PYTHONPATH には zope
.. のパスを指定します。 $ tar xvzf docutils-0.3.5.tar.gz $ cd
.. docutils-0.3.5/test $ export PYTHONPATH="/usr/lib/zope/lib/python" $ python
.. test...

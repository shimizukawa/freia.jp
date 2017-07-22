:date: 2005-04-01 22:36:34
:tags: Zope
:body type: text/x-rst

===========================================
2005/04/01 Re: DTMLファイルの中身を表示する
===========================================

[CD]CoffeeDiaryより

  `DTMLファイルの中身を表示する`_

おもしろい命題なので、獲得を使ってZopeっぽく作ってみる。

sourceという名前のScript(Python)::

  print '<pre>'
  print str(context)
  print '</pre>'
  return printed

これをルートディレクトリ等に作る。
実際に表示させるには::

  http://hoge.jp/foo/bar/index_html/source

という感じでアクセスする。（ 実例__ ）

.. __: http://www.freia.jp/taka/test/view_source/index_html/source

.. _`DTMLファイルの中身を表示する`: http://akiyah.bglb.jp/blog/642



.. :extend type: text/plain
.. :extend:



.. :trackbacks:
.. :trackback id: 2005-11-28.4906685706
.. :title: DTMLの中身表示は簡単だった
.. :blog name: [CD]CoffeeDiary
.. :url: http://akiyah.bglb.jp/blog/654
.. :date: 2005-11-28 00:48:10
.. :body:
.. 『DTMLファイルの中身を表示する』に対して
.. 清水川さんのところで獲得を使ったZopeらしい方法が紹介されていました。
.. なるほど。
.. ルートとかで作れば獲得で下のほうのフォルダからも使えるのですね。
.. さらに、この方法だとURLで指定してソースを見ることが出来るのですね。
.. 勉強になります。
.. こちらではまた別の方法を見つけてしまいました。
.. たとえばfooという名前の DTML Method があったら、
.. と『"』で囲ってあげるだけでソースが見られるのでした!
.. なーんだ。
.. というか、逆に『"』で囲っちゃ...

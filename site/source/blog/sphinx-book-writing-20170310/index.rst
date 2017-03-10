:date: 2017-03-10 22:30
:categories: ['Sphinx']
:body type: text/x-rst

==========================
2017/03/10 Sphinx本の執筆
==========================

*Category: 'Sphinx'*


`Sphinxをはじめよう`_ の改訂作業をやってます。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">Sphinx本の執筆中です。セルフカンヅメです。 (@ 喫茶室ルノアール 市ヶ谷駅前店 in 千代田区, 東京都) <a href="https://t.co/Ix1FXs53z2">https://t.co/Ix1FXs53z2</a> <a href="https://t.co/qZdpZn3efF">pic.twitter.com/qZdpZn3efF</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/840189438135271424">2017年3月10日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


いくつか章を追加したり、全体的にバージョンを最近の状況に合わせて更新したり、Appendixのリファレンスを書き足したりしてます。自分はリファレンス書き足しを担当してるので、どれを書き足そうかというのを調べるためにリストアップしてみました。

* reSTの文法: 13
* reSTのRole: 11
* reSTのDirective: 29
* SphinxのRole: 24
* SphinxのDirective: 15
* Sphinxの置換、docinfo: 少々
* Sphinxのドメイン: たくさん

...多すぎました。できるだけ載せたいと思ったけど、絶対使わないのとかもあるので、覚えておくと便利なあたりをピックアップしよう。

ところで、調べてたら知らなかった便利そうな記法に出会ったので紹介します。
`クオートリテラルブロック`_ です。

今日覚えた記法
=================

`クオートリテラルブロック`_

こう書きます::

   John Doe wrote::

   >> Great idea!
   >
   > Why didn't I think of that?

   You just did!  ;-)

こうなります:

--------------

John Doe wrote::

>> Great idea!
>
> Why didn't I think of that?

You just did!  ;-)

--------------

今まで、メール引用やチケット引用をreSTで書くとき面倒くさかったけど、クオートリテラルブロックを使うと良い感じに表示してくれました。こういうのこそ本に載せよう。


.. _Sphinxをはじめよう: http://www.oreilly.co.jp/books/9784873116488/
.. _クオートリテラルブロック: http://docutils.sphinx-users.jp/docutils/docs/ref/rst/restructuredtext.html#quoted-literal-blocks


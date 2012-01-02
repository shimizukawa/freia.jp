:date: 2006-01-28 13:22:34
:categories: ['Zope', 'Plone', 'IT-PC']
:body type: text/x-rst

===============================
2006/01/28 spamとの戦い（回顧編）
===============================

*Category: 'Zope', 'Plone', 'IT-PC'*

なにやらCOREBlogユーザーに大量スパムが投下されたらしい。

  - `スパムコメントたっぷり`_
  - `コメントスパム、、、`_
  - `分散型コメントSPAMツールが来てたらしい`_

.. _`スパムコメントたっぷり`: http://www.junktest.net/zope/junya/524
.. _`コメントスパム、、、`: http://z1r.dip.jp/COREBlog/376
.. _`分散型コメントSPAMツールが来てたらしい`: http://sitebites.homeip.net/blog/115


うちは特に今回は来なかったけど、今までがひどかったのでちょっと歴史としてまとめてみる。ちなみに右の画像は、10月から先のspam投稿数をグラフ化したもので、こうやってまとめてみると今月の **97件が少なく見える** という先月までのspamの多さ！ほんと勘弁して。。。

COREBlog1 未フィルタ期
-----------------------

2005年10月頃。何かに目を付けられたらしく、数分で数十件のspamが来るようになった。この頃はCOREBlogのコードを見始めたばかりだったのでspam-filterを作る事も出来ずとりあえず一括削除するための後ろ向きな対策をしてみたり ( http://www.freia.jp/taka/blog/257/ )。

その後しばらくspam削除の日々が続く。


COREBlog1 フィルタ期
----------------------

2005年某月、lirisさんとこの `COREBlogのコメントスパム対策 ― Emerge Technology`_ を参考に、buzz wordsフィルタリングを行ってみる。禁止語辞書は過去のspamとかから抽出。20語くらい追加したところで、ふと思い立って ``href`` を禁止語に加えてみる。効果覿面。

同じ時期に、せとみつさんも `blogSetomits : コメントスパム弾き実験 3`_ とか `blogSetomits : COREBlog で言及リンクのない TrackBack ping を弾く`_ とか色々とされていた。

.. _`COREBlogのコメントスパム対策 ― Emerge Technology`: http://www.liris.org/blog/626

.. _`blogSetomits : コメントスパム弾き実験 3`: http://matatabi.homeip.net/blog/setomits/473

.. _`blogSetomits : COREBlog で言及リンクのない TrackBack ping を弾く`: http://matatabi.homeip.net/blog/setomits/437


COREBlog2 設置初期
--------------------

2005年11月29日。Zopeを2.7系から2.8系に、Ploneを2.0.5から2.1.1に、そしてCOREBlog1からCOREBlog2αに移行した。移行直後はコメント投稿設定を間違っていたため一切のコメントが投稿できない状態だった。ところがこれを許可したとたん、ものすごい数のspam投稿が。この時点ではまだbuzz wordsフィルタをCOREBlog2用に作っていなかったので、一時コメント投稿を禁止せざるをえくなったりもした。


COREBlog2 フィルタ期
---------------------

2005年12月15日。buzz wordsフィルタをCOREBlog2用に作って設置(`COREBlog2簡易spam-filter ― 清水川Web`_)。これでspamを防げるかと思いきや、PloneとCOREBlog2のコードとかskinとかを知らないと出来ない方法でのspam投稿があることに気づく。Control Page Template の validator を回避して直接投稿してきていた。しかもaction先URLは普通の投稿と同じく見えるように細工までしてあった。 ``:method`` を使ったとしか思えない手の込みよう。

最終的には、直接投稿かどうかを判別する仕組みをCOREBlog2のskinカスタマイズで埋め込んで対処(`[COREBlog 1396] validateCommentを回避`_)。この回避方法で、403を返すようにしたためか、これ以降spamのPOSTリクエストがかなり減少する。

.. _`COREBlog2簡易spam-filter ― 清水川Web`: http://www.freia.jp/taka/blog/coreblog27c216613spam-filter/

.. _`[COREBlog 1396] validateCommentを回避`: http://mail.webcore.co.jp/pipermail/coreblog/2005-December/001395.html


現代
-----
今月は今のところ97件。そのうち以下のIPアドレスが6割を占めているので、さっそくapacheでspam様用にブロックすることにする::

  200.79.91.5
  209.190.4.10
  209.190.4.106
  209.67.219.178

問題は残りの4割。これらはほとんどが異なるIPアドレスなので、やはりbuzz wordsでフィルタするしか無いかと思う。コストの割に効果が高いので、個人サイトならこれでいいや。

別のアプローチとしては、投稿時に画像に書かれた文字列を入れてもらうCAPTCHAを使った方法がある(`COREBlog(2じゃない方)でCAPTCHA ― TRIVIAL TECHNOLOGIES 2.0`_)。面倒がってないでこの方法を導入するのがいいのかもしれない‥‥。


.. _`COREBlog(2じゃない方)でCAPTCHA ― TRIVIAL TECHNOLOGIES 2.0`: http://coreblog.org/ats/coreblog-de-captcha



.. :extend type: text/x-rst
.. :extend:

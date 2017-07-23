:date: 2017-05-27 23:50
:tags: Python, pyhack

=======================================
Python mini hack-a-thon 76回
=======================================

`Python mini hack-a-thon #76`_ (``#pyhack``) に参加しました。

.. _Python mini hack-a-thon #76: https://pyhack.connpass.com/event/55335/


今日やったこと
==============

* 某 :doc:`エキPy 第2版 <../expert-python-programming-2nd/index>` の翻訳を進めました

  翻訳の担当分として3つの章を受け持ってましたが、1つしか終わっていません。がんばります。

* 自分のサイトデザインを更新

  ずっと、 http://www.oswd.org/ にあったデザインをSphinxに組み込んで使っていましたが、スマートフォン向けの画面調整ができなかったり、はてなブックマークの表示用に仕込んだJSが重かったりで使い勝手が悪い状態でした。そこで、  `sphinx-bootstrap-theme <https://pypi.python.org/pypi/sphinx-bootstrap-theme/>`__ に入れ替えて、スマートフォンでも見やすくしました。

  サイトのぱっと見た感じの配色は前のCSSから移植しなおしたのであまり変わらないと思います。

* PyCon JP 2017 のプロポーザルを出した

  こちらです: https://pycon.jp/2017/ja/proposals/vote/54/

  「len()関数がオブジェクトの長さを手にいれる仕組み」 というタイトルで、Pythonのデータ型が実装しているプロトコルについて分かりやすく説明します。ターゲットはPython入門を終えたあたりの人で、このトークが中級者になるための足がかりになればと思っています。Pythonがデータ型の色々な動作を継承なしでどうやって決めているのか、という話を初級の用語でどこまで説明できるかに挑戦します。

  pyhack中にチャットで下書きを共有して、何人かの人に意見をもらいました。
  プロポーザルの段階から晒していって、はやめに叩いてもらうスタイルです。
  詰め込みたいネタがありすぎて内容がぶれている、タイトルがLTっぽい（釣りっぽいと解釈した）、〇〇と書いているその前提は初心者は気づいて無さそう、といった指摘をもらって、細部を修正して、応募しました。
  締め切りまでにもうちょっと磨こうと思います。指摘をくれたterapyon, aodag, driller, 他みなさん、ありがとうございます。

  ところでこのネタ、中級向け、上級向けにもアレンジ可能な話題っぽいので、気が向いたら同じネタで表現変えてプロポーザル出してみようかな。

昼食
====

中華組、沖縄料理組、熟成肉組に分かれて昼食をとりました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">糖質制限食です <a href="https://twitter.com/hashtag/pyhack?src=hash">#pyhack</a> (@ ビストロ熟肉 in 新宿区, 東京都) <a href="https://t.co/c4xZrPsC6z">https://t.co/c4xZrPsC6z</a> <a href="https://t.co/grTr4oxqnu">pic.twitter.com/grTr4oxqnu</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/868314394840707073">2017年5月27日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

自分はビストロ熟肉（びすとろなれにく）へ。豚レバーの熟成肉ハンバーガー美味しかった。豚レバー若干苦手だけど、ここのは美味しい。

やったこと発表
==============

今日は人数少なめだったので、比較的速く進みました。

ここ数回の参加で徐々に実装が進んで行ってる話とか、聴いてて面白いし、イベントやっててよかったなーと思うね。あと実装進まないけど意見交換（雑談）が捗ってるのもこのイベントの特徴かも。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pyhack?src=hash">#pyhack</a> LTタイム！！が終わって撤収しました。お疲れ様～ (@ BePROUD in 渋谷区, 東京都) <a href="https://t.co/qndk67WoF4">https://t.co/qndk67WoF4</a> <a href="https://t.co/B6n8ZG6C1E">pic.twitter.com/B6n8ZG6C1E</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/868407228432252928">2017年5月27日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


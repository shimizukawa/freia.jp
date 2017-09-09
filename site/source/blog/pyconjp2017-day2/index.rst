:date: 2017-09-09 11:00
:tags: Python, PyConJP, Conference

=====================================
PyCon JP 2017 2日目 参加ログ #pyconjp
=====================================

`#PyConJP`_ 2017 in Tokyo に参加しました。:doc:`../pyconjp2017-day7/index` に引き続きの参加です。

今日は名札あれば受付不要なので直接キーノート会場へ。

今日は開始5分前に着席して、時間ちょうどにキーノート始まった！よかったよかった


.. _PyCon JP 2017: https://pyconjp.connpass.com/event/59412/
.. _#pyconjp: https://twitter.com/search?f=tweets&vertical=default&q=%23pyconjp&src=typd

.. contents::
   :local:

キーノート
===========

* 堀越 真映 (`@sinhrks`_)
* https://pycon.jp/2017/ja/talks/keynote/
* 動画: https://www.youtube.com/watch?v=1Cb3OQTmeD4

.. _@sinhrks: https://twitter.com/sinhrks

400人くらい会場に来てるかな？

.. figure:: keynote.*
   :width: 80%

   キャー 堀越さーん！

メモ
-------

会場に質問

* Q. 自分はPyData系だと思う方 -> 3割くらい
* Q. Pandas知ってる方 -> 6～7割くらい

抜粋

* Pandasは、データ仕様が与えられない場合の、試行錯誤のためのツール
* 2012年に初Issue、2014年に活動開始、2015年にコアチーム加入
* 最近は 1 Pull Request, 1 commit 運用を徹底している （俺：Sphinxもその方がいいかもなあ）

  .. raw:: html

     <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">numpyもそういう運用だとiwiwiさんが言っていた気がします。git bisectしやすいからとか</p>&mdash; chezou (@chezou) <a href="https://twitter.com/chezou/status/906324595577253888">2017年9月9日</a></blockquote>
     <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

* コミッターに期待することを明記している -> `Code Of Conduct`_ （俺：あーこれはマネしようかな）
* 後方互換性: 良くないAPIなどをdeprecationして2バージョン維持 （俺：これはSphinxもやってるね。元ネタはDjango）
* `Pythonによるデータ分析入門`_ -> 10月に改訂版が！
* Issueテンプレートを使って報告しやすいように整備 （俺：Sphinxもやってるー。報告の質が格段にアップしたよ）
* 団体企業からの支援 （俺：何に使ってるのか聞き逃した）
* OSS活動ってやる必要あるんだっけ？

  * -> 承認欲求を満たせる （俺：うん）
  * -> 有識者のレビューを受けてスキルアップできる （俺：うんうん）
  * -> 内部実装が理解でき（使う側としても）効率的なコードが書ける （俺：わかる）
  * -> 修正を取り込んでもらえると、使う時のhackkyな書き方が不要になる （俺：超わかる）

* PRを出してみようと思ったら

  * 大きめのプロダクトならIssueがタグで整理されている
  * 難易度タグが付いてるので簡単なやつから手を付けてみる
  * 他の人が手を付けているものは避けた方がよいかも

  .. figure:: pandas-issue-tags.*
     :target: https://github.com/pandas-dev/pandas/issues

* プルリクエストでバグ修正した場合

  * 意図が伝わらなければコードを書く
  * 影響範囲が大きい場合ひたすらテストを足す

* 気をつけていること

  * 局所的な修正を避ける
  * テストをちゃんと書く
  * ドキュメントをできるだけ書く


.. _Code Of Conduct: https://github.com/pandas-dev/pandas-governance/blob/master/code-of-conduct.md
.. _Pythonによるデータ分析入門: http://amzn.to/2xbVLtr

Q&A
--------

* Q: 投げられるIssue/PRが大量に来ると思いますが、どうやってさばいてますか？

  - A: 気づいた人がやる。活動量が多い人がレビューしてくれたりします。

  - Q: 自分の機能に責任を持って対応してる感じですか？

  - A: リリースマネージャーみたいな人がいて、その人は全てのIssueを見たり返事したりしてます

* Q: `@nobolis_`_ : 仕事とプライベートの時間の使い分けをどうされてますか？

  - A: 業務上はOSS活動するために雇われていないので、基本的に個人で活動してます。そういう活動も評価されているので業務上無駄になってたりはしません

* Q: `@shimizukawa`_: SphinxのIssueは今600ちょっとあります。PandasのIssueを見てみたら2000を超えていて、それってIssueが右肩上がりになっていくと思うんですが、そういうときに、どうやって気持ちを維持していくのか、お聞かせ下さい

  - A: コアコミッターはPRのレビューなどで忙しくて自分でパッチを書く時間が取れない事が多いです。なので、自分で全部直すのではなく、自分たち以外の人でも直せるような体制をつくっていく。簡単そうなissuesだったらやり方を提案して報告者にやってみてもらうとか。そうやって直せる人を増やしていってます。

* Q: ドキュメントだけで1000ページ以上ありますよね。そういう巨大なOSSを維持していくのは専門家じゃないともうできないものなのでは？

  - A: Yes & No. ドキュメントを見る専任者みたいな人がいます（Anacondaや2sigmaの人）。ただ、専任者がいないとできないわけじゃなくて、居ないなら居ないなりのやり方があると思ってます。


* Q: 西本: 局所的な修正よりも大局的に直す、という話をもうすこし詳しく聞かせて下さい

  - A: 欠損値のバグをある関数でだけ直しても、欠損値の扱いはそこだけじゃなく、もっと深いところで問題があって他の関数にも影響がある

  - Q: その意図は凄くよく分かるんですが、Pandasのような巨大なプロダクトだと影響の広いコードを直すのはすごい影響ありそうで、そこで議論が紛糾したりしませんか？

  - A: 2つ話があります。開発者側としてはあまり議論にならなくて、全体的に直した方が良いと判断する。慣れていない人が直す場合、全体的な視点は持っていないこともあるので、そこは慣れている人がアドバイスしたりします。

* Q: ベンチマーク比較するツールの紹介(`airspeed velocity(asv)`_)がありましたが、そのツールはPythonでしか使えないものですか？

  - A: 基本的にはPythonでスクリプトを書くので、Pythonの方が便利に使えますが、他でも使えるとは思います。

* Q: OSSへのコントリビュートをし続けるってすごい難しいことだと思うんですが、1年継続していくのに工夫したことはありますか？

  - A: 自分のスキルアップのためにPandasにターゲットを絞って活動をしていました。Issueを眺めて自分で直せそうな部分があったら自分でやってみるというのを続けました。

.. _`@nobolis_`: https://twitter.com/nobolis_
.. _@shimizukawa: https://twitter.com/shimizukawa
.. _airspeed velocity(asv): http://asv.readthedocs.io/en/latest/

Pythonで実現する4コマ漫画の分析・評論 2017
===============================================

* SHINJI KITAGAWA (`@esuji`_)
* https://pycon.jp/2017/ja/schedule/presentation/27/
* 動画: https://www.youtube.com/watch?v=S70KqdRYJzo

.. _@esuji: https://twitter.com/esuji

* 情熱駆動開発
* 自分が欲しいものをだれかが作ってくれる、ということはない
* Pythonならライブラリたくさんあるからなんとかなるかな、と思った
* **情熱があれば作れる**

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">BPPRです。<a href="https://twitter.com/hashtag/pyconjp?src=hash">#pyconjp</a> <a href="https://twitter.com/hashtag/pyconjp_201?src=hash">#pyconjp_201</a> <a href="https://t.co/Co5VEQNeug">pic.twitter.com/Co5VEQNeug</a></p>&mdash; 佐藤治夫 (@haru860) <a href="https://twitter.com/haru860/status/906335711355211776">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">BPPR: 弊社 <a href="https://twitter.com/hashtag/BeProud?src=hash">#BeProud</a> の制度。カンファレンスで会社紹介すると代休もらえて参加費が出る(要約) <a href="https://twitter.com/hashtag/PyConJP?src=hash">#PyConJP</a><a href="https://t.co/2331mVAAdr">https://t.co/2331mVAAdr</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906337449248354304">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


Q&Aは時間切れで個別。「11:30からOpenSpaceでやります」

休憩
==========


.. note:: 内容は随時更新していきます



:date: 2018-01-08 18:00
:tags: Sphinx, camp

=================================================
Sphinx + 翻訳 hack-a-thon 開発合宿 2018 #sphinxjp
=================================================

`Sphinx + 翻訳 Hack-a-thon 開発合宿`_ を開催しました。Sphinx-users.jpの初合宿です。7人が参加して、Sphinx漬けの2日間を過ごしました。会場の国立女性教育会館は開発合宿にとても良い施設だったので、また近いうちに利用したいと思います。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash&amp;ref_src=twsrc%5Etfw">#sphinxjp</a> 開発合宿の様子です。わいわい。 (@ 国立女性教育会館 in 比企郡嵐山町, 埼玉県) <a href="https://t.co/9nb3siDyow">https://t.co/9nb3siDyow</a> <a href="https://t.co/n2SbrmBAuB">pic.twitter.com/n2SbrmBAuB</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/949876206031310848?ref_src=twsrc%5Etfw">2018年1月7日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

:イベント: `Sphinx + 翻訳 Hack-a-thon 開発合宿`_
:参加者: 7人
:会場: `国立女性教育会館`_ （埼玉県 嵐山）
:時間: 1/7 10:00 ～ 1/8 15:30

.. _Sphinx + 翻訳 Hack-a-thon 開発合宿: https://sphinxjp.connpass.com/event/72062/
.. _国立女性教育会館: https://www.nwec-bs.jp/

.. contents::
   :local:

Sphinx開発合宿やってよかった
============================

普段のhack-a-thonは6時間のイベントなので、集合して準備して・・とやっていると、軌道に乗った頃にはもう解散時間、という感じだった。大きめのトピックを話し合うとそれだけで1日が終わっちゃう感じ。

今回合宿をしたおかげで、時間を掛けて議論もできたし、Issue確認したり、PRレビューしたり、といった実質的な作業も色々できました。振り返ってみると、寝てる時間を除いて約20時間ずっとSphinxの話ができる環境だったなあと思います。それだけの時間があると、普段なかなか話題にのぼらない雑多なことも含めて話ができたのがとても良かったです。

.. figure:: recture.*
   :width: 80%

合宿に参加した他のメンバーともSphinxの内部構造だったり、チケットの対応方法だったり、過去の経緯だったりを色々話せました。Sphinxはコミッターでも知らない経緯や機能があるし、再現手順は各利用者のドキュメント対象プロジェクトによって違ったりします。参加者の何人かに問題の再現確認を手伝ってもらえてとても助かりました。そのおかげもあって、合宿中に16件のIssueとPRがクローズされました。

コミッターとしての成果は、Sphinx-2.0までどう進めるか、2.0って何なのか、という話を数時間かけて詰められたことです。Sphinxは2.0からsemverを採用します。2.0の次は3.0, 4.0と進めていくことになり、1.7からそのための仕込みをやっていきます。2.0に巨大な機能を全て詰め込むようなことはしません。なにを2.0に入れていくのかはだいたい決めたので、今後Issue化していく予定です。


開発合宿の様子
===============

.. figure:: hack.*
   :width: 80%

   開発中

.. figure:: breakfast.*
   :width: 80%

   朝食


国立女性教育会館は、開発合宿にはとても良かった
================================================

.. figure:: annai.*
   :width: 80%

   本日の利用団体

* 男性7名、5人部屋和室2つ、朝夜食事付き、研修室利用、で36,000円弱（1人約5000円）。 `利用区分B`_ とっても安い。
* 男性でも問題なく利用できる（女性だと利用区分Aになるっぽい）。
* 東京都心（新宿）から電車で1時間強で行ける。合宿モードに切り替えるのにちょうどよい距離。
* 和室には冷蔵庫やテレビはないので、夜まで開発に集中できる。
* 門限22時、お風呂は22時半まで、館内消灯が24時。健全。
* 食事はビュッフェで、豪華ではないけど十分美味しかった。
* コーヒーは1杯200円。ビールはジョッキ600円。ちょっとお高い。
* 近所のファミマまで徒歩10分弱。開発の合間のちょっとした気分転換に良い。
* インターネットもあったけど、無線LANの調子が悪くて自前を使ったのは残念（まあいいや、と思って問い合わせもしなかった）

会場について詳しくは `国立女性教育会館`_ のサイトを参照して下さい。

申込みは、サイトのフォームで申込みをしたあとに、メールや電話で詳細を詰める流れでした。人数や研修室などのこまかい調整もしてもらえそうな感じでした。次回も使わせてもらおうと思ってます。

.. figure:: receipt.*
   :width: 80%

   お会計

.. _利用区分B: https://www.nwec-bs.jp/?page_id=420

みんながやること、やったこと
============================

- @tk0miya: Sphinx-2.0のプランを考えた。1.7のリリース内容を現実的なものにするため、多くの内容を1.8に延期しました

- @kashew_nuts: Djangoのドキュメントを翻訳していました。Django-2.0のチュートリアルと、Djangoフォームの翻訳を進めました。ボリュームが大きくて翻訳率は1%進んだかどうか・・心折れそう

- @takuan_osho: Sphinxの未解決Issueを再現させようとしてました。2つチャレンジしてどちらも現象再現できなくて

- nskgch: OSSじゃないものの翻訳をするために、Transifexではなくzanataでやってみようと思い、アカウントを作りました。

- @usaturn: http://www.usaturn.club を作られました。SphinxのIssueを1つ閉じました（自分で出したやつです）。

- @jbking: 昨日は1つPRを出して、あとsmart_quote周りのIssueを読んでコメントしました。

- @shimizukawa: Sphinx-2.0に向けての計画をしました。今日はもらってるPRレビューします。後はIssueのトリアージをしつつ、もらうIssueをコミッター以外の協力者が確認したり対応しやすくするためのルール整備をします。


おまけ
======

夜中に、ドメイン登録料の話で盛り上がって、その流れで @tk0miya が ``usaturn.club`` を80円弱で取得。 http://www.usaturn.club/ をgithub pages使って公開。さっきそこに http://www.usaturn.club/ にogタグを指定するPR出したら速攻マージされた。今回の合宿の成果だ！


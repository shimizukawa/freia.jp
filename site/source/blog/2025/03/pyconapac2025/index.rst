:date: 2025-03-27 06:30
:tags: PyCon, PyCon APAC, PyCon Philippines

=================================================
PyCon APAC 2025 in Philippines に参加しました
=================================================

3月頭にフィリピンで開催された、PyCon APAC 2025に参加しました。

.. figure:: images/ph2025-day1-opening.*
   :width: 80%

   オープニング、共同座長のサイラスさん

昨年2月に参加したPyCon Philippines 2024からちょうど1年です。
前回参加時よりも、イベント全体は少しだけ落ち着いた雰囲気に感じたのは会場が大学だったからかもしれません。
大学の広い敷地を活用して、屋外のポスター展示や、その近くのコーヒー／アイスクリーム配布などがあり、開放的な雰囲気がありました。

また、今回はAPACの名前を冠したことで外国からの参加者が多かったと思います。また、日本からも10名以上が参加していました。
それもあって、現地コミュニティーの方と交流する時間よりも、日本からの参加者や、各国のAPACオーガナイザー関係者との交流が多くなりました。

- :doc:`/blog/2024/02/pyconph2024/index`
- :doc:`/blog/2024/10/pyconapac2024/index`


イベント概要
==============

:イベント名: PyCon APAC 2025
:公式ウェブサイト: https://pycon-apac.python.ph/
:日付: 2025年3月1日(土)DAY1トーク、2日(日)DAY2トーク、3日(月)DAY3スプリント
:場所: Ateneo de Manila University (Leong Hall)

私は、DAY1、DAY2に参加しました。
前日の金曜夜に現地到着して、月曜朝には帰るスケジュールにしたため、DAY3のスプリントと、さらに翌日に開催された観光ツアーには参加しませんでした。

参加時にトークのメモや質疑応答を書いたスクラップが以下にあります。

- https://scrapbox.io/shimizukawa/PyCon_APAC_2025

イベントレポートが公開されています（参加した池田さん執筆）。

- `PyCon APAC 2025参加レポート | gihyo.jp <https://gihyo.jp/article/2025/03/pycon-apac-2025>`_

来週、4月4日（金）に、参加報告会が実施されます。

- `PyCon APAC 2025 参加報告会 - connpass <https://pyconjp.connpass.com/event/349628/>`_

.. figure:: images/ph2025-day0-venue.*
   :width: 80%

   会場はマニラ首都圏のクバオ。

   Terminal3（空港）から、宿泊したRed Hotelまで、Grab（タクシー）で日中だと2時間。
   右上の会場までさらに30分。

.. figure:: images/ph2025-day1-reception.*
   :width: 80%

   受付（中央）と、スポンサーブース（壁ぞい）

総括
=========

PyCon APAC 2025は、1年前のPyCon PH 2024に比べて落ち着いた感じ。日本のPyCon JPっぽさを感じました。

- 質疑応答は日本よりも積極的な感じなのは変わらず。みなさんガンガン質問していました。
- イベント運営も素晴らしかった。APACとして開催するのが決まったのが11月頃だったので、元々PyCon PHをこの時期に開催する予定だったとしても看板掛け替えはけっこう大変だったろうと思う
- 全体写真撮影をメインホールで行った後、屋外でも撮ったのは驚きました。この人数で移動するの！？
- イベント中に使えるWiFiは無し。今回は27GBのSIMを（目論見を外した結果）用意していたので、困りませんでした。
- 日本からは参加者&スピーカーとして13名参加しました。自分を含む9名がトークやパネルで登壇しました。
- スポンサーブースは8テーブルほどで、2日間ともに活気があり、参加者みんなブースをよく廻っていました。スタンプラリー集めに積極的だったのかも？今回は日本の企業スポンサーは無し。
- エスプレッソコーヒーが1日1杯無料で、2杯目からは有料でした。他に無料のアイスクリームとタホがありました。暑い屋外でトーク後に食べるアイスクリームはめちゃくちゃ美味しかった。
- ランチは2日ともフィリピン料理のお弁当でした。フィリピン料理は辛いものが少なく、炭水化物が多め。1日目はチキンとパスタとライス。2日目はフィッシュと炒め野菜とライス。
- 全体の公式パーティーは無く、1日目にスピーカーと各国オーガナイザーの招待パーティーに参加しました。当然のようにお酒は無し（アジアのPyConではお酒が出る国の方が少ない）。パーティー後は日本からのメンバーでビールを求めて移動。

自分のトークセッション
=========================

- 日時場所

  - 3月1日（土） 13:15 - 13:45
  - Video: 準備中
  - Slide: `"Structlog in Practice" <https://docs.google.com/presentation/d/1lBd0d2z6urUl0bqpGZmM1KJ1eEzaDVmrSJXMTy-ywuQ/edit>`_

- "Structlog in Practice"

  - PyCon JP 2024 で話した「実践Structlog」を英語にしたもの（ :doc:`PyCon APAC 2024 </blog/2024/10/pyconapac2024/index>` と同じ）です。
  - クラウド時代のオススメロギングライブラリとしてstructlogの入門と実践で利用している事例を紹介しました。

.. figure:: images/ph2025-day1-shimizukawa-talk.*
   :width: 80%

   私のトーク、恒例の演台から写真 

- 質疑応答など

  - トーク後には質疑応答が2つありました。
  - 質問内容は、ログの集約と構造化をベンダー非依存で行いたいというニーズから来るものでした。私のトーク内では「ベンダー非依存でやりたいよね」というメッセージは含めていませんでしたが、そういうニーズは確実に存在するんだと実感しました。
  - トーク後に、「PyCon APAC 2024 のインドネシアでトーク聞きました」と声をかけてもらえました。びっくり。
  - 翌日のランチで同じ席になった方から、昨日のトーク聞きました、LinkedInにポストした写真のここです、と声をかけてもらえました。

- トークフィードバック

  後日、運営チームからトークへのフィードバックを共有いただきました。良い感触だったようで良かった。

  - 役に立つ話題でした。ありがとう! （Practically useful topic. Thank you!）
  - LokiやElasticSeatchへのログ記録など、例があるといいです。発表ありがとう。（want to get examples like logging to loki and elasticseatch. thanks for your speech）
  - 良い話でしたが、もっと例を共有する時間があればもっと良かったです。（insightful talk, but would be better if we have time to share additional examples）

  こういうフィードバックをもらえるの、良いな～。

イベント感想
================

この1年ちょっとで、フィリピン、日本、インドネシア（APAC）、東海、静岡、フィリピン（APAC）、とPyConに参加してきました。どのイベントも構成は異なっていますが、今回のフィリピンはAPAC地域の顔見知りが多数参加していたこともあってか、昨年のフィリピンとは違うような、APACイベント感があったような気がしました。

何にしても、イベントは楽しかった！なにより、トーク発表をしたことで色々な人に声をかけてもらえたのが嬉しかったです。

.. figure:: images/ph2025-day2-jpteam.*
   :width: 80%

   日本チームの集合写真。みんな良い笑顔～

次は、5月15日（木）から、1度は行ってみたかった `PyCon US 2025`_ に参加してきます。
トーク予定はありませんが、LTは応募したい。どうなるかなー。（英語特訓始めました）

.. _PyCon US 2025: https://us.pycon.org/2025/



写真で紹介
==================

イベント前日。日本から到着して野良前夜祭へ参加。

.. figure:: images/ph2025-day0-naia3-jeepney.*
   :width: 80%

   空港にあるジプニー（伝統的な乗り合いバス）。乗る度胸はない

   * 乗り方: 飛び乗る
   * 降り方: 声かける

.. figure:: images/ph2025-day0-turon.*
   :width: 80%

   TURON、25ペソ（約70円）
   
   サババナナとジャックフルーツの揚げ春巻き。
   SM（デパート）の地下に大抵あるスーパーマーケットのフードコートで売ってます。
   美味しいのでフィリピン行ったら是非。

.. figure:: images/ph2025-day0-omiyage-colgate.*
   :width: 80%

   Colgate（歯磨き粉）

   SMスーパーマーケットでお土産購入。
   Colgate Whiteはホワイトニング効果が高くて、フィリピンだと大分安く購入できる。
   （帰りに空港で没収された…100ml制限…）

.. figure:: images/ph2025-day0-jpteam-chikin.*
   :width: 80%

   チキンの丸焼き（多分アドボ）

   日本メンバーの野良前夜祭に合流して夕食

.. figure:: images/ph2025-day0-jpteam-ikaring.*
   :width: 80%

   カラマリ（イカリングフライ）

.. figure:: images/ph2025-day0-lawson-icecream.*
   :width: 80%

   でっかいアイスクリーム、330ペソ（約900円）

   ホテル下のローソンにて。
   フィリピンのアイスは大きい（このサイズでよく売ってる）。
   住んでたときによく食べてたロッキーロード、懐かしい。

.. figure:: images/ph2025-day0-lawson.*
   :width: 80%

   ローソンのレジ
   
   日本と似たレイアウトだけど、揚げ物コーナーが大きい

.. figure:: images/ph2025-day0-redhotel.*
   :width: 80%

   宿泊したRed Hotel Cubao の部屋。1泊約4000円


イベント1日目。

.. figure:: images/ph2025-day1-coffee.*
   :width: 80%

   1日1杯無料のコーヒー

   * Americano = エスプレッソのお湯割り
   * Longblack = お湯に注いだエスプレッソ

.. figure:: images/ph2025-day1-warroom.*
   :width: 80%

   War Room（スタッフ兼スピーカー部屋）

   トークの準備をするスピーカーのみなさん。

.. figure:: images/ph2025-day1-treat-bukopie.*
   :width: 80%

   Buko Pie （ココナッツパイ）
   
   めっちゃ美味しい。スピーカーにこういう差し入れをもらえるのも嬉しい。
   フォークとかは無いので、みんなで手でちぎって食べてました。

.. figure:: images/ph2025-day1-lunch-space.*
   :width: 80%

   ランチ会場

   会場まで長い長い行列で、全然進まないので写真だけ撮った。
   時間をずらして後で食べることにしました。

.. figure:: images/ph2025-day1-lunch-chikin.*
   :width: 80%

   1日目ランチ、チキン&パスタ弁当

   フィリピン人はチキン、パスタ、ライスが大好き（というイメージ）
   味付けは濃いめ。野菜が欲しくなるけど、野菜はなかなか見かけない。

.. figure:: images/ph2025-day1-booth-apac.*
   :width: 80%

   PyCon APAC ブースの寺田さん

.. figure:: images/ph2025-day1-snack-kakanin.*
   :width: 80%

   イベントおやつの「カカニン」

   カカニンは、ココナッツミルクともち米で作るらしい。
   フィリピン版おはぎ？ 色んな味があった。

.. figure:: images/ph2025-day1-ginos-member1.*
   :width: 80%

   日本メンバーでカンパイ

   1日目終了後、会場から徒歩10分ほどの GINO'S BRICK OVENPIZZA

.. figure:: images/ph2025-day1-ginos-member2.*
   :width: 80%

   日本メンバーでクラフトビール

   MITCHELL'S BACKYARD BREWERY。
   ピザ屋の奥に醸造エリアがあるらしい。

.. figure:: images/ph2025-day1-ginos-salada.*
   :width: 80%

   Salada with Burrata

   ピザ屋のサラダ、みんなで「生野菜久しぶりーーー！！」と食べた。
   Burrataは水牛のフレッシュチーズ。モッツァレッラチーズの仲間らしい。

.. figure:: images/ph2025-day1-inviting-dinner.*
   :width: 80%

   招待ディナー、Philippines料理たくさん

   10種類くらいあったけど写真撮り忘れました。

イベント2日目。

.. figure:: images/ph2025-day2-transcript.*
   :width: 80%

   Otter_ リアルタイム文字起こし

   `参加レポート記事 <https://gihyo.jp/article/2025/03/pycon-apac-2025>`_ を執筆した池田さんが Otter_ で英語リアルタイム文字起こししていたので、聞きながら目で追ってました。英語聞き取りが追いつかなかったので、ありがたい。

.. _Otter: https://otter.ai/

.. figure:: images/ph2025-day2-lunch-fish.*
   :width: 80%

   イベントランチ2: 魚の揚げ物、サヤインゲン炒め、米

   味はやっぱり濃いめ。飯が進む。
   フィリピン人は揚げ物も好き。

.. figure:: images/ph2025-day2-lunch-people.*
   :width: 80%

   イベントランチ2: 目閉じ

   このあと、同席した人に「昨日structlogのトークしてたよね？」って声をかけられた。
   devopsでログ取っててー、とのこと。
   声をかけてもらえると嬉しい。スピーカー特権ですね。

.. figure:: images/ph2025-day2-warroom-working.*
   :width: 80%

   War Room でトーク準備中の武居さん

   2日目のトーク直前まで準備に余念が無い
   （私はトークは1日目の方がうれしい..気が落ち着かないので）

.. figure:: images/ph2025-day2-icecream-vendor.*
   :width: 80%

   イベントの無料アイス

   フィリピン人はアイス好き（という印象）
   主催メンバーに「あの無料アイスは何？」と聞いたら、サプライズで用意したとのこと。
   コーヒーは高くて無料にてきなかったけど、アイスはできたらしい。

.. figure:: images/ph2025-day2-icecream-takei.*
   :width: 80%

   「この年になってもまだ挑戦できる」

   と、英語トーク初登壇をやり遂げた武居さん。
   「一仕事終えた後のアイス美味しい。」

.. figure:: images/ph2025-day2-taho.*
   :width: 80%

   イベントの無料タホ

   アイス屋さんが “タホ” も配ってました。

   「タホ」はタガログ語で「豆腐」。
   温かい豆腐、サゴ（タピオカぽい）、黒蜜をカップに入れてくれる

.. figure:: images/ph2025-day2-snack-pizza.*
   :width: 80%

   イベントおやつ2: ピザ

   フィリピン人はピザも好き（という体感。イートインできるピザ屋が多め）

.. figure:: images/ph2025-day2-gathering.*
   :width: 80%

   集合写真（後ろから）

.. figure:: images/ph2025-day2-elias-brewing.*
   :width: 80%

   日本から参加したみなさん
   
   イベント後に、Elias Wicked Ales & Spirits へGrabで移動。
   醸造エリアに入れてくれたので、記念撮影しました。

.. figure:: images/ph2025-day2-elias-menuboard.*
   :width: 80%

   クラフトビールのメニューボード

   Untapped_ でチェックインするとメニューボードに人が表示されて、楽しい。

.. _Untapped: https://untappd.com/

.. figure:: images/ph2025-day2-elias-shrimp.*
   :width: 80%

   SHRIMP GAMBAS（エビのガンバス）

   海老のピリ辛炒め。味は濃い。
   Philippinesの料理らしい。

.. figure:: images/ph2025-day2-elias-sisig.*
   :width: 80%

   Sisig（シシグ）

   Philippinesの伝統料理。
   豚コマをしょう油、 酢、にんにく、唐辛子で炒め。味は濃い。
   これは辛くなかった。

.. figure:: images/ph2025-day2-elias-streetfood.*
   :width: 80%

   ストリートフード大皿（内訳不明）

   おでんの具っぽい串、えびせん、イカ？


イベント翌日。

.. figure:: images/ph2025-day3-fruitas.*
   :width: 80%

   Fruitas のブコジュース（ココナッツジュース）

   ココナッツジュースはこれ一択（生ココナッツを除く）。
   空港の制限エリアで1本100ペソ（300円）だったので2本買って帰りました。
   ちなみに、街では75ペソだったと思う。

おしまい。

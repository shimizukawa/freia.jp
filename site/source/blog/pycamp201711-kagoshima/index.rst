:date: 2017-11-04 23:55
:tags: Python, PyCon, PyCon JP, PyCamp

====================================================
Python Boot Camp in 鹿児島で講師してきました #pycamp
====================================================

`Python Boot Camp in 鹿児島`_ に行ってきました。

一般参加者17数名、学生10名、TA・スタッフ・講師9名、合計36名くらいが参加しました。

.. figure:: attendees.*
   :width: 80%

   参加者のみなさん（開始時）

このblogは講師からみた参加レポートです。チュートリアル本体の様子なんかは、公式の開催レポートは別途書かれると思います。 -> `Python Boot Camp in 鹿児島を開催しました`_


.. note::

   "Python Boot Camp" は、 `一般社団法人PyCon JP`_ が日本各地で開催している、 **初心者向けPythonチュートリアルイベント** です。
   今回の鹿児島で `14回目`_ の開催です。
   `チュートリアルのテキスト`_ は公開されていて、ライセンスに従って自由に利用できます。詳しくは `Python Boot Camp について`_ を参照してください。

   現地スタッフになってくれる人がいれば、講師に行きますので、 `申込みフォーム`_ からひご連絡ください！

参加した感想、雑感など
======================

参加申込みペースはゆっくりでしたが、開催数日前にちょうど満席になる感じでした。

今回は学生枠が多い感じです。 `鹿児島キャリアデザイン専門学校`_ の先生にアナウンス協力してもらい、そこの生徒さんたちが10名参加されました（先生自身も受講生として参加してくれました）。他の学校などにも協力を仰いだけど、反応がなかったそう。学校内でPyCampだけ紹介するわけにもいかないのかな。しょうがないのかなー。

学生以外の参加者については、アナウンスする先が見つからなかったということであまり広報できていなかったみたいだけど、想定の倍の参加者になったそうです。主催者のmasakuraさんは「どうして人が来たのか分からない」とか言ってましたが、それって潜在需要結構あるということじゃないかな。 `CodeZineのイベント告知記事`_ を読んで参加したという人もいました。

.. _鹿児島キャリアデザイン専門学校: https://www.harada-gakuen.ac.jp/career/


.. figure:: connpass-stats.*

   イベント参加推移

これまでの講師活動では、どうしても講義資料の途中で時間切れになってしまって悔しかったため、今回のイベントでは、最後のスクレイピング章まで講義の時間中に紹介したい！と思って、5分単位のタイムテーブルを作りました。

- 13:00-13:15 会場案内、挨拶、自己紹介
- 13:15-13:25 1. Pythonをはじめる前に
- 13:25-13:55 2. Pythonをはじめよう
- 13:55-14:00 休憩
- 14:00-14:25 3. Pythonのデータ型（基本編）
- 14:25-14:50 4. Pythonのデータ型（コレクション編）
- 14:50-15:00 休憩（おやつ）
- 15:00-15:20 5. ファイル操作とモジュール
- 15:20-15:45 6. サードパーティ製パッケージと venv
- 15:45-15:50 休憩
- 15:55-16:25 7. スクレイピング
- 16:25-16:35 8. 次のステップ
- 16:35-17:00 アンケート、質疑応答、集合写真

実際にはみんなの集まりが良くて開始が10分早まったし、運営の都合もあって17時半までに集合写真撮影、解散でよいということになりました。このおかげもあって、上記タイムスケジュールを無事こなせました！

1つ気がかりだったのは、質問の量が少なめだったことです。後からでも、Slackで質問出してもらえると嬉しいな。

これまで、 :doc:`神戸 <../pycamp201705-kobe/index>`, :doc:`福岡 <../pycamp201709-fukuoka/index>` で講師をして、今回が3回目でした。 次は、 `11/18(土) 静岡`_ で講師してきます。


移動
=====

朝、 :ref:`飛行機乗り遅れ <pycamp-fukuoka-201709-flight>` とか怖いので、空港にフライトの1時間半前、7:45頃に到着しました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">フライトの1時間以上前に空港ついた。8:10発はまだ出発便一覧表示ないわ (@ 羽田空港 第1旅客ターミナル in 大田区, 東京都) <a href="https://t.co/sBPgoz5wBb">https://t.co/sBPgoz5wBb</a> <a href="https://t.co/f6geAVkZ94">pic.twitter.com/f6geAVkZ94</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926567797529997313?ref_src=twsrc%5Etfw">2017年11月3日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

JAL機内の無料WiFiを使うつもりでいたら、50分のフライトで半分くらいの時間、アクセスポイントが見えなくなってしまった。残念。オフラインのまま、今年3冊目の本の翻訳を進めました。前回 :ref:`福岡 <pycamp-fukuoka-201709-flight>` のときに自由な空だと思って喜んだけど、まあ繋がらない時もあるよね。がんばれJAL。


スタッフミーティング
=====================

今回はフライトに間に合ったので、事前ミーティングにちゃんと参加できました。

.. figure:: lunch-meeting-shop.*

   ランチミーティングで行ったお店

スタッフミーティングでは、ご飯を食べながら自己紹介したり。鹿児島中央駅はできてまだ10年経ってない話を聞いたりしました。

イベント準備として個人的に気にしていたのは、TAスタッフの顔と名前を一致させること。チャットではやりとりしてたけど、実際に会うのは初めてなので。あと人の名前と顔と覚えるの苦手なので。

あと、前回の福岡では、チャットでの質問にできるだけ回答しようとしてしまったので、今回はTAのみなさんに、チャットでの質問に回答できそうなものは回答してもらうようお願いしました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">かんぱちヅケ丼ダブル！！ご飯の下にまたかんぱちが！ <a href="https://twitter.com/hashtag/pycamp?src=hash&amp;ref_src=twsrc%5Etfw">#pycamp</a> (@ づけ丼屋 桜勘 in 鹿児島市, 鹿児島県) <a href="https://t.co/4Yk7gQtWco">https://t.co/4Yk7gQtWco</a> <a href="https://t.co/VX1sNHPTOJ">pic.twitter.com/VX1sNHPTOJ</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926640504305053696?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


Python Boot Camp 本編
========================

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">Python Boot Camp 鹿児島、本日13時から！ <a href="https://twitter.com/hashtag/pycamp?src=hash&amp;ref_src=twsrc%5Etfw">#pycamp</a> <a href="https://twitter.com/hashtag/pyconjp?src=hash&amp;ref_src=twsrc%5Etfw">#pyconjp</a> <a href="https://twitter.com/hashtag/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E5%85%A5%E9%96%80?src=hash&amp;ref_src=twsrc%5Etfw">#プログラミング入門</a> <a href="https://twitter.com/hashtag/python%E5%85%A5%E9%96%80?src=hash&amp;ref_src=twsrc%5Etfw">#python入門</a> <a href="https://t.co/MblKdRMLlj">https://t.co/MblKdRMLlj</a> <a href="https://t.co/dBM5MXHNbm">pic.twitter.com/dBM5MXHNbm</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926656707736014848?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


イベントの開始時に http://pyconjp-fellow.herokuapp.com/ からSlackに参加してもらって、チャットで質問を書いてもらいました。講義中も質問を見ながら、あとで回答したり、他の参加者やTAが答えてくれたり、テキストが進んだときに回答になるような説明を含めたり、と言った調整ができるし、チャットに質問内容が残って後で読み返せるし、ということで、とても良い方法なんじゃないかなーと思ってます。Slack慣れてない人にはハードルがちょっと高いと思うので、当日じゃなくもうちょっと前に参加してもらうと良いかも。

講義開始時に、参加者どのレベルに合わせれば良いのかを確認するため、参加者に「for文を書いたことが無い人？」という質問をしました。これで、どんな言語でもプログラミングしたことがないかどうかが分かります。分かるだけで無く、参加者全員が「その人のペースで進むんだな」と思ってもらう効果もあるんじゃないかな、と思ってます。

福岡に続いて、今回もfizzbuzzを実際に参加者と一緒にやりました。後々、このゲームのシーンを引用して「人間同様に、全ての手順をコンピューターに伝える必要がある」「人間は遅いけどコンピューターは速い」と紹介できたのは良かったんじゃないかな。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">人力 FizzBuzz <a href="https://twitter.com/hashtag/pycamp?src=hash&amp;ref_src=twsrc%5Etfw">#pycamp</a> <a href="https://t.co/TREn1sdald">pic.twitter.com/TREn1sdald</a></p>&mdash; まー (@tomo_masakura) <a href="https://twitter.com/tomo_masakura/status/926674399213711360?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

環境まわりでは、ほとんどはまることがなかったけど、2つひっかかったところがありました。1つはpipコマンドをPython対話シェル上で実行してしまった人が多かったこと。これは言い方が悪かったかなー。もう1つは、Ubuntu環境の人がpip使えなかったり、venv使えなかったりしたこと。 ``sudo apt install python3-pip python3-venv`` してもらって解決。python3-venvを入れずに ``python3 -m venv <env>`` すると、ディレクトリはできるけど ``<env>/bin/activate`` が生成されないという不思議な動作になってて、最初は何がおきてるのかよく分からなかった。解決してよかった。

本編中、いくつか質問をもらいました。

* Q リストと辞書の違い、使い分けがよくわかりません。もう一度教えてください。

  * A 辞書は、英語の辞書みたいに、取得したい単語（キー）を指定して内容（バリュー）を取り出します。リストはそういうキーがなくて、何番目のデータを取り出す、といった感じで、順番でデータにアクセスします。迷ったら、キーで扱いたいか、順番で扱いたいか、で使い分けを考えると良いです。

* Q WebSocketを使ったサーバーをTornadeで作ってるんですが、サーバー構築とか正しく出来てるのかよくわかりません、どうやって学んだら良いですか

  * A うーん、すぐに「このサイト、本を読むと良いよ！」と言えるものがないんですが、今回使った pyconjp-fellow Slack で聞いたり、質問サイトで同様の疑問を持っている人のQ&Aを読んだりするのが良いと思います。できるだけ、具体的に質問を重ねて、単に解決方法を知るのではなく、なぜそれが良いのかを突き詰めていくのをオススメします。

本編の最後には、ジャンケン大会に勝ち残った学生さんに Pythonプロフェッショナルプログラミング 本がプレゼントされました！清水川がこの本の著者の1人ということで、masakuraさんが自費で用意してくれました。ありがたいありがたい。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">今日はジャンケン大会に勝ち残った学生さんにPythonの本が送られました！　<a href="https://twitter.com/hashtag/pycamp?src=hash&amp;ref_src=twsrc%5Etfw">#pycamp</a> <a href="https://twitter.com/hashtag/%E9%B9%BF%E5%85%90%E5%B3%B6?src=hash&amp;ref_src=twsrc%5Etfw">#鹿児島</a> <a href="https://t.co/9nqYapvMuV">pic.twitter.com/9nqYapvMuV</a></p>&mdash; Katsuhiro Morishita (@KatsuhiroKU) <a href="https://twitter.com/KatsuhiroKU/status/926779644224815111?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


.. チャットメモ
.. -----------------
.. 
.. （ちょっと加工してあります）:
.. 
.. * ``8/2`` ってなんで小数点に？
.. * ちなみに数値を ``50_000`` みたいに(数値の中に `_` を入れられるように)なったのはPython 3.6からです
.. * “繰返し可能な型” の意味がはっきりわかりません。順序があるのはわかりました。


懇親会！
=============

12人で `懇親会`_ へ！

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pycamp?src=hash&amp;ref_src=twsrc%5Etfw">#pycamp</a> 懇親会！おつかれ！黒さつま鶏！！ (@ 地鶏の鶏膳 in 鹿児島市, 鹿児島県) <a href="https://t.co/DWca1V9yme">https://t.co/DWca1V9yme</a> <a href="https://t.co/PPLOHCbmVW">pic.twitter.com/PPLOHCbmVW</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926734801004060672?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


.. figure:: party.*

   懇親会の様子


4人で2次会へ。私の希望で、天文館通りにある BeerReise_ というお店にいきました。ビールうまかったし、フィッシュ&チップスのポテトがめっちゃうまかった。

.. _BeerReise: https://www.facebook.com/%E3%83%93%E3%82%A2%E3%83%A9%E3%82%A4%E3%82%BC-Beer-Reise-522883527804967/

.. figure:: beer.*

   ギネスの泡にハートマークが！

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">ビール、ビール！！ (@ BeerReise in Kagoshima) <a href="https://t.co/J1wuqrUGkg">https://t.co/J1wuqrUGkg</a> <a href="https://t.co/DyLTTZzRZ1">pic.twitter.com/DyLTTZzRZ1</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926780061176553472?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">富士桜高原麦酒 ミュンヘンラガー（山梨）ちょっと甘めで美味しい <a href="https://twitter.com/hashtag/pycamp?src=hash&amp;ref_src=twsrc%5Etfw">#pycamp</a> (@ BeerReise in Kagoshima) <a href="https://t.co/pWFVcz1sYg">https://t.co/pWFVcz1sYg</a> <a href="https://t.co/KaQ24YAY3A">pic.twitter.com/KaQ24YAY3A</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926786233983950848?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



おまけ
-------

1日目（朝の移動）

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">フライトの1時間以上前に空港ついた。8:10発はまだ出発便一覧表示ないわ (@ 羽田空港 第1旅客ターミナル in 大田区, 東京都) <a href="https://t.co/sBPgoz5wBb">https://t.co/sBPgoz5wBb</a> <a href="https://t.co/f6geAVkZ94">pic.twitter.com/f6geAVkZ94</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926567797529997313?ref_src=twsrc%5Etfw">2017年11月3日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">羽田空港の床になんかいた。おもしろいw 人の部分の反射をもう少し抑えられればきれいに見えそう <a href="https://t.co/qYcdNUNm4R">pic.twitter.com/qYcdNUNm4R</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926569846548004864?ref_src=twsrc%5Etfw">2017年11月3日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">空港に足湯が！！ <a href="https://t.co/Dlji25MnE4">pic.twitter.com/Dlji25MnE4</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926621259508596736?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">駅に観覧車が！？ (@ 鹿児島中央駅 - <a href="https://twitter.com/JR_kagoshima?ref_src=twsrc%5Etfw">@jr_kagoshima</a> in 鹿児島市, 鹿児島県) <a href="https://t.co/AYyf52sDle">https://t.co/AYyf52sDle</a> <a href="https://t.co/HBb4CzyHcz">pic.twitter.com/HBb4CzyHcz</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926632658423156737?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

1日目（夜の懇親会）

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pycamp?src=hash&amp;ref_src=twsrc%5Etfw">#pycamp</a> 懇親会！おつかれ！黒さつま鶏！！ (@ 地鶏の鶏膳 in 鹿児島市, 鹿児島県) <a href="https://t.co/DWca1V9yme">https://t.co/DWca1V9yme</a> <a href="https://t.co/PPLOHCbmVW">pic.twitter.com/PPLOHCbmVW</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926734801004060672?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">しろくま！！ (@ 天文館むじゃき in 鹿児島市, 鹿児島県) <a href="https://t.co/ZScjHIHtUL">https://t.co/ZScjHIHtUL</a> <a href="https://t.co/YUN8Ms6h5Y">pic.twitter.com/YUN8Ms6h5Y</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926773999773896705?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


宿泊は `法華クラブ鹿児島`_ 。鹿児島中央駅にも、天文館通りにも歩いて行ける場所で、交通の便も良いし、大浴場きれいでゆったりできたし、朝ご飯のビュッフェに並んだ鹿児島料理がめっちゃうまかったです。鶏皮とか豚軟骨煮とかまじうまかった。

.. _法華クラブ鹿児島: https://www.hokke.co.jp/kagoshima/

2日目

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">炭水化物少なめチョイス（多分 (@ ホテル法華クラブ鹿児島 in 鹿児島市, 鹿児島県) <a href="https://t.co/dzJ9wEJFMh">https://t.co/dzJ9wEJFMh</a> <a href="https://t.co/0re9b2HR79">pic.twitter.com/0re9b2HR79</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926936079583862786?ref_src=twsrc%5Etfw">2017年11月4日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">鹿児島の銭湯はほとんどが温泉だ、と聞いて来てみた。 (@ 霧島温泉 in Kagoshima) <a href="https://t.co/OmlsJlZhH9">https://t.co/OmlsJlZhH9</a> <a href="https://t.co/xh5tUGNvEc">pic.twitter.com/xh5tUGNvEc</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926971831483068416?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">鹿児島の温泉で温まった。お湯は熱め、飲用に柄杓置いてたので一杯やってきた。タオル貸してくれて値段変わらず390円。番台の渋いおっちゃんもステキ (@ 霧島温泉 in Kagoshima) <a href="https://t.co/kLkx6dNonz">https://t.co/kLkx6dNonz</a> <a href="https://t.co/5ZHASSN155">pic.twitter.com/5ZHASSN155</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926976911217168384?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">大久保利道様 (@ 大久保利通像 in 鹿児島市, 鹿児島県) <a href="https://t.co/FHam2Q6ia8">https://t.co/FHam2Q6ia8</a> <a href="https://t.co/3JIPkPZqTF">pic.twitter.com/3JIPkPZqTF</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926977834412924928?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">鹿児島中央駅にくっついてる観覧車。遠くからも目指しやすい。一周何分かな (@ アミュプラザ鹿児島 - <a href="https://twitter.com/amukagoshima?ref_src=twsrc%5Etfw">@amukagoshima</a> in 鹿児島市, 鹿児島県) <a href="https://t.co/8pMeDa2fJp">https://t.co/8pMeDa2fJp</a> <a href="https://t.co/qOV7UKzEP3">pic.twitter.com/qOV7UKzEP3</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926978974588252160?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">霧島温泉で熱々になったので、しろくま食べに来た (@ 天文館むじゃき アミュプラザ店 in 鹿児島市, 鹿児島県) <a href="https://t.co/f8ujfi8HWU">https://t.co/f8ujfi8HWU</a> <a href="https://t.co/4jZ3quKskD">pic.twitter.com/4jZ3quKskD</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926981222034788352?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">しろくま(M)でか！フワフワでうまいー！ (@ 天文館むじゃき アミュプラザ店 in 鹿児島市, 鹿児島県) <a href="https://t.co/eFsamek9QP">https://t.co/eFsamek9QP</a> <a href="https://t.co/G1ik3WViRE">pic.twitter.com/G1ik3WViRE</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926983117394644993?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">あっ、上から見て「しろくま」に見えるか確認するの忘れてた！ (@ 天文館むじゃき アミュプラザ店 in 鹿児島市, 鹿児島県) <a href="https://t.co/a0fY4VnnOO">https://t.co/a0fY4VnnOO</a> <a href="https://t.co/hX61zVcaTv">pic.twitter.com/hX61zVcaTv</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926987569128075264?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">空港に向かう。時間なくて観光無理と思ってたけど、思いのほか鹿児島満喫した！温泉は素晴らしい (@ 南国交通バスターミナル in 鹿児島市, 鹿児島県) <a href="https://t.co/AfBMASZwJ5">https://t.co/AfBMASZwJ5</a> <a href="https://t.co/sQFf6NSiDQ">pic.twitter.com/sQFf6NSiDQ</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/926993776308088832?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">空港で焼酎イベントやってるー (@ 鹿児島空港 in 霧島市, 鹿児島県) <a href="https://t.co/lgeolITLBB">https://t.co/lgeolITLBB</a> <a href="https://t.co/JgsPdEl7LA">pic.twitter.com/JgsPdEl7LA</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/927007025464266752?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">温めの足湯 (@ 天然温泉足湯 おやっとさぁ in 霧島市, 鹿児島県) <a href="https://t.co/JXU0Yb6OWI">https://t.co/JXU0Yb6OWI</a> <a href="https://t.co/JtA7SbzZYQ">pic.twitter.com/JtA7SbzZYQ</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/927007890342318080?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">芋きんつば、作ってるところ初めて見た。美しい (@ 鹿児島空港 in 霧島市, 鹿児島県) <a href="https://t.co/5LCUXRksoM">https://t.co/5LCUXRksoM</a> <a href="https://t.co/Oq0sxh2tWl">pic.twitter.com/Oq0sxh2tWl</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/927019873896681472?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">浜松沖上空で１人翻訳ハッカソン中。 <a href="https://t.co/24Dr55nEVX">pic.twitter.com/24Dr55nEVX</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/927037298117459968?ref_src=twsrc%5Etfw">2017年11月5日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

鹿児島は温泉県だった。今度は観光しに来よう。


.. _Python Boot Camp in 鹿児島を開催しました: http://pyconjp.blogspot.jp/2017/11/pycamp-in-kagoshima-report.html
.. _Python Boot Camp in 鹿児島: https://pyconjp.connpass.com/event/67709/
.. _懇親会: https://pyconjp.connpass.com/event/67710/
.. _14回目: https://www.pycon.jp/support/bootcamp.html#id5
.. _CodeZineのイベント告知記事: https://codezine.jp/article/detail/10446
.. _11/18(土) 静岡: https://pyconjp.connpass.com/event/67533/

.. _一般社団法人PyCon JP: http://www.pycon.jp/
.. _チュートリアルのテキスト: http://pycamp.pycon.jp/
.. _Python Boot Camp について: http://pycamp.pycon.jp/organize/0_about.html
.. _申込みフォーム: https://docs.google.com/forms/d/e/1FAIpQLSedZskvqmwH_cvwOZecI10PA3KX5d-Ui-74aZro_cvCcTZLMw/viewform


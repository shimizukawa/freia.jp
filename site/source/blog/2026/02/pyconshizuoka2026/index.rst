:date: 2026-02-23 23:59
:tags: PyCon, PyCon Shizuoka

=================================================
PyCon mini Shizuoka 2026 に参加しました
=================================================

2月21日に静岡市で開催された、PyCon mini Shizuoka 2026 に参加しました。
昨年2月の同イベントでは私が :doc:`キーノート登壇 </blog/2025/02/pyconshizuoka2024/index>` させていただきましたが、あっという間に1年たちました。

今回は一般（パトロン）チケットとして参加しつつ、副業先のFlying Duck社がスポンサーブースを出していて、そこのお手伝いもしました。

.. figure:: opening.*
   :width: 80%

   オープニングの様子

2トラックでトーク10本以上にLT4本と、今年も盛りだくさんなイベントでした。
今回は公式パーティーがイベント会場で行われて、サプライズもあり大いに盛り上がりました。
イベントは去年と同じ会場 `静岡市コ・クリエーションスペース`_ です。

イベント概要
============================

:イベント名: PyCon mini Shizuoka 2026
:公式ウェブサイト: https://shizuoka.pycon.jp/2026/
:日付: 2026年2月21日(土) 10:00 〜 18:00
:場所: 静岡市コ・クリエーションスペース & B-nest

私の参加時のメモ（blog元ネタ）が `PyCon mini Shizuoka 2026 - 清水川のScrapbox`_ にあります。

.. _PyCon mini Shizuoka 2026 - 清水川のScrapbox: https://scrapbox.io/shimizukawa/PyCon_mini_Shizuoka_2026
.. _静岡市コ・クリエーションスペース: https://coc-shizuoka.jp/


総括
=========

- 2トラックあって、どちらを聞くか悩むこともありましたが、迷ったらスポンサーブースで聞く、という感じにしていました。
- 会場は運営メンバーが他のイベントでも利用させてもらっていて、静岡市が無料で提供しているとのこと。キャンプをイメージしたメインルームはとてもきれいで使いやすかったです。WiFiも完備。
- キーノートは静岡出身の @aodag さん。以前からキーノートやりたいとアピールしていたとか何とか。
- 飲み物やお昼ご飯の提供などは無し。スタッフがランチマップを提供してくれていました。
- 公式パーティーが会場内で開かれて 18:20 スタート。去年は懇親会が別会場（クラフトビールのお店）でしたが、今年は会場そのままで行われた（ビールあり）。初めて会う方と話すきっかけがたくさんあって良かったです。
- スポンサーブースがいくつか。今回Flying Duck社はブース用にロゴ入りテーブルクロスを用意しました。PyCon JP やBeProudでのブース出展ノウハウが活かされました。さくらインターネットさんのブースはクオリティ高かったな。


開場〜オープニング
=========================

10時開場。昨年と同じ `静岡市コ・クリエーションスペース`_ 、静岡駅から徒歩10分ほどです。地下道をうまく使って到着。

.. figure:: venue.*
   :width: 80%

   会場の様子

ConnpassのQRコードで受付を済ませ（手軽で良いですね）、受け取った名札に手書きで名前を書くスタイル。

10時半からオープニング。スタッフからイベントの案内がありました。


キーノート
================================

- 10:45 〜
- Atsushi Odagiri (@aodag)
- 資料: https://github.com/aodag/pycon-mini-shizuoka-2026/blob/main/slide.org

.. figure:: keynote.*
   :width: 80%

   キーノートの @aodag さん

キーノートは、スクリプトとして使うのに知っておきたいPythonの使い方。
着眼点が最近のAIやデータ系でなく、Webですらなく、Pythonの基本という感じで良かった。
参考文献がPython公式ドキュメントのみ。

振り切り方が良いですね。

詳しい内容は `PyCon mini Shizuoka 2026 - 清水川のScrapbox`_ のメモを参照ください。

ランチ
===========

キーノートが終わったら午前中おわり。
スタッフが用意してくれた `グルメマップ`_ を頼りに各自ランチに出かけていきました。


.. figure:: lunch1.*
    :width: 80%

    のっけ家、並んでたのでまちながらメニュー検討

.. figure:: lunch2.*
    :width: 80%

    のっけ家、まぐろづくし丼

.. figure:: gelato1.*
    :width: 80%

    ななやの、ジェラート。7番が一番濃い

.. figure:: gelato2.*
    :width: 80%

    ほうじ茶+抹茶7番

ななやの7番は、3年くらい前に知ってからずっと狙ってましたが、これまで日が合わず行けていませんでした。この日は日中とても暖かくて上着不要なくらいだったこともあり、とても美味しい濃い抹茶ジェラートを楽しめました。

.. _グルメマップ: https://www.google.com/maps/d/u/4/edit?mid=1C4EJXgTE4CnC1-HQOO-D4A0xqCP2zdc&usp=sharing

トーク
================================

2トラック6セッション + ブース出展ショートトーク + LT という構成でした。

PythonでWeb地図アプリを作ってみよう（ぴっかりん）
-----------------------------------------------------------------

- 13:20 〜 トラック2
- ぴっかりん
- レベル：Basic / カテゴリ：可視化
- 資料: https://speakerdeck.com/ra0kley/pythondewebdi-tu-apuriwozuo-tutemiyou

.. figure:: talk1.*
    :width: 80%

    ぴっかりんさん

静岡県は3Dデータの作成に力を入れていて、 `東京都デジタルツイン3Dビューア`_ でみれるということで紹介されてました。
また、3次元空間を2次元の地図で表示するのに、「Webメルカトル」という図法があって、これを作ったのがGoogleの人。北極点南極点付近をカットすることで2次元に展開したときの歪みの影響を減らしているらしい。なるほどーー。

今回のトークでは、 `leafmap`_ を使ってJupyter上でインタラクティブな地図を表示する紹介でした。
タイル地図をベースに、マーカーを重ね合わせて表示など、Pythonで地図アプリが作れるのはとても便利そう。

コード3行で地図が出る！

.. code-block:: python

   import leafmap
   m = leafmap.Map(center=(40, 140), zoom=4)
   m

トーク中にさっそく ``uv init`` して ``uv add leafmap`` でインストールして試してみました。
Windowsターミナルでは、Jupyter上でのように地図は表示されず。
``m.to_html("index.html")`` でHTMLとして出力してブラウザで開いたら見れました。


.. _leafmap: https://pypi.org/project/leafmap/
.. _東京都デジタルツイン3Dビューア: https://3dview.tokyo-digitaltwin.metro.tokyo.lg.jp/


Pydanticで複雑なJSONを一発でValidation（Takanori Suzuki）
-----------------------------------------------------------------

- 15:50 〜 トラック1
- Takanori Suzuki
- レベル：Advanced / カテゴリ：Pythonコア, プログラミングノウハウ（RPA, 自動化）
- 資料: https://slides.takanory.net/slides/20260221shizuoka/

.. figure:: talk3.*
    :width: 80%

学習教材の入力フォーム形式定義を JSON + JSONSchema で行っていたけど、共通部分もそれぞれで定義する必要があり、 Pydantic_ に切り替えたという話でした。

Pydantic、ちょっとしたことのために導入するにはフットプリントが大きそうで避けたい気もしますが、JSONのデータ構造をPythonコードで表現できて、IDE補完も効くようになり、バリデーションもできるので、便利ですよね。
JSONをDBに格納することも多いので、そのデータ構造を保証するバリデーションに使いたい。

質疑応答でも、Pydanticにしたことでテストがしやすくなった、と言及されてました。

.. _Pydantic: https://docs.pydantic.dev/latest/


その他のトーク
---------------------

今回参加したトークのメモや質疑応答は `PyCon mini Shizuoka 2026 - 清水川のScrapbox`_ にメモしました。


ブース出展
=======================

Flying Duck 社で副業を1年ほどしてます（いずれblog書きたい）。
代表の八木さんは今回イベントの当日スタッフもやっているため、ブースにずっと居るわけにもいかず、午後は私がお店番しつつトークを聞いたり、ブースに来てくれた方何人かと話したりしていました。

.. figure:: flyingduck-booths.*
   :width: 80%

   Flying Duck ブースの、用意したロゴ入りテーブルクロスが眩しい

14:50 からのブース出展ショートトークでは、kata-studio さん、Flying Duck、さくらインターネット、PythonED、BeProud などが、5分LT形式でスポンサートークを行いました。

.. figure:: flyingduck-talk.*
   :width: 80%

   Flying Duck のスポンサートーク（横に立ってみた）

`Flying DuckのLTスライド`_ は前日に八木さんが作ったものを私と会社のもう1人とでレビューをして、話す順番を入れ替えたり、トーンを調整したりして用意しました。Flying Duckのシステムは、グリーンエナジーを活用して工場の電力需要と燃料消費を社会全体で最適化することを目指しています、という話をPythonのカンファレンスで分かりやすく、面白く伝えるには話をどう展開したら良いか・・・、試行錯誤した甲斐あって会場の反応も良かったように思います。

.. raw:: html

   <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTvvT_6IQpW23Z7CWk76cMAVCxL1Wcm0jqMjzEivQkTzAjzfcpuQQxmQI-8PmpZarnYfZsM200qVgXb/pubembed?start=false&loop=false&delayms=3000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

そういえば、ブースで銭湯経営で重油消費をなんとか改善したいという方の話を聞くこともでき、大規模工場でなくてもニーズがありそうな予感がしました。

LTについて詳しくは `PyCon mini Shizuoka 2026 - 清水川のScrapbox`_ にメモしました。

.. _Flying DuckのLTスライド: https://docs.google.com/presentation/d/e/2PACX-1vTvvT_6IQpW23Z7CWk76cMAVCxL1Wcm0jqMjzEivQkTzAjzfcpuQQxmQI-8PmpZarnYfZsM200qVgXb/pub

LT & クロージング
=========================

17:20 から LT & クロージング。

.. figure:: lt.*
   :width: 80%

   LTのwhitphxさん

LTでは、Yuichiro Tachibana (whitphx) さんの話 `How OSS becomes a give-and-take activity`_ が良かった。
「OSSへの貢献は **善意** だけでなく、保守コストを減らしてお互いを活かす **経済合理性** で持続する」という内容でした。
20年以上OSSに関わってきたなかで、OSSコードにカスタマイズパッチを当てて使い続けるのが大変だ、という企業利用者の話は何度も聞いたことがあります。OSSへの寄生ではなく共生関係を作れた例としてとても良い事例の紹介でした。


.. _How OSS becomes a give-and-take activity: https://slides.whitphx.info/202602-oss-give-and-take/

そしてクロージング。

.. figure:: closing.*
   :width: 80%

   クロージング

最後にみんなで集合写真を撮影して、解散になりました。

公式パーティー
=================================

18:20 から会場内でパーティーが行われました。去年はお店へ移動しましたが、今年は会場そのままでの開催。会場移動なしだと、イベント参加そのままの雰囲気で色々な人と話せて良いですね。あと、立食だと適度にまざりつつ話せるのでそれも良い。

パーティー冒頭で、West Coast Brewing の樽がサプライズ登場！すごい！
（一部のビール好きのひとたちがキャッキャしてました。キャッキャッ）
わざわざ用宗まで車で取りに行ってきてくれたとのこと。塚本さんありがと～！

.. figure:: party-kyakkya.*
   :height: 400px

   キャッキャッ

ビールは他にもWCBの500ml缶や御殿場高原ビールの1L缶などあり、また、料理のオードブルもかなり美味しかった！

.. figure:: party-food.*
   :width: 80%

   オードブル美味しかった

.. figure:: party-kanpai.*
   :width: 80%

   かんぱい！

.. figure:: party-beers.*
   :width: 80%

   ありがとうございました！


感想
=====================

去年はキーノートとして参加したこともあり前夜まで準備が大変でしたが、今年は登壇なしでスポンサー関係者、という少し違う角度からイベントを楽しめました。

イベント運営のみなさん、素敵なイベント開催、ありがとうございました！

次は、3月にフィリピンで開催される PythonAsia イベント（ `PyCon APACの後継のようなもの`_ ）に行きます。トーク予定あり。
この1年、英語の練習は続けていますが、トーク練習はあんちょこを見ずに英語で話せるように準備しないと.. がんばろう。

.. _PyCon APACの後継のようなもの: TBD

:date: 2026-04-05 23:00
:tags: Python, PythonAsia, PAO, フィリピン, PyCon

==========================================
PythonAsia 2026 に参加しました
==========================================

3月下旬にフィリピン・マニラで開催された、PythonAsia 2026 に参加しました。
PythonAsia は、昨年まで開催されていたPyCon APACの後継 [#]_ にあたるイベントで、Python Asia Organizationが主催する最初のカンファレンスになります。

.. [#] 詳細は以下の記事を参照してください

       - https://pyconjp.blogspot.com/2025/12/pythonasia-online-charity-talk-h2.html
       - https://iqbalabdullah.net/en/posts/2025/03/the-final-pycon-apac/

.. figure:: opening-remarks.*
   :width: 80%

   PythonAsia 2026 オープニング。テーマは KALINGA / CARE

今年はフィリピンの De La Salle University (DLSU) を会場として開催されました。
私のフィリピンでのイベント参加は一昨年2月の :doc:`PyCon PH 2024 </blog/2024/02/pyconph2024/index>` 、昨年3月の :doc:`PyCon APAC 2025 </blog/2025/03/pyconapac2025/index>` に続き、3年連続となります。

今回も日本から7名ほどがスピーカーとして参加しました（今年も日本勢おおいな！）

イベント概要
==============

:イベント名: PythonAsia 2026
:公式ウェブサイト: https://2026.pythonasia.org/
:日付: 2026年3月21日(土)DAY1トーク、22日(日)DAY2トーク、23日(月)スプリント
:場所: De La Salle University (DLSU), Manila, Philippines

私はDAY1、DAY2に参加しました。DAY3のスプリントはオープニングだけ顔を出しました。

参加時のトークのメモや質疑応答のメモが以下にあります。

- https://scrapbox.io/shimizukawa/PythonAsia_2026


総括
=========

PythonAsia 2026 は、昨年の PyCon APAC 2025 と同じフィリピン開催で、昨年とは別の大学キャンパスが会場でした。
日本からのスピーカーが7名、イベント名や主催が変わって最初のカンファレンスではありますが、イベントとしては例年どおりにぎやかな雰囲気でした。

- 全体の雰囲気は明るくにぎやか。しかし会場の空調が効きすぎてて寒い！
- イベント中の WiFi はスピーカー限定かつあまり強くないこともあり、au海外放題（容量無制限 日/800円 = 3日間2400円）を利用しました。安定して使えて良かったです。
- 1日目夜はVIP招待パーティーで kuya's へ。一昨年の :doc:`PyCon PH 2024 </blog/2024/02/pyconph2024/index>` でも行ったお店です。Sisig（肉の唐辛子炒め、フィリピンの伝統料理）をつまみながらアジア各国のPythonistaと交流しました（お酒なし！）。その後、知り合い同士でビールにいって、1杯（翌日のトーク準備もあるので自重）。
- コーヒーはチケット制で提供されていました。2日目に @takanory さんからチケットをもらえてラッキー！ ありがとうございます。
- ランチは2日目に選んだチキンイナサルがおいしかった！ イナサルはフィリピンの伝統的な炭火焼き？チキングリルです。2日目のトーク直前だったこともあり、スピーカールームでスライド確認しながら1人淋しく食ました。
- 2日目夜は有志で Perfect Pint へ。醸造タンクをみながら知り合い同士で飲んでました。
- Financial Aid（旅費補助）を申請していて、DAY2に無事フィリピン₱を受け取りました。ありがたい。

自分のトークセッション
=========================

- 日時場所

  - 3月22日（日） 13:15 - 13:45
  - Talk: https://pretalx.com/python-asia-2026/talk/SHDM83/
  - Title: "Creating Presentation Slides with the Retro Game Engine Pyxel"
  - Slide: https://shimizukawa.github.io/pyxel-slide-pyasia-2026/index.html
  - Repo: https://github.com/shimizukawa/pyxel-slide-pyasia-2026/

.. figure:: mytalk-photo.*
   :width: 80%

   恒例の演台からの写真。みんないい笑顔！

このトークでは、レトロゲームエンジンPyxelと、私が実装したレトロプレゼンスライドエンジンを紹介しました。

レトロプレゼンスライドの技術的な実装詳細（BDFフォント、画像バンク、ディザリング、Markdownパーサー等）については、昨年12月に日本語で書いた記事 :doc:`/blog/2025/12/pyxel-slide/index` を参照してください。

上記の記事は、今回のトークに向けた原稿の日本語版で、英語版ではスライド上の文章量を減らして「文章を読み上げない」ための対策をしたり、プレゼンしやすいように順番を入れ替えたり調整したり、プログラム自体にもデモが面白くなるようにデモ用の隠し機能を追加しました。

また、今回は「英語スクリプトなし」でのトークに初挑戦しました。


英語スクリプトなしトークに挑戦
------------------------------------

今回のトークは、英語のスクリプト（原稿）を一切用意しませんでした。

2012年に初めて海外トークを行いましたが、その時は英語スクリプトを読み上げるので精一杯でした。
その後、技術の進歩によって、 :doc:`/blog/2024/03/talk-shadowing/index` が出来るようになり、2年前の :doc:`PyCon PH 2024 </blog/2024/02/pyconph2024/index>` では多少気持ちの余裕ができたものの、スクリプトを用意するとどうしても「ちゃんと読もう」とする意識が働くのか、読み上げる感じでずっと下を向いて話してしまってました。

昨年5月の :doc:`PyCon US 2025 in Pittsburg に参加 </blog/2025/05/pyconus2025/index>` に向けて、なかなか始められなかった英会話レッスンを3月から始めて、「準備なしで英語で会話」「思ったことをその場で話す」事ができるようになることを目標にしていました。
今回のトークは、レッスンを始めてちょうど1年目のタイミングで、「スクリプトなしで、スライドに合わせて思ったことを話す」のを試す場になりました。

スライドはあくまで話したいことの要点、骨格で、それを「読む」のではなく「見ながら話す」ことを目指しました。
その結果、スライドに書いていない話題を自然な感じ（読み上げではない感じ）で話せたのではないかと思います。


**スライド外1：導入のゲームデモ**

トーク開始直後、「Do you like video games?（ビデオゲーム好きですか？）」と会場に呼びかけ、Pyxelで作ったゲームをその場で参加者にプレイしてもらいました。
プレイしてもらっている間、「このゲームは息子に『宿題やってる間にゲーム作ってあげる』と伝えて、宿題をしている横で60分ほどで作りました」と話しました。
私のハイスコアは155mだと言ったら笑いが起きて、ほどよいアイスブレイクになりました。

Pyxelはゲームエンジンなので、参加者に遊んでもらうのが一番分かりやすいんじゃないかと思い、最初に参加者を巻き込む形で入れつつ、小話を英語で話すということに挑戦してみました。


**スライド外2：自己紹介の肉付け**

スライドの自己紹介欄には「Takayuki Shimizukawa, co-maintainer of Sphinx, started programming in 199x」と書いて、
実際のトークでは「2年前までマニラに住んでいた」「Sisigが大好き（フィリピンの豚肉料理）、妻はChikin Inasalが好き」という話をしました。

フィリピンでの開催というコンテキストで、現地の食べ物の話を盛り込んだ自己紹介をしたんですが、1日目のキーノートでJayさんも同じ手法でよりトーク内容と関連したつなぎ方をされていて、やられたなーと思いながら聞いていました。


**スライド外3：WebSocket機能の紹介**

WebSocket通信は、時間の余裕があれば話そうと思い、スライドには書きませんでした。
「スライドを開いている全員のページ表示位置がお互いのスライドに表示する機能を WebSocket 通信で実装していて、PyodidoではwebsocketライブラリがないのでJSのWebSocket APIをPythonから呼び出している」といったことを話しました。

表示位置は、Pyxelのサンプルに入っていたキャラクターを使っています。トーク中ずっと表示されていて、他の人がどのあたりを読んでいるのか分かるのは自分も見ていて面白かったです。

**スライド外4：デバッグモードの実演**

「ノートPCからこのスライドを開いている人は、キーボードの ``0`` を押してみてください」と呼びかけて、デバッグモードの実演をしました。
スライドエンジンのレイアウト実装でバグが出やすく、それを確認するためのデバッグ表示モードを作った、という話です。
「まだバグが残ってます（バウンディングボックスの位置が合っていないものがある）」という正直なコメントも付け加えました。

文法や単語の間違いは色々あったと思います。
でも「スライドを読む」から「スライドを見ながら話す」への移行という意味では、一歩前進できたかなと感じています。


質疑応答
-----------

トーク後の質疑応答で印象に残ったのは、最初のコメントでした。

「質問ではないのですが、これは技術の無駄遣いだとは思いません。これは創作活動だと思います（Not a question, more of a comment. I don't think this is a waste of technology. I think this means creativity.）」

スライドに「技術の無駄遣い（A waste of technology）」というキーワードを入れていて、「それも大事だよ」ということを伝えたつもりでしたが、こんなふうに受け取ってもらえたのは嬉しかったです。

DAY1 キーノート
============================

最初のキーノートは Jay Miller さんによる「Yellow Cab, Jollybee, Haircuts and Smoothies: Building Legendary Communities through experiences beyond the walls」。
2009年にフィリピンに住んでいた頃の体験（Yellow CABのピザ、ジョリビーのチキン、スムージ、床屋！）から始まる話で、フィリピンに住んでいる人であれば分かるあるあるネタで私も一時期住んでいたのでとても面白く聞いていました。そこからコミュニティ形成の話に進んでいき、その秘訣として「予定外の誰かとランチしよう」「ライトニングトークに登壇しよう」「パックマンルールで輪を広げよう」を紹介してくれました。
全体的に面白くて引き込まれる話でした。

.. figure:: keynote1-jay2.*
   :width: 80%

   Yellow CAB、ジョリビー…… フィリピンの思い出を語る Jay Miller さん

.. figure:: keynote1-jay.*
   :width: 80%

   「HUNGRY?」— フィリピン経験からコミュニティ形成の話へ

Q&A も活発で、「これまで訪れた国で最高だった食事は？」という質問への答えが「ラトビアのリガのお店が最高だった（誰もミシュラン星付きだと知らずに入った）」というエピソードで、会場が沸いていました。

2つ目のキーノートは Charibeth Cheng さんによる「Architectures of Ambiguity: Mapping the Technical Hurdles of Cultural Sensitivity in Localized LLMs」。LLMをローカライズする際の文化的感受性に関する技術的なハードルを扱う内容でした。

DAY2 キーノート
====================

2日目のキーノートは Daniel Roy Greenfeld さんと Audrey Roy Greenfeld さん。
お二人は『Two Scoops of Django』という書籍（日本未翻訳）の著者です。
トークは「Air: The Web Framework AI Can Actually Understand」で、AI時代に合わせて設計した新しい Webフレームワーク `Air`_ の紹介でした。

ベースにFastAPIを使っていて、Jinja2とHTMXのテンプレート層を載せたような感じ、でしょうか。
お二人によると、従来のDjangoのようなフレームワークはAIにとって生成・管理すべきファイル数が多すぎるので、必要なファイル数を少なく保てるWebフレームワークが必要と感じたそうです。そのため、Airは設計を根本から見直し、利用者が実装するべきコード量を最小限に抑えることで、AIがバグを出さずにアプリを構築・保守しやすい環境を実現した、ということでした。

まだ発展途上ということで今後どうなっていくのかが気になるところです。
Q&A で「Django みたいなバッテリー同梱の計画はあるか？」と聞いたら「Admin はほしいと思う」と回答されていました。

.. figure:: keynote3-air.*
   :width: 80%

   Daniel & Audrey Roy Greenfeld さんによる Air フレームワーク紹介

.. _Air: https://github.com/feldroy/air


参加した他の方のトーク
============================

以下のトークを聞きました。メモや質疑応答は https://scrapbox.io/shimizukawa/PythonAsia_2026 にあります。

- **nikkie**: `Breaking Free from Virtual Environments`_— venv歴史からuv/PEP-723への道筋。これまでのトークの集大成で「とにかくuv！」という締め。
- **whitphx**: `A reliable development/release workflow for open source Python libraries`_ — hatch-vcs、changelog管理。CI のセキュリティ面で ``test-build.yml`` にはシークレットを公開せず、 ``post-test.yml`` でシークレットが必要な処理を行う手法の紹介、これは良い知見でした。
- **Yu Saito**: `Zstandard in Python 3.14 Faster Compression You Can Use Today`_ — Python 3.14から標準入りする圧縮ライブラリ。ロギングコスト2〜3分の1の事例。
- **Anahara**: `Fixit linter+AI coding`_ — MetaのFixitツールのルールをAIに自然言語で書かせて翻訳。 ``structlog.get_logger()`` への統一ルールは有る有る。
- **kamijo**: `Inside a Database: A Code-Level Walkthrough of an RDBMS I Built in Python`_ — SQLパースからディスク読み書きまでPythonでRDBMSを自作。仕組みを学ぶ最高のプロジェクト。
- **HayaoSuzuki**: `Let's implement useless Python objects`_ — Pythonオブジェクトプロトコルを実装し続けた結果、確かに役に立たなかったw
- **Romar Mayer R. Micabalo**: `Parenting with Python`_ — ``The Zen of Python`` を子育てに適用するというトーク。「Beautiful is better than ugly」「Errors should never pass silently」「Now is better than never」など、プログラミングにも人生にも通じる言葉を子育ての文脈で解釈していく内容で、ほっこりしました。
- **MrValdez**: `Let's live code a game with Arcade in less than 30 minutes!`_ - Pythonの `Arcade`_ を使ったライブコーディングセッション。といっても基本コピペでデバッグ時間が多め、ただ見せ方が面白かった。最後に動いたときは拍手喝采でした

.. _`Breaking Free from Virtual Environments`: https://pretalx.com/python-asia-2026/talk/FNMQY9/
.. _`A reliable development/release workflow for open source Python libraries`: https://pretalx.com/python-asia-2026/talk/SYAEEJ/]
.. _`Zstandard in Python 3.14 Faster Compression You Can Use Today`: https://pretalx.com/python-asia-2026/talk/G3WBUG/
.. _`Fixit linter+AI coding`: https://pretalx.com/python-asia-2026/talk/3EU3VA/
.. _`Inside a Database: A Code-Level Walkthrough of an RDBMS I Built in Python`: 
.. _`Let's implement useless Python objects`: https://pretalx.com/python-asia-2026/talk/9YYPZU/
.. _`Parenting with Python`: https://pretalx.com/python-asia-2026/talk/GHHRQF/
.. _`Let's live code a game with Arcade in less than 30 minutes!`: https://pretalx.com/python-asia-2026/talk/7CZJH9/
.. _Arcade: https://api.arcade.academy/


食べ物、飲み物
===================

1日目、2日目ともスナックがありましたが、おやつというより、軽食。焼きそば。
そういえば一昨年のスナックはスパゲッティだった。

焼きそば食べながら「来年の PythonAsia はどこかねえ？」とtakanoryさんと話していました。
タイ？ ベトナム？ インド？ インド料理好きだから行ってみたいけど、水が合わないと大変そうなイメージ。
フィリピンでも生水は飲んではいけないですが、氷が生水のこともあるし、硬水が合わないことも。

1日目の夜はVIP招待パーティーで kuya's へ。
昨年の PyCon PH 2024 でも行ったお店で、Sisigをつまみながらアジア各国のPythonistaと交流しました。

.. figure:: kuyas-vip-dinner.*
   :width: 80%

   kuya's のビュッフェ。フィリピン料理がずらりと並ぶ

2日目の夜は Perfect Pint で日本チームで打ち上げ！ 2日間お疲れ様でした〜。

.. figure:: perfect-pint.*
   :width: 80%

   The Perfect Pint の醸造タンク。これを眺めながら乾杯

.. figure:: sisig.*
   :width: 80%

   Sisig — 豚肉と野菜の炒め物。フィリピンの伝統料理


イベント感想
================

フィリピンで開催のPyCon的イベントには、縁あって3年連続の参加でした。
1回目は「フィリピンに住んでるから参加しよう」と思って参加。2回目は「PyCon APACだから参加」。3回目は「PythonAsiaだから参加」。
それぞれトークも採択され、日本からの参加時には旅費支援も申請させていただき、継続的な参加ができています。
ありがとうございます。

.. figure:: jpteam-photo.*
   :width: 80%

   日本から参加したみなさん

DAY 0 には、フィリピンに住んでいたときに通っていたビアパブ Tap Station にも行けた。楽しかった！

.. figure:: tapstation.*
   :width: 80%

   Tap Station での前夜ビアバッシュ。みんないい笑顔！

来年の PythonAsia がどこで開催されるかは未定ですが、タイ・インドあたり、行ったことがない国だと個人的には嬉しいなあ。
どこで開催されるにしても、プロポーザルを出して参加したいと思っています。

その前に、まずは8月開催のPyCon JP 2026 に向けてトークネタを絞り出さねば.. 

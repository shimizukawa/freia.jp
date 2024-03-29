:date: 2024-03-09 16:00
:tags: English, Talk, Amazon Polly, Gemini

===============================================================
Amazon Pollyで英語トークのシャドーイング練習
===============================================================

海外イベント登壇の準備として、トーク原稿をAmazon Pollyで英語の音声合成して、その音声を真似て話すシャドーイング練習をしました。

海外イベントに登壇するとき、トークを少しでも伝わるように話したいと思いました。8年くらい前は翻訳にしろ発音練習にしろ、ネイティブ英語話者に見て教えてもらう必要がありましたが、今は自力で短時間でなんとかできるようになりました。

先日参加した :doc:`PyCon Philippines 2024 <../../02/pyconph2024/index>` ではトークセッションを1つ持たせていただいたので、シャドーイングのための原稿用意から音声合成まで、以下の手順で行いました。

.. contents::
   :local:

.. 1. 日本語音声を用意（録音ツールや録画を使う）
.. 2. 日本語文字起こし（Windowsの場合はWin+Hで起動）
.. 3. 文字をト書きに清書（ここは人力。文字起こし精度次第で手間が変わる）
.. 4. Geminiで英訳（高校生レベルの英語にしてください）
.. 5. Amazon Pollyで音声合成（マネしやすい声を選ぶ）
.. 6. トークのシャドーイング
.. 7. スライドのスピーカーノートにト書きを反映

それぞれ紹介します。

.. image:: ./amazon-polly.*
   :width: 1px
   :height: 1px

前提として、自分はあまり英会話が得意ではありません。出来れば話さずに済ませたいくらいです。
英語書籍の翻訳を10年以上やってきたおかげで、その分野の英語は読めるし語彙もそれなりに身に付いていると思います。
しかし、音声情報は発音が悪いと伝わらないし、文字のように読み返すことも出来ないこともあって、けっこう苦労しています。

トーク2日前の時点で、発音が悪いまま英語トークするのはマズいな、、という思いがあり、日本語で話した内容を文字起こしして、英語ネイティブ発音を合成してシャドーイング練習しよう、と思い付きました。

思い付いてから練習開始できるようになるまで2～3時間くらいで準備出来ました。


1. 日本語音声を用意（録音ツールや録画を使う）
==================================================

まず、自分でスライドをめくりながら、実際の時間でしゃべるのを録音する。

- 録音はGoogle Meetで録画とか、アプリの録音ツールとか、色々あります
- 今回は、 `PyCon JP 2017のトーク`_ を英語で再演するので、その録画を使いました

今回、この手順を飛ばして英語ト書きを作ったところ、淡々とした内容になってしまったので捨てました。母国語で良い感じに話した録音があると、それを元にするのが自分には一番良さそうです。

.. _PyCon JP 2017のトーク: https://youtu.be/aich6wqftkA

2. 日本語文字起こし（Windowsの場合はWin+Hで起動）
=========================================================

録音からの文字起こしはWindows標準ツール（Ctl+Hで起動）でやりました。

- `タイピングではなく音声で PC に入力するために音声入力を使用する - Microsoft サポート <https://support.microsoft.com/ja-jp/windows/fec94565-c4bd-329d-e59a-af033fa5689f>`_
- 他にも、OpenAIの文字起こしAI "Whisper"なども使えると思います

.. figure:: 20240309-mojiokoshi.mp4
   :class: controls

   Windows11標準アプリでの音声文字起こし

録音からこのツールで文字起こしするために、音声ループバックで文字起こしツールに流し込む必要があります。以前のWindowsには音声ミキサーツールでループバック設定ができましたが、今は出来ないっぽいので、別途ドライバーをインストールしました。

- `VB-Audio Virtual Apps <https://vb-audio.com/Cable/index.htm>`_

3. 文字をト書きに清書（ここは人力。文字起こし精度次第で手間が変わる）
======================================================================

文字起こしが出来たら、文章を校正します。

しゃべった録音から文字起こしをすると、漢字変換ミスや専門用語の間違い、そして「えっと」などの発言がけっこう入ってしまいます。これがあると、次のステップで英訳がおかしくなるので、このタイミングで清書します。

他にも、誤解しそうな文面なども直します。
日本語（母国語）で誤解を招きそうなら、英語では意味が通じないかも？と思います。

この作業で、英語でしゃべる予定の文面の日本語版ト書きが完成しました。

実際に用意したト書きはこちらです::

    `len()`関数がオブジェクトになると手に入れる方法初級。唐辛子レベル1です。
    唐辛子は難易度だと思ってください。

:doc:`pyconph-2024-howlenfunctiongetlength-ja`

4. Geminiで英訳（高校生レベルの英語にしてください）
=========================================================

英訳は、数年前までは自分にとってけっこう大変な作業でした。
当時のツールは怪しい英語が出てきていたのて、その文面が英語として使えるのかを調べる必要がありました。

今はAIチャットに翻訳をお願いすれば、自然な英語がでてきます（たぶん）。
今回は、ChatGPT-4（OpenAI）と Gemini（Google）を比べてみたらGeminiの方が良かったので、そちらで翻訳しました。

私がAI英訳に使う定番プロンプトは「高校生レベルの英語にしてください」です。
自分が使い慣れていない英語だと、英文として正しいか判断できないし、話せる自信が無いためです。

実際に使ったプロンプト:

    以下はカジュアルな技術カンファレンスでの発表資料のト書きです。これを高校生レベルの英語に翻訳してください。記法は変えず、そのまま読み上げられるようにしてください。

    <以下、ト書き全文>

これで出力された英文がこちら::

    Part1
    How does `len()` get the length of an object?
    This part is beginner level.
    Think of the chili as indicating difficulty.

:doc:`pyconph-2024-howlenfunctiongetlength-en`

5. Amazon Pollyで音声合成（マネしやすい声を選ぶ）
===================================================

英語文面ができたら、Amazon Polly で音声を合成します。

.. figure:: ./amazon-polly.*
   :width: 800px

   AWS Console の Amazon Polly 画面

英語は声を10種類くらいから選べるので、自分が話せそうな英語のイントネーションで、話す速度が理想に近い声を選びます。

- AWS Consoleにログインして、Pollyを表示
- 先頭の1000文字くらいを貼って、サンプル再生しながら声を選択
- 良さそうな声が決まったら、全文を貼り付けて音声生成
- 1分弱でS3に出力されるので、これでシャドーイングの音声が完成

この方法だと、抑揚なく途切れなく話し続ける音声が出来上がります。
Pollyの制御コマンド SSML_ を使えば、間を空けるとかもできるらしいですが、
シャドーイング用としては十分かなと思います。

最終的に出来上がった音声ファイルはこちら。

.. raw:: html

   <audio controls="controls">
     <source src="../../../../_static/pyconph-2024-howlenfunctiongetlength-en.mp3" type="audio/wav">
     Your browser does not support the <code>audio</code> element. 
   </audio>

.. _SSML: https://docs.aws.amazon.com/ja_jp/polly/latest/dg/supportedtags.html

6. トークのシャドーイング
=============================

音声ファイルが生成されたら、スマートフォンにコピーして、できるだけ繰り返し聞いてマネします。

- 音声に合わせて自分でも発音してみる
- 話しづらい箇所、使い慣れない単語などは、元の英文を修正してPollyで再生成
- できる限り耳を慣らして、発音できるように繰り返す

7. スライドのスピーカーノートにト書きを反映
==============================================

スライドに埋め込んで、トーク中に見れるようにしておきます。
ト書きを読み上げるためにずっと画面をみてしまいがちですが、シャドーイングを繰り返せば画面を見なくなる・・かも？

今回、音声ファイルの時間が15分で、トークの持ち時間が30分だったので、すこし間を多めにするとか、読み上げない予定のスライド上の文面を読むとかをして調整出来ました。

最終的なスライドはこちらです。

.. figure:: ./pyconph-2024-howlenfunctiongetlength-slide.*
   :width: 800px
   :target: https://docs.google.com/presentation/d/1_TSnjsaVJnqMb9VjaYmlPJqO-TVi0KoM8FZg55vOP70/edit#slide=id.g2b642c9cc19_0_15

   `How does Python get the length with the len function for PyCon PH 2024 - Google スライド <https://docs.google.com/presentation/d/1_TSnjsaVJnqMb9VjaYmlPJqO-TVi0KoM8FZg55vOP70/edit#slide=id.g2b642c9cc19_0_15>`_


以上です。

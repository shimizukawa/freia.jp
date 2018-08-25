:date: 2018-08-19 23:59
:tags: Sphinx

===========================================
Sphinx + 翻訳 hack-a-thon 2018.08 #sphinxjp
===========================================

久々にhack-a-thon参加blog.

SphinxのHack-a-thonイベントに参加してきました。

.. figure:: oyatsu.*
   :width: 80%

   今日のオヤツ. @usaturn++

:イベント: `Sphinx+翻訳 hack-a-thon 2018.08`_
:参加者: @tk0miya, @shimizukawa, @cocoatomo, nskgch, @usaturn
:会場: タイムインターメディア社（曙橋）

.. _Sphinx+翻訳 hack-a-thon 2018.08: https://sphinxjp.connpass.com/event/96320/


自己紹介、やること
==================

.. figure:: todos.*
   :width: 80%

   やること

* @tk0miya: 「Sphinx-1.7.7と1.8.0b1のリリースに向けてコード書きます。」
* @shimizukawa「Sphinx-1.7.7リリースに向けてIssue/PR確認を手伝います」
* @cocoatomo: 「 `Python公式ドキュメント <https://docs.python.org/ja/>`_ の翻訳と関連チケットの確認をやります。疲れたらpipenvの翻訳、飽きたらdocutilsの型付け。逃げ道をたくさん用意してます。」
* nskgch: 「Sphinxドキュメント翻訳の手伝いをしてます。今日もやります」
* @usaturn: 「」


自分がやったこと
================

用事で15時に帰らないといけなくなったため、朝10時くらいから近所でhackしてました。@tk0miya が会場をはやく開けてくれたので、12時すぎくらいから現地でhack開始。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">pre- sphinx hack-a-thon!! <a href="https://twitter.com/hashtag/sphinxjp?src=hash&amp;ref_src=twsrc%5Etfw">#sphinxjp</a> (@ Starbucks Coffee 北の丸スクエア店 - <a href="https://twitter.com/Starbucks_J?ref_src=twsrc%5Etfw">@starbucks_j</a> in 千代田区, 東京都) <a href="https://t.co/3UkT5YdSvc">https://t.co/3UkT5YdSvc</a> <a href="https://t.co/CYYMBGnKoN">pic.twitter.com/CYYMBGnKoN</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/1030989327571079168?ref_src=twsrc%5Etfw">2018年8月19日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


PRをいくつかレビューして、Issue見ました

* https://github.com/python-doc-ja/python-doc-ja/issues/792

* https://github.com/sphinx-doc/sphinx/pull/5312

  ``sphinx-quickstart`` コマンドをPowerShellで使うと、質問文の文字色が背景色と同じで読めない、という問題への対処。 ``purple`` をやめて ``bold`` にするPRを実際にWindows PowerShell で動作検証した。

  結局、 ``bold`` っていってもコンソール上ではフォントを変えて文字を太くできるわけではないので、デフォルトの文字色をちょっとくすんだ色にして、 ``bold`` 指定が来たらハッキリした色で表示するように、ターミナルのカラースキーマが設定されています。

  この確認のために、purpleとは何か、boldとは何か、みたいなのを把握する必要がありました。
  ANSIのエスケープコードを使って文字色を変えるんだけど、黒なら ``30m`` 、白なら ``37m`` 、白のボールドなら ``1;37m`` で白の標準色なら ``0;37m`` みたいに指定する。各エスケープコードで実際にどんな色を表示するかはターミナルのカラースキーム設定に依存しているので、PowerShellでの出力を把握するために `Windows Console Colortool <https://scrapbox.io/shimizukawa/Windows_Console_Colortool>`_ を使ってみました。

  .. figure:: ansi-escape-code-color.png
     :width: 80%

     Sphinxの文字出力と `Windows Console Colortool`_


  残念ながらPowerShellでは実際のANSIエスケープコードでの表示色とは異なる色を提示しているみたい。cmd.exe向けなのかな。

  このときの結論としては、PowerShellでboldというと黄色で出力される。背景色とかぶらない方がよいので、Windowsでは質問文をpurpleではなくboldで表示する、ということにしました。

* https://github.com/sphinx-doc/sphinx/pull/5315

* https://github.com/sphinx-doc/sphinx/pull/5297


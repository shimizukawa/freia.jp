:date: 2017-05-07 19:00
:categories: ['Sphinx']
:body type: text/x-rst

=====================================================
2017/05/07 Sphinx+翻訳 hack-a-thon 2017.05 #sphinxjp
=====================================================

*Category: 'Sphinx'*

`Sphinx+翻訳 hack-a-thon 2017.05`_ に参加しました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash">#sphinxjp</a> GW最終日はSphinx+翻訳 Hack-a-thon。 おやつ食べながらhack中 (@ タイムインターメディア in 新宿区, 東京都) <a href="https://t.co/REysQI6gGN">https://t.co/REysQI6gGN</a> <a href="https://t.co/1p78NlWQ1L">pic.twitter.com/1p78NlWQ1L</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/861112789053706240">2017年5月7日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script><S-Del>


:参加者: @tk0miya(会長), @shimizukawa(会計), @pashango2, retsuyam

前回 :doc:`../sphinxjp-hack-a-thon-20170423/index` より、人数へったなー、と思ったけど、前回開催がGWの前週で、今日はGW最終日。そりゃ人も減るか。


みんながやったこと
=====================

.. figure:: todo.*
   :width: 500

* @tk0miya: Sphinx-1.6b3 リリースに向けて作業します -> 1.6b3リリースしました。来週末くらいには、1.6最終版がリリースできそうな感じになってきました
* @pashango2: SphinxのGUIツール開発と、ShinxのGFMソース読み込みを拡張 -> Sphinxのプロジェクト作成時にrecommonmarkなども含めようとするとけっこう手間がかかっていたのが、2クリックで生成出来るようになりました。epubボタンをおすとepubでビルドもできるようになりました。縦書きのepubを生成したら、カギ括弧がおかしいです（フォントが縦書きフォントじゃないからですね・・・Sphinx的にどう解決したらいいんだろう）
* @shimizukawa: sphinx.testing モジュールの実装と、sphinx PRレビュー -> だいたい動くようになってきました
* @retsuyam: bitbucket/github + sphinx + readthedocs で共同編集したドキュメントをビルドしてホスティングできるようにしてみます -> bitbucketにpushしたところまでできたので、あとはreadthedocsと繋いでビルドするところです


自分がやったこと
==================

* `Sphinxのテストユーティリティをsphinx.testingとして提供しよう`_ と実装してました。

  * Sphinx拡張のテストに利用できる `sphinx-testing`_ パッケージというのがります。これは `Sphinxの/testsディレクトリ`_ に置いてあった ``util.py``, ``path.py`` を第三者が利用できるようにパッケージ化したものです。

  * Sphinxのテストをpytestに切り替えたあとも、sphinx-testingは以前のnose実装のままでした

  * Sphinx-1.6(b2)ではsphinx-testingがうまく動かなくなってしまったみたい(`sphinx-dev › Fate of sphinx-testing?`_)

  * そもそもsphinx本体にtestingを（再利用可能な形式で）含めていなかったのはGeorgの意向だった

  * もう、含めて良いよね...? （イマココ）

  * ということで、実装中です - `PR#3718`_

* あと、いくつかのPRをレビューしました。


.. _Sphinx+翻訳 hack-a-thon 2017.04: https://sphinxjp.connpass.com/event/56547/

.. _Sphinxのテストユーティリティをsphinx.testingとして提供しよう: https://github.com/sphinx-doc/sphinx/issues/3458

.. _sphinx-testing: https://pypi.python.org/pypi/sphinx-testing

.. _Sphinxの/testsディレクトリ: https://github.com/sphinx-doc/sphinx/tree/4fc77026a/tests

.. _sphinx-dev › Fate of sphinx-testing?: https://groups.google.com/d/msg/sphinx-dev/8iiwt4Yr28E/yEJt01lmBAAJ

.. _PR#3718: https://github.com/sphinx-doc/sphinx/pull/3718

:date: 2017-04-23 19:00
:categories: ['Sphinx']
:body type: text/x-rst

=====================================================
2017/04/23 Sphinx+翻訳 hack-a-thon 2017.04 #sphinxjp
=====================================================

*Category: 'Sphinx'*

`Sphinx+翻訳 hack-a-thon 2017.04`_ に参加しました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash">#sphinxjp</a> hack-day! 黙々ワイワイやってます (@ タイムインターメディア in 新宿区, 東京都) <a href="https://t.co/eNGak6OQV5">https://t.co/eNGak6OQV5</a> <a href="https://t.co/xHKF5S21WS">pic.twitter.com/xHKF5S21WS</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/856047505116725248">2017年4月23日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


:参加者: @tk0miya(会長), @usaturn, @shimizukawa(会計), @pashango2, @TudaRom, @yosuken900(副会長), nskgch

参加者が7人。前回 :doc:`../sphinxjp-hack-a-thon-20170318` より1人減だけどまだまだ賑やかな人数です。

みんながやったこと
=====================

.. figure:: todo.*
   :width: 500

* @tk0miya: Sphinx-1.6b1 リリース準備. 今日のhack-a-thon開始時に16個あったIssue/PRが6本まで減ったので、今日もうちょっとがんばってリリースしたいなと思ってます。
* @pashango2: 前回に引き続き、SphinxのGUIツールをQtで作ってます。venvとanacondaをサポートしようとしてます。。Sphinxがconf.pyのテンプレートをべた書きで持っていて、外部ツールが再利用するのはつらい。プロジェクトのソースディレクトリもconf.pyになくてMakefileにしかないのでつらい。
* @nskgch: ひたすらSphinx-1.6向け翻訳とチェックを進めた。全体のなかの1,2%は進んだかなと思います
* @shimizukawa: Sphinx-1.6b1 リリース準備
* @usaturn: `World Plone Day`_ のプレゼン資料作成がんばりました。資料作成のための情報収集をしてた感じです。
* @yousken900: 静的HPをデプロイするHerokuの登録と"Hello World"の表示 -> Herokuをちょっとあきらめて、Read The Docsにデプロイするのを目指そうと思います。
* @TudaRom: Sphinx入門をやってましたが、SphinxというよりもreST記法を覚えるのをやってました。

.. _World Plone Day: https://plonejp.connpass.com/event/51340/


自分がやったこと
==================

* 4つか5つのPRをレビューしました。

  * `#3649 <https://github.com/sphinx-doc/sphinx/pull/3649>`__ pkg_resourcesの ``sphinx_themes`` entry point 名を ``sphinx.html_themes`` に変更
  * `#3653 <https://github.com/sphinx-doc/sphinx/pull/3653>`__ 画像フォーマットを変換する ``sphinx.ext.imgconverter`` 拡張の追加
  * `#3654 <https://github.com/sphinx-doc/sphinx/pull/3654>`__ sphinx.websupport を別パッケージに分離
  * `#3655 <https://github.com/sphinx-doc/sphinx/pull/3655>`__ CIテストで、LaTeXのビルドをpy36環境でのみ行うことで高速化
  * `#3656 <https://github.com/sphinx-doc/sphinx/pull/3656>`__ SphinxComponentRegistryクラスの実装
  * `#3658 <https://github.com/sphinx-doc/sphinx/pull/3658>`__ ``get_full_qualified_names()`` を追加して、domain毎に対象のフルネームを取得する
  * `#3659 <https://github.com/sphinx-doc/sphinx/pull/3659>`__ Sphinxのテーマ拡張のコード生成コマンドの実装


レビューがんばりました。


.. _Sphinx+翻訳 hack-a-thon 2017.04: https://sphinxjp.connpass.com/event/53950/


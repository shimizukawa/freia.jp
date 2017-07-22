:date: 2017-07-15 20:00
:tags: Python, Sphinx, Heroku, Hosting
:body type: text/x-rst

======================================================================
2017/07/15 SphinxドキュメントをHerokuに数クリックでホスティングしたい
======================================================================

:doc:`../pyhack-20170714/index` に参加しています。


先日、 :doc:`../sphinx-private-hosting-on-heroku/index` というBlogを書きました。今日は、これをもうちょっと楽に使えるようにカスタマイズしました。

動作するけど、まだ実用にはならない感じです。

先日作成した版
===============

:doc:`先日のBlog <../sphinx-private-hosting-on-heroku/index>` に書いた方法だと、いくつか面倒な部分がありました。

短所

* GitLab（またはHerokuのgitリポジトリ）を使う必要がある
* ドキュメントのリポジトリ内にHerokuのための設定ファイルを置く必要がある
* Herokuのインスタンス起動時にbuildする場合、大きいドキュメントだと120秒の時間制限で終わらない
* 環境変数設定など、手順が多い


手間が多くて大変なのと、制約が多いので、もっと楽にできるようにしてみました。

今日作成した版
==============

Herokuのテンプレートを使って、数クリックでHerokuアプリを立てて使えるようにしてみました。

作ったヤツはこちら: https://github.com/shimizukawa/heroku-sphinxbuild-template

長所

* ドキュメントのリポジトリに手を加える必要がない
* Herokuの設定が楽。アカウントがあれば、2クリックとパラメータ入力のみ。
* ドキュメントのビルドは起動時にやらないので起動が速い
* （今回も）アプリはBASIC認証を提供する（設定次第）
* （今回も）Herokuの無料枠時間内（ `全アプリで1,000時間`__ ）なら無料

.. __: https://github.com/shimizukawa/heroku-sphinxbuild-template

短所

* まだ色々。ドキュメントの再ビルドが出来ないのがクリティカル。詳しくはこちら -> https://github.com/shimizukawa/heroku-sphinxbuild-template#limitations


使い方

1. ボタンをクリックする

   https://github.com/shimizukawa/heroku-sphinxbuild-template

2. Herokuの起動画面にアプリ名や、Githubのリポジトリ等の必要情報を入力する
3. Herokuにアプリが作られる
4. アプリが起動してビルドされたSphinxドキュメントが見れる


.. figure:: heroku-button.*
   :target: https://github.com/shimizukawa/heroku-sphinxbuild-template#limitations


.. figure:: sphinx-heroku-deploy.*


今後実装したいこと
===================

とりあえず、夢だけ書いときます。

基本機能

* リポジトリからのpush通知て、ドキュメントを再ビルドする
* OAuthログイン認証を提供する（最初の設定次第、要DB）

追加機能

* ドキュメントへのコメント機能（レビューに使いたい）
* 飜訳機能（ビルドされたHTMLの画面で飜訳したい）

Sphinxドキュメントにテンプレ注入

* 文字数情報の表示（ある）
* 書籍で何ページに相当するか情報（コードブロック等の面積を考慮したい）
* 飜訳率の表示（日本語・英語比率でいいかなあ）
* 文面からgithubの当該行へのリンク


技術メモ
=========

ここから調べたときの技術メモです。

---------------------

Herokuのアプリテンプレート

* https://devcenter.heroku.com/articles/heroku-button
* https://github.com/rauchg/slackin/blob/master/app.json
* https://devcenter.heroku.com/articles/app-json-schema


GithubのToken / Deploy key

* https://developer.github.com/v3/guides/managing-deploy-keys/

  * OAuth Tokenは人単位。作るのが一手間要りそう？使うのは楽かも
  * SSH Deploy Keyはリポジトリ単位。SSH鍵の生成が必要（Heroku初回起動時に自動化しないと面倒）

HerokuでSphinxドキュメントビルドするときの課題

* Heroku起動時にSphinxドキュメントをビルドする方法だと、Dynoが起動するときにドキュメントビルドして時間がかかる（120秒でkillされる）
* Procfileにworkerを追加しても、Dyno単位でストレージが独立なので、workerプロセスでビルドしたドキュメントをwebプロセスで参照できない
* Herokuのbuildpackを使うと、イメージ(slug)のビルドステージにカスタムの手順を追加できる。今はそこでドキュメントビルドしてる. buildpacks.

  * https://devcenter.heroku.com/articles/buildpacks 実はrequirements.txtでのパッケージインストールもheroku公式のbiuldpack
  * https://devcenter.heroku.com/articles/buildpack-api buildpackの作り方. githubに3つのファイルを置く
  * https://github.com/heroku/heroku-buildpack-python/blob/master/bin/compile heroku/python (公式)のbuildpack
  * http://blog.flect.co.jp/labo/2013/06/herokubuildpack-c488.html buildpackを作る参考になりそうなblog
  * https://github.com/shimizukawa/heroku-buildpack-sphinxbuild 作ったbuildpack


Herokuの再buildをやる方法

* イメージ(slug)のリビルドをする良い方法がない
* https://devcenter.heroku.com/articles/build-and-release-using-the-api
* これをHeroku内からキックする手軽な方法がない（Herokuのトークンどうする？）


別の方法を考える

* ビルドした静的ファイルを全てredisかrdbに格納する
* うーん、他にあるかなあ


.. note:: 【急募】 良い解決方法


:date: 2010-12-21 20:00:00
:categories: ['Event', 'python', 'study', 'gae']
:body type: text/x-rst

===========================================================
2010/12/21 BPStudy#40 に参加しました Google Appengine 1.4.0
===========================================================

`BPStudy#40`_ に参加してきました。
いつも通り走り書きメモです。

.. _`BPStudy#40`: http://atnd.org/events/10717

今回のネタは"Google Appengine 1.4.0"。

第一部「Google App Engine1.4.0概説」
-------------------------------------------------------------

* 発表: Ian M Lewis (BeProud): `@IanMLewis`_

* 資料: http://www.slideshare.net/IanMLewis/bpstudy-40-google-appengine-140

.. _`@IanMLewis`: http://twitter.com/IanMLewis


発表からひろったポイント & 清水川メモ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 今回の1.4.0はけっこう大きなリリース。
    * channel API
    * ライブラリ構成が変わって古いのはdeprecated扱い
    * Cronとタスクキュー時間制限が30秒から10分へ
    * タスクキューのデータがQuotaに含まれる

* ChannelAPI
    * サーバーからクライアントへデータをpushする
    * データが大容量だときついかも知れない
    * 使うための3つのステップ
        1. サーバーで ``Channel ID`` を生成してクライアントに渡す
        2. クライアントでそのIDを使って ``socket`` に接続する
        3. サーバーからchannelにメッセージを送信。クライアントで受け取る
    * 繋ぐためのサンプルコード
        * 資料のp14- http://www.slideshare.net/IanMLewis/bpstudy-40-google-appengine-140
    * データpushはJSONがお勧め（楽なので）
    * デモ:
        * http://s.beproud.jp/bpstudy40demo (検索)
        * http://s.beproud.jp/channel-api-demo (検索のソース)
        * http://s.beproud.jp/bpstudy40map (地図)
    * 質疑
        * channelは何個まで開けるのか？
            * 何個でも大丈夫なはず
            * channelはブラウザ毎でも全部で1つでもよい
            * ユーザー毎に別の作業をするページならユーザー毎に開く
            * 1つのページで共同作業する場合は全体で1つ開く
        * channelのタイムアウトは？
            * 2時間くらい
            * ブラウザ側で切れてたらつなぎ直す（自動？要実装）

* Taskキュー
    * 質疑
        * 課金は1.4から？
        * DataStoreのquotaに含むので普通のデータと合計でquota扱い
        * DataStoreが一杯で課金設定してなければTaskキューも積めない
        * Taskキューの処理は即時処理サーバーと遅いサーバーとで処理される
            * 長いTaskは遅いサーバーで。
            * どのあたりが境界線？
                * 「そうなんですよねー。よく分からないんです」@IanMLewis


第二部「Google App Engine1.4.0 ソースコードリーディング（python編）」
-----------------------------------------------------------------------

* 発表: `@tagomoris`_

.. _`@tagomoris`: http://twitter.com/tagomoris

発表からひろったポイント & 清水川メモ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* キャメルケース
* 同じ名前のメソッドがあちこちのモジュールにある
* SDKのインデントが2
* Google Python Style Guide は1度読むと良いと思いますよ
    * 本家: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
    * 日本語訳: http://works.surgo.jp/translation/pyguide.html
    * インデントは4を推奨
    * from xxx.xxx import * はNG
* SDKには不自然な空行がときどきある
    * リリース時に削除されているんじゃないかと思うが中の人じゃないと分からないだろう

以降、コードリーティング。


.. :extend type: text/x-rst
.. :extend:

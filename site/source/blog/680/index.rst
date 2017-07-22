:date: 2009-10-25 04:47:47
:tags: python, pyspa

=================================================
2009/10/25 Expert Python Programming の目次の和訳
=================================================

Tarek Ziadé 著の Expert Python Programming の目次を和訳しました。Pythonの初心者向けではなく、何かの言語(Python, Ruby, Perl, ...)を理解している人がPythonを取り巻く開発環境、作法などを理解するのにとても良い本だと思います。

本は以下から購入できます。PACKTのサイトからは `10章: プロジェクトの文書化`_ が丸々1章分DL出来ます。

* `PACKT <http://www.packtpub.com/expert-python-programming/book>`_
* `Amazon(米) <http://www.amazon.com/dp/184719494X/freiaweb-22/>`_
* `Amazon(日本) <http://www.amazon.co.jp/dp/184719494X/freiaweb-22/>`_

自分はPACKTで購入して、紙の本とPDFとセット購入で45$でした。PDFには注文者の住所と名前が全ページに印字されます。紙の本はシンガポールでオンデマンド印刷されて1ヶ月くらいで手元に届きました。


Tarek自身による紹介文

* `Expert Python Programming book, more details + sample chapter <http://tarekziade.wordpress.com/2008/09/24/expert-python-programming-book-more-details-sample-chapter/>`_

`目次(英語) <http://www.packtpub.com/view_popup/page/expert-python-programming-table-of-contents>`_ の内容を和訳しました。1時間ちょっとで訳したので間違い等あると思います。指摘歓迎。


エキスパートPythonプログラミング
=================================

目次
-----

* `序文`_
* `1章: 始めよう`_
* `2章: 構文ベストプラクティス - クラスの世界`_
* `3章: 構文ベストプラクティス - クラスを超えて`_
* `4章: 良い名前の選択`_
* `5章: パッケージを作る`_
* `6章: アプリケーションを作る`_
* `7章: zc.buildoutを使う`_
* `8章: コードの管理`_
* `9章: ライフサイクルの管理`_
* `10章: プロジェクトの文書化`_
* `11章: テスト駆動開発`_
* `12章: 最適化: 一般原則とプロファイリングテクニック`_
* `13章: 最適化: 解法`_
* `14章: 有用なデザインパターン`_
* `索引`_

序文
-----

1章: 始めよう
--------------

* Pythonのインストール
      * Pythonの実装系
            * Jython
            * IronPython
            * PyPy
            * その他の実装
      * Linux へのインストール
            * パッケージインストール
            * ソースコンパイル
      * Windows へのインストール
            * Python のインストール
            * MinGW のインストール
            * MSYS のインストール
      * Mac OS X へのインストール
            * パッケージインストール
            * ソースコンパイル
* Python プロンプト
      * インタラクティブプロンプトのカスタマイズ
            * iPython: より良いプロンプト
* setuptools のインストール
      * 動作原理を理解する
      * EasyInstallを使ったsetuptoolsのインストール
      * distutilsにMinGWのフックを入れる
* 作業環境
      * エディターと補助ツールを使う
            * コードエディター
            * Vimのインストールと設定
            * その他のエディタを使う
            * その他のバイナリ
      * 統合開発環境を使う
            * PyDev と Eclipse を使う
* 要約


2章: 構文ベストプラクティス - クラスの世界
-------------------------------------------
* リスト内包表記
* イテレータとジェネレータ
      * ジェネレータ
      * コルーチン
      * ジェネレータ表現
      * itertools モジュール
            * islice: The Window Iterator
            * tee: The Back and Forth Iterator
            * groupby: The uniq Iterator
            * その他の関数
* デコレータ
      * デコレータの書き方
      * 引数チェック
      * キャッシュ
      * プロキシ
      * コンテキストプロバイダ
* with と contextlib
      * contextlib モジュール
      * Context Example
* 要約


3章: 構文ベストプラクティス - クラスを超えて
---------------------------------------------
* 組み込み型のサブクラス化
* super クラスを使ってメソッドにアクセスする
      * Pythonのメソッド解決順序(MRO)を理解する
      * super の落とし穴
            * super と従来型の呼び出しを混在させる
            * 親クラスと異なる引数定義の混在
* ベストプラクティス
* Descriptors と Properties
      * Descriptors
            * イントロスペクション Descriptor
            * メタ descriptor
      * Properties
* スロット
* メタプログラミング
      * __new__ メソッド
      * __metaclass__ メソッド
* 要約


4章: 良い名前の選択
--------------------
* PEP 8 と名前付けのベストプラクティス
* 名前付けのスタイル
      * 変数
            * 定数
            * パブリックとプライベートの変数
      * 関数とメソッド
            * プライベートの論争
            * 特殊メソッド
            * 引数
      * プロパティー
      * クラス
      * モジュールとパッケージ
* 名前付けガイド
      * "has" か "is" を二値型に前置する
      * シーケンス型は複数形にする
      * 辞書に明示的な名前を付ける
      * 一般的な名前を避ける
      * 既存の名前を避ける
* 引数のベストプラクティス
      * イテレーティブなデザインのための引数構築
      * 引数とテストを信じる
      * `*args` 引数と `**kw` 引数は気をつけて使おう
* クラスの名前
* モジュールとパッケージの名前
* Working on APIs
      * Tracking Verbosity
      * 名前空間木の構築
      * コードの分割
      * Eggを使う
      * Deprecation 手順を使う
* 役に立つツール
      * Pylint
      * CloneDigger
* 要約


5章: パッケージを作る
------------------------
* 全てのパッケージで共通のパターン
      * setup.py: 全てをコントロールするスクリプト
            * sdist
            * build と bdist
            * bdist_egg
            * install
            * パッケージのアンインストール
            * develop
            * test
            * register と upload
            * 新しいコマンドを作る
            * setup.py の役に立つ要約
            * その他の重要なメタデータ
* テンプレートベースのアプローチ
      * Python Paste
      * テンプレートを作る
* パッケージのテンプレートを作る
* 開発サイクル
* 要約


6章: アプリケーションを作る
----------------------------
* Atomisator: 導入
* 全体像
* 開発環境
      * テストランナーを追加する
      * パッケージ構造を追加する
* パッケージを書く
      * atomisator.parser
            * 最初のパッケージを作る
            * 最初のdoctestを作る
            * テスト環境を構築する
            * コードを書く
      * atomisator.db
            * SQLAlchemy
            * APIを提供する
      * atomisator.feed
      * atomisator.main
* Atomisator を配布する
* パッケージの依存関係
* 要約


7章: zc.buildoutを使う
-----------------------
* zc.buildout の哲学
      * ファイル構造を調整する
            * 最小の設定ファイル
            * [buildout] セクションのオプション
      * buildout コマンド
      * レシピ
            * 重要なレシピ
            * レシピを作る
      * Atomisator buildout 環境
            * buildout フォルダ構造
      * さらに先へ
* リリースとと配布
      * パッケージをリリースする
      * リリース設定ファイルを追加する
      * アプリケーションのビルドとリリース
* 要約


8章: コードの管理
------------------
* バージョン管理システム
      * 中央集中型システム
      * 分散システム
            * 分散の戦略
      * 中央集中か、分散か?
      * Mercurial
      * Mercurial でプロジェクトを管理する
            * 専用フォルダのセットアップ
            * hgwebdir の設定
            * Apache の設定
            * 認証の設定
            * クライアントの設定
* 常時結合
      * Buildbot
            * Buildbotのインストール
            * Buildbot と Mercurial のフック
            * Apache と Buildbot のフック
* 要約


9章: ライフサイクルの管理
--------------------------
* 異なるアプローチ
      * ウォーターフォール開発モデル
      * スパイラル開発モデル
      * 漸進型開発モデル
* ライフサイクルの定義
      * プランニング
      * 開発
      * 総合デバッグ
      * リリース
* トラッキングシステム設定
      * Trac
            * インストール
            * Apache 設定
            * アクセス許可設定
      * Trac でのプロジェクトライフサイクル
            * プランニング
            * 開発
            * クリーニング
            * リリース
* 要約


10章: プロジェクトの文書化
---------------------------
* テクニカルライティングの7つのルール
      * 2ステップで書く
      * Target the Readership
      * シンプルなスタイルを使う
      * 情報の範囲を制限する
      * 現実的なコード例を使う
      * 必要十分なアプローチを使う
      * テンプレートを使う
* reStructuredText 入門
      * セクション構造
      * リスト
      * インラインマークアップ
      * リテラルブロック
      * リンク
* ドキュメントをビルドする
      * 書類をビルドする
            * デザイン
            * 使い方
            * 手順
* 書類を作成する
      * Building the Landscape
            * プロデューサーのレイアウト
            * カスタマーのレイアウト
* 要約


11章: テスト駆動開発
---------------------
* テストをしていない人へ
      * テスト駆動開発の原則
            * ソフトウェアの退行を防ぐ
            * コードの品質を上げる
            * 最良の開発者ドキュメントを提供する
            * 強健なコードを素早く生産する
      * どんなテストがありますか?
            * 受け入れテスト
            * ユニットテスト
            * Python の標準テストツール
* テストをしている人へ
      * ユニットテストの落とし穴
      * ユニットテストの置き換え
            * nose
            * py.test
      * フェイクとモック
            * フェイクを構築する
            * モックを使う
      * ドキュメント駆動開発
            * ストーリーを書く
* 要約


12章: 最適化: 一般原則とプロファイリングテクニック
---------------------------------------------------
* 最適化の3つのルール
      * まず動くように作る
      * ユーザー視点で動くようにする
      * コードの可読性(とメンテナンス性)を維持する
* 最適化戦略
      * 他の原因を見つける
      * ハードウェアをスケールする
      * 速度テストを書く
* ボトルネックを見つける
      * CPU使用率のプロファイルを取る
            * Macro-Profiling
            * Micro-Profiling
            * Pystoneで計測する
      * メモリ使用率のプロファイルを取る
            * Pythonがメモリをどのように使うか
            * メモリのプロファイルを取る
      * ネットワーク使用率のプロファイルを取る
* 要約


13章: 最適化: 解法
-------------------
* 複雑さを縮小する
      * Measuring Cyclomatic Complexity
      * Big-O 表記を計測する
      * シンプルにする
            * リストの探索
            * Listの代わりにSetを使う
            * 外部呼び出しをやめ、仕事量を減らす
            * コレクション型を使う
* マルチスレッドを使う
      * マルチスレッディングとは?
      * Pythonはスレッドをどのように使うか
      * スレッドをいつ使うべきか?
            * Building Responsive Interfaces
            * Delegating Work
            * マルチユーザーアプリケーション
            * シンプルな例
* マルチプロセスを使う
      * Pyprocessing
* キャッシュを使う
      * Deterministic Caching
      * Non-Deterministic Caching
      * Pro-Active Caching
      * Memcached
* 要約


14章: 有用なデザインパターン
-----------------------------
* 生成パターン
      * Singleton
* 構造パターン
      * Adapter
            * Interfaces
      * Proxy
      * Facade
* 振る舞いパターン
      * Observer
      * Visitor
      * Template
* 要約


索引
-----


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2009-10-26.2634175742
.. :title: Re:Expert Python Programming の目次の和訳
.. :author: methane
.. :date: 2009-10-26 21:14:30
.. :email: 
.. :url: 
.. :body:
.. 「テストする、テストしない」は、「テストをしていない人へ、テストをしている人へ」が良いかなーと思いました。
.. 
.. :comments:
.. :comment id: 2009-10-27.4387341573
.. :title: Re:Expert Python Programming の目次の和訳
.. :author: t2y
.. :date: 2009-10-27 01:44:05
.. :email: 
.. :url: http://d.hatena.ne.jp/t2y-1979/
.. :body:
.. Tarek さんに和訳したいと交渉していたのですが、出版社の編集者さんの同意が得られずに断念しました。残念です。
.. 
.. :comments:
.. :comment id: 2009-10-27.0969909552
.. :title: Re:Expert Python Programming の目次の和訳
.. :author: しみずかわ
.. :date: 2009-10-27 10:14:59
.. :email: 
.. :url: 
.. :body:
.. > methane
.. 
.. ありがとうございます。修正しました。他にもいくつか和訳化しました(3章とか)。
.. 
.. > t2y
.. 
.. な、なんだってー！
.. 
.. 
.. :comments:
.. :comment id: 2009-11-05.7267967702
.. :title: Re:Expert Python Programming の目次の和訳
.. :author: しみずかわ
.. :date: 2009-11-05 12:45:34
.. :email: 
.. :url: 
.. :body:
.. >> Tarek さんに和訳したいと交渉していたのですが、出版社の編集者さんの同意が得られずに断念しました。
.. >な、なんだってー！
.. 
.. 上記の続報。
.. ・t2yに聞いたところ、同意が得られないというか、返事がなかったそうです。
.. ・別口で、日本の某編集者さんがPACKTの編集者さんと話をしていて、微妙に前進中。
.. 
.. 
.. :comments:
.. :comment id: 2010-01-23.2593967830
.. :title: 現在翻訳中！
.. :author: しみずかわ
.. :date: 2010-01-23 11:37:39
.. :email: 
.. :url: 
.. :body:
.. 現在、「エキスパートPythonプログラミン（仮）」として出版に向けて数名で翻訳中です！
.. 
.. :comments:
.. :comment id: 2010-05-22.0013879531
.. :title: 2010/5/31発売！
.. :author: しみずかわ
.. :date: 2010-05-22 13:20:01
.. :email: 
.. :url: 
.. :body:
.. 「エキスパートPythonプログラミング」2010/5/31発売です！ http://www.freia.jp/taka/blog/717
.. 

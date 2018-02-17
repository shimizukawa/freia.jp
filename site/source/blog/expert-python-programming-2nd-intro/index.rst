:date: 2018-02-17 17:00:00
:tags: python, expertpython

==================================================
『エキスパートPythonプログラミング 改訂2版』の紹介
==================================================

清水川が翻訳に参加した `エキスパートPythonプログラミング 改訂2版`_ (原題 `Expert Python Programming - Second Edition`_) が2018/2/26にアスキードワンゴさんより発売されます！

.. figure:: expert-python-programming-2nd-ja-cover.*

   エキスパートPythonプログラミング 改訂2版 カバー

:タイトル: `エキスパートPythonプログラミング 改訂2版`_
:原題: `Expert Python Programming - Second Edition`_
:著者: Michał Jaworski, Tarek Ziadé
:翻訳: 稲田直哉、芝田将、渋川よしき、清水川貴之、森本哲也
:出版社: KADOKAWA（アスキードワンゴ）
:Price: 3,600円+税
:ISBN-13: 978-404-8930611
:購入: Amazon_, `カドカワストア`_

.. _`エキスパートPythonプログラミング 改訂2版`: https://www.kadokawa.co.jp/product/301801000262/
.. _`Expert Python Programming - Second Edition`: https://www.packtpub.com/application-development/expert-python-programming-second-edition
.. _`Amazon`: http://amzn.to/2o5JRvZ
.. _カドカワストア: https://store.kadokawa.co.jp/shop/g/g301801000262/


どんな本?
==========

.. figure:: expert-python-ja-1-and-2.jpg

   (左)エキスパートPythonプログラミング 改訂2版、(右)同 1版

   見本誌が届いたので1版と並べて比較してみました

1版は、「Pythonを知っている」状態から「Pythonをマスターしている」状態に成長するための本であり、また、他の言語をある程度マスターしている人がPythonの世界でどのように活動していけばいいのかを知るのに最も適した本でした（1版について詳しくは :doc:`../717/index` を参照）。

1版と改訂2版で、特に変わった箇所は以下:

- Pythonのバージョンは2.7->3.6に更新（原著は2.5->3.5)
- 章削除: buildoutの章
- 章追加: 6章: コードをデプロイする: Twelve-Factor、Fabric、デプロイ、モニタリング
- 章追加: 7章: 別言語で作るPython拡張: C拡張、Cython、ctypes
- 章追加: 13章: 並列実行: マルチスレッド、マルチプロセス、非同期プログラミング
- 8章: Mercurial -> Git、 buildbot -> JenkinsやCIサービス

全体的にはこんな感じ:

- めっちゃ読み応えのある実践的なネタ満載
- ドキュメントに書いてある話や、初級中級レベルの紹介はなくなった
- 高度な話題や、Pythonの場合にどうするかという話題が増加
- ページ数は100ページ増量、さらに情報の密度はアップ
- 2017年末の情報に追従（原著は2015年末）
- お値段は1版から据え置き！


目次
=====

改訂2版の目次です。

1版からの変更がある部分に **(更新)** 等のマークを入れてありますが、変更無しの箇所についても、1版で誤訳していた部分や、読みづらかった部分など、翻訳自体の見直しは行っています。


  * 序文

    * はじめに **(新規)**
    * 日本語翻訳出版によせて（初版）
    * 日本語翻訳出版によせて（改訂2版） **(新規)**
    * 日本語版まえがき **(新規)**

  * 1章 現在のPythonのステータス **(新規)**

    * われわれは今どこにいて、どこに行こうとしているのか？ **(新規)**
    * Pythonはなぜ/どのように変化するのか？ **(新規)**
    * PEP文書から最新の変更情報を得る **(新規)**
    * 本書執筆時点でのPython 3の浸透度合い **(新規)**
    * Python 3とPython 2の主な違い **(新規)**

      * なぜそれを気にする必要があるのか？ **(新規)**
      * 主な構文上の違いと、よくある落とし穴 **(新規)**
      * バージョン間の互換性を保つ時によく利用されるツールやテクニック **(新規)**

    * CPython以外の世界

      * なぜCPython以外も考慮すべきなのか **(新規)**
      * Stackless Python **(更新)**
      * Jython **(更新)**
      * IronPython **(更新)**
      * PyPy **(更新)**

    * 現代的なPython開発の手法 **(新規)**

    * アプリケーションレベルでのPython環境の分離 **(新規)**

      * なぜ分離が必要なのか？ **(新規)**
      * 人気のあるソリューション **(新規)**
      * どのツールを選択すべきか？ **(新規)**

    * システムレベルでの環境の分離 **(新規)**

      * Vagrantを使った仮想的な開発環境 **(新規)**
      * コンテナ化 VS 仮想化 **(新規)**

    * 人気のある生産性向上ツール

      * 拡張インタラクティブセッション - IPython, bpython, ptpythonなど **(更新)**
      * インタラクティブ・デバッガー **(新規)**

    * 役に立つリソース **(更新)**
    * まとめ

  * 2章 構文ベストプラクティス -- クラス以外

    * Pythonの組み込み型 **(更新)**

      * 文字列とバイト列 **(更新)**
      * コレクション **(更新)**

    * 高度な文法 **(更新)**

      * イテレータ **(更新)**
      * "yield"文（ジェネレータ） **(更新)**
      * デコレータ **(一部更新)**
      * コンテキストマネージャ - "with"構文 **(一部更新)**

    * 知っておくべきその他の文法 **(更新)**

      * "for … else"節 **(更新)**
      * 関数アノテーション **(更新)**

    * まとめ **(更新)**

  * 3章 構文ベストプラクティス: クラスの世界

    * 組み込みクラスのサブクラス化
    * スーパークラスからメソッドへのアクセス **(更新)**

      * 旧スタイルクラスとPython 2の "super" **(更新)**
      * Pythonのメソッド解決順序（MRO）を理解する **(一部更新)**
      * "super" の落とし穴 **(一部更新)**
      * ベストプラクティス **(一部更新)**

    * 高度な属性アクセスのパターン **(更新)**

      * ディスクリプタ **(内容は削減、かなり分かりやすくなった)**
      * プロパティ **(一部更新)**
      * スロット **(一部更新)**

    * メタプログラミング **(更新)**

      * デコレータ - メタプログラミングの方法 **(更新)**
      * クラスデコレータ **(更新)**
      * "__new__()" メソッドによるインスタンス作成プロセスのオーバーライド **(一部更新)**
      * メタクラス **(更新)**
      * コード生成のTips **(更新)**

    * まとめ **(更新)**

  * 4章 良い名前を選ぶ

    * PEP 8と命名規則のベストプラクティス

      * どうして、いつPEP 8に従うのか
      * PEP 8 のその先へ - チーム固有のスタイルガイドライン

    * 命名規則のスタイル

      * 変数

    * 名前付けガイド

      * ブール値の名前の前にhasかisをつける
      * コレクションの変数名は複数形にする
      * 辞書型に明示的な名前をつける
      * 汎用性の高い名前を避ける
      * 既存の名前を避ける

    * 引数のベストプラクティス

      * 反復型設計を行いながら引数を作成する
      * 引数とテストを信頼する
      * 魔法の引数である \*args と \*\*kwargs は注意して使用する

    * クラス名
    * モジュール名とパッケージ名
    * 役に立つツール

      * Pylint
      * pycodestyleとflake8 **(更新)**

    * まとめ **(更新)**

  * 5章 パッケージを作る

    * パッケージ作成 **(更新)**

      * 混乱するPythonパッケージングツールの状態 **(更新)**
      * プロジェクトの設定
      * カスタムセットアップコマンド **(更新)**
      * 開発時にパッケージを利用する **(更新)**

    * 名前空間パッケージ **(更新)**

      * なぜこれが便利なのか？ **(更新)**
      * PEP 420 -  暗黙の名前空間パッケージ **(更新)**
      * 以前のバージョンのPythonにおける名前空間パッケージ **(更新)**

    * パッケージのアップロード **(更新)**

      * PyPI – Python Package Index **(更新)**
      * ソースパッケージとビルド済みパッケージ **(更新)**

    * スタンドアローン実行形式 **(新規)**

      * スタンドアローンの実行形式が便利な場面 **(新規)**
      * 人気のあるツール **(新規)**
      * 実行可能形式のパッケージにおけるPythonコードの難読化 **(新規)**

    * まとめ **(更新)**

  * 6章 コードをデプロイする **(新規)**

    * The Twelve-Factor App **(新規)**
    * Fabricを用いたデプロイの自動化 **(新規)**

    * 専用のパッケージインデックスやミラーを用意する **(新規)**

      * PyPIをミラーリングする **(新規)**
      * パッケージを使ったデプロイ **(新規)**

    * 一般的な慣習と実践 **(新規)**

      * ファイルシステムの階層 **(新規)**
      * 環境の分離 **(新規)**
      * プロセス監視ツールを使う **(新規)**
      * アプリケーションコードはユーザー空間で実行しよう **(新規)**
      * リバースHTTPプロキシを使う **(新規)**
      * プロセスのgracefulリロード **(新規)**

    * 動作の追跡とモニタリング **(新規)**

      * エラーログ収集 - sentry/raven **(新規)**
      * モニタリングシステムとアプリケーションメトリクス **(新規)**
      * アプリケーションログの処理 **(新規)**
      * ログを処理するツール **(新規)**

    * まとめ **(新規)**

  * 7章 他言語によるPythonの拡張 **(新規)**

    * 他言語 = C/C++ **(新規)**

      * C/C++ による拡張 **(新規)**

    * 拡張を使う理由 **(新規)**

      * コードのクリティカルな部分の性能を向上する **(新規)**
      * 別の言語で書かれたコードを利用する **(新規)**
      * サードパーティー製の動的ライブラリを利用する **(新規)**
      * カスタムのデータ構造を作る **(新規)**

    * 拡張を書く **(新規)**

      * ピュアC拡張 **(新規)**
      * Cython **(新規)**

    * 拡張のデメリット **(新規)**

      * 増加する複雑さ **(新規)**
      * デバッグ **(新規)**

    * 拡張を使わずに動的ライブラリを利用する **(新規)**

      * ctypes **(新規)**
      * CFFI **(新規)**

    * まとめ **(新規)**

  * 8章 コードの管理

    * バージョン管理システム

      * 中央集中型システム
      * 分散型システム
      * 中央集中か、分散か？
      * できればGitを使う **(新規)**
      * Git flow と GitHub flow **(新規)**

    * 継続的開発プロセス **(新規)**

      * 継続的インテグレーション **(新規)**
      * 継続的デリバリー **(新規)**
      * 継続的デプロイメント **(新規)**
      * 継続的インテグレーションを行うのに人気のあるツール **(新規)**
      * 適切なツール選択とよくある落とし穴 **(新規)**

    * まとめ **(更新)**

  * 9章 プロジェクトのドキュメント作成

    * 技術文書を書くための7つのルール

      * 2つのステップで書く
      * 読者のターゲットを明確にする
      * シンプルなスタイルを使用する
      * 情報のスコープを絞る
      * 実在するようなコードのサンプルを使用する
      * なるべく少なく、かつ十分なドキュメント
      * テンプレートの使用

    * reStructuredText入門

      * セクション構造
      * Lists
      * インラインマークアップ
      * リテラルブロック
      * リンク

    * ドキュメントの構築

      * ポートフォリオの構築

    * 自分自身のポートフォリオを構築する

      * ランドスケープの構築 **(一部更新)**
      * ドキュメントのビルドと継続的インテグレーション **(更新)**

    * まとめ

  * 10章 テスト駆動開発

    * テストをしていない人へ **(一部更新)**

      * テスト駆動開発の原則 **(一部更新)**
      * どのような種類のテストがあるのか？ **(更新)**
      * Pythonの標準テストツール **(更新)**

    * テストをしている人へ **(更新)**

      * ユニットテストの落とし穴
      * 代替のユニットテストフレームワーク **(一部更新)**
      * テストカバレッジ **(更新)**
      * スタブとモック **(一部更新)**
      * テスト環境と依存関係の互換性 **(更新)**
      * ドキュメント駆動開発

    * まとめ **(更新)**

  * 11章 最適化 -- 一般原則とプロファイリングテクニック

    * 3つのルール **(更新)**

      * まず、動かす
      * ユーザー視点で考える
      * 可読性とメンテナンス性を保つ

    * 最適化戦略

      * 外部の原因を探す
      * ハードウェアを拡張する
      * スピードテストを書く

    * ボトルネックを見つける

      * CPU使用量のプロファイル **(一部更新)**
      * メモリー使用量のプロファイル **(更新)**
      * ネットワーク使用量のプロファイル **(更新)**

    * まとめ **(更新)**

  * 12章 最適化 -- いくつかの強力な解決方法

    * 複雑度を下げる **(加筆あり)**

      * 循環的複雑度 **(一部更新)**
      * ビッグ・オー記法 **(一部更新)**

    * シンプルにする

      * リストからの探索
      * list の代わりに set を使う
      * 外部呼び出しを減らす

    * collections モジュールを使う

      * deque
      * defaultdict
      * namedtuple

    * トレードオフを利用する **(新規)**

      * ヒューリスティクスや近似アルゴリズムを使う **(新規)**
      * タスクキューを使って遅延処理を行う **(新規)**
      * 確率的データ構造を利用する **(新規)**

    * キャッシュ

      * 決定的キャッシュ
      * 非決定的キャッシュ
      * キャッシュサーバー

    * まとめ **(更新)**

  * 13章 並行処理 **(新規)**

    * なぜ並行処理が必要なのか？ **(新規)**
    * マルチスレッド **(新規)**

      * マルチスレッドとは？ **(新規)**
      * Pythonはどのようにスレッドを扱うのか？ **(新規)**
      * いつスレッドを使うべきか？ **(新規)**

    * マルチプロセス **(新規)**

      * 組み込みの multiprocessing モジュール **(新規)**

    * 非同期プログラミング **(新規)**

      * 協調的マルチタスクと非同期I/O **(新規)**
      * Pythonにおける async と await **(新規)**
      * 以前のバージョンにおける asyncio **(新規)**
      * 非同期プログラミングの実践例 **(新規)**
      * Future を利用して同期コードを結合する **(新規)**

    * まとめ **(新規)**

  * 14章 Pythonのためのデザインパターン

    * 生成に関するパターン

      * Singleton パターン

    * 構造に関するパターン

      * Adapterパターン
      * Proxyパターン
      * Facadeパターン

    * 振る舞いに関するパターン

      * Observerパターン
      * Visitorパターン
      * Templateパターン

    * まとめ



おまけ
=======

2018年2月26日（月） 発売です。

.. raw:: html

   <div class="amazlet-box" style="margin-bottom:0px;"><div class="amazlet-image" style="float:left;margin:0px 12px 1px 0px;"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4048930613/freiaweb-22/ref=nosim/" name="amazletlink" target="_blank"><img src="https://images-fe.ssl-images-amazon.com/images/I/51ivxfpMPKL._SL160_.jpg" alt="エキスパートPythonプログラミング改訂2版" style="border: none;" /></a></div><div class="amazlet-info" style="line-height:120%; margin-bottom: 10px"><div class="amazlet-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4048930613/freiaweb-22/ref=nosim/" name="amazletlink" target="_blank">エキスパートPythonプログラミング改訂2版</a><div class="amazlet-powered-date" style="font-size:80%;margin-top:5px;line-height:120%">posted with <a href="http://www.amazlet.com/" title="amazlet" target="_blank">amazlet</a> at 18.02.11</div></div><div class="amazlet-detail">Michal Jaworski Tarek Ziade <br />KADOKAWA (2018-02-26)<br />売り上げランキング: 11,344<br /></div><div class="amazlet-sub-info" style="float: left;"><div class="amazlet-link" style="margin-top: 5px"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4048930613/freiaweb-22/ref=nosim/" name="amazletlink" target="_blank">Amazon.co.jpで詳細を見る</a></div></div></div><div class="amazlet-footer" style="clear: left"></div></div>

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">エキPy 改訂2版のレビューしてるけど、3章まじ面白い（時間の都合で今まで読んでなかった）。1版より具体的で実践的で深くてだいぶ面白い。 <a href="https://t.co/HXHq8Codz8">https://t.co/HXHq8Codz8</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/957598718244433921?ref_src=twsrc%5Etfw">2018年1月28日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">エキPy改訂2版、C拡張関連な7章レビューdone. 前知識あって読んだのを差し引いても、すごく読みやすくて分かりやすかった。Cython便利。</p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/958262698541694976?ref_src=twsrc%5Etfw">2018年1月30日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">エキスパートPythonプログラミング改訂2版の見本きた！ページ数は100ページ増量、密度はアップ、2017年末の情報に追従、お値段は1版から据え置き！ <a href="https://twitter.com/hashtag/expertpython?src=hash&amp;ref_src=twsrc%5Etfw">#expertpython</a> <a href="https://t.co/6U5Gq624kn">https://t.co/6U5Gq624kn</a> <a href="https://t.co/2SauP9B1Op">pic.twitter.com/2SauP9B1Op</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/964727534427324416?ref_src=twsrc%5Etfw">2018年2月17日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">2冊の見本を手にご満悦の訳者近影です <a href="https://twitter.com/hashtag/pyhack?src=hash&amp;ref_src=twsrc%5Etfw">#pyhack</a> <a href="https://twitter.com/hashtag/%E7%8B%AC%E3%83%97%E3%83%AD?src=hash&amp;ref_src=twsrc%5Etfw">#独プロ</a> <a href="https://twitter.com/hashtag/expertpython?src=hash&amp;ref_src=twsrc%5Etfw">#expertpython</a> (@ 株式会社ビープラウド - <a href="https://twitter.com/beproud_jp?ref_src=twsrc%5Etfw">@beproud_jp</a> in 渋谷区, 東京都 w/ <a href="https://twitter.com/shimizukawa?ref_src=twsrc%5Etfw">@shimizukawa</a>) <a href="https://t.co/d6hdO1HUSY">https://t.co/d6hdO1HUSY</a> <a href="https://t.co/aDGC3K7rhr">pic.twitter.com/aDGC3K7rhr</a></p>&mdash; Takanori Suzuki (@takanory) <a href="https://twitter.com/takanory/status/964696217224609792?ref_src=twsrc%5Etfw">2018年2月17日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">エキスパートPythonプログラミング改訂2版 <a href="https://t.co/4yVJDi2EEz">https://t.co/4yVJDi2EEz</a> をチラ見した。前と比べてもすごくわかりやすくなってる気がする。エキスパートと銘打ってるだけあって、実践するのに「ここどうするの？」というところにも触れられてていい感じだ。はやく発売されないかなー <a href="https://twitter.com/hashtag/expertpython?src=hash&amp;ref_src=twsrc%5Etfw">#expertpython</a> <a href="https://twitter.com/hashtag/pyhack?src=hash&amp;ref_src=twsrc%5Etfw">#pyhack</a></p>&mdash; かしゅー (@kashew_nuts) <a href="https://twitter.com/kashew_nuts/status/964727054011850752?ref_src=twsrc%5Etfw">2018年2月17日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


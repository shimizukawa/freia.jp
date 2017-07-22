:date: 2015-02-18 13:50:00
:tags: book, Python, beproud, work

==============================================================================
2015/02/18 「Pythonプロフェッショナルプログラミング第2版」が2/27発売 #pypro2
==============================================================================

Pythonプロフェッショナルプログラミング、第2版を書きました。
さきほど印刷所に最終版を提出した、ということで、ちょと紹介します。

.. figure:: pypro2-20150205.png
   :width: 400

   書影: Pythonプロフェッショナルプログラミング第2版

   * 金額: 2,800円
   * ページ: 472ページ
   * 発売日: 2/27(金)
   * 出版社: `秀和システム <http://www.shuwasystem.co.jp/>`__
   * ISBN: 479804315X,  978-4798043159
   * Amazon: 

     .. raw:: html

        <iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&nou=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=freiaweb-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=479804315X" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>



前回の第1版は3年前: :doc:`../2012-03-27-python-professional-programming/index` 。

コンセプトは変わらず、 **BPStyle** 。「Pythonで仕事をしていく上でのBPのノウハウ」を集めた本です。みなさんの仕事での参考になれば幸いです。

第2版での見所と章構成を紹介します。

みどころ
==========

3つの章を新しく書き下ろしました。

* 3章. Pythonプロジェクトの構成とパッケージ作成

  Pythonでの開発に必須なツール、pipとvirtualenvを紹介。
  2章で作成したWebアプリケーションを題材に、Pythonの開発を始めるときのディレクトリ構成、
  setup.pyの用意、リポジトリの登録、PyPIへの公開、といった流れを扱っています。

* 9章. Pythonパッケージングと運用への活用

  Pythonパッケージングを活用して、デプロイやCIに適用する、といった内容です。
  3章の応用編です。

* 11章. 環境構築とデプロイの自動化

  Deployの話は第1版でもありましたが、内容がFabricからAnsibleに変わりました。
  といっても、Ansibleの詳しい内容は別のAnsible本等にまかせて、サーバー構築時の
  考え方と、それをAnsibleでどうやって扱っていくのかというところにフォーカスしています。


全体的に現在のバージョン、一般的な作法に合わせて書き直しました。また、BPの社内標準の現状にあわせて更新しています。

* Ubuntu 14.04, Python 2.7.6 をベースに更新しました
* distributeとsetuptoolsは紹介から消してpipだけにしました
* エディタの比較紹介を追加しました: Vim, Emacs, PyCharm
* HTMLが出てくるところはHTML5で書き直しました
* Tracの説明はなくなってRedmineだけになりました
* Skypeの説明はなくなってSlackになりました
* チケットテンプレートで運用している話を追記しました
* testfixturesの紹介を追加し、noseからpytestに変更しました
* Sphinxは1.3に更新しました
* Djangoは1.7を扱っていて、southからDjango migrationに書き直されました
* chardet, feedparserの紹介を削除し、requestsの紹介を追加しました


もう内容が古いなんて言わせない！（distributeとかdistributeとか）


章構成
========

Pythonで開発しよう
---------------------
* 1. Pythonをはじめよう
* 2. Webアプリケーションを作る
* 3. Pythonプロジェクトの構成とパッケージ作成

チーム開発のサイクル
-----------------------
* 4. チーム開発のためのツール
* 5. 課題管理とレビュー
* 6. Mercurialによるソースコード管理
* 7. ドキュメントの基盤を整える
* 8. モジュール分割設計と単体テスト
* 9. Pythonパッケージングと運用への活用
* 10. Jenkinsで継続的インテグレーション

サービス公開
---------------
* 11. 環境構築とデプロイの自動化
* 12. アプリケーションのパフォーマンス改善

開発を加速させるテクニック
----------------------------
* 13. テストを味方にする
* 14. Djangoを便利に使う
* 15. 便利なPythonモジュールを使おう

Appendix
---------
* Appendix A: VirtualBoxのセットアップ
* Appendix B: OS(Ubuntu)のセットアップ


お礼
========

今回、知っている範囲で以下のメンバーにて制作しました。

* 11人の執筆者
* 12名の社外レビューアー
* 7名の社内レビューアー
* 編集さんと組版担当者さん

総勢32名！みなさん、ありがとうございました。お疲れ様でした！

システム
===========

32名を支えたシステム構成について、機会があればどこかでまとめたいと思います。

* Slack: 会話や連絡は全てSlackでした。今回メールゼロ。書籍体裁のPDF渡しもSlackで。
* Redmine: Wikiと文面のDiffビューワーとして使いました
* Mercurial: Sphinxの原稿を管理しました
* Sphinx: 原稿はSphinxで書いて、拙作Shuwa builderで提出用に変換しました
* Sphinx term validator: 用語を登録しておくとビルド時に用語揺れを検出します
* Google Spreadsheet: レビュー指摘はspreadsheetでやりました
* Google App Script: レビュー追加されたときや、レビュー対処状況(12/99とか)をSlackに通知してました
* Jenkins: Sphinxの原稿をpushしたときにPDF,HTML,Shuwa出力を自動ビルド、いつでも最新を閲覧
* Dropbox: 書籍体裁になる前に、HTML出力をレビューしてもらうために使いました


まとめ
========

ハッシュタグは `#pypro2`_ ですね。

（Sphinx-1.3をはやくリリースしないと・・）


.. note::

   訂正: 発売日を 2/28(金) としていましたが、2/27(金)でした。


.. _#pypro2: https://twitter.com/hashtag/pypro2?f=realtime&src=hash


:date: 2005-09-04 18:11:05
:categories: ['Zope']
:body type: text/x-rst

============================
2005/09/04 Zope3勉強会 第6回
============================

*Category: 'Zope'*

Zope3勉強会(第6回)に参加してきました。前回8/7は参加できなかったので、記憶が……(笑)

以下、参加メモです。



.. :extend type: text/plain
.. :extend:

今日読んだChapter
------------------

- 17

  - コンテナの中身のサイズを取得するAdapterの作成とZCMLへの登録
  - ISizedインターフェースを実装したら、デフォルトのZope3のスキンへの表示が
    変わった。

- 18

  - 国際化(i18n)
  - poファイルをmsgfmtでmoに変更
  - さっそくmessageboardのpoファイルを翻訳してみた

- 19

  - Event,Subscription,Annotation
  - Zope3のオブジェクトはセキュリティークラスでラッピングされている


API Doc について
-----------------

登録したProductのInterfaceやAdapterが自動的にAPIDocに登録・表示される。どのコンテンツがどのInterfaceを実装しているか、どのAdapterを使えるか、という情報が自動的にドキュメント化されるので、誰かが作ったプロダクトの関連プロダクト(やAdapter)を作るときに構成を調べやすい。




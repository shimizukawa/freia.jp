:date: 2006-01-30 13:02:25
:tags: Plone

==============================
2006/01/30 Plone2.5 最初のα版
==============================

Plone2.5 最初のα版が出ました。 `Ploneサイトに掲載されたニュース`_ の一部をざっと意訳してみたので、時間のある人はニュースの最後の方にある協力依頼に応えてみてはどうでしょう？

.. _`Ploneサイトに掲載されたニュース`: http://plone.org/news/first-plone-2-5-alpha-released

以下、意訳。

.. :extend type: text/x-rst
.. :extend:


Plone 2.5 最初のα版をリリース
================================
2006/1/29 13:21 by Alec Mitchell

PloneチームはPlone2.5の最初の公式プレビューをリリースします。このバージョンはインフラの変更にフォーカスしています。

α版に含まれている新機能
------------------------

- PloneでZope3 MessageIDsを使う機能; これはpythonで翻訳機能を実装するオフィシャルな方法です (plip108_)
- ステータスメッセージをクエリ文字列で渡す機能を廃止し、Zope3的なグローバルユーティリティーを利用します。このため、メッセージの翻訳や複数のメッセージを表示することが出来ます。(plip111_)
- PloneはCMFPlacefulWorkflowを同梱します。このため、ポータル内の場所毎に独立した type->workflow マッピングを行うことが出来ます。(plip52_)

.. _plip108: http://plone.org/products/plone/roadmap/108
.. _plip111: http://plone.org/products/plone/roadmap/111
.. _plip52: http://plone.org/products/plone/roadmap/52

今後のリリースで実装される機能
------------------------------

- 認証メカニズムをGroupUserFolderからPAS/PlonePASに入れ替え、Pluggableで拡張可能なシステムにします。(plip102_)
- Replacing the current python site creation mechanisms with an XML driven portal setup using GenericSetup. (plip113_)
- 多くのpython script、ツール関数、ユーティリティーテンプレートをZope3 Browser Viewに入れ替えます。(plip105_, plip106_)

.. _plip102: http://plone.org/products/plone/roadmap/102
.. _plip113: http://plone.org/products/plone/roadmap/113
.. _plip105: http://plone.org/products/plone/roadmap/105
.. _plip106: http://plone.org/products/plone/roadmap/106

重要！ あなたに手伝って欲しい事
-------------------------------

- **インストールやアップグレード** インスタンスをバックアップして、Plone 2.5にしてください。そしてマイグレーションの問題やバグを見つけたらIssue Trackerに報告してください。多くのマイグレーションと報告が行われれば、最終リリースまでにあなたのサイトを問題なくマイグレーション出来るようになると思います。
- **テスト** α版を多くの環境でセットアップして、問題を報告してください。
- **あなたのプロダクトをPlone2.5αでテストしてください** 。もしあなたがサードパーティの開発者なら、あなたのコードをPlone2.5の環境に合わせてアップグレードする事で、スケーラブルでファスターになるでしょう。開発者メーリングリストがあなたの助けになるでしょう。
- もし上記の機能を完了したりデバッグするのを手伝いたいのであれば、PLIPの著者と連絡を取ってください。

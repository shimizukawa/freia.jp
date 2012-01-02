:date: 2009-11-01 01:30:00
:categories: ['Event', 'Zope', 'python', 'Plone']
:body type: text/x-rst

====================================================================
2009/11/01 Deliverance - オープンソースカンファレンス2009 Tokyo/Fall
====================================================================

オープンソースカンファレンス2009 Tokyo/Fall にて、 `Japan Zope Users Group`_ と `Plone User's Groups Japan`_ の連名で45分1コマをいただき、Deliveranceのプレゼンを行ってきました。申込みは100名Maxまで行ったのですが、実質は50人くらいだったようです。

資料の大枠とデモ環境はだいぶ事前に出来ていたものの、プレゼン資料としては前日の夜20時ころから作り始めて、当日の朝11時に完成したような感じで、徹夜で協力してくれた友人とみたに心から感謝します。

プレゼン資料公開
----------------

プレゼン資料ですが、以下のURLで公開しています。

* `Deliveranceによるデザインカスタマイズ - プログラム不要・Ploneのサイトデザインの新潮流`_

プレゼン補足
------------

ここで、プレゼンについていくつか補足しておきます。

* ユーザー会の都合上Plone関連技術っぽいタイトルですが、Ploneあんまり関係ないです。
* WSGIとの親和性が高く、Proxyモードなら他のアプリにも適用出来ます。
* 実際、Drupal の方が非常に興味を持ってくれたりしたので、他言語への適用事例になるかも知れず（言い過ぎ？

また、DeliveranceをProxyモードで動作させる方法など、環境構築方法については資料では全く触れていません。プログラマーの人がセットアップしてくれるよ！という前提でした。その方法については以下のページを参照してみてください。

* `buildoutで開発 番外編2: buildoutでDeliverance環境を作る`_ 
* `DeliveranceでOSWDのデザインをTwitter.comに適用してみた`_


技術的な側面
------------

また、技術的な面についての補足です。

* デモスライド自体がDelivaranceでデザイン適用されたPloneS5です。
* 適用前後は http://admin.plone3d.freia.jp/, http://plone3d.freia.jp/ で見比べられます
* デモサイトは以下の技術で構成されています

  * ZEO
  * Zope2 (2.10.9)
  * Plone
  * repoze.zope2 (2.10.7)
  * Deliverance (0.3 middleware mode)
  * Paster
  * WSGI
  * Apache2.2
  * reStructuredText (元テキスト作成に使用)
  * PloneS5 (プレゼンモードに使用)
  * PloneSWFUpload (プレゼンの画像一括Uploadに使用)
  * Slimbox2 (Deliverance適用版プレゼンモードの画像拡大に使用)

この構成とほぼ同じ構成を作るためのbuildoutスケルトンを公開してるので、興味のある方は `Plone-3.3.1をWSGIで稼働させるための設定テンプレ`_ を参照してください。

おまけ
------

Deliveranceとcollective.xdvを比較している英語ドキュメントがあったので和訳してみました。プレゼンに組み込もうかと思って用意したのですが使われなかったやつです。参考まで。

* `テーマ適用アプローチの選択肢`_

さいごに
--------

皆さんお疲れ様でした！ 打ち上げで `渋川師匠`_ から色々とプレゼンの極意を聞いたので、少しずつプレゼンに生かしていきたいと思います！


.. _`Japan Zope Users Group`: http://zope.jp/
.. _`Plone User's Groups Japan`: http://plone.jp/
.. _`Deliveranceによるデザインカスタマイズ - プログラム不要・Ploneのサイトデザインの新潮流`: http://plone3d.freia.jp/deliverance/deliverance-presentation/presentation_view
.. _`Plone-3.3.1をWSGIで稼働させるための設定テンプレ`: http://www.freia.jp/taka/blog/673
.. _`buildoutで開発 番外編2: buildoutでDeliverance環境を作る`: http://www.freia.jp/taka/blog/668
.. _`DeliveranceでOSWDのデザインをTwitter.comに適用してみた`: http://www.freia.jp/taka/blog/669
.. _`テーマ適用アプローチの選択肢`: http://admin.plone3d.freia.jp/deliverance/choosing-the-appropriate-theming-approach
.. _`渋川師匠`: http://shibu.jp


.. :extend type: text/html
.. :extend:


.. :comments:
.. :comment id: 2009-11-01.7023097508
.. :title: バックアップスライドのところで
.. :author: jack
.. :date: 2009-11-01 15:25:09
.. :email: 
.. :url: 
.. :body:
.. Varnish とかリバースプロクシがある場合どこに置くかみたいなスライドで Load Balancer が Load Barancerになっていた気がします。勘違いだったらシツレイしました
.. 
.. :comments:
.. :comment id: 2009-11-01.0061196945
.. :title: バランサー
.. :author: しみずかわ
.. :date: 2009-11-01 15:30:06
.. :email: 
.. :url: 
.. :body:
.. ほんとうだ！某所からコピペしたときに気づかなかった.... とりあえず放置しますｗ
.. 

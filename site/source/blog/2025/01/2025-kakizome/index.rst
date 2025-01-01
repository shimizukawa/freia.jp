:date: 2025-01-01 19:00
:tags: kakizome

=====================
書き初め
=====================

明けましておめでとうございます。

.. figure:: hebi-kama.*
   :width: 500px

   へび蒲鉾

TL;DR
========

* 2024年は、イベントの現地参加、OSSリリース、blog、読書量を増やした。英語の練習はあまりできてない。
* 2025年は、引き続き個人のアウトプットを増やし、仕事の時間を減らして成果を上げる

昨年はこちら: :doc:`/blog/2024/01/2024-kakizome/index`

2024年振り返り
==================

PyCon JP 2024、PyCon APAC 2024、PyCon mini 東海
--------------------------------------------------

2024年はこれまで抑え気味だった現地イベント参加を増やしました。
4つのPyCon関連イベントに参加しました。

- :doc:`/blog/2024/02/pyconph2024/index`
- `PyCon JP 2024 <https://scrapbox.io/shimizukawa/PyCon_JP_2024>`_
- :doc:`/blog/2024/10/pyconapac2024/index`
- :doc:`/blog/2024/11/pycontokai2024/index`

本当はもう一つ、 `PyCon mini Shizuoka 2024 <https://shizuoka.pycon.jp/2024>`_ の参加を予定していましたが、台風の影響で延期になってしまいました（2025年2月に開催決定しています）。準備はしていたけど、

PyCon関連では、PyCon JP 2024で行った遠方支援の支払い方改善チャレンジもやりました。
これについては、 `PyCon JP Blog: PyCon JP 遠方支援を支える技術 <https://pyconjp.blogspot.com/2024/12/technology-for-pycon-jp-travel-support.html>`_ に詳しくまとめました。

それぞれのイベントの直前は登壇準備に時間を使うので、6ヶ月くらいはイベント向けに忙しかった感じがします。
2025年はもうちょっと数を減らさないといけない、と思いつつ、既に4つ参加する予定がある..

- 2月 `PyCon mini Shizuoka 2024 Continue <https://shizuoka.pycon.jp/2024>`_ 
- 3月 `PyCon APAC 2025 in Philippines <https://pycon-apac.python.ph/>`_
- 5月 `PyCon US 2025 <https://us.pycon.org/2025/>`_
- 秋 PyCon JP 2025


OSSのリリース
--------------

django-redshift-backend
^^^^^^^^^^^^^^^^^^^^^^^^^

`django-redshift-backend <https://pypi.org/project/django-redshift-backend/>`_ のリリースを5回。その前のリリースから1年半も空いてしまいました。

- 3.0.0 - 2022年2月27日: Django-4.0, Python-3.10 対応
- 4.0.0 - 2024年7月23日: Django-4.2 対応
- 4.1.0 - 2024年7月27日: Python-3.11, 3.12 対応
- 4.1.1 - 2024年8月20日: bugfix
- 4.2.0 - 2024年10月30日: Django-5.0, 5.1 対応
- 5.0.0 - 2024年11月28日: Python-3.13 対応

Django-4.2 からはDjangoのDBバックエンドの内部構造が変わってしまって、もらっていたPull Requestでは対応しきれず、そのまま1年以上時間が空いてしまいました。最終的には、内部構造が変わる前のDjangoのコードを一部同梱することで対応しましたが、それも問題があるようです。

- `#167: Reimplementation for Django 4.2+ Compatibility and Security Enhancement <https://github.com/jazzband/django-redshift-backend/issues/167>`_
- `#171: Signature for various "operations" incompatible with Django >= 4.1 <https://github.com/jazzband/django-redshift-backend/issues/171>`_

ちゃんとした対応が必要になっています。2025年はコードをガッツリ書き直しかなあ..

sphinx-intl
^^^^^^^^^^^^^^^^

`sphinx-intl <https://pypi.org/project/sphinx-intl/>`_ のリリースを3回。その前のリリースから1年2ヶ月空いてしまいました。

- 2.1.0 - 2023年2月5日: Python-3.11, 3.12 対応
- 2.2.0 - 2024年4月20日: Python-3.13 対応
- 2.3.0 - 2024年11月10日: Python-3.7, 3.8 の廃止
- 2.3.1 - 2024年12月1日: bugfix

あまり機能追加するツールではないので、やることはバージョンアップ対応くらい。
マルチプロセス実行での高速化のPRとかがあったので、Rustで書き直して高速化とかはありかもしれない。


書籍とかPodcastとか
--------------------

書籍紹介を2回、寄稿しました。

- `基礎の学び直しから実践へ。『エキスパートPythonプログラミング』翻訳者が推薦するPython本3冊 | レバテックラボ（レバテックLAB） <https://levtech.jp/media/article/column/detail_560/>`_
- 2つめは1月公開予定

書籍紹介の流れで手元にあった積読本を読んで、さらにAudibleに加入したので通勤中や運転中に聞いてます。

* `バッタを倒しにアフリカへ <https://amzn.to/4fF9Voz>`_ (紙)
* `ハイパーモダンPython <https://scrapbox.io/shimizukawa/%E3%83%8F%E3%82%A4%E3%83%91%E3%83%BC%E3%83%A2%E3%83%80%E3%83%B3Python>`_ (紙)
* `勉強の仕方 <https://scrapbox.io/shimizukawa/%E5%8B%89%E5%BC%B7%E3%81%AE%E4%BB%95%E6%96%B9>`_ (紙)
* `上達の法則 効率のよい努力を科学する <https://scrapbox.io/shimizukawa/%E4%B8%8A%E9%81%94%E3%81%AE%E6%B3%95%E5%89%87>`_ (Kindle)
* `コーディングを支える技術 <https://scrapbox.io/shimizukawa/%E3%82%B3%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%82%92%E6%94%AF%E3%81%88%E3%82%8B%E6%8A%80%E8%A1%93>`_ (紙)
* `#100日チャレンジ 毎日連続100本アプリを作ったら人生が変わった <https://amzn.to/4gA2Y9r>`_ (紙)
* `やる気に頼らず「すぐやる人」になる37のコツ <https://amzn.to/3PglLe7>`_ (Audible)
* `還暦からの底力 - 歴史・人・旅に学ぶ生き方 <https://amzn.to/3BUQQAT>`_ (Audible)
* `復活への底力 - 運命を受け入れ、前向きに生きる <https://amzn.to/3BP8Ix8>`_ (Audible)
* `本の「使い方」 <https://amzn.to/40dZBPY>`_ (Audible)

Podcast。通勤とドライブのお供に。

* `fukabori.fm <https://fukabori.fm/>`_
* `hogehoge radio show | Podcast on Spotify <https://open.spotify.com/show/2d0T8uzFXojLTwzlOjHSBG>`_
* `Python Bytes Podcast <https://pythonbytes.fm/>`_
* `Rebuild - Podcast by Tatsuhiko Miyagawa <https://rebuild.fm/>`_
* `terapyon channel podcast <https://podcast.terapyon.net/>`_


2025年の目標
============

個人のアウトプットを増やして仕事の効率アップを狙う
---------------------------------------------------------

2024年の目標と同じです。
個人でスクラッチで書いたコードをblogにして仕事で使う、というのを引き続きやっていきます。

2024年はあまり残業せずに個人のプログラミングとかコミュニティー活動とかに時間を振りましたが、それでも有休が余りすぎています。
有休を取ってオフィスの近くで一日作業するとかやろうかな。
PyConなどのイベントに参加して試したいツールやライブラリはたくさんあるけど、試す時間が足りない。本も読みたい。


blogとscrap
------------------

アウトプットとしては、ここ数年はblogより 清水川のScrapbox_ に技術メモを書いていましたが、2024年からは書きっぱなしではなく、blogでまとめを書くようにしています。
スクラップに知識の断片をダンプするだけでは無く、blogを書くことで断片をまとめられ、知識や理解が整理されて、結果として試行錯誤時間が短縮される体験ができています。

.. _清水川のScrapbox: https://scrapbox.io/shimizukawa/

英語のリスニングを鍛える
------------------------------

2024年のリスニング練習は2月のPyCon Philippines以降は途切れてしまいました。
:doc:`/blog/2024/03/talk-shadowing/index` は10月のPyCon APAC in Indonesia でも使いましたが、2月のときほど集中して練習できていませんでした。

今年は、3月にPyCon Philippines、5月にPyCon USに行くので、練習を再開しようかな。
ソフトウェア開発関連ネタで英会話練習できる環境ないかなあ。週何回か通って、マンツーマンで教えてもらって、宿題が出るようなのだと続けられるかなあ。

おまけ
--------

家族がインフルエンザに感染してしまったため、年末年始は自宅に引き籠もっています。
そのため、元日朝からボードゲーム三昧。

.. figure:: catan.*
   :width: 500px

   カタン

.. figure:: catan-startrek.*
   :width: 500px

   カタン STARTREK版

.. figure:: monopoly-tokyo.*
   :width: 500px

   モノポリー 東京版

全敗しました...。

それでは、今年もよろしくお願い致します。

:date: 2007-04-18 21:05:09
:categories: ['Event', 'Zope', 'Plone']
:body type: text/x-rst

=======================
ZopeEssentials6 参加log
=======================

今日は `Zope Essentials 6`_ に参加してきました。
天気は残念ながら雨でしたが、参加者30名の定員いっぱいでした。それにしても最近寒すぎ。

PART 1 : Plone in New Zealand
-------------------------------
ニュージーランドでPlone会社を経営しているTim Knappが、ニュージーランドでのPlone事情を紹介してくれました。ちなみに会社名は `Emerge Technology`_ というそうです。

最初、PCが起動しなくなってかなりハラハラしましたが、PCも無事起動し、プレゼンが始まりました。

.. epigraph:: 

  私たちは、必要な機能性、信頼のおけるヒストリー、十分なデベロッパサポート付きのオープンソースソリューションを求めています。Ploneはこれら全ての条件を満たしています。

  -- Laurence Millar

ニュージーランドでオープンソースを使用しているのはベンチャー企業と政府が主だそうです。日本はどうですか？とTimさんから会場に質問が出ましたが、あまり良い反応はありませんでした。ニュージーランドに比べると、残念ながら日本政府でのオープンソース利用はまだまだ初期段階という感じです。

開発に使っている主要ツールとして、 `Instance manager`_ と `ArchGenXML`_ が上げられました。Instance managerは複数の環境でまったく同じProductを設置して設定して‥‥という初期設定を設定に従って一発で行ってくれる超便利なツールっぽいです。また、ArcheGenXMLも2年前に見たときにくらべてかなりパワーアップしていて、ワークフローの設定やテストのセットアップについても **超** 手軽に作ることが出来るようです。実際にTimさんがデモでInstance managerとArchGenXMLを組み合わせて、サクっとコンテンツタイプとワークフローを作って動く状態にしていました。すごすぎ！要チェックや！

最後に、プレゼントということでPloneのTシャツがプレゼントされました。ほしかったー


PART 2 : Plone Sprint レポート
------------------------------
ジョナサンのPlone Sprintレポートです。最近寺田さんがジョナサンのとこの大学でPloneについてホゲホゲしてるらしく、今日もちょっと遅れてやってきました。PloneインストーラでインストールしたらVistaで動かなかったらしいです。Program Filesにインストールしちゃだめよー。

前回のSprintは、目標がきっちりきまっていて発表盛りだくさんだったのに対して、今回のSprintは、発表無し＆みんなやりたいことを自由にやる、というかんじの、かなりイタリアンな感じだったようです。

Plone3.0に向けてKSSをSeleniumでのテストがたくさん作られたけど、新しく入ったAjaxの仕組みとKupuの仕組みがバッティングして大変だったようです。

XML import/exportの機能をPloneに実装。でもLinguaPloneのように多言語対応コンテンツはコンテンツのインスタンス間にリファレンスが張られていて、XMLで書き出したデータを他の環境で読み込んだ時にリファレンス情報を正しく復元するのがかなり大変だったようです。でもちゃんと出来たらしい。

他にも以下のような開発があったそうです。

- media file 対応
- formlib widget作成
- remember (CMF Memberの置き換え)作成
- deliverance （デザイナー向け、Ploneテンプレート作成）

Q and A
~~~~~~~~~

Plone-3.0は実用になるか？

- Plone-3.0はまだバグが多い
- でもPlone-3.0がリリースされればPlone-2.1系はサポートされなくなる
- LinguaPloneはPlone-2.5系にちゃんと対応してない。3.0はもっと対応してない。

Sprintに行ったのは仕事？趣味？

- 開発スキルはそれほどないので貢献はなかなかしづらい
- でも開発者達のオーラを浴びることが出来る！
- あるいみ無料のトレーニング
- Sprintから得るものはものすごく大きい
- 何気ない会話からチーム内の会話まで全部Plone。

  - 一番困る顧客はPloneをちょっと知っている人
  - 勝手にPloneプロダクトを入れてしまう
  - 一番良い顧客はPloneかどうかを気にしない人
  - 契約でZMIへのアクセスを禁止したりする

PART 3 : 二次会
---------------
これから行ってきます:-)


.. _`Zope Essentials 6`: http://zope.jp/events/zopeessentials/6
.. _`Emerge Technology`: http://www.emergetec.com
.. _`ArchGenXML`: http://plone.org/products/archgenxml
.. _`Instance manager`: http://plone.org/products/instance-manager



.. :extend type: text/html
.. :extend:

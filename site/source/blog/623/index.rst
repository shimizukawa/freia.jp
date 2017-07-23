:date: 2009-02-03 02:29:21
:tags: Programming, boadgame, ruby-on-rails

=============================
2009/02/03 BattleLine RoR (4)
=============================

*注）ここで記載しているBattleLineは、GoogleでたくさんヒットするBattleLine Onlineとは別物です。*

---------------

最後にプレイしたカードの外枠に色を付けて、いちいち手順履歴を見なくても分かるようにしてみた。
あと、アレキサンダー vs ダリウス なゲームなので、ALEXANDERを使ったプレーヤーはDARIUSを使えないように判定を入れようと思ったけど、このために ``リーダー使ったflag`` を持たせるのはイヤだなぁ。でもflag持たせないと全履歴サーチしないといけないのでやっぱりroundテーブルにflagを持たせるべきか...。

そろそろDBの設計は再検討したほうが良いかもしれない。再設計するならテストを書かないといかんなぁ。

とりあえずゲームの勝敗の確定部分を実装して、公開可能にするか。


勉強したこと
------------
ここまで実装が進むと、特に新しいネタは無し。helperに関数を色々つけていたら無法地帯になったので、モデルに移植しつつテストを書きたくてしょうがない感じになってきた。


.. :extend type: text/html
.. :extend:



.. image:: battleline_20090112a.*
   :width: 33%

.. image:: battleline_20090112b.*
   :width: 33%

.. image:: battleline_20090119.*
   :width: 33%

.. image:: battleline_20090120.*
   :width: 33%

.. image:: battleline_20090121a.*
   :width: 33%

.. image:: battleline_20090121b.*
   :width: 33%

.. image:: battleline_20090122a.*
   :width: 33%

.. image:: battleline_20090126.*
   :width: 33%

.. image:: battleline_20090128.*
   :width: 33%

.. image:: battleline_20090201.*
   :width: 33%


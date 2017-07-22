:date: 2009-01-23 01:24:07
:categories: ['ruby-on-rails']
:body type: text/x-rst

=============================
2009/01/23 BattleLine RoR (1)
=============================

`今年の目標`_ のエントリに書いたように、いろんなフレームワークでBattleLineを実装しようというやつの第一弾。

Pure HTML から始めて、AJAXでの操作の辺りでRESTfulとかWebAPIとか整備して、UIをFlexとかで置き換えて、どっかのタイミングでWebサーバー側を別フレームワークに切り替えて...みたいな感じで色々なフレームワークを勉強していきたい。

まずは Ruby on Rails 2.1 + Pure HTML で実装してみる。

正月の開発合宿から作り始めて、先週末後、1/18にやっと遊べるようになった。そのときの画面のスナップショットを貼っておく。

このときはまだ情報が並んでいるだけでとても遊びづらかった。TROOPカードはほんとは6色あるのに、A～Fの記号で表示されてたり、手札がソートされてなかったり、最後に指した手がなんだったか分からなくなったり、部隊カード山と戦術カード山を間違えたり...。

**そうか、機能要件だけは満たしてるけど使えないシステムって、こういう感じだよね。**

勉強したこと
------------

RoR: Modelにserialize指定でオブジェクトをRDBに保存出来る
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

あるターンでの山札の並びはRDBにどうやって格納するべきか。山札配列にカード名の文字列を入れておいて、プレイ時に先頭から取り出していきたい。ZopeならListに入れておけばそのままZODBに保存してくれるけど、RoRの場合は...?

解: serialize を使う

.. code-block:: ruby

  class Round < ActiveRecord::Base
    serialize :troops, Array
    ...
  end

DB保存時にto_yamlでyaml化したものが保存されるので、上記のように書いておくことでDBからのロード時にArrayとして復元してくれるようになる。ArrayとかHashとか独自クラスとかイケル。

でも、以下のようにしたらはまった。

.. code-block:: ruby

  round = Round.last
  card = round.troops.shift
  round.save

上記だとtroopsの中身が変わっている事をRailsが見逃してしまう(2.1からpartial updates対応になったため?)ので、 ``round.troops_will_change!`` を呼んであげてからsaveすることにした。

一応ODBっぽい感じに使えるけど、バグの原因になりそうだな。


.. _`今年の目標`: http://www.freia.jp/taka/blog/617



.. :extend type: text/html
.. :extend:


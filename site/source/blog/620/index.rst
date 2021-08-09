:date: 2009-01-24 20:41:53
:tags: Programming, boadgame, ruby-on-rails

=============================
BattleLine RoR (2)
=============================

1/19日時点でカードに色を付けて手札をソートするようにしたら、格段に見やすくなってゲームに集中できるようになった。やっぱり見た目のわかりやすさは重要。あと人間がものを判別するときってかなり色に頼ってるんだなぁと思った。識別のための配色は重要。

スナップショットでは左の手札のところがラジオボタンとカードの位置がずれていて縦に伸びてしまっている。カードに画像を使えば簡単に直せそうなんだけど、とりあえずは画像は無しで。

次の目標は、実際のカードを使ったプレート同じように、場のカードの並べ方を右に90度回転させて、自分の置いたカードが手前側に表示されるようにして、より分かりやすくすることかな！


勉強したこと
------------

RoR: 命名規約に沿っていないクラスをserializeすると復元出来ない
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
`BattleLine RoR (1)`_ では部隊カードの山札を格納する変数 troops や戦術カード山札の tactics を以下のように実装していた。

app/models/round.rb:

.. code-block::

  class Round < ActiveRecord::Base
    serialize :troops, Array
    ...

    def setup
      self.troops = ['A1','A2','A3',...,'B1','B2',...].sort_by{rand}
      self.tactics = ['ALEXANDER','DARIUS',...,'REDEPLOY',...].sort_by{rand}
      ...
    end
  end

このままだと色づけのためのスタイルシートclassの設定とか諸々がif文の嵐になってしまうので、Cardクラスを作ってゲームに使用するカードは全てCardクラスの派生クラスとして再実装した。

lib/card.rb:

.. code-block:: ruby

  class Card
    ...
    def self.new_troops
      TROOP_NAMES.collect{|name| TroopCard.new name}
    end
    def self.new_tactics
      TACTICS_NAMES.collect{|name| TacticsCard.new name}
    end 
  end

  class TroopCard < Card
    ...
  end

  class TacticsCard < Card
    ...
  end

で、改めてround.rbの実装を以下のように書き直した。

app/models/round.rb:

.. code-block:: ruby

  class Round < ActiveRecord::Base
    serialize :troops, Array
    ...

    def setup
      self.troops = Card.new_troops.sort_by{rand}
      self.tactics = ...
      ...
    end
  end

そうしたところ、画面表示にエラーが出るようになってしまったので、script/console で原因を確認したところ、保存してあったRoundレコードを読み込んだときにtroopsが正しくロードされなくなってしまっていた！


.. code-block:: ruby

  $ ruby script/console
  >> round = Round.last
  >> round.troops[0]
  => #<YAML::Object:0x5832ad4 @ivars={"name"=>"A1"}, @class="Card">

なんじゃこりゃ。#<YAML::Object .. ってYAMLのクラス？なんでTroopCardじゃないんだろう？

（...試行錯誤1時間くらい...）

round.rb で require 'card' してあげたらちゃんとロード出来るようになった。

.. code-block::

  $ ruby script/console
  >> round = Round.last
  >> round.troops[0]
  => #<TroopCard:0x4f12a1c @name="A1">

Rails の仕組みで、正しい名前のクラスなんかは自動的にファイルから読み込んでロードしてくれるようになっているけど、lib/card.rb ファイルに実装したTroopCardクラスはシリアライズした文字列からオブジェクトに戻す時に不明なクラス扱いされてしまっていたらしい。とりあえずrequire 'card'ってしておいたら、ちゃんと TroopCardクラスのインスタンスに戻してくれるようになった。

でも、そんな細かいクラス一つ一つのために命名規約に沿ってファイルを分けるの面倒くさいよ？


RoR: lib以下のファイルは自動再読み込みしてくれない
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

lib以下のファイル、というよりは特定のクラスの派生クラスしか自動再読込してくれないっぽい。コントローラやモデルなんかは自動再読込してくれるけど、独自に作ったクラスはだめだった。試しにlib以下じゃなくてmodels以下に置いてみたけどやっぱり駄目だった。

で、色々調べていったところ、Railsで行われている自動リロードは以下のような手順で実現しているっぽい。

 1. active_support/dependencies.rbでModelとClassに ``const_missing`` メソッドが定義されていて、定数(クラスとか)が無い場合に自動ロードする仕組みになっている
 2. Rails(というか今回調べたのはMongrel)はRequest処理が終わる毎にリロード可能なクラスとかを無効化(unload)している
 3. 無効化のためにactive_support/dependencies.rbの ``Dependencies.clear`` が呼び出されている
 4. 次のRequest時にはunloadされた定数が見つからないので ``const_missing`` でリロードされる

このとき無効化されるクラスはActiveRecord::Baseの継承クラスとか特定のクラスに限られるっぽい。

じゃあ、無効化される対象クラスにするにはどうすれば良いのか...と思ってさらに active_support/dependencies.rb を読んだところ、 Model, Class, Object に ``unloadable`` というメソッドが追加されていて、これ呼び出すと Dependencies.clear でunloadされるようになるらしい。

実際ちゃんと動くかどうか以下のようにして試してみた。

lib/foo.rb:

.. code-block:: ruby

  class Foo
    puts 'class Foo loaded!'
  end
  Foo.unloadable

.. code-block:: ruby

  $ ruby script\console
  Loading development environment (Rails 2.1.0)
  >> Foo
  class Foo loaded!
  => Foo
  >> Foo
  => Foo
  >> Dependencies.clear
  => ["Foo"]
  >> Foo
  class Foo loaded!
  => Foo

  /* modify puts line in foo.rb */

  >> Dependencies.clear
  => ["Foo"]
  >> Foo
  class Foo loaded! loaded! yahoo!!
  => Foo

うまくいったっぽい！


しかし、Railsで使う用の独自クラス(Card)に上記を適用してみたところ、serializeで独自クラスを含むArray, Hashの復元がうまくいかなくなってしまった‥‥。あちらを立てればこちらが立たず。あと一歩というところなんだけどなぁ。


.. _`BattleLine RoR (1)`: http://www.freia.jp/taka/blog/618



.. :extend type: text/html
.. :extend:


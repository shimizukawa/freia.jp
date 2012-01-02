:date: 2009-01-25 19:11:03
:categories: ['Programming', 'boadgame', 'ruby-on-rails']
:body type: text/x-rst

====================================================================
BattleLine RoR (3) serializeした独自クラスをYAMLからロード時に再読込
====================================================================

注）ここで記載しているBattleLineは、GoogleでたくさんヒットするBattleLine Onlineとは別物です。


1/20, 1/21 と、場のカードを90度回転させて、配色をより分かりやすくしてみた。このへんの実装そのものは殆どCSSの設定とテンプレートの変更だったのであんまり勉強ってことはなかったんだけど、カードの表示をする部分を部分テンプレートにして呼び出すようにしたのがせめてもの工夫と言えば工夫か。なんかdevelopment.logにテンプレートレンダリングのログがたくさん出てしまって邪魔だけど。

勝利ラインに色を付けて、だいぶそれっぽくなってきたので、次はそろそろゲームの勝敗の確定部分を実装する頃か‥‥と思ってたらaihatenaからリプレイ閲覧機能が欲しいとメッセージが来た。リプレイ見るためにはまず勝敗を確定させないとね‥‥。


勉強したこと
------------

RoR: 命名規則に沿っていないファイル名/クラスを自動ロードする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

独自クラスが自動リロードされない問題を色々調べていたら、ApplicationControllerもapplication_controller.rbではなくapplication.rbという名前のファイルで定義されているのになぜかちゃんと自動読み込みされていたので、どこかで特別な処理をしているはずだ！と思って調べてみた。

まずは自動ロード関連ということで active_support/dependencies.rb でapplication.rbを検索。発見っ。Dependencies#loadable_constants_for_path でなんかやってるらしい事が分かったので周辺の実装を読んでいったところ、Dependencies#depend_onでconst_missing時にたどるファイルを追加できる事が分かった。さらにObjectクラスへの追加メソッド Object#require_dependency でdepend_onが呼び出されるようになっている。何という迷路。

.. code-block:: ruby
  :title: active_support/dependencies.rb

  Object.instance_eval do
    define_method(:require_or_load)     { |file_name| Dependencies.require_or_load(file_name) } unless Object.respond_to?(:require_or_load)
    define_method(:require_dependency)  { |file_name| Dependencies.depend_on(file_name) }       unless Object.respond_to?(:require_dependency)
    define_method(:require_association) { |file_name| Dependencies.associate_with(file_name) }  unless Object.respond_to?(:require_association)
  end


Rubyのモンキーパッチ的なこういう実装って分かりやすいんだか分かりにくいんだかよく分からない...。Pythonだとこういう書き方はしないなぁ。

ということで、このrequire_dependencyを使うことで、自動ロードされない名前を探しに行ってくれるようになった。

.. code-block:: ruby
  :title: lib/foo.rb

  class Foo
    puts 'class Foo loaded!'
  end
    
  class Bar
    puts 'class Bar loaded!'
  end


.. code-block:: ruby

  $ ruby script\console
  Loading development environment (Rails 2.1.0)
  >> Bar
  NameError: uninitialized constant Bar
          from activesupport-2.1.0/lib/active_support/dependencies.rb:278:in `load_missing_constant'
          from activesupport-2.1.0/lib/active_support/dependencies.rb:467:in `const_missing'
          from activesupport-2.1.0/lib/active_support/dependencies.rb:479:in `const_missing'
          from (irb):1
  >> require_dependency 'foo'
  class Foo loaded!
  class Bar loaded!
  => true
  >> Bar
  => Bar

ところで、 ``require 'foo'`` や ``load 'foo'`` するのと ``require_dependency 'foo'`` するのとでは何が違うのか？よくわからなかったので調べてみると、requireやloadはそれを実行したファイル内などでしか有効じゃないけど、require_dependencyはシステム全体に影響するらしい事が分かった。で、それを消すのがDependencies.clearらしい。なるほど。

さらに grepしてみると action_controller/dispatcher.rb で以下のように使っているのを見つけた。

.. code-block:: ruby
  :title: action_controller/dispatcher.rb

  require_dependency 'application' unless defined?(::ApplicationController)

Request処理するときに最初に関連づけ設定してるのね。


RoR: serializeした独自クラスをYAMLからロード時に再読込
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

独自クラスはソースコード更新しても自動再読込されない問題に対して、昨日書いた ``unloadable`` を使う方法ではない方法で解決してみた。serializeしたインスタンスはYAMLでDBに保存されるので、これをde-serializeする時にYAMLの処理をhookしてリロードできないか試してみたらうまくいった。

まず、独自のクラスをYAML化する機能は、以下のように特に何もしなくても提供される。

.. code-block:: ruby
  :title: ruby script/console

  >> class MyClass
  >>   def initialize(name=nil)
  >>     @name = name
  >>   end
  >> end
  => nil

  >> o1 = MyClass.new 10
  => #<MyClass:0x4f0a420 @name=10>

  >> o1.to_yaml
  => "--- !ruby/object:MyClass \na: 10\n"

  >> o2 = YAML::load(o1.to_yaml)
  => #<MyClass:0x4efc44c @name=10>

で、これをload時にhook出来るようにするにはYAMLモジュールにtypeを追加定義してあげる。

.. code-block:: ruby
  :title: ruby script/console

  >> class MyClass
  >>   yaml_as "tag:freia.jp,2009:console"
  >> end
  => MyClass

  >> o1.to_yaml
  => "--- !freia.jp,2009/console \na: 10\n"

最後に、YAMLのloading機構に登録する。 ``add_domain_type`` の使い方は `YAML::add_domain_type Method`_ を参照。

.. code-block:: ruby
  :title: ruby script/console

  >> YAML::add_domain_type( "freia.jp,2009", "console" ) do |type, val|
  ?>   puts type
  >>   puts val.inspect
  >>   MyClass.new val['name']
  >> end
  => nil

  >> o3 = YAML::load(o1.to_yaml)
  tag:freia.jp,2009:console:MyClass
  {"name"=>10}
  => #<MyClass:0x44e3064 @name=10>

これでシリアライズされたインスタンスをYAMLから戻すときに任意の処理が出来るようになった。さらに継承したクラスについても一括で処理出来るようにもう一工夫。

.. code-block:: ruby
  :title: ruby script/console

  >> YAML::add_domain_type( "freia.jp,2009", "console" ) do |type, val|
  ?>   puts type
  >>   puts val.inspect
  >>   klass = type.split(':')[-1].constantize
  >>   klass.new val['name']
  >> end
  => nil

最後に、上記のconstantizeの行の前にrequire_dependencyを記述しておけば、YAML::load時に、require_dependencyしたファイルをリロードしてくれて、命名規則違反のクラスもちゃんとロード出来るよになった。

対象ファイルに定数定義があると問題になるけどな！（対策はまたいつか考えよう・・・）

以下が完成したmy_class.rbと実行結果。

.. code-block:: ruby
  :title: my_class.rb

  class MyClass
    yaml_as "tag:freia.jp,2009:my_class"

    def initialize(name=nil)
      @name = name
    end
  end

  class MySecondClass < MyClass
  end

  YAML::add_domain_type( "freia.jp,2009", "my_class" ) do |type, val|
    require_dependency 'my_class'
    klass = type.split(':')[-1].constantize
    klass.new val['name']
  end

.. code-block:: ruby
  :title: ruby script/console

  >> o1 = MyClass.new 'abc'
  => #<MyClass:0x4ed4190 @name="abc">

  >> y1 = o1.to_yaml
  => "--- !freia.jp,2009/my_class \nname: abc\n"

  >> YAML::load(y1)
  => #<MyClass:0x4ecded0 @name="abc">


  >> o2 = MySecondClass.new 'def'
  => #<MySecondClass:0x4567e04 @name="def">

  >> y2 = o2.to_yaml
  => "--- !freia.jp,2009/my_class:MySecondClass \nname: def\n"

  >> YAML::load(y2)
  => #<MySecondClass:0x4561d74 @name="def">

  >> Dependencies.clear
  => []
  >> MySecondClass
  NameError: uninitialized constant MySecondClass
  ...

  >> YAML::load(y2)
  => #<MySecondClass:0x5219c60 @name="def">

.. _`YAML::add_domain_type Method`: http://yaml4r.sourceforge.net/doc/class/yaml_add_domain_type_method.htm



.. :extend type: text/html
.. :extend:


.. :comments:
.. :comment id: 2009-01-31.1873859753
.. :title: Re:BattleLine RoR (3) serializeした独自クラスをYAMLからロード時に再読込
.. :author: aihatena
.. :date: 2009-01-31 10:59:48
.. :email: 
.. :url: 
.. :body:
.. 本日のdebug結果
.. * 先攻1ターン目に手札がソートされていない
.. * IEで表示すると青の背景色が無い/赤が原色
.. * AとE、BとFの色が同じに見えるので差が欲しい
.. * 後攻の見た目が先攻の鏡面表示。本来は9->1列の順
.. 　これはまあシステム上仕方がないかも
.. * SCOUT,DESERTER使用時にもライン選択が必須。
.. 　平常時はかまわないけど、置けないときに困る。
.. 　戦術カード引ききって邪魔するような場合もあるので
.. * 3枚置いた列にラジオボタンでないので MUD,FOG置けない
.. 　置ける列だけラジオボタン、という前提が間違ってた。
.. 　もしくはMUD,FOG持ってるときだけラジオボタン出すなど
.. * 勝利判定が動いてない。SKIPしまくりで終わらない
.. 
.. :comments:
.. :comment id: 2009-01-31.1612190362
.. :title: Re: バグ報告
.. :author: しみずかわ
.. :date: 2009-01-31 13:29:23
.. :email: 
.. :url: 
.. :body:
.. 報告感謝！
.. 
.. けっこうバグってるな－・・・。やっぱりテスト書かないと駄目だね。
.. 

:date: 2009-06-28 21:32:31
:tags: Zope, pyspa
:body type: text/x-rst

==================================================
2009/06/28 [pyspa5] Zope2でformlibベースのフォーム
==================================================

pyspa5の成果１。

:やりたいこと: Zope2で簡単にフォームを作る
:前提条件1: フォームの定義は自由に決められる
:前提条件2: Zope3のformlibのようにSchemaを決めるだけでUIの生成からチェックまでやってくれる
:前提条件3: 設定UIは無くても良いがtextで保存出来るようにする

以前から、お問い合わせフォーム１つ作るのに毎回毎回プログラムを書いてデバッグしてテストして‥‥というのを考えるのが面倒だと思っていたけど、一般解も無いし、どの言語の既存コードもしっくりこない、と思っていたので作ってみた。zope.formlib は良くできていて、zope.interface を使ってSchemaを定義するだけである程度の事はやってくれるし、Widgetの切り替えもzcmlでDIの定義を返れば良いので、結果的にDRYで手軽だと感じていて、Zope2のダイナミックな変更が効くとさらに良いなあと。

実際の所Zope2からformlibを使うのはそんなに難しくなくて、SchemaとなるInterfaceクラスを動的に生成することさえ出来れば、同じ感じでcontenttypeやviewのためのクラスも生成すればよい。ということで、コード。

スキーマ定義::

      from zope.schema import TextLine, Text, Choice, Set
      from Products.SimpleForm2 import FieldArgsWrapper as aw
  
      fields = [
          TextLine(**aw("name", "名前", required=True)),
          TextLine(**aw("email", "メールアドレス", required=True)),
          TextLine(**aw("addr", "住所", required=True)),
          TextLine(**aw("tel", "電話番号", required=False)),
          Text(**aw("message", "ご質問内容等", required=False)),
      ]


他に、複数選択のチェックボックスや単一選択のChoiceなどを定義する。定義したfieldsを使ってIntefaceを自動生成したり、Viewを自動生成して、問い合わせ画面表示や, バリデーションを行う。デザインはPageTemplateをいじる必要があるけど、上記のschema定義とデザイン設定だけZMIで設定すればOK、な作りに最終的にはしたいなあ。正直、Formとかコンテンツタイプなんて、いちいち開発なんてしてられないよね。

まあ、設定を動的に変えたいシーンというのは実際はほとんど無くて、最初の作成時と、あと運用中に1,2回あるかどうかなんで、そんなに力を入れるところかと言われると....やっぱり「うん」と答えるな。使うのが自分だけだとしてもあった方が便利だ。

もうちょっと整理したらSVNに入れよう。


.. :extend type: text/html
.. :extend:


:date: 2007-08-26 02:02:30
:categories: ['python', 'django']
:body type: text/x-rst

===============================
Django勉強会DISC4に参加しました
===============================

場所
=====
- サイボウズラボ
- 赤坂見附
- プレデンシャルタワー
- 参加者30人くらい

プレゼンとか
-------------
他の人のBlogかLingrのDjango-ja見てね！（超手抜き）
というか動画が公開されるかも。

http://groups.google.com/group/django-ja/browse_thread/thread/21503c49b25256b6

質問とか
---------
:Pythonを仕事に使ってる人:
  10人くらい
:Djangoを仕事に使ってる人:
  4人くらい
:Mac率:
  半分くらい？
:年齢分布:
  高校生 １,
  大学生 ０,
  失業者 １,
  会社員 他全員
:djangoproject.jpを知ってますか:
  8割くらい知ってた
:newforms使ってますか:
  半々くらい


感想
-----
- oldforms は詳しく解説されなかったのであまり把握できなかったけど、 newforms はとても理解しやすい構造だった。これから使うとしたらnewforms以外ありえない！
- django.contrib.admin ステキすぎ
- 普段見てるBlogの人とかお世話になってるサイトの人とかに会えた！
- ueblogの中の人から `MOO`_ で作った名刺をもらった！俺も作ろうかな。。
- ウノウの中の人から `/dev/null Tシャツのサイト`_ を教えてもらった！買おうかな。。
- 今週リリースしたFlashで大富豪！ http://plash.jp/ Wiiで遊べる！
- 高校生Pythonista山岸さんキター！しかも偽名(違) 正字正かな、て。将来は書店の店員て！？
- amachang さんカッコエエ！
- サイボウズラボかっこええ！
- 次のDjango勉強会は高校の体育館に西尾さんデビュー！？


ところで、Model, Field, Form, Widget という分割は自分はとても理解しやすかった。今まで触った他のWebフレームワークが似た構成だったから。

:Django:
  Model, (Modelの)Field, (Formの)Field, Form, Widget

:Zope2(archetypes):
  Schema(=Model), Field, ContentType(=Form), Widget

:Zope3:
  Interface(=Model), Field, formlib.form_fields(=Form). Widget

:TurboGears:
  Model, Field, Form, Widget

FieldのプレゼンテーションレイヤーとなるWidgetはデフォルトでどれが使われるかが決まっていて、ある状況下で変更するためには密結合(Fieldの初期化で渡すとか)する必要があるところも似ている。Zope3はDIなのでもうちょっとだけ柔軟性が高いけど、設定のためにはXML書かないといけない。Django的に柔軟性をもたせるならurls.pyみたいな設定でFormとWidgetのデフォルトの対応を決められればいいのかな。このサイトではToscaWidgetセットを使う、とか、AJAXなWidgetセットを使う、とかごそっと切り替えられるとうれしい人もいるかも。


.. _`MOO`: http://www.moo.com/vox/
.. _`/dev/null Tシャツのサイト`: http://www.upsold.com/imshop/app/b/13614/


.. :extend type: text/html
.. :extend:

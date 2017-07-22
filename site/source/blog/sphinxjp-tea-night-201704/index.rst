:date: 2017-04-17 22:40
:categories: ['Sphinx']
:body type: text/x-rst

=============================================
2017/04/17 Sphinx Tea Night 2017.04 #sphinxjp
=============================================

:doc:`前回 <../sphinxjp-tea-night-201703/index>` に引き続き、 `Sphinx Tea Night 2017.04`_ に参加しました。

自己紹介
========


:参加者: @usaturn, @narita_susumu, empress_012, @yosuke_bayashi, @shimizukawa, @cocoatomo

* @usaturn: 転職したインフラエンジニアです。いまは業務ではSphinxを使ってません。あれ、最近Sphinxなんにもやってないな・・。

* @narita_susumu: Macアプリの開発者です。最近はMacアプリを書く機会が減ってきてiOSアプリばかり書いています。

* empress_012: ふだんJavaを使って開発してるシステムエンジニアです。外部の人とSphinxでドキュメントを作る機会があって使い始めました

* @yosuke_bayashi: 組織向けのプロバイダーの仕事をしている。WebサーバーでBlog公開までいきたい

* @shimizukawa: 最近Sphinxのコミッターをtk0miyaさんにまかせっきりのコミッターです。そろそろSphinxの本を書き終わらないといけない時期なのにまだ出来ていないのでがんばります。

* @cocoatomo: 普段はJavaのバッチを書いたり色々やってます。Python公式ドキュメントの翻訳をやっていて、ドキュメントがSphinxで書かれているのでSphinxを使っている感じです。


今回から、開催場所が変更になりました。喫茶室ルノアール　市ヶ谷駅前店、です。イベントの写真撮り忘れたので、様子を知りたい方は次回参加ください。


話したこと
===========

AppleHelpの多言語化
----------------------
@narita_susumu さん: SphinxでAppleHelpの出力ができることを知ったので、多言語をどうやったら良いか知りたくて参加、とのこと。

AppleHelpにも多言語化の仕組みがあって、そのためには各言語別ディレクトリにSphinxのビルド結果を出力しなければいけない、らしい。Sphinxの言語コードは日本語なら ``ja`` だけど、AppleHelpでは ``JPN`` を指定するようだ（言語コードじゃなくて国コードなのかな？）。このため、Sphinxの出力先ディレクトリを自動的に決定するにはAlpha-2, Alpha-3のマッピングを持たないといけないとか。自動的に変換してくれるライブラリありそうだけど、それでもなんだか手間がかかりそうな話。

さらに、「日本語」で原文を書いているそうなので、各言語に翻訳してもらうための元言語が「日本語」になってしまっている問題もあり。Sphinxのi18n機能は「ドキュメントソースに書いた言語を元言語」にするので、みんなに英語から各言語へ翻訳してほしいと思ったら、ドキュメントソースを英語で書かないといけない。

このあたり、たしかに体系的にまとまった情報はないなあ。自分がSoftware Design 2016年4月号、5月号、に書いた記事がいちばんまとまってるけど、それでもまだ足りないかもしれない。

singlehtmlのリンクターゲット重複問題
-------------------------------------

前回参加した empress_012 さんが、 ``make singlehtml`` した結果、リンクターゲットがかぶりまくった問題。

章ごとにディレクトリを分けていて、章の中でもファイルを複数に分けているけれど、ビルドしたHTMLは章ごとに1つのHTMLになってほしい、という話が前回。解決方法として ``make singlehtml`` で妥協してもらったけれど、その後試してみたら、singlehtmlの出力ファイルで目次のリンクをクリックすると違うセクションにジャンプしてしまう。

これとおなじ問題 https://github.com/sphinx-doc/sphinx/issues/1878

原因は、各rstファイル毎に生成されたユニークIDをそのまま1つのHTMLに統合したときに使ってしまってるから。

正しく修正するためには、各セクションのリンクターゲット名をdocname別にユニークにするのではなく、ドキュメント全体でユニークにしないといけない。しかし、docutilsのmake_id関数にはdocname情報がこない。このため、reSTファイルの読み込み時点で与えられたリンクターゲットIDをあとのフェーズのsinglehtml builderの時点で付け替えするしかないんだよなー

とりあえず今回は急ぎの対応が必要そうだったので、アドホックなモンキーパッチを作成。以下のパッチは、「docname+セクション名」のmd5をリンクターゲットにしている。
これで、別のrstファイルにまったく同じセクション名があっても、おなじmd5値にはならないので問題が解決できる。

以下のコードをconf.pyに書いて使う。

.. code-block:: conf.py

   current_docname = ''

   def handle_current_doc(app, docname, source):
       global current_docname
       current_docname = docname

   def setup(app):
       app.connect('source-read', handle_current_doc)
       import hashlib
       from docutils import nodes
       nodes.make_id = lambda msg: hashlib.md5((current_docname + msg).encode('utf-8')).hexdigest()


このパッチは並列ビルドすると破綻しそう。


.. _Sphinx Tea Night 2017.04: https://sphinxjp.connpass.com/event/53471/


:date: 2017-09-08 11:00
:tags: Python, PyConJP, Conference

=====================================
PyCon JP 2017 1日目 参加ログ #pyconjp
=====================================

年に一度のお祭り、 `#PyConJP`_ 2017 in Tokyo に参加しました。

今日の14:05から、 `len()関数がオブジェクトの長さを手にいれる仕組み`_ というタイトルでトークもやるので、それまでは資料のブラッシュアップをがんばります。

今年はスタッフをしてないので、後はのんびり楽しもうと思います。

:イベント: `PyCon JP 2017`_
:参加者: 計測中（チケットは620完売、スポンサー多数？）
:会場: 早稲田大学 西早稲田キャンパス63号館


.. _PyCon JP 2017: https://pyconjp.connpass.com/event/59412/
.. _#pyconjp: https://twitter.com/search?f=tweets&vertical=default&q=%23pyconjp&src=typd
.. _len()関数がオブジェクトの長さを手にいれる仕組み: https://pycon.jp/2017/ja/schedule/presentation/22/

.. contents::
   :local:

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pyconjp?src=hash">#pyconjp</a> きたー。今年はスタッフじゃないぜー (@ 早稲田大学 西早稲田キャンパス 63号館1F 情報ギャラリー - <a href="https://twitter.com/waseda_univ">@waseda_univ</a> in 新宿区, 東京都) <a href="https://t.co/l7opmPgKNv">https://t.co/l7opmPgKNv</a> <a href="https://t.co/IzLtWXuCjw">pic.twitter.com/IzLtWXuCjw</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/905952696540258305">2017年9月8日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

レジストレーション
===================

.. figure:: registration.*
   :width: 80%

   受付。今年は **パトロン & スピーカー** だ！

.. figure:: patron.*
   :width: 80%

   パトロンバナー！！

受付後に、キーノート開始5分前に行ったらもう始まってた... つらい

キーノート
===========

* Peter Wang さん
* https://pycon.jp/2017/ja/talks/keynote/
* 動画: https://www.youtube.com/watch?v=kIgGHTsig6g

---------------------------------

本編は動画（↑）もあるし、Q&Aだけメモ。けっこうみなさん英語でサクサク質問してて、だいたい聞き取れませんでした。参考程度に。

Q&A

* Q（あくつたけしさん） USコミュニティと日本のコミュニティの違いについて。USのデータサイエンスイベントに参加したら3000人以上が参加していた。どうやったらそのような環境を日本でもつくれるでしょうか？

  * A: 日本とUSのPythonコミュニティの違いについて
  * A: 日本とUSのデータサイエンスコミュニティの違いについて
  * A: コミュニティ主導のカンファレンス
  * A: 商業ベースのカンファレンス

    * これはお金を産む
    * ブースを出すのにもお金が要る
    * お金が掛かっている分、大きくなる
    * 多くの人が訪れる

  * A: 日本のスタイルも良いと思う

    * （聞き取れず）

* Q SciPyがWindowsで使いづらいのが最後の問題だと思っている。なにかコミュニティ主導でできることはないだろうか？

  * A: 面白い話があるんだ。3年前、Pythonのパッケージングはひどい状況だった。Pythonはパワフルで拡張性があります。問題は、C,C++などで書かれた拡張をみんなが使える状態ではなっかったことです。どうやったらみんながバイナリパッケージを受け取れるだろうか。condaでバイナリパッケージを作ったとき、非常に多くのコーナーケースにつきあたった。2012年に解決に向けて取り組み始めた。...（聞き逃し）


* Q 例えば、condaがやっているように、pypiでも使えるようにならないでしょうか。condaからwheelへの変換といったようなことです。それが出来れば今よりもずっと使いやすくなるんじゃないかと思ってます。Pythonデータサイエンティストはみんなそれを待ち望んでいます。

  * A: （聞き取れず...）


メディア会議
====================

* 12:10-13:00
* https://pycon.jp/2017/ja/events/media-meeting/
* Togetter: https://togetter.com/li/1148594

.. figure:: media-meetup.*
   :width: 80%

   登壇されたみなさん（左から敬称略）高屋、緑川、大津、原（司会）、岩崎、杉谷

----------------

* 単著と共著

  * （司会）Amazonとかで出てくる著者名が1人だけの場合があるけど、あれはランダムとかジャンケンとかですか？

  * （緑川）一番えらいひとですよ

* 自己紹介

  * （緑川）翔泳社、岩崎さんの `スラスラわかるPython`_ の編集をやりました
  * （高屋）技術評論社、専門書をやってます
  * （大津）リブロワークス、編集して出版社までもっていく役割。 `いちばんやさしいPythonの教本`_ の編集をやりました
  * （岩崎） `スラスラわかるPython`_ 書きました。 今回PyCon JPのスポンサーもしているSQUEEZE所属です
  * （杉谷） `いちばんやさしいPythonの教本`_ 著者の1人、Webアプリケーション開発者。今日もスポンサーしているRetty所属です


* 売れる本、売れない本

  * （司会）売れなくても良い、ってことはないですよね
  * （司会）売れるっていうのは、どういう状態のことですか？印刷部数が最初ありますよね
  * （緑川）7割で黒字、9割で刷り直して増販。最初に刷ったものが売り切れたら売れたって言って良さそうだけど、最近はそんな本もあまり...
  * （司会）売れなかったらどうなりますか？
  * （高屋）次の本を書くしか無いですよね... 怒られたりはしないです

* 売れる本

  * （司会）入門書で一番売れてるPythonの本ってなんですか？
  * （緑川）技術評論社さんの `Pythonスタートブック`_ じゃないですかね..
  * （高屋）10万部は行ってない・・・かな
  * （司会）オライリーさんの `ゼロから作るDeep Learning`_ はどのくらいでしょう？
  * （緑川）表に出てる数字だと、5万部ですかね。そのくらいいくと家が建ちます

* 著者が増えた気がする

  * （司会）最近、技術書を書いたっていう人がすごい増えた気がします
  * （高屋）すごい増えました。発行部数は減りましたけど、初刷りがだいぶ増えましたね

* 著者は人生変わりましたか？

  * （司会）人生かわりましたか？
  * （岩崎）うーん、知り合いが「おめでとう」って声かけてくれるくらい・・？
  * （司会）お母さんや家族に伝えましたか？
  * （岩崎）達成感はありますね。本という形になるとわかりやすいので。
  * （司会）杉谷さんはどうですか？
  * （杉谷）初心者にコーチするときの表現が前に比べて大分変わりました。
  * （司会）Amazonに著者ページつくりました？
  * （岩崎）いつのまにかページできてました
  * （司会）SNSのマイページみたいに使えるので充実させておくと良いですよ

* 本を書くためにすること

  * （司会）参考にした本やWebサイトとかありますか？
  * （岩崎）初心者の方にどういう伝え方をすると分かりやすいか、メンバーで話し合ったりしました。そのあと、関連して参考になりそうな本を読みました。特に、Pythonの公式ドキュメントはたくさん読みました。
  * （杉谷）私は、結城先生が公開している「文章の書き方」 [#writing]_ というページを読んで、読点の付け方などに気をつけました。あとは、オライリーさんの `初めてのプログラミング 第2版`_ をけっこう参考にしました。図は少ないんですけど、文章でこれだけ表現できるんだな、と思って参考になりました。

* 本が店頭にならぶまで

  * （司会）大津さんに聞きたいことがあります。本ってどういう流れで店頭に並ぶのか教えてもらえますか？最初は何でしょう？

  * （大津）企画からですね。どういう本を作りたいか、そのあと誰に書いてもらうかという流れですかね。その後打ち合わせをして、構成案をつくって、良い感じになったらスタートします。そのあとはずっとマラソンですね。ある程度書き終わったら、途中で変換して本になったらこういう感じです、というのを著者さんに見せて、雰囲気を掴んでもらいます。そしてDTP（DeskTopPublishing）して、出版社さんと著者さんにお見せして、校正を繰り返して、印刷所に入ります。
  * （緑川）印刷所からあがったら、見本誌が届くので、取次さんに送って全国に届ける感じです。
  * （司会）企画書ってどんなものを作るんでしょうか
  * （大津）企画書は、どういう本か、誰に向けてか、というのを書きます。出版社さん向けにはあとは部数なども添えます。企画書に構成案（目次のようなもの）を作って添える感じです。

  * （司会）著者さんはどんな感じで進めましたか？
  * （岩崎）特別なツールは使わなかった感じです。Gitlabのプライベートリポジトリをつくってそこで共同作業をていきました。
  * （杉谷）ツールは、すばらしいツールを使わせてもらって、Markdownで書いてビューアーで見るとほとんど実際に印刷された本と同じように見えて、すごい分かりやすかったです。
  * （司会）なるほど、お二人ともMarkdownなんですね。ツールは誰が作られたんですか？
  * （大津）私が去年作りました。MarkdownからHTMLに変換したものを Vivliostyle_ さんの `CSS組版`_ と合わせて表示するツールです。いちばんやさしいシリーズはレイアウトと見せ方がすごい重要なので、そういうツールで著者さんにイメージを見てもらえるようにしました。

* 本のレイアウト

  * （司会）似顔絵とフキダシが特徴的でしたが、フキダシなんかはいつ入れていくんですか？
  * （大津）隙があればすかさず、ですね
  * （司会）EPUBのあるなしはどういう感じで決まるんでしょう？
  * （緑川）技術書で文字が多い場合はEPUBに比較的簡単にできるんですが、いちやさPythonのようにレイアウトが多いと難しくなっていきます

* 本のレビューについて

  * （司会）レビューはやりましたか？
  * （岩崎、杉谷）はい
  * （岩崎）本と同じレイアウトのPDFになったをDropboxに置いてDropboxでPDFにマーキングコメントできるので、それでレビューアーさんにガンガンコメントしてもらいました。
  * （岩崎）むしろレビュー段階になってからそのやり方をしました
  * （司会）編集者サイドでもDropboxのツールでコメントしたり校正したりしたんですか？
  * （緑川）そうですね、そうやったと思います
  * （司会）杉谷さんはどうでしたか？
  * （杉谷）外部のレビューアーさんというのは、いちやさPythonではやってなくて、社内の色んな人にコメントしてもらってやりました。

* blogと本の違い

  * （司会）blogと同じ感じで書いていったらいいんでしょうか？なにか違うんでしょうか？僕の場合、紙になる本なんて書けないよ、っていうようなハードルを感じたんですよ
  * （緑川）最初の原稿が来たときに時々言うことは「これはQiitaっぽいですよ」と言うことがあります
  * （司会）それはQiitaディス..?
  * （緑川）いやDisっていうことではないんですけど、紙の本は、前提の情報をしっかり伝えないといけないというのがあります。Blog, Qiita, Twitterとの違いはそこかなと思います。
 

* 出会いは？

  * （司会）どういうことがきっかけで本を書くことになったんですか？
  * （岩崎） `Python mini hack-a-thon`_ という勉強会というかコミュニティがあるんですが、そこで寺田さんに「ちょっと本書かない?」と引きずり込まれました。
  * （司会）杉谷さんはどうですか？
  * （杉谷）最初に別の社員に連絡が来て、それを会社でやることになったので、私は仕事でアサインされて書いた感じです。
  * （司会）あ、じゃあそれは仕事の時間で書いたんですね。岩崎さんはプライベート時間ですか？
  * （岩崎）そうです。プライベートです。コワーキングスペースにこもって書き続ける、というのを3,4ヶ月やりました。
  * （司会）なるほど、それはプライベート時間を印税に変えたという感じですね。そうなると疑問なのは、杉谷さんは仕事の時間で書いてその時間お賃金が入って、もしかして印税も・・・？
  * （杉谷）いえ、印税は入りません。お給料だけです。
  * （司会）そういう会社で本を書くというのは珍しい気がするんですけど、そういうのってけっこうあるものなんですか？
  * （??）けっこうありますね。会社組織で書いてくれれば、万一の場合もなんとかしてくれるというのはありますね。

* 企画の作り方

  * （司会）企画になんでも持っていけば良いわけじゃないですよね。Python本でどんな企画を出したら通るんでしょう？
  * （緑川）技評さんでJupyter本を出す [#jupyter-book]_ って聞いて、えっそれ出すんだ、Jupyterで400ページも何を書くんだろう？というのがあって、内容期待してます。

  * （司会）事前に質問を集めておいたんですけど、次に書きたい本などありますか？
  * （岩崎）PythonとWeb全般みたいなのがあれば書きたいなと思ってます
  * （緑川）お待ちしてます
  * （杉谷）私はそうですね、PythonistaっていうGUIアプリの作り方の本がれば自分が読みたいので、書きたいなって思います。

* 会場から質問

  * （参加者1）技術書の場合、翻訳本とかありますが、翻訳本とイチから書く本のメリットデメリットなどあれば教えてください
  * （高屋）メリットは構成が決まっている。デメリットは、バージョンが変わってたりするので著者に確認が必要だったりします。
  * （緑川）アメリカと日本で状況が全然違うというものもあったりします。例えば、まずガレージを用意して次に3Dプリンタを用意しましょう、という内容だと、日本だと無理！ってなったりします。
  * （司会）翻訳本ってどこまで変更していいものなんでしょう？
  * （緑川）原著者によります。厳しい人だと、本のPDFくださいチェックします、という人もいます。

  * （参加者2）最近だと技術書展なんかありますが、同人誌みたいな感じで技術書を出すというのも一般化してきている気がします。そういうのって出版社から見てどういう感じなんでしょう？
  * （緑川）我々もプロとしてしっかりやっていきたいと思うし、そこは敵とかじゃなくて、技術が盛り上がるのは良いことだなーと思います。
  * （参加者2）同人誌から始まって出版という流れもあったりするんでしょうか？
  * （高屋、緑川）あります。実例もありますし。良いことだと思います。歓迎します

  * （司会）出版的には、Amazon Publishingやコミケといったあたり、どのへんが脅威だと思ってますか？
  * （緑川）USで公開されている英語の本を日本語でボランティアで和訳して公開！っていうのが怖いですかね・・
  * （高屋）あんまり脅威だと思っているものは無くて、体系的に学びたい方には書籍の立ち位置というのが良いかなと思います

  * （参加者3）Pythonの本を本をこの出版社から始めようと思うきっかけってなんでしょう？
  * （緑川）翔泳社の一番最初のPython本は寺田さんが関わられた `10日でおぼえる Python 入門教室`_ という本で、編集者の勢いで決まった感じです。これからPythonくるぞ！という

* まとめ

  * （司会者）本を書いたことがない、書く予定がない人に向けてメッセージなどください。こういう世界が待ってるよ、とか、苦労の割に良いこと無いぞ、とか
  * （岩崎）技術書を書くというのはblogを書いたりするのとはだいぶ違うんですけど、自分が持っている知見をアウトプットする手段の1つかなと思います。やってみると面白いと思います。だれでも出来るわけでは無いし、けっこう長い時間掛ける必要があります。
  * （杉谷）本を書くのは大変。初心者向けといえど、普段自分が意識しないことを調べて書いていくのは技術力が上がります。人に伝えるというのは仕事をする上でも重要な能力で、そこも鍛えられます。本はblogとちがって色んな人に校正されるしバシバシ叩かれるし、想定してない人達の目に触れることになるので、機会があればぜひやってみると良いと思います。

  * （司会者）14:35から17時まで、1Fでこのメディア会議に登壇した出版社さんとミートアップというのをやるので、握手したい、名刺交換したい、だけでも良いので来て下さい。

  * （司会者）言い残したことなどありますか？
  * （緑川）そろそろ来期に向けて企画をたくさんだしていかないといけない時期なので、みなさんのご協力などもらえるととても嬉しいです


（司会）以上で終わりになります。みなさんありがとうございました。

.. _初めてのプログラミング 第2版: http://amzn.to/2j8lQ7c
.. _ゼロから作るDeep Learning: http://amzn.to/2eLnu9Y
.. _Pythonスタートブック: http://amzn.to/2wNlgS9
.. _スラスラわかるPython: http://amzn.to/2jbiHUu
.. _10日でおぼえる Python 入門教室: http://amzn.to/2jaH7NP
.. _いちばんやさしいPythonの教本: http://amzn.to/2eLfuFT
.. _文章を書く心がけ: http://www.hyuki.com/writing/writing.html
.. _Vivliostyle: http://vivliostyle.com/ja/
.. _CSS組版: http://vivliostyle.com/presen/presen20150829/vivliostyle-dtp.html
.. _Python mini hack-a-thon: https://pyhack.connpass.com/
.. _PythonユーザのためのJupyter[実践]入門: http://amzn.to/2wNlGId

.. [#writing] `文章を書く心がけ`_ かな？
.. [#jupyter-book] `PythonユーザのためのJupyter[実践]入門`_


ランチ
===========

メディア会議を全力でメモってたら疲弊しました・・。ご飯食べて体力回復

.. figure:: lunch-halal.*
   :width: 70%

   ハラルの海南鶏飯

トーク: len()関数がオブジェクトの長さを手にいれる仕組み
==========================================================

* 英語タイトル: How does python get length with the len() function?
* 14:05～ #pyconjp_203
* Togetter: https://togetter.com/li/1148634
* 発表資料 https://goo.gl/8R6Bn2
* アジェンダ: https://pycon.jp/2017/ja/schedule/presentation/22/
* 動画: https://www.youtube.com/watch?v=aich6wqftkA

自分の発表です。

よろしくおねがいします！

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pyconjp?src=hash">#pyconjp</a> <a href="https://twitter.com/hashtag/pyconjp_203?src=hash">#pyconjp_203</a> 発表を聞きに来てくれたみなさんです。ありがとー <a href="https://t.co/WuZomOEzIR">pic.twitter.com/WuZomOEzIR</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906020640284540929">2017年9月8日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

.. raw:: html

   <iframe src="//www.slideshare.net/slideshow/embed_code/key/aM9Yf35L5nu2e1" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/shimizukawa/how-does-python-get-the-length-with-the-len-function" title="Pythonはどうやってlen関数で長さを手にいれているの？" target="_blank">Pythonはどうやってlen関数で長さを手にいれているの？</a> </strong> from <strong><a href="https://www.slideshare.net/shimizukawa" target="_blank">Takayuki Shimizukawa</a></strong> </div>

.. figure:: shimizukawa-and-atendees.*
   :width: 80%

   参加されたみなさん（150人くらい？）

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">おかげさまで、「len()の仕組み」トーク、無事おわりました！参加されたみなさん、ありがとうございました！！！ <a href="https://twitter.com/hashtag/pyconjp?src=hash">#pyconjp</a> <a href="https://twitter.com/hashtag/pyconjp_203?src=hash">#pyconjp_203</a><a href="https://t.co/4R97XhXkQO">https://t.co/4R97XhXkQO</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906033954070839297">2017年9月8日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

ありがとうございました～～！


食堂でのんびり書籍出版の話
=================================

食堂でやっていた「出版社さんとミートアップ」を聞いたり、  `@igaiga555`_ さんと入門向けの本をどの辺狙って書いたら良い本になるか、みたいな話をしてました。

`いちばんやさしいPythonの教本`_ を `@igaiga555`_ に紹介したらえらく気に入ってくれて、編集の大津さんと三人で1時間くらい話し込んでました。

.. _@igaiga555: https://twitter.com/igaiga555


クロージング
===================

LT
------

- LT楽しかった！
- `@yotchang4s`_ のJavaでPython実装系作った、っていう話、もうちょっと「ザワッ」とするかと思ったけど、反応薄かったね。なかなか反応引き出すのはなかなか難しいね(´･ω･\`)
- 司会者の繋ぎがうまい！しっかりスピーカーを見ながらどうでもいい短いトークで会場を沸かせてた。

.. _@yotchang4s: https://twitter.com/yotchang4s

スポンサーLT
-------------------

- お、初の試み？と思ったら時間配分ミスで今日のクロージングでやることになったらしい。そういう企画だって言えば良いのにーｗ
- `モノタロウ`_ さん、東京オフィス用意するらしい。チャレンジングな人を募集！
- モノタロウさんのLT最後にLINEスタンプ紹介して、次がLINEさんのトークっていうナイスな繋がり
- Retty_ さん、 iRidge_ さんのスポンサーLT


.. _モノタロウ: https://www.monotaro.com/
.. _LINE: https://linecorp.com/ja/
.. _Retty: https://retty.me/
.. _iRidge: https://iridge.jp/


挨拶、他
-----------

.. figure:: closing-staff.*
   :width: 80%

   PyCon JP 2017 を創ったスタッフのみなさん

座長挨拶

* 「今日だけで500人以上の参加者が来場」ほう。けっこう来たなー
* 「この後パーティーも楽しんでくださ」あっ、終わった。短い！

忘れ物

* ノベルティ、iPhoneのイヤフォン、マーキーペン、100円
* 拍手でたｗ

スピーカーTシャツ

* 「手違いでTシャツを配れていない人が。受付に来て下さい」あらあら..

明日の企画

* `キーノートは堀越真映さん`_ です
* 3Fで `オープンスペース`_ やります。1Fのホワイトボードにサインアップしてください
* `ポスターセッション`_ は1Fで行います
* `Youth Coder Workshop`_ もやります
* 明日もLTやります。1Fのホワイトボードにサインアップしてください
* ベストトークアワードをやります。1票よろしくおねがいします

.. _オープンスペース: https://pycon.jp/2017/ja/events/openspace/
.. _キーノートは堀越真映さん: https://pycon.jp/2017/ja/talks/keynote/
.. _ポスターセッション: https://pycon.jp/2017/ja/schedule/posters/list/
.. _Youth Coder Workshop: https://pycon.jp/2017/ja/events/youth-ws/


Party
===========

今日は全体パーティー！

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">今日は <a href="https://twitter.com/hashtag/pyconjp?src=hash">#pyconjp</a> partyで <a href="https://twitter.com/chezou">@chezou</a> <a href="https://twitter.com/tokuhirom">@tokuhirom</a> に挨拶をキメた！繋いでくれた <a href="https://twitter.com/turky">@turky</a> に感謝～！</p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906159828715814912">2017年9月8日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

.. figure:: party-foods.*
   :width: 50%

   自分の好きそうな料理が多い！串！肉！辛！

.. figure:: party-sake.*
   :width: 50%

   日本酒の生酒が10本！

.. figure:: party-sake.*
   :width: 50%

   日本酒の生酒が10本！

.. figure:: party-sake2.*
   :width: 50%

   琵琶のささ浪、酸味強めで美味しかった！

Party2
========

Python Start Club の人達に混ざって2次会に参加しました

.. figure:: party-chikin.*
   :width: 50%

   鶏の唐揚げ


疲労のため途中で帰りましたが、楽しかったです。お疲れ様でした！


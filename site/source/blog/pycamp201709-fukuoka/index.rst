:date: 2017-09-30 23:55
:tags: Python, PyCon, PyCon JP, PyCamp

==================================================
Python Boot Camp in 福岡で講師してきました #pycamp
==================================================

`Python Boot Camp in 福岡`_ に行ってきました。 :doc:`神戸 <../pycamp201705-kobe/index>` 以来、2回目の講師です。
福岡は参加申込みペースが早かったという話を聞きました。参加者30数名、TA・スタッフ・講師9名、合計40名くらいが参加しました。

.. figure:: attendees.*
   :width: 80%

   参加者のみなさん（開始時）

このblogは講師からみた参加レポートです。チュートリアル本体の様子なんかは、公式の開催レポートは別途書かれると思います。

.. note::

   "Python Boot Camp" は、 `一般社団法人PyCon JP`_ が日本各地で開催している、 **初心者向けPythonチュートリアルイベント** です。
   今回の福岡で `12回目`_ の開催です。
   `チュートリアルのテキスト`_ は公開されていて、ライセンスに従って自由に利用できます。詳しくは `Python Boot Camp について`_ を参照してください。

   現地スタッフになってくれる人がいれば、講師に行きますので、 `申込みフォーム`_ からひご連絡ください！


移動
=====

朝、十分余裕を持って空港につける予定が、チェックイン時刻を微妙に過ぎてしまい、8:20発の飛行機に乗れず！！やばい。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">8:20発の飛行機に間に合わなかった…! 「20分前までにチェックインでOK」は「18分前だとNG」なんだ！！（そして振替の9:15発が55分遅れてる (@ 東京国際空港 / 羽田空港) <a href="https://t.co/WNTdIQykIh">https://t.co/WNTdIQykIh</a> <a href="https://t.co/PesGBvOe8k">pic.twitter.com/PesGBvOe8k</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/913929860527136768?ref_src=twsrc%5Etfw">2017年9月30日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

なんとか次の次の便(9:15発)に振り替えてもらったものの、その便が55分遅れ。結局、福岡空港には12時前くらいに着陸し、会場には12:40頃に到着しました。ギリギリセーフ... 本当にあせった。会場についた時点で、今日の仕事をやりきった感じでしたが、気を取り直して本番へ。

ところで、今回使ったJALは、飛行中のWiFiが無料提供されていたので、非常に助かりました。通信はhttp(s)のみ、ということもなく、ssh経由のgithub pushができたので（！）、某エキPy2本の翻訳作業をガシガシと進めてました。
ちょっと前まで、電波Offどころか電源Offがあたりまえな時期がずっと続いてたことを考えると、空の上でももう不自由ないですね。pingを飛ばせる幸せ。ほんと、すばらしい。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">神戸を過ぎました。福岡着陸は33分後らしい <a href="https://t.co/FJHoPKdjKv">pic.twitter.com/FJHoPKdjKv</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/913949223502077953?ref_src=twsrc%5Etfw">2017年9月30日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


スタッフミーティング
=====================

私は諸般の事情で欠席。すみません、ほんと、すみません。


Python Boot Camp 本編
========================

13時開始。体調不良などで3名欠席があったみたい。それでも参加者数は30名くらい。多いなー。

自己紹介もそこそこに、さっそく講義を開始しました。所属とかPyCon JPの活動とか PyQ.jp の宣伝とかしなかった気もするので、あとで参加者向けSlackに流しておこう。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pycamp?src=hash&amp;ref_src=twsrc%5Etfw">#pycamp</a> おやつタイム！！ Pyの実が！！ (@ Nulab Inc. - <a href="https://twitter.com/nulabjp?ref_src=twsrc%5Etfw">@nulabjp</a> in Fukuoka, 福岡県) <a href="https://t.co/wfIHuKV8c3">https://t.co/wfIHuKV8c3</a> <a href="https://t.co/xrOuFGvG9I">pic.twitter.com/xrOuFGvG9I</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/914013265688178689?ref_src=twsrc%5Etfw">2017年9月30日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

イベント自体は、進捗が少しずつ遅れながら進みました。4時間のイベントだとテキストをこなすのがなかなか厳しい、というのが前回の :doc:`神戸 <../pycamp201705-kobe/index>` と同様でした。教え方のスタイルとして、手を動かしてもらいながら進めるというのをやってることもあり、どうしても時間が厳しいですね。結局、終了時刻の17時を少しオーバーしました。7章のスクレイピングは今回もスキップ。

イベントの開始時に http://pyconjp-fellow.herokuapp.com/ からSlackに参加してもらって、チャットで質問を書いてもらいました。講義中も質問を見ながら、あとで回答したり、他の参加者やTAが答えてくれたり、テキストが進んだときに回答になるような説明を含めたり、と言った調整ができるし、チャットに質問内容が残って後で読み返せるし、ということで、とても良い方法なんじゃないかなーと思ってます。Slack慣れてない人にはハードルがちょっと高いと思うので、当日じゃなくもうちょっと前に参加してもらうと良いかも。

.. figure:: pycamp-slack-chat.*

   Slackチャットでの質問の様子


次は、 `11/4(土) 鹿児島`_, `11/18(土) 静岡`_ で講師してくるので、チャット工夫してみようかな。

.. _11/4(土) 鹿児島: https://pyconjp.connpass.com/event/67709/
.. _11/18(土) 静岡: https://pyconjp.connpass.com/event/67533/

雑感
------

講師をしていると、参加者の力量に合わせた講義をしたいところだけど、時間の都合もあり、ここまではちゃんと伝えたいっていうのもあり、なかなか難しいですね。

力量を測るのが難しいところの一つに、分かった人は質問してこないし、分からない人は質問以前の状態にあって質問できない、というのがありそう。pip installコマンドやvenvの話で、だれも「うまくいかない」という反応がなかったけど、本当に大丈夫だったかなー？各人の画面を後ろから覗き込んで確認していくしかないのかなと思う（仕事の講師では4倍くらい時間取ってるのでやれてるけど..）。

参加者の個別フォローはTA（ティーチングアシスタント）のみなさんがやってくれたので、自分はチャットでのフォローと講義で伝える方に集中できました。みなさん、ありがとうございます！後で聞いたら、TAじゃっかん余裕だったっぽいので、みなさん、もっとTAに質問してくれていいのよ。


チャットメモ
-----------------

（ちょっと加工してあります）:

* ``8/2`` ってなんで小数点に？
* ちなみに数値を ``50_000`` みたいに(数値の中に `_` を入れられるように)なったのはPython 3.6からです
* “繰返し可能な型” の意味がはっきりわかりません。順序があるのはわかりました。
* Windowsのメモ帳ではまるポイントってなんですか？

  * （清水川）一般的に日本語を含むテキストファイルは、 ``UTF-8`` で保存してほしいんですが、Windowsのメモ帳の場合 ``UTF-8`` を選ぶと ``BOM付き UTF-8`` というものになります。BOM付きだとうまく動作しないツールなどがあって、原因特定しづらくて面倒なんですよ
  * python に限らず win でプログラミングする場合は文字コード周りには注意が必要ですね。

* pythonって一つの文を複数行で書くことはできますか?下みたいな感じで::

    if num % 3 == 0 and
       num % 5 == 0:

* 関数の終わりに ``end`` が無いのはまだ慣れないですね

  * （清水川）他の多くの言語では、ブロックの開始終了マーカーありますからねー

* Pythonのインデント幅は基本スペース4つ分なのでしょうか?

  * （清水川）基本はそうです
  * 了解です ありがとうございます〜
  * （清水川）Googleはむかしスペース2つでしたが、今は4つのルールを採用してますねー

* '(シングルクオート)と"(ダブルクオート)ってどちらを主に使った方がいいのでしょうか？

  * （清水川）どちらでもよいです、意味に違いはありません。シングルを推奨する人が多い気もしますね（私は混在してても気にしないです）

* Fizzbuzz関数難しいから、fizz関数とbuzz関数から始めました。
* 文字列に対して、メソッドで提供されているものと関数で提供されているものがありますが、そこにルールはあったりしますか？

  * （清水川）オブジェクト特有のものはメソッド、さまざまなオブジェクトに適用できるものは関数、と説明したいところですが、歴史的経緯もあります。ちょうど先日PyCon JPで発表したスライドがあるので、参考にしてみてください https://www.slideshare.net/shimizukawa/how-does-python-get-the-length-with-the-len-function

* そういえば、、3.4.7.の ``in`` って、関数でもメソッドでもなく何者なんでしょう？

  * （清水川）構文です。実際には  `obj1 in obj2` と書くと、  `obj2.__contains__(obj1)` が実行されます。
  * あー、listにも使えたりするんですね。
  * 主にif文で使うようなものだから読みやすいようにこのような構文を用意している、という感じでしょうか？
  * （清水川）構文が先(Python 1.x)にあって、 `obj2.__contains__(obj1)` というオブジェクト指向的な実装が後(Python2.x)で追加されました

* dictはrubyで言うhashにあたるものですか?

  * （清水川）はい

* タプルだけがイミュータブルな値なんですか？ ~~Pythonには定数というものがなさそうなんですが、定数が欲しいPythonプログラマの方はタプルを利用したりする習慣があったりしますか？~~

  * （清水川）文字列と数値もイミュータブルです。定数のためにタプルを使うという習慣はないですね。固定長の変化しないシーケンスとしてタプルを使うことはあります。

* タプルの中にリストを入れるとリスト部分は可変なんですね。::

    >>> a = ([1,2],3,4)
    >>> a
    ([1, 2], 3, 4)
    >>> a[0][0] = 5
    >>> a
    ([5, 2], 3, 4)


* ::


    >>>user_info = {'user_name': 'taro', 'last_name':'Yamada'}
    >>> user_info{'user_name'}
     File "<stdin>", line 1
        user_info{'user_name'}
                 ^
    SyntaxError: invalid syntax

  どうしてなんでしょう？


  * ``user_info['user_name']`` でアクセスするとイケルと思います
  * 辞書型でも、アクセスする時は角カッコ ``[ ]`` です！
  * （清水川） そうなんですよねー。値の初期化のときに使っている記号(``{}`` や ``[]`` や ``()`` )と、その変数の要素にアクセスするときの記号を合わせる、という意味ではないんです。要素にアクセスするときは、それがリストでもタプルでも辞書でも、 ``[]`` 角カッコです。

* dictは順序を持たないということですが、forとかで全部出力した際、登録した順では表示されないということでしょうか？

  * ならないですねー 一応こんなのも有るみたいです。(使ったことない) https://docs.python.jp/3/library/collections.html#collections.OrderedDict
  * http://methane.hatenablog.jp/entry/2016-09-12/Python3.6b1 shimizukawaさんの今はなしてる話はこれがベースです{advanced}


* リスト内包表記でタプルを生成しようとしたらできませんでした。::

    >>>animals
    ['cat', 'dog', 'snake']
    >>> [len(animal) for animal in animals]
    [3, 3, 5]
    >>> (len(animal) for animal in animals)
    <generator object <genexpr> at 0x10185cfc0>

  * （清水川）タプルは内包表記で生成できないんです。ジェネレーター内包表記というものになってしまいます。


* readで開いたファイルをread()したあと、もう一度最初から読みたいと思ったときにrewind()とかないんでしょうか？

  * （清水川） ``f.seek(0)`` でファイルの読み取り位置を先頭に移動できます。その後でもう一度 ``f.read()`` すれば読めます。とはいえ、何度もファイルから読み取るのはあまりやらず、最初の ``f.read()`` で変数に代入しておいてそれを使う方が一般的ですね。

* pyenv(pythonのバージョン管理) + venv っていう開発環境の構成は良さそうですか? (edited)

  * （清水川）pyenvが環境を作る機能を持っているので、pyenvを使うのであれば、わざわざそのなかでvenvを使わずに、pyenvの機能でやった方がよさそうです。

* ベンブって読んでた。。。

  * 僕もそうでした。。

* RubyのBundlerみたいなツールはありますか?

  * （清水川） pipenv というものが推奨になるかもしれない、という話があります。
  * https://github.com/kennethreitz/pipenv

* pip listで以下エラーが出ます。::

    DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.

  * （清水川） これはエラーではなく、DEPRECATION WARNINGというものです。「今後仕様が変わるよ、pip.confにこう書いておけばこの警告は表示されなくなるよ」と書いてあります。とりあえず無視して大丈夫です。 pip.confの置き場所がOS毎に異なるので、昨日は設定方法などを伝えませんでしたが、 https://pip.pypa.io/en/stable/user_guide/#config-file に置き場所について書いてあります（とっても分かりづらいけど）



懇親会！
=============

24人で懇親会へ！

楽天地というお店でモツコース。というかお通しの他はモツ鍋しかない！博多すごい！！

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pycamp?src=hash&amp;ref_src=twsrc%5Etfw">#pycamp</a> 懇親会～ モツ鍋～ (@ 楽天地 福岡天神西通り店 in 福岡市中央区, 福岡県) <a href="https://t.co/SZsrGcllnU">https://t.co/SZsrGcllnU</a> <a href="https://t.co/ZzAUiO2oMs">pic.twitter.com/ZzAUiO2oMs</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/914053455949570048?ref_src=twsrc%5Etfw">2017年9月30日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

色んな話が出来て楽しかった。全員とは話せなかったけど、普段なにをしているとか、Pythonを勉強しはじめたのはなぜか、といった話が多かったと思う。特に、最近機械学習を取り込むためにPythonを勉強し始めた、というJava,PHP,Ruby,Perlの人が多かったイメージ。


懇親会2
----------

クラフトビール好き、っていう話をしたら連れてってもらった。

.. figure:: pub.*
   :width: 80%

   `クラフトビール 福岡 GASTRO PUB ALES エールズ`_

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pyhack?src=hash&amp;ref_src=twsrc%5Etfw">#pyhack</a> 志賀高原ビール Hervest Brew 生ホップ収穫仕込みDPA!! (@ GASTRO PUB <a href="https://twitter.com/ALES_maizuru?ref_src=twsrc%5Etfw">@ALES_maizuru</a> in 福岡市, 福岡県) <a href="https://t.co/691J1k64fr">https://t.co/691J1k64fr</a> <a href="https://t.co/pjsiy7Ht3B">pic.twitter.com/pjsiy7Ht3B</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/914092642455183361?ref_src=twsrc%5Etfw">2017年9月30日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pycamp?src=hash&amp;ref_src=twsrc%5Etfw">#pycamp</a> よなよなリアルエール!! (@ GASTRO PUB <a href="https://twitter.com/ALES_maizuru?ref_src=twsrc%5Etfw">@ALES_maizuru</a> in 福岡市, 福岡県) <a href="https://t.co/s8bSKmoofr">https://t.co/s8bSKmoofr</a> <a href="https://t.co/4qfhfahEvD">pic.twitter.com/4qfhfahEvD</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/914104360434532352?ref_src=twsrc%5Etfw">2017年9月30日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

おまけ
-------

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">なんかでかい川 (@ 西中洲公園 in 福岡市, 福岡県) <a href="https://t.co/1jGnIR3BHW">https://t.co/1jGnIR3BHW</a> <a href="https://t.co/RDDEKNqaFi">pic.twitter.com/RDDEKNqaFi</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/914131718302568453?ref_src=twsrc%5Etfw">2017年9月30日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">屋台～ (@ 中洲 in 福岡市, 福岡県) <a href="https://t.co/U0lt1iLvmc">https://t.co/U0lt1iLvmc</a> <a href="https://t.co/VIxl6KDqN1">pic.twitter.com/VIxl6KDqN1</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/914132028945256450?ref_src=twsrc%5Etfw">2017年9月30日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


.. _12回目: https://www.pycon.jp/support/bootcamp.html#id5
.. _Python Boot Camp in 福岡: https://pyconjp.connpass.com/event/62769/
.. _Python Boot Camp in 福岡 懇親会: https://pyconjp.connpass.com/event/62770/
.. _一般社団法人PyCon JP: http://www.pycon.jp/
.. _チュートリアルのテキスト: http://pycamp.pycon.jp/
.. _Python Boot Camp について: http://pycamp.pycon.jp/organize/0_about.html
.. _申込みフォーム: https://docs.google.com/forms/d/e/1FAIpQLSedZskvqmwH_cvwOZecI10PA3KX5d-Ui-74aZro_cvCcTZLMw/viewform

.. _クラフトビール 福岡 GASTRO PUB ALES エールズ: http://alescook.blog.fc2.com/

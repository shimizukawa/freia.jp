:date: 2017-09-09 11:00
:tags: Python, PyConJP, Conference

=====================================
PyCon JP 2017 2日目 参加ログ #pyconjp
=====================================

`#PyConJP`_ 2017 in Tokyo に参加しました。:doc:`../pyconjp2017-day7/index` に引き続きの参加です。

今日は名札あれば受付不要なので直接キーノート会場へ。

今日は開始5分前に着席して、時間ちょうどにキーノート始まった！よかったよかった


.. _PyCon JP 2017: https://pyconjp.connpass.com/event/59412/
.. _#pyconjp: https://twitter.com/search?f=tweets&vertical=default&q=%23pyconjp&src=typd

.. contents::
   :local:

キーノート
===========

* 堀越 真映 (`@sinhrks`_)
* https://pycon.jp/2017/ja/talks/keynote/
* 動画: https://www.youtube.com/watch?v=1Cb3OQTmeD4

.. _@sinhrks: https://twitter.com/sinhrks

400人くらい会場に来てるかな？

.. figure:: keynote.*
   :width: 80%

   キャー 堀越さーん！

メモ
-------

会場に質問

* Q. 自分はPyData系だと思う方 -> 3割くらい
* Q. Pandas知ってる方 -> 6～7割くらい

抜粋

* Pandasは、データ仕様が与えられない場合の、試行錯誤のためのツール
* 2012年に初Issue、2014年に活動開始、2015年にコアチーム加入
* 最近は 1 Pull Request, 1 commit 運用を徹底している （俺：Sphinxもその方がいいかもなあ）

  .. raw:: html

     <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">numpyもそういう運用だとiwiwiさんが言っていた気がします。git bisectしやすいからとか</p>&mdash; chezou (@chezou) <a href="https://twitter.com/chezou/status/906324595577253888">2017年9月9日</a></blockquote>
     <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

* コミッターに期待することを明記している -> `Code Of Conduct`_ （俺：あーこれはマネしようかな）
* 後方互換性: 良くないAPIなどをdeprecationして2バージョン維持 （俺：これはSphinxもやってるね。元ネタはDjango）
* `Pythonによるデータ分析入門`_ -> 10月に改訂版が！
* Issueテンプレートを使って報告しやすいように整備 （俺：Sphinxもやってるー。報告の質が格段にアップしたよ）
* 団体企業からの支援 （俺：何に使ってるのか聞き逃した）
* OSS活動ってやる必要あるんだっけ？

  * -> 承認欲求を満たせる （俺：うん）
  * -> 有識者のレビューを受けてスキルアップできる （俺：うんうん）
  * -> 内部実装が理解でき（使う側としても）効率的なコードが書ける （俺：わかる）
  * -> 修正を取り込んでもらえると、使う時のhackkyな書き方が不要になる （俺：超わかる）

* PRを出してみようと思ったら

  * 大きめのプロダクトならIssueがタグで整理されている
  * 難易度タグが付いてるので簡単なやつから手を付けてみる
  * 他の人が手を付けているものは避けた方がよいかも

  .. figure:: pandas-issue-tags.*
     :target: https://github.com/pandas-dev/pandas/issues

     pandas-dev の難易度タグ

* プルリクエストでバグ修正した場合

  * 意図が伝わらなければコードを書く
  * 影響範囲が大きい場合ひたすらテストを足す

* 気をつけていること

  * 局所的な修正を避ける
  * テストをちゃんと書く
  * ドキュメントをできるだけ書く


.. _Code Of Conduct: https://github.com/pandas-dev/pandas-governance/blob/master/code-of-conduct.md
.. _Pythonによるデータ分析入門: http://amzn.to/2xbVLtr

Q&A
--------

* Q: 投げられるIssue/PRが大量に来ると思いますが、どうやってさばいてますか？

  - A: 気づいた人がやる。活動量が多い人がレビューしてくれたりします。

  - Q: 自分の機能に責任を持って対応してる感じですか？

  - A: リリースマネージャーみたいな人がいて、その人は全てのIssueを見たり返事したりしてます

* Q: `@nobolis_`_ : 仕事とプライベートの時間の使い分けをどうされてますか？

  - A: 業務上はOSS活動するために雇われていないので、基本的に個人で活動してます。そういう活動も評価されているので業務上無駄になってたりはしません

* Q: `@shimizukawa`_: SphinxのIssueは今600ちょっとあります。PandasのIssueを見てみたら2000を超えていて、それってIssueが右肩上がりになっていくと思うんですが、そういうときに、どうやって気持ちを維持していくのか、お聞かせ下さい

  - A: コアコミッターはPRのレビューなどで忙しくて自分でパッチを書く時間が取れない事が多いです。なので、自分で全部直すのではなく、自分たち以外の人でも直せるような体制をつくっていく。簡単そうなissuesだったらやり方を提案して報告者にやってみてもらうとか。そうやって直せる人を増やしていってます。

* Q: ドキュメントだけで1000ページ以上ありますよね。そういう巨大なOSSを維持していくのは専門家じゃないともうできないものなのでは？

  - A: Yes & No. ドキュメントを見る専任者みたいな人がいます（Anacondaや2sigmaの人）。ただ、専任者がいないとできないわけじゃなくて、居ないなら居ないなりのやり方があると思ってます。


* Q: 西本: 局所的な修正よりも大局的に直す、という話をもうすこし詳しく聞かせて下さい

  - A: 欠損値のバグをある関数でだけ直しても、欠損値の扱いはそこだけじゃなく、もっと深いところで問題があって他の関数にも影響がある

  - Q: その意図は凄くよく分かるんですが、Pandasのような巨大なプロダクトだと影響の広いコードを直すのはすごい影響ありそうで、そこで議論が紛糾したりしませんか？

  - A: 2つ話があります。開発者側としてはあまり議論にならなくて、全体的に直した方が良いと判断する。慣れていない人が直す場合、全体的な視点は持っていないこともあるので、そこは慣れている人がアドバイスしたりします。

* Q: ベンチマーク比較するツールの紹介(`airspeed velocity(asv)`_)がありましたが、そのツールはPythonでしか使えないものですか？

  - A: 基本的にはPythonでスクリプトを書くので、Pythonの方が便利に使えますが、他でも使えるとは思います。

* Q: OSSへのコントリビュートをし続けるってすごい難しいことだと思うんですが、1年継続していくのに工夫したことはありますか？

  - A: 自分のスキルアップのためにPandasにターゲットを絞って活動をしていました。Issueを眺めて自分で直せそうな部分があったら自分でやってみるというのを続けました。

.. _`@nobolis_`: https://twitter.com/nobolis_
.. _@shimizukawa: https://twitter.com/shimizukawa
.. _airspeed velocity(asv): http://asv.readthedocs.io/en/latest/

Pythonで実現する4コマ漫画の分析・評論 2017
===============================================

* SHINJI KITAGAWA (`@esuji`_)
* https://pycon.jp/2017/ja/schedule/presentation/27/
* 動画: https://www.youtube.com/watch?v=S70KqdRYJzo

.. _@esuji: https://twitter.com/esuji

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">BPPRです。<a href="https://twitter.com/hashtag/pyconjp?src=hash">#pyconjp</a> <a href="https://twitter.com/hashtag/pyconjp_201?src=hash">#pyconjp_201</a> <a href="https://t.co/Co5VEQNeug">pic.twitter.com/Co5VEQNeug</a></p>&mdash; 佐藤治夫 (@haru860) <a href="https://twitter.com/haru860/status/906335711355211776">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">BPPR: 弊社 <a href="https://twitter.com/hashtag/BeProud?src=hash">#BeProud</a> の制度。カンファレンスで会社紹介すると代休もらえて参加費が出る(要約) <a href="https://twitter.com/hashtag/PyConJP?src=hash">#PyConJP</a><a href="https://t.co/2331mVAAdr">https://t.co/2331mVAAdr</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906337449248354304">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


* 情熱駆動開発
* 自分が欲しいものをだれかが作ってくれる、ということはない
* Pythonならライブラリたくさんあるからなんとかなるかな、と思った
* **情熱があれば作れる**

Q&Aは時間切れで個別。「11:30からOpen Spaceでやります」

Open Space でProtocol話
===========================

昨日の私の資料を肴に、4人くらいでプロトコルについて話してました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">11:30 からオープンスペース3F room F で、Pythonのプロトコルのやつやりまーす！ 場所分かりづらいけど、3階で看板探して来てくださーい <a href="https://twitter.com/hashtag/pyconjp?src=hash">#pyconjp</a> <a href="https://t.co/OQUBqBNK7y">pic.twitter.com/OQUBqBNK7y</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906345492962877440">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pyconjp?src=hash">#pyconjp</a> オープンスペースでlen()の話やってまーす。今は__str__と__repr__とprint()の話 <a href="https://t.co/d4J8tMwPlo">pic.twitter.com/d4J8tMwPlo</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906349253152301056">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

* ``print(obj)`` もAdapter?

  * それは単に関数
  * printの中では、文字列の表示用に ``str(obj)`` するけど、これはAdapterと言って良さそう
  * ``str(obj)`` は ``obj.__str__`` を呼び出す。もしなければ ``obj.__repr__()`` にフォールバックする
  * ``obj.__repr__()`` はオブジェクトのrepresentationで、対話シェルに値を表示するために ``repr(obj)`` したときに呼ばれる。これはAdapter

* Swiftには適合(adopt)というのがある

  * ``CustomStringConvertible`` を適合(adopt)させると、 ``description`` プロパティの実装を強制されて、これで ``obj.__str__`` 相当のことをやる
  * Pythonだと ``abc`` で抽象仮想クラスを継承するような感じだね。Pythonだと適合みたいな文法はないけど、継承で実現する
  * PythonってTraitsないの？ -> 継承で
  * PythonってMixInないの？ -> 継承で
  * Pythonって適合ないの？ -> 継承で
  * そういえば `Zope Component Architecture (ZCA)`_ では ``interface.implements`` というのがあるなあ

* Pythonというか、プログラミング言語一般で共通した「プロトコル」っていう概念がある？

  * 一般的にはないかも
  * 通信用語だと、通信プロトコルとしてよく登場するよね
  * オブジェクト指向の文脈で、メッセージパッシングがあるけど、あれはオブジェクト間の通信仕様だと思うので、プロトコルなのかも

* Python公式リファレンスにそんな情報が書いてあるなんて全然しらなかった

  * 公式リファレンス、とりあえず一通り読んだりしないの？
  * 難しくて最初からアレを読むのは無理では...
  * まあ公式ドキュメントは教科書ではないのでしょうがないよね。それにしてもPythonの公式ドキュメントは入門者に易しくないｗ
  * 他の本でPythonを勉強して、公式リファレンスを一通り読めるようになったらもう初心者卒業って言えそう

* それにしてもPython公式リファレンス、Protocolの話が少なすぎる

  * ドキュメントのソースコメントに、 `talk about protocols?`_ って書いてあるよｗ
  * プロトコルのドキュメントを書こう！
  * よーし、プロトコルハッカソンだ～

.. _Zope Component Architecture (ZCA): https://docs.zope.org/zope.component/narr.html
.. _talk about protocols?: https://github.com/python/cpython/blame/0264e46caa854803a5318d75ae7893e9174f3f70/Doc/faq/design.rst#L225


書籍販売コーナー
====================

`PythonユーザのためのJupyter[実践]入門`_ 、買おうかどうしようかと思ってたけど、  `@chezou`_ さんの以下のツイートを見て買いました！イベント価格で税込み3,000円！

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">.<a href="https://twitter.com/iktakahiro">@iktakahiro</a> さんからご恵贈いただきましたJupyter本、PyConJPの基調講演でもあったpandasの基礎からmatplotlibの詳細Bokehまであり分析入門に良いです。具体的な分析例や日本語フォント紹介も <a href="https://t.co/o2ud1sSNRl">https://t.co/o2ud1sSNRl</a> <a href="https://t.co/RgkdrCJyHK">pic.twitter.com/RgkdrCJyHK</a></p>&mdash; chezou (@chezou) <a href="https://twitter.com/chezou/status/906328774274301952">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

.. _PythonユーザのためのJupyter[実践]入門: http://amzn.to/2vM4OO2
.. _@chezou: https://twitter.com/chezou

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/PyConJP?src=hash">#PyConJP</a> で &quot;Jupyter実践入門&quot; 買ってサインもらった！やったー！！ <a href="https://t.co/X0l1A3OclK">pic.twitter.com/X0l1A3OclK</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906356511621836801">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


`Pythonエンジニア ファーストブック`_ も販売してた。おれも本売りたかったなあ...


.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">モノタロウ侍も推薦！！「Pythonエンジニア ファーストブック」と「Jupyter実践入門」 <a href="https://twitter.com/hashtag/pyconjp?src=hash">#pyconjp</a> <a href="https://twitter.com/hashtag/pyfirst?src=hash">#pyfirst</a> (@ 早稲田大学 63号館 in 新宿区, 東京都) <a href="https://t.co/162uhnyhfd">https://t.co/162uhnyhfd</a> <a href="https://t.co/QORl9jRlkM">pic.twitter.com/QORl9jRlkM</a></p>&mdash; Takanori Suzuki (@takanory) <a href="https://twitter.com/takanory/status/906375620380254209">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

いいなあぁ...

.. _Pythonエンジニア ファーストブック: http://amzn.to/2wNWX6y


ランチ
==========

チキン～

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/pyconjp?src=hash">#pyconjp</a> ランチ弁当～ <a href="https://t.co/YW60MjR6tP">pic.twitter.com/YW60MjR6tP</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906358894452023296">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

ポスターセッション
===================

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">Python Boot Camp のポスター！日本地図に開催実績塗って、希望地に付箋貼ってもらっている。付箋多く貼られたら開催が早まる....かも? <a href="https://twitter.com/hashtag/PyConJP?src=hash">#PyConJP</a> <a href="https://twitter.com/hashtag/pycamp?src=hash">#pycamp</a> <a href="https://t.co/STy2mGrx1Z">pic.twitter.com/STy2mGrx1Z</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906373732809113600">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">Python Boot Camp の講師、スタッフ、各地域の現地スタッフが勢ぞろい！！広がってる感すごい <a href="https://twitter.com/hashtag/pyconjp?src=hash">#pyconjp</a> <a href="https://twitter.com/hashtag/pycamp?src=hash">#pycamp</a> <a href="https://t.co/oLhJZiBgTU">pic.twitter.com/oLhJZiBgTU</a></p>&mdash; Takanori Suzuki (@takanory) <a href="https://twitter.com/takanory/status/906369461514420224">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

`Python Boot Camp`_ から始めて、将来的に地域PyCon、っていう流れもありだと思います！誘致に興味ある方は `Python Boot Camp`_ を見てくださーい。よろしくー


.. _Python Boot Camp: https://peraichi.com/landing_pages/view/pycamp


Python におけるドメイン駆動設計(戦術面)の勘どころ
===================================================

* Junya Hayashi
* https://pycon.jp/2017/ja/schedule/presentation/31/
* 動画: https://www.youtube.com/watch?v=SWUq335On5Y
* 資料: https://www.slideshare.net/ledmonster/python-79561227

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">「リポジトリとの接続にDIコンテナを使う。今は <a href="https://t.co/OhcWR98VTS">https://t.co/OhcWR98VTS</a> を使っている。DIを使わずにヘキサゴナルアーキテクチャで実装すると破綻する」 <a href="https://twitter.com/hashtag/pyconjp_201?src=hash">#pyconjp_201</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906380689020354560">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">ヘキサゴナルアーキテクチャのリポジトリでORMを使う話。ORMのモデルインスタンスをリポジトリの外に出したくなっちゃうんだよね。リポジトリに閉じ込める場合、ORMが提供する便利な機能を活用できなくなるので、開発メンバーの納得感が下がるんだよー <a href="https://twitter.com/hashtag/pyconjp_201?src=hash">#pyconjp_201</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/906380220688502784">2017年9月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

一般社団法人PyCon JP ミーティング
======================================

一社の会計理事として参加してきました。

参加は、理事4名、PyCon JPスタッフ3名、興味ある参加者3名、合計10名でした。

* 議題です: https://docs.google.com/presentation/d/108NACaC4WGxvao-aVLM4114lOjO2R4I9dwLsQVOXG3c/present?token=AC4w5Vg3QLPhwqZHKgFEraUy44LknaSumQ%3A1504939156274&includes_info_params=1#slide=id.p

* 議事録は後日公開予定です: https://www.pycon.jp/committee/meeting/index.html


クロージング
===============


.. note:: 内容は随時更新していきます



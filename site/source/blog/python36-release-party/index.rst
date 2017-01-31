:date: 2017-01-31 21:00
:categories: ['Python']
:body type: text/x-rst

=================================================================
2017/01/31 Python 3.6 リリースパーティーに参加しました #pystudy
=================================================================

Python3.6 リリースパーティーに参加しました。その時のメモです。
https://pystudy.connpass.com/event/48361/

免責事項: 雑なメモなので間違ってる部分もあるかもしれません。


.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">Python 3.6 Release Party!! (@ LODGE in 千代田区, 東京都) <a href="https://t.co/FoJoKLw48q">https://t.co/FoJoKLw48q</a> <a href="https://t.co/mze4lm6tgz">pic.twitter.com/mze4lm6tgz</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/826373606137593857">2017年1月31日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

.. contents::
   :local:


パーティー
================

(@t2y)「Python 3.6 リリースおめでとー！（クラッカーぱーん！）」

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">パーティー感の残骸です <a href="https://twitter.com/hashtag/pystudy?src=hash">#pystudy</a> <a href="https://t.co/ttz93fuqB5">pic.twitter.com/ttz93fuqB5</a></p>&mdash; Takanori Suzuki (@takanory) <a href="https://twitter.com/takanory/status/826374654138818560">2017年1月31日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


パーティー終了（開始数十秒ｗ）

@atsuoishimoto Python 3.6 の新機能と改善
=========================================

* 発表者: @atsuoishimoto
* テーマ: Python 3.6 の新機能と改善
* スライド: http://atsuoishimoto.hatenablog.com/entry/2017/01/31/202202

@atsuoishimoto「今日はオライリー帽子をかぶって発表します。オライリーさんで本を書くと、著者帽子をもらえて、こういうイベントでかぶらなければいけないんですね」（ｗ


新機能全文はこちら: https://docs.python.org/3/whatsnew/3.6.html


* f文字列（フォーマット済み文字列）

  * ``f'{式}'`` で波カッコ内に計算式や変数をかける
  * 式には一通り書ける。f文字列もかける。yieldも書ける。awaitは書けなかったけどバグらしい
  * 制約: ``f'{"\t"}'`` のようにバックスラッシュ文字は書けない（文字列の中の文字の扱いが面倒らしい）
  * 制約: lambda式はそのままは書けない。 `:` が別の意味になってしまうので。 ``()`` で囲んだら書ける
  * f文字列のパフォーマンスは比較するととくに速くも遅くもない

* :pep:`515` underscores in numeric literals

  * 数字に ``123_456_789`` のように桁区切りを分かりやすく書けるようになった
  * 二進数や16進数にも使える。  ``0b1110_1011`` など

* :pep:`487` Simpler customization of class creation

  * クラス生成器のカスタマイズがやりやすくなった
  * Enum型のように、属性値に1と入れたはずなのに、定義後にアクセスすると別の型になっている、など
  * いままではメタクラスを使ってカスタマイズしていた
  * 複数のメタクラスを組み合わせられない問題や、Python型システムがそれなりに難しい問題などが解決？
  * ``__init_subclass__(cls, kwargs)``

    * 基底クラスに実装しておくと、サブクラス定義時に呼び出される
    * メタクラスなしにカスタマイズできる！
    * この方式なら多重継承したそれぞれの基底クラスにカスタマイズ実装をしておけば、派生クラス定義時に両方が呼び出される
    * （呼び出し順はmroに従うんだろうな）

  * ``__set_name__(self, cls, name)``

    * 属性に代入するクラスインスタンスがこれを持ってたら、代入時に呼び出される
    * （簡易デスクリプタっぽいね）

  * 属性の登録順

    * クラスの ``__dict__`` は登録順を記録する
    * （OrderedDict？ @methane が実装したdict順序維持が使われてる？）

* :pep:`506` Adding A Secrets Module To The Standard Library

  * 新規モジュール: ``secrets``

* :pep:`495` Local Time Disambiguation

  * date/datetime にfold属性が追加された
  * 夏時間の終了時に時間の巻き戻しが発生する
  * 巻き戻ってる状態で時刻重複してますよ状態 = ``fold=1``

* :pep:`519` Adding a file system path protocl

  * ``__fspath__(self)`` プロトコルメソッド実装を持っているオブジェクトなら何でもopen()に渡せる
  * pathlib.Path オブジェクトなどを渡せる

    * ``open(str(Path(__file__)))`` これが
    * ``open(Path(__file__))`` これでよくなる


* :pep:`528` Change Windows console encoding to UTF-8

  * 従来は、日本語Windowsならcp932だった
  * ``print('\N{EURO SIGN}')``
  * 出力できない文字もある（お寿司とか）
  * ファイルリダイレクトすると従来通りとなる（cp932になる）

* :pep:`529` Change Windowsfilesystem encoding to UTF-8

  * ``os.listdir('.')`` と ``os.listdir(b'.')`` の動作の違い
  * Windowsでは、bytesを渡すのは非推奨だった（ANSI系APIの都合）
  * Python-3.6 から、Pythonが自前実装した（ANSI系APIを使わなくなった）ので、Windowsだからとか気にしなくてよくなった

* 正規表現

  * group参照機能の改善: ``m.group('G1')`` を ``m['G1']`` で書けるようになった
  * フラグ指定の改善: フラグ指定を正規表現パターン内に書けるので全体適用しない使い方ができるようになった

Q&A
-------

* ``sys.path`` に ``pathlib.Path`` を入れたらパスとして認識されなかったのですが、 ``__fspath__`` がどこに使えるかという情報はどこかにまとまっていますか？（しみずかわ）

  * あるとしたら :pep:`519` にあるくらいです（いしもと）
  * ``sys.path`` はPython起動処理にも絡む部分なので、 ``__fspath__`` のような複雑な仕組みは動作しないかも
  * まだ全体的に使えるとは言えないと思うし、実装がまだ不安定な部分もあるようです（いしもと）
  * ``__fspath__`` メソッド内で例外が発生したら、Pythonプロセスごと落ちてしまった（いしもと）


（ここで10分ほど休憩）

@Masahito :pep:`526` and 周辺ツールについて
=============================================

* 時間: 20:10 - 20:32
* 発表者: @Masahito
* テーマ: :pep:`526` and 周辺ツールについて
* スライド: 

* :pep:`526` Syntax for Variable Annotations

  * :pep:`526` は :pep:`484` の拡張です
  * 参考資料: `[翻訳] PEP 0484 -- 型ヒント (Type Hints)`_
  * :pep:`484` スタイルで変数の型ヒントをコメントで書くと、コードコメントを書きづらい
  * :pep:`526` では、変数定義時にPythonの新しい文法で書けるようになった
  * アノテーション情報は __annotations__ 属性に格納されている

* typing

  * typoingモジュールはPython3.5で導入
  * PyPIにあるので、 ``pip install typing`` でインストールすればPython2.7以降で使える
  * Python3.6でのtypoingの変更点: Collection, ContextManager, NamedTuple 型の追加

* 周辺ツール

  * mypy
  * pytype
  * PyCharm

    * （PyCharmのtype hint対応を使ってるけど、便利です（型間違えがハイライトされるとか、呼び出しが複数階層あっても伝搬するとかという普通の便利さ））

* pytype

  * Python 3.4, 3.5 で動かすと良い
  * （はじめて聞いた）

* MyPy

  * 参考資料: `[翻訳] Python の静的型、すごい mypy!`_
  * 最近パッケージ名が変わった: `mypy-lang`_ -> `mypy`_
  * MyPyが持っている `typeshed`_ はまだPython-3.6対応できてないようだ
  * MyPy自体が新しいPython文法に未対応な部分もある

* ``Protocol`` typingの中身

  * ダックタイピングな関数の動作に対して型を指定できる仕組みがtyping内部にありそう
  * 

.. _`[翻訳] PEP 0484 -- 型ヒント (Type Hints)`: http://qiita.com/t2y/items/f95f6efe163b29be59af
.. _`[翻訳] Python の静的型、すごい mypy!`: http://qiita.com/t2y/items/2a1310608da7b5c4860b
.. _mypy: https://pypi.python.org/pypi/mypy
.. _mypy-lang: https://pypi.python.org/pypi/mypy-lang
.. _typeshed: https://github.com/python/typeshed

Q&A
-------

* typingの使い方について、Tupleの場合全要素を型指定指定しないといけない（aodag）

  * リストの例: ``List[str]`` リストの要素全部がstrだよという意味
  * タプルの例: ``List[str, str, str]`` 3要素のstrのタプルはこう書かないと行けない
  * （まさひと）今のところ良い方法はなさそう

.. * pytypeのメリットはなんですか？（しみずかわ）


@methane 新dict実装の話, New dict implementation
===================================================

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">本日家族の都合で参加できなくなってしまいました。申し訳ありません。<br>発表資料だけ共有しておきます。 <a href="https://twitter.com/hashtag/pystudy?src=hash">#pystudy</a><br>New dict implementation in Python 3.6 <a href="https://t.co/tQFUm2PrLL">https://t.co/tQFUm2PrLL</a></p>&mdash; INADA Naoki (@methane) <a href="https://twitter.com/methane/status/826350271089348609">2017年1月31日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>



@t2y async関連, :pep:`525`, :pep:`530`
=========================================

* 時間: 20:33 - 21:00
* 発表者: @t2y
* テーマ: async関連, :pep:`525`, :pep:`530`
* スライド: https://speakerdeck.com/t2y/python-3-dot-6-release-party-async-guan-lian

はい

* 非同期／並行処理の背景

  * マルチスレッド vs イベント駆動

    * 例: Apache vs Nginx

  * 並行と並列 -> 厳密な定義はない
  * 並行: 1CPUでタイムシェアして動くやつ
  * 並列: マルチコアで動いてるやつ

  * 実行単位: プロセス、スレッド、コルーチン
  * コルーチン

    * ファイバーとかジェネレータとか
    * 処理を一時中断したり復元したりしながら実行

  * ジェネレータ: yield とか yield from を使って定義した関数
  * コルーチン

    * ネイティブコルーチン: async def で実装
    * ジェネレーターベースのコルーチン: ジェネレータ構文で書ける

* Python3の非同期処理の変遷

  * 3.3: yield from 構文, :pep:`380`
  * 3.4: asyncioモジュール(暫定), :pep:`3156`
  * 3.5: async, await (=ネイティブコルーチン), :pep:`492`
  * 3.6: ayncioモジュールの暫定解除！, :pep:`525`, :pep:`530`

* ユースケース

  * producer-consumer pattern
  * ネイティブ: async def と awit <func call> で実装する
  * ジェネレータ: ``@asynciocoroutine`` デコレータをジェネレータ関数に付けることで ``async def`` 相当になる

* 非同期ジェネレータ :pep:`525`

  * 3.6で ``async def`` + ``yield`` で済むようになった

* 非同期内包表記 :pep:`530`

  * ``[await afun(i) async for i in agen()]`` のように書く... ごちゃごちゃしてるｗ
  * list, set, dict, generator 各内包表記で使える
  * async関数内でしかつかえません

* @mitsuhiko (ARMIN) のブログ

  * twistedから概念を持ってきている
  * ジェネレータの設計ミスがあるという指摘

    * 3.3 から ``yield`` と ``return`` を両方使えるようになった
    * ジェネレータの ``return`` は ``StopIteration`` を発行するだけで、返値は無視される
    * ``return [1]`` なんて書いても呼出元には値が渡らないので分かりにくいバグの原因になるね

  * asyncioの最悪なところは、がんばって書いても大して速くない

    * IO待ちのある細かい大量の並列処理がないと効果が出ないかも

* まとめ

  * 非同期は難しい
  * 難しいから言語処理系が記法をサポートする
  * Py2 -> Py3 に移行するモチベーション？（Py2には無いから）
  * Py3.6 でasyncioの開発は一段落したっぽい

Q&A
-------

* これはZen of Pythonに抵触しているのでは？（お名前不明）

  * threadやmultiprocessでできていることを言語レベルで導入した理由が理解できない（質問者）
  * アプローチの違い、という理解（t2y）
  * イベント駆動のほうが最近のトレンドかなと思う（t2y）
  * マルチスレッドは人類には早すぎる、タスクを細切れにしたasync的モデルが推奨されている （いしもと）
  * スレッドは2000年頃まで。2000年以降はQueueを使うなどの非同期方面へシフトしてきた（いしもと）
  * 計算モデルが異なるので、まったく同じ用途という感じでもない（いしもと）


LT: @cardinalxaro Effective PythonとPython 3.6, Python 3.6における『Effective Python』 項目33はこう変わる
===========================================================================================================

* 時間: 21:05 - 21:10
* 発表者: @cardinalxaro
* テーマ: Effective PythonとPython 3.6, Python 3.6における『Effective Python』 項目33はこう変わる
* スライド: https://speakerdeck.com/hayaosuzuki/effective-python-in-python-3-dot-6

- Python3.5まで: デスクリプタ実装でやった
- Python3.6から: メタクラス使わなくてもできる！


LT: @terapyon この10年のPython
======================================

* 時間: 21:10 - 21:15
* 発表者: @terapyon
* テーマ: この10年のPython
* スライド: 

- （会場に質問）みんないつから使い始めた？

  - 2.4以前から: 10人弱
  - 3.0以降から: 1人

* （1年ごとにPythonになにが起きたかを振り返るスタイルのLTおもしろいw）


LT: @aodag Python3移行への軌跡
===============================

* 時間: 21:15 - 21:20
* 発表者: @aodag
* テーマ: Python3移行への軌跡
* スライド: http://www.slideshare.net/aodag/python3-71585420

(@aodag)「満席だけどLTやるなら来ても良いよ、と言われてLT作ってきたけどキャンセル結構出たからLTしなくても来れたんじゃねえかこれ」たしかにｗ

* 2010年頃にPython3対応してないライブラリを晒し上げしてたサイト `PYTHON 3 WALL OF SHAME`_ （今はWALL OF SUPERPOWERS)
* six.u めっちゃがんばって入れてたけどPython3.3でuリテラル復活したからいらなくなった（ほんとね...）
* Linuxディストリは2020年以降も2.7をサポートするらしいんで独自に頑張ってください
* `PYTHON 3 WALL OF SUPERPOWERS`_ だいぶグリーン！赤いのは、主に、moz(mozilla)って書いてあるやつ


.. _PYTHON 3 WALL OF SHAME: https://python3wos.appspot.com/
.. _PYTHON 3 WALL OF SUPERPOWERS: https://python3wos.appspot.com/

LT: @koedoyoshida PyCon JP 2017の宣伝
=========================================

* 時間: 21:20 - 21:25
* 発表者: @koedoyoshida
* テーマ: PyCon JP 2017の宣伝
* スライド: 


- PyCon JP歴は若い方ですが、今年は座長をやります
- これまでほぼ全部ボランティアスタッフで運営してきました
- 今日はボランティアスタッフの募集に来ました


おわりに(@t2y)
=====================

* Go リリースパーティーを参考に、Pythonでもやってみたくて主催しました
* Goは短い期間で新しいバージョンがでますが、Pythonの場合バージョンが上がるのが1年後とかなので、また1年後にやるかもしれません（ｗ
* ビジターカードちゃんと返して帰ってね

はい。

全体的な感想
================

* 100人くらい参加者きた
* スタッフとして最初期に@t2yから声かけてもらったけど、ちょっとしたアドバイスと当日の受付少々くらいしか手伝えなかった
* 言語アップデートというテーマなので、話のレベルが高めだった。付いて来れなかった人けっこういるんじゃないかな
* Python-3.6 の新機能についていっぺんに知ることができたので面白かった
* 主催者の@t2yさん、会場を貸してくれたYahooさん、ありがとうございました!


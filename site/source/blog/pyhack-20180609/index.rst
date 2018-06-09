:date: 2018-06-09 22:00
:tags: Python, pyhack, hack-a-thon

====================================
Python mini hack-a-thon 89回 #pyhack
====================================

毎月恒例の `#pyhack`_ 黙々ガヤガヤイベントに参加しました。

.. figure:: members.*
   :width: 90%

   hack中のみなさん1

.. figure:: members2.*
   :width: 90%

   hack中のみなさん2

:イベント: `Python mini hack-a-thon #89`_
:参加者: 25人くらい
:会場: `BeProud社（新宿）`_
:時間: 11:00 - 19:00 （自分は14時-17時で参加）

`#pyhack`_ は毎月開催しているイベントで、Pythonに関係あってもなくても、好きな事を各自やってOKなイベントです。


.. _Python mini hack-a-thon #89: https://pyhack.connpass.com/event/87316/
.. _#pyhack: https://twitter.com/hashtag/pyhack?f=tweets&vertical=default&src=hash
.. _BeProud社（新宿）: https://www.beproud.jp/

今日やったこと
==============

ネタだし
----------

ある執筆中の本とPyCon JP 2018のトークのネタを考えました。

PSF寄付のシール受取り
------------------------

PSF(Python Software Foundation)に寄付したこともり、PSFコントリビューションメンバーの @terapyon から、寄付した人シールをもらいました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">I DONATED TO THE PSF!! / PSFのcontributionメンバー <a href="https://twitter.com/terapyon?ref_src=twsrc%5Etfw">@terapyon</a> から実シールもらった！！ <a href="https://t.co/2mBNpNSbkY">pic.twitter.com/2mBNpNSbkY</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/1005327588133236736?ref_src=twsrc%5Etfw">2018年6月9日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


それPyPro3に書いてあるよ
-------------------------

パッケージング周りの質問がことごとくPyPro3（ `Pythonプロフェッショナルプログラミング第3版 <https://amzn.to/2sIBhFM>`_ ）に書いている内容だったので、「それPyPro3に載ってるよ」という合いの手を入れてました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">なにか質問があるたびに、(今日持ってきてある <a href="https://twitter.com/hashtag/pypro3?src=hash&amp;ref_src=twsrc%5Etfw">#pypro3</a> に)書いてあるから！と言われるのすごい <a href="https://twitter.com/hashtag/pyhack?src=hash&amp;ref_src=twsrc%5Etfw">#pyhack</a></p>&mdash; かしゅー (@kashew_nuts) <a href="https://twitter.com/kashew_nuts/status/1005358752147501056?ref_src=twsrc%5Etfw">2018年6月9日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">Pythonプロフェッショナルプログラミング 第3版、パッケージ周りだけでも買う価値がありそう</p>&mdash; driller/どりらん (@patraqushe) <a href="https://twitter.com/patraqushe/status/1005352665751085056?ref_src=twsrc%5Etfw">2018年6月9日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">どうも、パッケージ周りの著者です <a href="https://twitter.com/hashtag/pypro3?src=hash&amp;ref_src=twsrc%5Etfw">#pypro3</a> 『Pythonプロフェッショナルプログラミング 第3版』 <a href="https://t.co/lwrPmSykCr">https://t.co/lwrPmSykCr</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/1005367851354447872?ref_src=twsrc%5Etfw">2018年6月9日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


独学プログラマー
------------------

自分が帰った後に、独学プログラマーを読んだ話が出たらしい。その場に居たかったなあ。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">.<a href="https://twitter.com/yoshizirou?ref_src=twsrc%5Etfw">@yoshizirou</a> IoTの部署に決まったのでみんなのIoTを読んでいる。Javaの研修なのでPythonを忘れたので独学プログラマーを読んでいる。Jupyterで不快指数を出す <a href="https://twitter.com/hashtag/pyhack?src=hash&amp;ref_src=twsrc%5Etfw">#pyhack</a></p>&mdash; Takanori Suzuki (@takanory) <a href="https://twitter.com/takanory/status/1005370509255536645?ref_src=twsrc%5Etfw">2018年6月9日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">「独学プログラマーの言葉にガツンときた」すごい <a href="https://twitter.com/hashtag/pyhack?src=hash&amp;ref_src=twsrc%5Etfw">#pyhack</a></p>&mdash; かしゅー (@kashew_nuts) <a href="https://twitter.com/kashew_nuts/status/1005370291541835776?ref_src=twsrc%5Etfw">2018年6月9日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">「口ではなんとでも言える コードを見せなさい」 <a href="https://twitter.com/hashtag/pyhack?src=hash&amp;ref_src=twsrc%5Etfw">#pyhack</a></p>&mdash; Takanori Suzuki (@takanory) <a href="https://twitter.com/takanory/status/1005371217086279680?ref_src=twsrc%5Etfw">2018年6月9日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-conversation="none" data-lang="ja"><p lang="ja" dir="ltr">あと「スキルが上達しているように感じないのは継続して学習していないからだ」っていう言葉にも心に来るものがあったらしいです。</p>&mdash; かしゅー (@kashew_nuts) <a href="https://twitter.com/kashew_nuts/status/1005372239968006144?ref_src=twsrc%5Etfw">2018年6月9日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   <blockquote class="twitter-tweet" data-conversation="none" data-lang="ja"><p lang="ja" dir="ltr">なるほどー。たぶんこれかな「&quot;練習をしても完璧にはなれない。練習が末梢神経を作り、末梢神経が完璧を作る&quot; -- ダニエル・コイル」</p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/1005374087810519040?ref_src=twsrc%5Etfw">2018年6月9日</a></blockquote>
   <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


やったこと発表
==============

発表タイムは（毎回だけど）残念ながら不参加。 `#pyhack`_ を眺める。


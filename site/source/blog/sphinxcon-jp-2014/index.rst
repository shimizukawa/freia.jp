:date: 2014-10-31 20:30
:tags: Sphinx, SphinxCon

===========================================================
2014/10/31 SphinxCon JP 2014 で発表してきました #sphinxjp
===========================================================

.. figure:: sphinxconjp2014-logo.png
   :target: http://sphinx-users.jp/event/20141026_sphinxconjp/index.html

   SphinxCon JP 2014 を開催しました


SphinxCon JP 2014 を、先日10/26(日)に開催しました。

イベントの報告は `SphinxCon JP 2014 (2014/10/26)`_ のページにあるので、そちらをご覧下さい。このblogでは自分の発表と、イベントについての感想を書きたいと思います。

.. _SphinxCon JP 2014 (2014/10/26): http://sphinx-users.jp/event/20141026_sphinxconjp/index.html

開催した経緯
==============

午前中の参加者は30名ほど。ハンズオンに20名、ハッカソンに10名という感じで参加していました。午後のプレゼン時間には43名くらいまであつまりました。

.. raw:: html

   <a href="https://www.flickr.com/photos/shimizukawa/15455199869" title="SphinxCon JP 2014 by Takayuki Shimizukawa, on Flickr"><img src="https://farm6.staticflickr.com/5609/15455199869_505413d607.jpg" width="500" height="334" alt="SphinxCon JP 2014"></a>



このイベントを企画したきっかけは、Sphinx関連の情報を発表する場が欲しかったけど `PyCon JP 2014`_ ではSphinx関連の発表がまったく無かったため（ `自分もPyCharmの紹介の方が採用された`_ ）、そういう場を作りたかったという感じでした。人数は30名前後集まればいいかな、と思っていたところ、もっと大きなキャパシティーの会場をVOYAGE GROUPさんでお借りすることが出来た感じです。募集人数50人に対して一時はキャンセル待ちも発生しましたが、43名なら想定以上のあつまりだったかな、というところです。

今回のイベントは、 http://sphinxjp.connpass.com/ で掲載しているSphinx Tea Night というイベントで立ち上がりました。Sphin Tea Nightは、ファミレスでお茶を飲みながらSphinx関連の雑談をする気楽な会ですが、そこで気楽に「やろうよ！」と言って、そこから進み始めた感じです。



出席率について
================

懇親会は参加者登録者数の7割かなー、と思って懇親会の注文数を計画しましたが、実際には以下のような感じでした。

* イベント参加数: 24時間前の登録数の **7割**
* 懇親会参加率: 出席者の **7割**

0.7 x 0.7 = **0.49** ということで、20%ほど予測を外してしまいました。無料イベントだというのと、日曜夜に懇親会だったというのが要因でしょうか。次はもうちょっとシビアに行こうと思います。


発表について
==============

当日は、14時から7つのプレゼンを行いました。

`SphinxCon JP 2014 タイムテーブル`_

#. Welcome to Sphinx-1.3 (清水川)
#. SIerでもSphinxを使いたい！総括 (kk_Ataka)
#. SphinxとLaTeXで作る英文マニュアル (力武 健次)
#. Markdownもはじめよう (高橋征義)
#. Sphinx拡張 探訪 2014 (小宮 健 (@tk0miya))
#. 検索エンジンOktavia (渋川よしき)
#. Sphinx HTML Theme Hacks (shkumagai)


どのプレゼンも質問がよく出ていて、良いネタをみんなで共有できたんじゃないかと思います。今回のイベント開催にあたり、もっと多くの人に発表応募してもらっていましたが、その方々の発表もまた別の機会で聞きたいものが多かったので、またイベント企画しなきゃなあ、とも思ったり（いつやるんだろう）。

発表してくれたみなさん、応募してくれたみなさん、ありがとうございました。



自分の発表について
=====================

私も、先日リリースされた `Sphinx-1.3b1`_ をベースに、 **Welcome to Sphinx-1.3** というタイトルでプレゼンしました。

.. raw:: html

   <iframe width="560" height="420" src="http://shimizukawa.bitbucket.org/sphinxconjp2014-welcome-to-sphinx-1.3/index.html" frameborder="0"></iframe></div>


例によって、 `sphinxjp.themes.s6`_ で書きました。ソースコードはbitbucketの `/shimizukawa/sphinxconjp2014-welcome-to-sphinx-1.3`_ にあります。


LTについて
==============

.. raw:: html

   <a href="https://www.flickr.com/photos/shimizukawa/15455204079" title="SphinxCon JP 2014 by Takayuki Shimizukawa, on Flickr"><img src="https://farm4.staticflickr.com/3939/15455204079_38c7da93ba.jpg" width="500" height="334" alt="SphinxCon JP 2014"></a>

VOYAGE GROUPさん提供でビアバッシュをしながら、ライトニングトーク大会をしました。だれか話してくれるんだろうか、と思っていましたが、10個くらいのトークが行われて安心しました。

自分も、EuroPython 2014に行ったときに発表できなかったLTのネタで1個やりました。
そのLTスライドもsphinxjp.themes.s6で作っていたんですが、日本語で一度書いてから、Sphinxのi18n機能を使って英語に翻訳してスライド出力していました。多言語対応スライド。


まとめ
========

`@usaturn`_, 座長お疲れ様でした！

参加された皆さん、発表者の皆さん、発表応募してくれたみなさん、会場を貸してくれたVOYAGE GROUPさん、ありがとうございました。

またやろう！

.. raw:: html

   <a href="https://www.flickr.com/photos/shimizukawa/15456294240" title="SphinxCon JP 2014 by Takayuki Shimizukawa, on Flickr"><img src="https://farm4.staticflickr.com/3938/15456294240_7165b33424.jpg" width="500" height="334" alt="SphinxCon JP 2014"></a>



.. _PyCon JP 2014: https://pycon.jp/2014/
.. _自分もPyCharmの紹介の方が採用された: http://www.freia.jp/taka/blog/pyconjp2014-pycharm-and-other-rejected-proposals/index.html

.. _SphinxCon JP 2014 タイムテーブル: http://sphinx-users.jp/event/20141026_sphinxconjp/index.html#id4
.. _Sphinx-1.3b1: https://pypi.python.org/pypi/Sphinx/1.3b1

.. _sphinxjp.themes.s6: https://pypi.python.org/pypi/sphinxjp.themes.s6

.. _/shimizukawa/sphinxconjp2014-welcome-to-sphinx-1.3: https://bitbucket.org/shimizukawa/sphinxconjp2014-welcome-to-sphinx-1.3

.. _@usaturn: https://twitter.com/usaturn


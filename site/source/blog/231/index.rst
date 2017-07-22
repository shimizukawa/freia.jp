:date: 2005-07-18 20:36:29
:tags: Zope

============================
2005/07/18 Zope3勉強会 4回目
============================

`Zope3勉強会`_ に行ってきました(おととい)。そろそろ簡単な掲示板は作れそうな雰囲気になってきています。

今回から、後半は実際にプログラムを書いてみるということで、デモの掲示板(ZopeBookのMessageBoard Step02)をベースに改造してみたのですが、そろそろZopeBookだけでは分からない事が多くなってきました。基本的にArchetypesの事を知っていると入りやすいけど、細かいところが違っていて苦労しています。

.. _`Zope3勉強会`: http://www.zope.org/Members/yusei/zope3meeting


.. :extend type: text/x-rst
.. :extend:

今自分の壁になっている主な違いは...

- アダプターの概念の存在
- ZCMLファイルの存在

この2点です。デザインパターンのアダプターは分かるんです。問題は、Zope3において、どことどこがAdapter,Adapteeの関係になるのか。コンテンツをDublinCoreとして扱うことが出来るのはアダプターが影でゴリゴリやってくれるから、というのは分かる(合ってる?)んですが、今回やりたかったことにアダプターが関係するのかどうかが分からない。多分関係するんだと思うけど。

ということで、やりたかったのは **掲示板の投稿内容をSilverCityでHighlightingする** 事。今回はViewに表示する段階でbodyをSilverCityに渡して変換しましたが、本来はアダプターを介してコンテンツを変換するのが正しいんじゃないかと思っています。そういうアダプターを作れば流用可能だし。これは今後の課題かな。

あとはZCML。何を書くとどことどこが繋がるのか...部分的には分かるけどまだもやもやしてます。どこの名前空間でどのディレクティブを使えるのか、、はディレクティブ定義を探せばいいのか。あとで探してみよう。

.. figure:: zope3silvercity
  :align: left
  :class: visualClear

  とうことで、今回の成果です。
  SilverCityを使ってHighlightingしている状態です。

  この改造をしたファイルも置いておきます。
  `messageboard_step02_silvercity.tgz`__

  .. __: http://www.freia.jp/taka/file/Zope/messageboard_step02_silvercity.tgz

.. cssclass:: visualClear

次回は8/7の予定です。‥‥近いな。



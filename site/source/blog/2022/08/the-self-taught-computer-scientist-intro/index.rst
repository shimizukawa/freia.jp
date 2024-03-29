:date: 2022-08-19 12:00
:tags: python, tstcs, 独CS

=====================================================================================
『独学コンピューターサイエンティスト』 The Self-Taught Computer Scientist の紹介
=====================================================================================

清水川が監訳した `独学コンピューターサイエンティスト`_ (原題 `The Self-Taught Computer Scientist`_) が2022/8/26に日経BP社さんより発売されます！

.. figure:: the-self-taught-computer-scientist-en-ja-cover.*

   独学コンピューターサイエンティスト / The Self-Taught Computer Scientist

:タイトル: `独学コンピューターサイエンティスト`_ Pythonで学ぶアルゴリズムとデータ構造
:原題: `The Self-Taught Computer Scientist`_: The Beginner's Guide to Data Structures & Algorithms
:著者: コーリー・アルソフ(Cory Althoff)
:監訳: 清水川貴之
:翻訳: 清水川貴之、新木雅也、大村 和子、tell-k
:出版社: 日経BP社
:Price: 2,300円+税
:ISBN-13: 978-4296070343
:購入: Amazon_

.. _独学コンピューターサイエンティスト: https://bookplus.nikkei.com/atcl/catalog/22/07/19/00285/
.. _The Self-Taught Computer Scientist: https://amzn.to/3QpGj2C
.. _Amazon: https://amzn.to/3zZymtV


どんな本？
==========

`『独学プログラマー』`_ 著者による、待望の2冊目です！今回は **アルゴリズムとデータ構造** に焦点を当て、「コンピューターサイエンティスト」を独学で目指します。コンピューターサイエンスを学ぶ、というよりも、 **コンピューターサイエンティストを目指す** 、という気持ちで読んでもらえればと思います。

アルゴリズムとデータ構造は面白いトピックなのですが、説明しようとすると難しい解説になってしまいがちで、読んですぐ「なるほど！」となりにくい分野です。前作ではデータ構造（21章）とアルゴリズム（22章）の紹介はほんの触りだけでしたが、続編となる本書『独学コンピューターサイエンティスト』は1冊かけて、『独学プログラマー』同様の平易で読みやすい文章で、アルゴリズムとデータ構造を紹介しています。

著者前書きから引用します。

  前作『独学プログラマー』では、プログラミングとプログラミングの仕事をするうえで必要なスキルを紹介しました。（中略）本書はコンピューターサイエンスの学位に必要な内容を **網羅するのではなく** 、独学プログラマーが活躍するうえで役に立つ、コンピューターサイエンスの **基本的な概念に絞って紹介** します。

  **独学プログラマーが理解しておくべきもっとも大切な分野は、アルゴリズムとデータ構造です。** 本書ではこの2つに焦点を当てることにしました。本書は第1部と第2部に分かれています。第1部はアルゴリズム入門です。アルゴリズムとは何か、アルゴリズムの優劣を決めるのは何か、そして線形探索、二分探索などのさまざまなアルゴリズムを学びます。第2部はデータ構造入門です。データ構造とは何か、そして配列、連結リスト、スタック、キュー、ハッシュテーブル、二分木、二分ヒープ、グラフについて学びます。最後に、 **本書を読み終えた後にやるべきこと、プログラミングを学び続けるのに役立つ情報や次のステップについて紹介** します。

訳者あとがきから引用します。

  本書の著者、コーリー・アルソフ（Cory Althoff）は、独学プログラマーです。（中略） **コーリー自身が学びの途中にあり、対象読者と同じ視点でアルゴリズムとデータ構造というコンピューターサイエンスの必須知識を説明してくれている** ことに価値があります。アルゴリズムとデータ構造を扱う本はたくさんありますが、本書ほど入門しやすく説明してくれている本は稀でしょう。

  本書は、難しい内容であるアルゴリズムとデータ構造について、要点を絞って分かりやすく伝えています。そのため、これらを学ぶ1冊目としてちょうど良い難易度になっています。本書を読んだ後ならきっと、技術面接においてある程度の自信が持てるでしょうし、プログラムを実装する際にもキーワードとその内容を知っているので、文献探しや実装例を見つけ出す手がかりが得やすいでしょう。

  **本書はコンピューターサイエンスを学んだことがない初学者を対象** にしています。平易な文章で読みやすく、そして学びの階段をできるだけ小さく、なだらかにして理解しやすいよう解説しています。本書だけで十分な高さには到達できないかもしれませんが、世の中にある多くの書籍を読み始められるだけの知識と、難しいという先入観を乗り越えられると思います。

私自身、ゲームを作りたくて高校生からプログラミングをしていましたが、当時はまだアルゴリズムとデータ構造を学ぶ必要性を分かっていませんでした。コンピューターサイエンスの基礎とも言えるアルゴリズムとデータ構造は、あらゆるプログラミングに必要な知識です。ゲームで自動追尾してくる敵の動きを計算しようとすれば、グラフから最短経路を瞬時に求める必要があります。シミュレーションゲームの処理順を扱うには優先度付きキューが必要になります。それを知らなくてもゲームは作れましたが、思いどおりに動かなかったり、計算量が大きくなりすぎて遅かったりと、満足のいくレベルにはなかなか届きませんでした。本書は、そんな当時の私が読みたかったアルゴリズムとデータ構造の入門書です。

.. _『独学プログラマー』: http://amzn.to/2EwY6Ea


目次
-----

* 第１部　アルゴリズム入門

  * 第0章　イントロダクション
  * 第1章　アルゴリズムとは何か？
  * 第2章　再帰
  * 第3章　探索アルゴリズム
  * 第4章　ソートアルゴリズム
  * 第5章　文字列のアルゴリズム
  * 第6章　数学
  * 第7章　独学伝：マーガレット・ハミルトン

* 第２部　データ構造

  * 第8章　データ構造とは何か？
  * 第9章　配列
  * 第10章　連結リスト
  * 第11章　スタック
  * 第12章　キュー
  * 第13章　ハッシュテーブル
  * 第14章　二分木
  * 第15章　二分ヒープ
  * 第16章　グラフ
  * 第17章　独学伝：イーロン・マスク
  * 第18章　次のステップ

* 第３部　もっと学ぼう

  * 補章1　アルゴリズムへの理解を深めるために―ハッシュテーブル―
  * 補章2　アルゴリズムへの理解を深めるために―ダイクストラ法―
  * 補章3　継続して学ぶために


17の格言
---------

本書には、各章に1つずつ格言が紹介されています。

  "数学に難ありと悩んでいる君、心配は要らない。間違いなく私のほうがよっぽど悩んでいるはずだ。" -- アルベルト・アインシュタイン

  "最強の人類は、決して学ぶことをやめない人たちだ。" -- リジョイス・デンヘリ

モチベーションが上がる格言もあれば、意味深なものもあり.. ぜひ、書籍をめくって確認してみてください。


著者はどんな人？
================

独学プログラマーです。全くのプログラミング初心者から始まり、自分の経験を書籍『独学プログラマー』にまとめました。『独学プログラマー』は日本だけでも10万部発行されるなど彼の想像以上に大ヒットしました。コーリーはこれ起点に `Udemyのコース <https://www.udemy.com/user/coryalthoff/>`_ を作ったり、日本に来て  `PyCon JP 2019でキーノート <https://youtu.be/Bcxz-jXMLZk?t=285>`_ をしたりと、独学プログラマーなどのプログラミング入門者を支援する活動を行っています。

コーリーの活動については、以下の記事も参考になると思います。

* :doc:`/blog/2017/07/pycharm-blog-201706-self-taught-programmer-interview-with-cory-althoff/index`
* :doc:`/blog/2018/02/the-self-taught-programmer-intro/index`
* :doc:`/blog/2018/07/the-self-taught-programmer-events/index`

この本は買いですか？
====================

日本語版の翻訳では、 **読みやすく、親しみやすい文体** を目指しました。
読み進める上で誤解や疑問の元になりそうな箇所には訳注とコラムを追加しています。
また、 **原書には無い「第3部」を追加** しています。「第３部　もっと学ぼう」では、アルゴリズムをイメージしやすいように、 **プログラムの動作を可視化する方法を紹介** しています。プログラムがデータ構造をどのように変化させていくのか、アルゴリズムがどのように問題を解決していくのかを理解しやすくなっていると思います。 **日本語で読める本やサイトも紹介** しているので、参考にしてみてください。

まとめると、 **日本語版は原著以上にオススメできる本** に仕上がったと思います。

2022年8月26日（金）発売です。よろしくおねがいします！

.. raw:: html

  <div class="amazlet-box" style="margin-bottom:0px;">
    <div class="amazlet-image" style="float:left;margin:0px 12px 1px 0px;"><a href="https://www.amazon.co.jp/dp/4296070347/?tag=freiaweb-22" name="amazletlink" target="_blank"><img src="https://m.media-amazon.com/images/I/513IPCO9oML._SL200_.jpg" alt="独学コンピューターサイエンティスト Pythonで学ぶアルゴリズムとデータ構造" style="border: none;" /></a></div>
    <div class="amazlet-info" style="line-height:120%; margin-bottom: 10px">
      <div class="amazlet-name" style="margin-bottom:10px;line-height:120%"><a href="https://www.amazon.co.jp/dp/4296070347/?tag=freiaweb-22" name="amazletlink" target="_blank">独学コンピューターサイエンティスト Pythonで学ぶアルゴリズムとデータ構造</a></div>
      <div class="amazlet-detail">コーリー・アルソフ(著), 清水川 貴之(翻訳), 新木 雅也(翻訳), 大村 和子(翻訳), tell-k(翻訳)<br />日経BP<br /><br />￥2,530<br /></div>
      <div class="amazlet-sub-info" style="float: left;">
        <div class="amazlet-link" style="margin-top: 5px"><a href="https://www.amazon.co.jp/dp/4296070347/?tag=freiaweb-22" name="amazletlink" target="_blank">Amazon.co.jpで詳細を見る</a></div>
      </div>
    </div>
    <div class="amazlet-footer" style="clear: left"></div>
  </div>

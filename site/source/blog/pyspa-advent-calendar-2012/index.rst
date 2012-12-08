:date: 2012-12-08 18:00
:categories: ['Python', 'PySpa']
:body type: text/x-rst

======================================================
2012/12/08 #PySpa アドベントカレンダー 8日目
======================================================

*Category: 'Python', 'PySpa'*

`PySpaアドベントカレンダー`_ 8日目の清水川です。

PySpaと全く関係ない役に立たないことを書こうと思ってたんですが、みんなPySpaについて書いてるみたいなのでちょっと予定を変更します。

.. _`PySpaアドベントカレンダー`: http://connpass.com/event/1443/

前置き
========

その前に事実誤認があるらしいので自分も訂正しておきますね。

   アドベントカレンダー栄えある1日目は
   `@akisutesamaが書いている <http://akisute.com/2012/12/pyspa-1-python.html>`_
   わけですが、いきなり事実誤認があるわけですよ。

      例えば今回のアドベントカレンダー参加メンバーだと

      ::

         12/1 akisutesama
         12/3 tokibito
         12/4 torufurukawa
         12/8 shimizukawa

      あたりがPySpa経由で雇用されたビープラウド社員だったりします。

   待てやこら。PySpa に初参加したときには、すでにビープラウドを退職した後ですよ。

   -- `中間地点としての PySpa - PySpaアドベントカレンダー4日目 <http://torufurukawa.blogspot.jp/2012/12/pyspaadvent2012.html>`_

自分もPySpa経由でBeProudに雇用されたんですねー。知らなかったわー、知らなかったわー。

そういえば色々な事情で仕事や所属関連の話題はあまり書いてなかったので、ちょっとPySpaの参加と絡めてそのあたりのことを書いてみようと思います。

ちなみに、自分がPySpa全10回のうち参加したのは7回ですね。

PySpa 第2回目 2007/10/27 - 29
==============================

2007年10月が最初の参加。このときは `タイムインターメディア`_ 所属2年目で、某CMSを開発していた頃ですね。5人から7人くらいの部署でリーダー的なことをしていた時期。

PySpa初参加で知り合いがほとんど居ない状況で伊豆高原駅に来たときは結構心細かったのを覚えてます。シャボテン公園近くの貸別荘が会場でした。

* `伊豆高原のコンドミニアムタイプ貸別荘　パークイン理想郷 <http://www.izu-risokyo.com/index.html>`_

けっこう広い庭があってバーベキュー出来る環境だったんですがバーベキューが雨で中止になって、バーベキューの材料でみんなで台所で調理したり。そういえばコストコのパンが美味しかった。 `@aodag`_ と初めて会話したのもこの頃。まだ西の方に住んでた@aodagと温泉に入りながら話をしていたのを不思議と良く覚えてます。あ、このとき@aodagは2つくらい年上だと認識してました。

そいうえば、参加者がほとんどMacBookで、この日にMac OS Xの新しいバージョンが出たとかで、インストール大会が始まったりしていました。なんというか不思議な光景でしたね。

.. _`タイムインターメディア`: http://www.timedia.co.jp/

そのときやったことを日記に書いています。

* :doc:`../487/index`
* :doc:`../488/index`
* :doc:`../489/index`
* :doc:`../490/index`



PySpa 第3回目 2008/6/27 - 29
=============================

芳泉閣に会場が移った回です。某CMS製品のアップデートが大変だった時期を超えて、製品開発時のノウハウを使って他の案件に色々適用していた時期です。

参加2回目のPySpaでは、Trac/Buildbot をセットアップしていました。

* :doc:`../583/index`
* :doc:`../585/index`
* :doc:`../586/index`
* :doc:`../587/index`
* :doc:`../588/index`
* :doc:`../589/index`
* :doc:`../590/index`

このときの成果を仕事に反映して、コミット時自動ビルド・テストの結果とTracとを連携させたりした覚えがあります。Tracを採用する前はXPlannerを使ってチケット駆動でやってました。Buildbot自体はもっと前に採用してましたね。BuildbotはLinuxとWindowsとで動作させたりとかしてました。


PySpa 第4回目 2008/10/26 - 28
=============================

.. raw:: html

   <object width="600" height="450"> <param name="flashvars" value="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157632196296330%2Fshow%2F&page_show_back_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157632196296330%2F&set_id=72157632196296330&jump_to="></param> <param name="movie" value="http://www.flickr.com/apps/slideshow/show.swf?v=122138"></param> <param name="allowFullScreen" value="true"></param><embed type="application/x-shockwave-flash" src="http://www.flickr.com/apps/slideshow/show.swf?v=122138" allowFullScreen="true" flashvars="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157632196296330%2Fshow%2F&page_show_back_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157632196296330%2F&set_id=72157632196296330&jump_to=" width="600" height="450"></embed></object>

* :doc:`../609/index`

この頃はたしか仕事でRailsを使って開発していた頃です。Rails-2.1が出たばっかりの頃で、100日連続出勤とか馬鹿なことしていたのも良い思い出です。色々まずいよね。このときPythonではなくRailsでがんばっちゃったために、仕事でPythonではなくRailsを使うことが多少増えたりしました。Pythonにしておけば良かったと何度か思ったこともありましたが、その後Railsのおかげで新しい縁が出来たりとかもしていて、これはこれで得がたいものになりました。


PySpa 第5回目 2009/6/26 - 28
=============================

.. raw:: html

   <object width="600" height="450"> <param name="flashvars" value="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157632192128501%2Fshow%2F&page_show_back_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157632192128501%2F&set_id=72157632192128501&jump_to="></param> <param name="movie" value="http://www.flickr.com/apps/slideshow/show.swf?v=122138"></param> <param name="allowFullScreen" value="true"></param><embed type="application/x-shockwave-flash" src="http://www.flickr.com/apps/slideshow/show.swf?v=122138" allowFullScreen="true" flashvars="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157632192128501%2Fshow%2F&page_show_back_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157632192128501%2F&set_id=72157632192128501&jump_to=" width="600" height="450"></embed></object>

渋川さん(`@shibukawa`_)の車で熱海まで行った回。このとき同乗したのは **イアンさん** と **東さん** でした。イアンさんと東さんとはそれまで話したことが無かった（あったかも？）のであまり車の中でも話をしなかったかもしれません。その後イアン(`@IanMLewis`_)と `@feiz`_ (東)とはBeProudで同僚になるわけですが。

この回の時に渋川さんがPythonの属性アクセス時に処理を挟み込む方法を調べてて、後でそれはPythonのデスクリプタ(__get__)で出来るのを知ったんですが、当時は自分も渋川さんも知らなかったので、二人でPythonのCの実装コードを読んで追いかけてました。PySpaに行くと周りでいろんな事が起きるのでそれに巻き込まれてるだけで楽しいし勉強になるのが良いですね。

そういえばこの回のときに某CMS製品でさんざん触ったzope3のコンポーネントを最小限組み合わせてなにか出来ないかと色々実験してました。その流れで「どうもeggというものを理解した方が良さそうだけど全然わからん」と思って勉強し始めたのもこの頃。

PySpaとは別件ですが、Plone関連で知り合いだった寺田さん、たかのりさんと3人で `Zope/Plone開発勉強会`_ (15回目にPython mini hack-a-thonに名前を変えました)を始めたのもこの頃です。

.. _`Zope/Plone開発勉強会`: http://atnd.org/events/709

* :doc:`../648/index`
* :doc:`../649/index`
* :doc:`../650/index`
* :doc:`../651/index`
* :doc:`../652/index`
* :doc:`../654/index`

.. （その某製品自体はこの頃には（略））。


PySpa 第6回目 2009/10/23 - 25
================================
.. raw:: html

   <object width="600" height="450"> <param name="flashvars" value="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157627558403883%2Fshow%2F&page_show_back_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157627558403883%2F&set_id=72157627558403883&jump_to="></param> <param name="movie" value="http://www.flickr.com/apps/slideshow/show.swf?v=122138"></param> <param name="allowFullScreen" value="true"></param><embed type="application/x-shockwave-flash" src="http://www.flickr.com/apps/slideshow/show.swf?v=122138" allowFullScreen="true" flashvars="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157627558403883%2Fshow%2F&page_show_back_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157627558403883%2F&set_id=72157627558403883&jump_to=" width="600" height="450"></embed></object>

非常に印象深い回。

この回のPySpaのちょっと前に行われた :doc:`(第1回)Zope/Plone開発勉強会 <../656/index>` で Expert Python Programming という本を知って、早速買ってPython温泉に持ってきていました。で、参加者にはおなじみの階段下にいた人たちに目次をちょっと紹介していたらけっこう反応が良かったので、その場の勢いで1時間くらいで目次だけ翻訳してblogに載せてみたりしました (:doc:`../680/index`)。

この目次の翻訳に `methaneがコメントをくれた`_ んですが、この頃はまだ `@methane`_ のことを知りませんでした。2週間後の ``Python Hack-a-thon`` ( `@Voluntas`_ 主催の、後の #pyfes。miniじゃない方) でVoluntasに紹介されることになり、4人で翻訳を始めることになります。

エキPyの翻訳中にデスクリプタの話が出てきて、「これこの間のPySpaで追っかけてたところだねー」と渋川さんと話したりしてました。エキPy翻訳をしてPythonのことをたくさん学んだし、その後読書会で人に説明することで更に勉強になりました。翻訳して一番得をしてるのは翻訳者の自分だったと思うので、みんなも温泉入って翻訳すると良いと思います。

.. _`methaneがコメントをくれた`: /blog/680/index.txt

* :doc:`../677/index`
* :doc:`../678/index`
* :doc:`../679/index`
* :doc:`../680/index`



PySpa 第7回目 2010/06/25 - 27
================================

.. raw:: html

   <object width="600" height="450"> <param name="flashvars" value="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157627550201881%2Fshow%2F&page_show_back_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157627550201881%2F&set_id=72157627550201881&jump_to="></param> <param name="movie" value="http://www.flickr.com/apps/slideshow/show.swf?v=122138"></param> <param name="allowFullScreen" value="true"></param><embed type="application/x-shockwave-flash" src="http://www.flickr.com/apps/slideshow/show.swf?v=122138" allowFullScreen="true" flashvars="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157627550201881%2Fshow%2F&page_show_back_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157627550201881%2F&set_id=72157627550201881&jump_to=" width="600" height="450"></embed></object>

2010年4月末に `タイムインターメディア`_ を退職して、5月に :doc:`エキスパートPythonプログラミングが発売 <../717/index>` されて、6月からフリーランスとして活動し始めた頃の回。写真はあるけど、当日なにをやっていたかはblog書いてなかったので覚えてません。最近もあまりblog書けてないのでまずいなあ。当時、フィンランドの某社から声をかけられていたり、個人的にも色々あり4末で退職したのですが、その話がなくなっちゃったんですね。以前からPySpaで個人事業主とかフリーランスとか色々単語が飛び交っていたので、じゃあ自分もちょっとだけやってみるかと思って始めてみました。普段のhack-a-thonや勉強会ではあんまりフリーランスについての話とか聞かないので、そういう意味ではここにもPySpa効果が出てるのかもしれません。

ところで、前回転職したときは無職期間が0日だったので、今回は3ヶ月くらい間を空けてみようと思ったんですが、6月ってちょうど税金とか色々ある時期なんですよね。あと年金とか市民税とか色々会社が払っていたものを自分で払うことになるし、個人事業主だと仕事しても支払いは月末締めの翌々月末払いだったりするので（6月に働いたお金は8月末に入金される）、計算してみたら自分の貯金では無職は1ヶ月が限界でした。フリーランスやろうとしてる人はこのあたり気をつけましょう。


PySpa 第10回目 最終回 2011/11/18 - 20
=======================================

.. raw:: html

   <object width="600" height="450"> <param name="flashvars" value="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157628046164641%2Fshow%2F&page_show_back_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157628046164641%2F&set_id=72157628046164641&jump_to="></param> <param name="movie" value="http://www.flickr.com/apps/slideshow/show.swf?v=122138"></param> <param name="allowFullScreen" value="true"></param><embed type="application/x-shockwave-flash" src="http://www.flickr.com/apps/slideshow/show.swf?v=122138" allowFullScreen="true" flashvars="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157628046164641%2Fshow%2F&page_show_back_url=%2Fphotos%2Fshimizukawa%2Fsets%2F72157628046164641%2F&set_id=72157628046164641&jump_to=" width="600" height="450"></embed></object>


PySpa最終回、この回の4日後に来宮から25kmくらい南の伊豆高原のあたりで :doc:`結婚式してきました <../767/index>` 。 :doc:`11月1日に結婚した <../764/index>` のですが、結婚したらしばらくはイベント参加を減らそうと思っていた事もあり、PySpa最終回だったこともあり、この回だけはどうしても参加したかったんですよね。

フリーランスはこの年の5月まで1年ちょっとやっていました。その間に `タイムインターメディア`_ 様でPythonのお仕事をしたり、 `万葉`_ 様でRailsのお仕事をしたり、 BeProud_ 様でDjangoのお仕事をしたりしてました。一人では出来なそうな規模の仕事の依頼を受けたこともあってBeProud様と組んで仕事を受けたんですが、長くなりそうだったこともあり途中からBeProudに入社して、2012年末の今もそのお客さんの仕事をしています。

.. _`万葉`: http://everyleaf.com/
.. _BeProud: http://www.beproud.jp/

まとめ
=============

ということで、PySpaに行ってなければもしかしたら退職してフリーランスにならなかったかもしれないし、BeProudにも入らなかったかもしれません。そういう意味では `@akisutesama`_ の言うとおり **PySpa経由で** 入社したのかもしれないですね。PySpaすごい！


明日の `PySpaアドベントカレンダー`_ は `@everes`_ の親分です。親分よろしくお願いします！！


.. _`@aodag`: https://twitter.com/aodag
.. _`@everes`: https://twitter.com/everes
.. _`@Voluntas`: https://twitter.com/Voluntas
.. _`@methane`: https://twitter.com/methane
.. _`@shibukawa`: https://twitter.com/shibukawa
.. _`@IanMLewis`: https://twitter.com/IanMLewis
.. _`@feiz`: https://twitter.com/feiz
.. _`@akisutesama`: https://twitter.com/akisutesama


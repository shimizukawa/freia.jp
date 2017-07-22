:date: 2012-07-04 12:00:00
:tags: JavaScript, SenchaTouch2, ExtJS

============================================
2012/07/04 Sencha Touch 2 はじめました
============================================

あ、始めたのは3月末くらいです。忘れないようにこれからいくつかメモを残していこうと思います。

最近、必要があってSencha Touchを使ったiOSアプリのモックアップの作成などを行っています。
最初はjQuery MobileとSencha Touch 2どちらを使ってモックアップを作成しようかちょっと比較してみたりもしましたが、
jQuery Mobile はあくまでモバイル向けWebサイト作成用で、Senchaはアプリケーション作成向けだろうということになり、
Senchaを使ってアプリっぽいものを作っています。

jQuery Mobile と Sencha の比較検討についてはけっこうみんな気になるところなんでしょうね。

* `jQuery Mobile と　jQTouch と Sencha Touch の事など - 牌語備忘録 - pygo <http://d.hatena.ne.jp/CortYuming/20110924/p1>`__
* `Sencha Touch vs jQuery Mobile &#8212; a first look | Code for Concinnity <http://cfc.kizzx2.com/index.php/sencha-touch-vs-jquery-mobile-a-first-look/>`__

Sencha Touch そのものの紹介などは自分はやらないので、以下の記事等を参考にすると良いと思います。

* `Sencha Touch について調べました。 | ありえるえりあ <http://dev.ariel-networks.com/wp/archives/973>`__


Sencha Touch 2
===================

ところで自分がSenchaに着手したのは3月末くらいで、ちょうどその頃にSencha Touch 2がリリースされていました。
Sencha Touch 1 を使ったことがないのですが紹介記事などを見ていると良さそうに思えます。

* `HTML5ベースのモバイルアプリが作れる「Sencha Touch 2.0」公開。性能向上とiOS/Androidネイティブ変換機能が目玉 － Publickey <http://www.publickey1.jp/blog/12/html5sencha_touch_20iosandroid.html>`__
* `Sencha Touch 2 First Look :) | ありえるえりあ <http://dev.ariel-networks.com/wp/archives/1056>`__

短期間で成果物を作ろうとしてるならリリース直後のものは避けますが、今回は新しい方が良い事情もあり、2の方を使うことになりました。

Sencha Touch 2はリリースされたばかりだし、 Sencha Touch 1とは異なりコンポーネント分割して作ると良いらしいということもあり、頼れるのは公式ドキュメントと公式のサンプルコード集な訳ですが、大前提になるExtJSの知識とSencha Touch 1の知識がないためドキュメントを読んでも分からないことがあったり、ドキュメントが間違っていたり、バグがあったり等で始めた直後はプログラムが動かないときに切り分けすら出来ないことが何度もありました（今もあるな・・）。

あ、公式ドキュメントの読み方（というか探検の仕方）に慣れるのにも多少かかりました。

* `Sencha Docs Touch 2.0 <http://docs.sencha.com/touch/2-0/>`__

サンプルコードデモは実装したい動きに近いものを探してコードを読むには良いですね。これを読んでからドキュメントを読むと何となく使い方が分かる気がします。

* `Kitchen Sink Example - Sencha Docs Touch 2.0 <http://docs.sencha.com/touch/2-0/#!/example/kitchen-sink>`__


コード例
============
とりあえずJavaScriptを書くつもりで構えない方が良い気がします。

`Building your First App - Sencha Docs Touch 2.0 <http://docs.sencha.com/touch/2-0/#!/guide/first_app>`__ から一番小さいコードを引用します。

.. code-block:: javascript

   Ext.application({
       name: 'Sencha',

       launch: function() {
           Ext.create("Ext.tab.Panel", {
               fullscreen: true,
               items: [
                   {
                       title: 'Home',
                       iconCls: 'home',
                       html: 'Welcome'
                   }
               ]
           });
       }
   });

これをapp.jsに保存しておいて、index.htmlはこんな感じに書けば動くはず(確認してない):

.. code-block:: html

   <!DOCTYPE html>
   <html lang="en">
       <head>
           <meta charset="UTF-8">
           <title>sencha</title>
           <meta name="viewport" content="width=device-width, initial-scale=1">
           <link rel="stylesheet" href="css/sencha-touch.css" type="text/css">
           <script type="text/javascript" src="js/sencha-touch-all.js"></script>
           <script type="text/javascript" src="js/app.js"></script>
       </head>
       <body></body>
   </html>

bodyの中身、書かないんですねー。

ところで、Sencha Docs に掲載されているコード片は、 `Code Editor` と `Live View` をボタンで切り替えればそのままドキュメント上で実行してiPhoneで動作している風に見せてくれるので便利です。最初これに気づかなくて(ChromeでLive Viewが動作しなくて)、もっと早くこれに気づいていれば少しは楽だったかもしれません。Code Editorモードは掲載されているサンプルコードを変更することも出来るので、書き換えてLive Viewモードに切り替えるなどでAPIの把握の役に立ちました。これは知っておくべき。

あと、これも Sencha Docs ですが、ドキュメントにコメントを付けられるようになってて(要ログイン)、APIが間違っているとか、説明が足りなくて使い方が分からないといったところに先人のコメントが埋まってて何度か助かったことがあります。自分も今まで遭遇した問題などをちゃんと検証できたらコメントしないと。

次へ
======

いまだ試行錯誤中なので、ノウハウ、定石、バッドノウハウの区別が出来ていないですが、いまのところ理解している範囲でSencha Touch 2のアプリの書き方をメモしていきたいと思います。

書こうと思っていること（予定）:

* 出来るだけ小さいアプリを作る
* 作ったアプリをコンポーネント分解して改善する
* 複数のviewを1画面に合成する
* どこかのWebAPIと繋いで画面表示する
* Store.filterを使いこなせなくてはまる
* RESTful APIでデータ読み込みしようとしてはまる
* フォームを作って変更を保存する
* ラジオフィールドに値が反映されなくてはまる
* トグルフィールドの変更イベントが発火されなくてはまる
* GoogleのOAuth2で認証してみる
* GoogleMapを表示してみる
* リモートフィルタではまる
* モデルのアソシエーションではまる
* Sencha Touch 2 + Touch Chart 2 でグラフ描画してみる
* sencha コマンドを使ってscaffoldを作る
* sencha コマンドを使ってリリース用にminify,結合等する


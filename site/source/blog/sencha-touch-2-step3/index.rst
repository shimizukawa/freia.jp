:date: 2012-07-17 22:00:00
:categories: ['JavaScript', 'SenchaTouch2', 'ExtJS']
:body type: text/x-rst

======================================================================================
2012/07/17 Sencha Touch 2 で小さなアプリを作る(step3 listenersのコード分割)
======================================================================================

*Category: 'JavaScript', 'SenchaTouch2', 'ExtJS'*

:doc:`../sencha-touch-2-step2/index` の続きです。

前回は以下の分割を行いました。

* View単位で定義を分割しました
* xtypeを使って再利用しやすくなりました

今回はlisteners定義を分割します。コンポーネントの粒度や役割、実装上の機能はなにも変えません。

前回作ったソースコード
=========================

step2では以下のコードが出来ました。

app.js:

.. code-block:: javascript

   Ext.application({
       name: 'App',
       launch: function() {
           Ext.create('Ext.navigation.View', {
               fullscreen: true,
               items: [{
                   xtype: 'mybooklist'
               }]
           });
       }
   });

   Ext.define('App.view.MyBookList', {
       extend: 'Ext.dataview.List',
       xtype: 'mybooklist',

       config: {
           title: 'My Books',
           itemTpl: [
               '<div><strong>{title}</strong></div>',
               '<div><span>{price}</span></div>'
           ],
           store: {
               fields: ['title', 'price'],
               data: [{
                   title: 'エキスパートPythonプログラミング',
                   price: 3780
               },{
                   title: 'Pythonプロフェッショナルプログラミング',
                   price: 2940
               }]
           },
           listeners: {
               itemtap: function (list, index, item, record) {
                   this.getParent().push({
                       xtype: 'mybookdetail',
                       data: record.getData()
                   });
               }
           }
       }
   });

   Ext.define('App.view.MyBookDetail', {
       extend: 'Ext.Panel',
       xtype: 'mybookdetail',

       config: {
           data: {},
           tpl: [
               '<table>',
                   '<tr>',
                       '<th>Title:</th>',
                       '<td>{title}</td>',
                   '</tr>',
                   '<tr>',
                       '<th>Price:</th>',
                       '<td>{price}</td>',
                   '</tr>',
               '</table>'
           ]
       }
   });


このコードではlistenersの部分に直接イベントハンドラ関数を実装しています。この実装の問題点の把握と改善を行います。

イベントリスナー定義とコンポーネントアクセスを抽象化して分割する
==================================================================

問題の把握
-----------

まずは問題を把握するため、mybooklistのlistners周りのコードを再掲します。

.. code-block:: javascript

   Ext.define('App.view.MyBookList', {
       extend: 'Ext.dataview.List',
       xtype: 'mybooklist',

       config: {
           title: 'My Books',
           itemTpl: [...],  //省略
           store: {...},  //省略
           listeners: {
               itemtap: function (list, index, item, record) {
                   this.getParent().push({
                       xtype: 'mybookdetail',
                       data: record.getData()
                   });
               }
           }
       }
   });


listnersにはitemtapイベントに対するハンドラ関数が実装されています。これによりmybooklistの要素(item)がタップ(tap)されたときにitemtapイベントをlistenersで捕まえてハンドラ関数でイベントに対する処理を行っていますが、この実装には2つの問題があります。

1つ目の問題は、ハンドラ関数内に ``this.getParent().push(...)`` という記述があり、mybooklistコンポーネントの親コンポーネントがnavigationview(Ext.navigation.View)であることが期待されている事です。せっかくコンポーネント分割したのに、mybooklistコンポーネントをnavigationview以外の子要素としては使えない実装になっています。

2つ目の問題は、mybooklistというViewコンポーネントで表示上の定義・実装以上に、一覧に表示された要素(item)をタップしたときの挙動まで定義・実装してしまってい事です。これではmybooklistを別の場所で再利用しようとしたときに操作に対する挙動が同じになります。

この問題を解決するために、Sencha Touch 2で導入されたコントローラを使うように実装を変更します。


コントローラの導入
--------------------

まずはコントローラを使えるようにするため、アプリケーションの実装部分をすこし変更します。

.. code-block:: javascript

   Ext.application({
       name: 'App',

       // 'Main' コントローラを使用することを宣言し、フレームワークに自動的にロードさせる
       controllers: ['Main'],

       launch: function() {
           Ext.create('Ext.navigation.View', {
               fullscreen: true,

               // コンポーネントに任意のIDを割り当て、コントローラ等からIDで参照させる
               id: 'main',

               items: [{
                   xtype: 'mybooklist'
               }]
           });
       }
   });

変更したのはコメントを入れてある2カ所です。

まず1つ目は、アプリケーション自体にコントローラを関連づけるため(?) ``controllers`` にこれから実装するコントローラ名 'Main' を指定します。'App'アプリケーションの'Main'コントローラなので、フルネームは'App.controller.Main'です。

.. todo:: 上記のcontrollers宣言とフルネームについて説明しているURLを記載

2つ目は、navigationviewコンポーネントのpush()メソッドにコントローラから呼び出したいので、コントローラがnavigationviewのインスタンスがどこにあるか知らなくても取得できるようにIDを設定します。

それでは次に、コントローラ 'App.controller.Main' の定義を追加します。

.. code-block:: javascript

   // 'App'のcontroller 'Main' を定義
   Ext.define('App.controller.Main', {

       // コントローラのクラスを継承
       extend: 'Ext.app.Controller',

       config: {
           // refsで名前とID等を関連づける
           refs: {
               // '#main'(= IDがmain)に'main'という名前を関連づける。これで
               // コントローラ.getMain()等でコンポーネントを取得できるようになる。
               main: '#main'
           },
           // 操作に対するイベントリスナーを定義する
           control: {
               // 'mybooklist' (この例ではxtypeで指定) に対するイベントリスナー
               mybooklist: {
                   // 'itemtap'イベント発生時に'showMyBookDetail'メソッドを実行
                   itemtap: 'showMyBookDetail'
               }
           }
       },

       // イベントハンドラの実装
       showMyBookDetail: function (list, index, item, record) {
           // thisはコントローラ。this.getMain()で '#main' を取得するようrefsで
           // 定義している。'#main' はnavigationviewにID=mainで指定している。
           this.getMain().push({
               xtype: 'mybookdetail',
               data: record.getData()
           });
       }
   });

``refs`` はコントローラ内でidやxtypeで指定したコンポーネントを扱うために定義しています。

.. todo:: refsのリファレンスのURL。もうすこし説明を追加。

``control`` には色々なコンポーネントの色々なイベントリスナーを定義します。

.. todo:: controlのリファレンスのURL。もうすこし説明を追加。refsと組み合わせた書き方とかあれば紹介


最後に、コントローラに実装を移して不要となったmybooklistのlistenersを削除します。

.. code-block:: javascript

   Ext.define('App.view.MyBookList', {
       extend: 'Ext.dataview.List',
       xtype: 'mybooklist',

       config: {
           title: 'My Books',
           itemTpl: [...],  //省略
           store: {...},  //省略
           //listeners: {...}  //削除
       }
   });





ここまでのまとめ
===================

* イベント処理をコントローラに分離しました

mybooklist はまだstoreの定義が残っているので、次回からはこれを分割していきます。

.. note::

   なお、ソースコードは全て https://bitbucket.org/shimizukawa/sencha-touch2-exercise のstep3ディレクトリにあります。

   また、スマートフォンから http://dlvr.it/1pyvt3 にアクセスすれば、ここで作ったアプリを実際に操作出来ます。


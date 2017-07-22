:date: 2012-07-18 17:10:00
:tags: JavaScript, SenchaTouch2, ExtJS

======================================================================================
2012/07/18 Sencha Touch 2 で小さなアプリを作る(step3 listenersのコード分割)
======================================================================================

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

この問題を解決するために、コントローラを使うように実装を変更します。


コントローラの導入
--------------------

まずはコントローラを使えるようにするため、アプリケーションの実装部分をすこし変更します。

.. code-block:: javascript

   Ext.application({
       name: 'App',

       // 'Main' コントローラを使用することを宣言し、フレームワークに自動的にロードさせる。
       // 今回のコードは全てapp.jsに記述しているのでロードのためではなくコントローラの利用を
       // フレームワークに伝えるために記載している。
       // `requires ['App.controller.Main']` と等価、ではない。
       controllers: ['Main'],

       launch: function() {
           Ext.create('Ext.navigation.View', {
               fullscreen: true,

               // コンポーネントに任意のIDを割り当て、コントローラ等からIDで参照させる
               id: 'mainview',

               items: [{
                   xtype: 'mybooklist'
               }]
           });
       }
   });

変更したのはコメントを入れてある2カ所です。

まず1つ目は、アプリケーション自体にコントローラを関連づけるため(?) ``controllers`` にこれから実装するコントローラ名 'Main' を指定します。'App'アプリケーションの'Main'コントローラなので、フルネームは'App.controller.Main'です。

.. seealso:: 上記のcontrollers宣言とフルネームについて詳しくは http://docs.sencha.com/touch/2-0/#!/guide/mvc_dependencies を参照してください。

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
               // '#mainview'(= IDがmainview)に'main'という名前を関連づける。これで
               // コントローラ.getMain()等でコンポーネントを取得できるようになる。
               main: '#mainview'
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
           // thisはコントローラ。this.getMain()で '#mainview' を取得するようrefsで
           // 定義している。'#mainview' はnavigationviewにID=mainviewで指定している。
           this.getMain().push({
               xtype: 'mybookdetail',
               data: record.getData()
           });
       }
   });

``refs`` はコントローラ内でidやxtypeで指定したコンポーネントを扱うために定義しています。この例では ``main`` という名前で ``#mainview`` を取得できるように定義しています。IDを指定する場合はCSSセレクタのように ``#`` を付けます。付けない場合はxtypeとして解釈されます。

refsで定義した名前を使って、コントローラ内で ``this.getMain()`` のようにコンポーネントのインスタンスを取得できます。'main'なので'getMain()'。もし'foo_bar'という名前を付けていたら'getFoo_bar()'で取得します。これは内部的には ``Ext.ComponentQuery.query('#mainview')`` と同義です。refsの書き方次第では異なるマッピングも出来るようですが詳しくは `Refs and Control :: Controllers - Sencha Docs - Touch 2.0`_ を参照して下さい。


``control`` には色々なコンポーネントの色々なイベントリスナーを定義します。この例では、mybooklistコンポーネントのitemtapイベントをshowMyBookDetailメソッドでハンドリングするように定義しています。ところで、mybooklistという指定はComponentQueryの表現ですが、ここにはrefsの名前を指定することも出来ます。

controlの中に直接showMyBookDetailの実装を書かないようにしていますが、こうしておくことで読みやすくなり、他のところで同じハンドラを簡単に使えるようになります。

showMyBookDetailメソッドでは先ほど定義したrefsを使って#mainviewのpush()を呼び出すようにしました。これでコンポーネントの階層構造が変わっても実装を変える必要がなくなりました（例えば、今は '#mainview > mybooklist' という構造ですが、タブUIを追加する場合 '#mainview > tabpanel > mybooklist' といった構造に変わる可能性があります）。


refsで'#mainview'と書いた部分やcontrolで'mybooklist'と書いた部分には、実際にはComponentQueryの書式で記載することが出来ます。例えば ``#mainview > mybooklist`` は#mainviewコンポーネントの直下のmybooklistコンポーネントの意味になります。CSSセレクタ的に色々書くことが出来ます。書式については `Ext.ComponentQuery - Sencha Docs - Touch 2.0`_ を参照して下さい。


.. _`Refs and Control :: Controllers - Sencha Docs - Touch 2.0`: http://docs.sencha.com/touch/2-0/#!/guide/controllers-section-3
.. _`Ext.ComponentQuery - Sencha Docs - Touch 2.0`: http://docs.sencha.com/touch/2-0/#!/api/Ext.ComponentQuery


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



最終的に
----------

以下のコードが出来ました。（#mainviewを#mainに変えてあります）

app.js:

.. code-block:: javascript

   Ext.application({
       name: 'App',
       controllers: ['Main'],

       launch: function() {
           Ext.create('Ext.navigation.View', {
               fullscreen: true,
               id: 'main',
               items: [{
                   xtype: 'mybooklist'
               }]
           });
       }
   });

   Ext.define('App.controller.Main', {
       extend: 'Ext.app.Controller',

       config: {
           refs: {
               main: '#main'
           },
           control: {
               mybooklist: {
                   itemtap: 'showMyBookDetail'
               }
           }
       },

       showMyBookDetail: function (list, index, item, record) {
           this.getMain().push({
               xtype: 'mybookdetail',
               data: record.getData()
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


ここまでのまとめ
===================

* イベント処理をコントローラに分離しました

コントローラのrefsやcontrolは自分もまだ良く理解できていない部分がありますが、この例のように使うくらいであれば使えています。また、refs,control以外にもroutesなどの設定も出来るようですが、使ったことがないので説明できません。

次回は、mybooklistにまだstoreの定義が残っているので、これを分割していきます。

.. note::

   なお、ソースコードは全て https://bitbucket.org/shimizukawa/sencha-touch2-exercise のstep3ディレクトリにあります。

   また、スマートフォンから http://dlvr.it/1pyvt3 にアクセスすれば、ここで作ったアプリを実際に操作出来ます。


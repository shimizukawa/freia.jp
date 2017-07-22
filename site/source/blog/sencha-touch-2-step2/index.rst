:date: 2012-07-11 17:00:00
:tags: JavaScript, SenchaTouch2, ExtJS
:body type: text/x-rst

======================================================================================
2012/07/11 Sencha Touch 2 で小さなアプリを作る(step2 Viewコンポーネントのコード分割)
======================================================================================

:doc:`../sencha-touch-2-step1/index` の続きです。
前回作った小さいアプリのコードをコンポーネント毎に分割します。
今回は、コンポーネントの粒度や役割、実装上の機能はなにも変えません。

前回作ったソースコード
=========================

以下のコードが出来ました。

app.js:

.. code-block:: javascript

   Ext.application({
       name: 'App',

       launch: function() {
           Ext.create('Ext.navigation.View', {
               fullscreen: true,
               items: [{
                   xtype: 'list',
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
                               xtype: 'panel',
                               data: record.getData(),
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
                           });
                       }
                   }
               }]
           });
       }
   });

これはコンポーネント内で別のコンポーネントの定義を直接行っているので、これらを分割して見通しを良くします。

書き方の違いを把握する
=======================

Sencha Touch 2 では(1も?)コンポーネントを使うときに、インスタンス化して使う、xtypeを指定して使う、の大きく分けて2つの使い方があります。
例えばlist(Ext.dataview.List)コンポーネントを使った書籍一覧表示を実装するときに以下の複数の書き方が出来ます。

xtypeに'list'(Ext.dataview.List)を指定して使う場合(一部省略していますが、前回実装したコードのままです):

.. code-block:: javascript

   Ext.application({
       name: 'App',
       launch: function() {
           Ext.create('Ext.navigation.View', {
               fullscreen: true,
               items: [{
                   // ここで利用するコンポーネントとして'list'(Ext.dataview.List)を指定。
                   // 必要になったときにインスタンス化される。
                   xtype: 'list',

                   title: 'My Books',
                   itemTpl: [...],
                   store: {...},
                   listeners: {...}
               }]
           });
       }
   });


'list'(Ext.dataview.List)をインスタンス化して使う:

.. code-block:: javascript

   Ext.application({
       name: 'App',
       launch: function() {
           // Ext.dataview.Listコンポーネントを事前にインスタンス化しておく。
           // パラメータをExt.createの第2引数に指定してインスタンスを初期化。
           var books = Ext.create('Ext.dataview.List', {
               title: 'My Books',
               itemTpl: [...],
               store: {...},
               listeners: {...}
           });
           // booksのインスタンス化はlaunch内で行う。
           // app.jsロード時に実行してしまうとsenchaフレームワークの初期化が
           // 完了して無くて(想像)、listenersでイベントを捕まえられない。
           // 想像が合っていれば、listeners以外にも問題がありそう。

           Ext.create('Ext.navigation.View', {
               fullscreen: true,

               // booksのインスタンスをitemsに指定
               items: [books]
           });
       }
   });

前者のようにxtypeを指定して実装した場合、後者のようなインスタンス化などはSencha Touch 2 の内部で自動的に行われます。
この例では後半のコード内でインスタンス化した変数booksを参照しており、分割はできたものの実装順序や実行タイミングに気をつける必要が出てきました。

分割して書きたいけどインスタンス化は今は行いたくないし、実装順序を気にしたくない、ということもあります。この場合、listを継承した独自のクラスを実装する方法が使えます。

'list'(Ext.dataview.List)を継承して新しいクラスを定義する:

.. code-block:: javascript

   Ext.application({
       name: 'App',
       launch: function() {
           Ext.create('Ext.navigation.View', {
               fullscreen: true,

               // xtypeでitemsを指定
               items: [{xtype: 'mybooklist'}]
           });
       }
   });

   // Ext.defineで新しいクラスを定義
   Ext.define('App.view.MyBookList', {
       // 継承元の指定。文字列で指定出来ます。
       extend: 'Ext.dataview.List',

       // 独自のxtypeを定義
       xtype: 'mybooklist',

       // 設定可能なフィールドのデフォルト値指定。
       // config属性に書きます。
       config: {
           title: 'My Books',
           itemTpl: [...],
           store: {...},
           listeners: {...}
       }
   });


この例では新しいApp.view.MyBookListを定義したときに、外部から参照されるためのxtypeを定義しています。定義したxtype='mybooklist'はExt.navigation.Viewコンポーネントのインスタンスから参照しています。xtypeのおかげでインスタンス化せずに他のコンポーネントで扱いやすくなり、実装順序も気にしなくて良くなりました。

ちなみに、もしApp.view.MyBookListのインスタンスが欲しくなったときには以下のように書きます:

.. code-block:: javascript

   var books = Ext.create('App.view.MyBookList');

タイトルを変えたい場合は以下のようにしてconfig部分をオーバーライド出来ます:

.. code-block:: javascript

   var books = Ext.create('App.view.MyBookList', {title: 'MyBooks2'});

同様に、xtype指定で使うときにもオーバーライド出来ます:

.. code-block:: javascript

   items: [{
      xtype: 'mybooklist',
      title: 'MyBooks3'
   }]


Viewのコードを分割
===================

xtypeを使ってViewコンポーネントの記述を分割していきます。

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


2つのViewクラス ``App.view.MyBookList (xtype: mybooklist)`` と ``App.view.MyBookDetail (xtype: mybookdetail)`` を定義しました。

mybookdetail はconfigのdata属性を設定しないとtplのレンダリングが出来ないので、利用時にdataを設定するように書いています(itemtapイベント処理のところ)。このくらい他との依存関係がなくなると再利用しやすくなり、色んなところで本の詳細表示したいときに使えるコンポーネントになりました。

ここまでのまとめ
===================

* View単位で定義を分割しました
* xtypeを使って再利用しやすくなりました

mybooklist はまだlistenerの処理とstoreの定義が多少残っているので、次回からはこれらを分割していきます。

.. note::

   なお、ソースコードは全て https://bitbucket.org/shimizukawa/sencha-touch2-exercise のstep2ディレクトリにあります。

   また、スマートフォンから http://dlvr.it/1pyvt3 にアクセスすれば、ここで作ったアプリを実際に操作出来ます。


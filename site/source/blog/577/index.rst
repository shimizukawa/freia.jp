:date: 2008-06-06 02:29:26
:categories: ['Zope', 'web']
:body type: text/x-rst

========================================
IEで「操作は中断されました」の罠にはまる
========================================

JavaScriptで ``include('foo.js')`` とか書ける様になる include.js というのがあります。

- `JavaScriptMVC - Include`_

やってることは非同期に指定されたファイルを読み込んでHTMLにscriptエレメントを挿入しているだけなんで、単純な用途なら自分で作ってもいいかな、という感じですが、とりあえず使ってみました。

初めのうちは特に問題もなく、Zopeで表示するページに組み込んで使っていたのですが、IE6で動作確認したところ、思わぬ問題が。includeを使うとIE6で ``「操作は中断されました」`` というDLGが出てページが表示されません。色々コードをいじったりググったりして、あるていどの発生条件が分かった気がします。

1. HTMLのロードがまだ完了していないときに
2. 動的にHTMLを変更する（include.jsでincludeを実行する等)
3. <head>タグの最初にbaseタグがZopeによって挿入されている
4. baseタグの挿入により、meta contentTypeタグが<head>直後ではなくなる

Zopeでは例えばフォルダのURLで末尾に'/'を付けていない場合などにZope的に正しいURLをbaseタグとしてZPTのレンダリング結果に挿入します。Zope的に正しいURLにアクセスするとbaseタグは挿入されません。今回の現象はbaseタグが挿入されていない場合には発生しなかったので、(3)を条件に入れています。

.. code-block:: xml

  <head>
    <base href="http://www.example.com/index.html" />
    <meta http-equiv="Content-Type"
          content="text/html; charset=utf-8"/>
    <script type="text/javascript"
            src="/js/include.js"></script>
    ....
  </head>

(4)はどこかのサイトで見かけた情報なので条件に入れてますが、もしかしたら違うかも。

今回は、(1)の条件を無くすために、HTMLロード終了付近(</body>直前)でincludeすることにより回避。onloadハンドリングでなくてもいちおう大丈夫みたい。

.. code-block:: xml

    ....
    <script type="text/javascript">include('/js/foo.js');</script>
  </body>

もう深夜2:30か...。IE6はとっとと無くなってくれ。

.. _`JavaScriptMVC - Include`: http://javascriptmvc.com/learningcenter/include/index.html


.. :extend type: text/html
.. :extend:


.. :comments:
.. :comment id: 2011-01-19.8541924096
.. :title: Re:IEで「操作は中断されました」の罠にはまる
.. :author: Anonymous User
.. :date: 2011-01-19 16:57:35
.. :email: 
.. :url: 
.. :body:
.. この理由かも？
.. http://blogs.msdn.com/b/ie/archive/2008/04/23/what-happened-to-operation-aborted.aspx
.. 
.. include.jsを使ったら、JavascriptのロードはHTMLのパージングのあとなので、問題はなくなります。
.. 

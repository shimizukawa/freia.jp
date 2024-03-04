:date: 2007-04-10 00:43:41
:tags: turbogears

=======================
tgcrudを試す
=======================

TurboGearsの周辺プロジェクトが格納されている http://svn.turbogears.org/projects/ を久しぶりに眺めてみたところ、FastData2とかToscaWidgetsとか色々増えてました。その中にtgcrudというのもあり、昨日tgdatacontrollerを公開した身としては気になるところです。

ということで、早速試してみました。

インストールは easy_install http://svn.turbogears.org/projects/tgcrud/ で終了。以降、以下のようにtg-adminのコマンドとして使えるようになります::

  % tg-admin tgcrud Todo TodoController

上記コマンドを実行するとカレントのプロジェクトにTodoControllerという名前でcrudフォーム用のcontrollerのソースコードが追加されるので、これを好きなURLにマッピングして使う、というアプローチのようです。

http://groups.google.com/group/turbogears/browse_thread/thread/7abbf88d4edb36ba/cfec4759cf29f55e?lhl=ja

しかし、上記のリリースノートにもあるように、特別なことが出来るようになるわけではなく、crudフォームを作る時のコード作成の手助けをしてくれるだけのものです。また、現時点では、指定したModelのフィールド情報からWidgetを選択してコード生成してくれるわけでもないので、この点については今後の発展に期待、というところです。

生成されたコードから先は各自で実装する必要があるので、細かなカスタマイズはしやすいのかもしれませんが、コード生成は個人的にはあまり好きじゃなかったりします。(VC++の頃のいやな思い出が...)

いろんな意味でtgdatacontrollerとは対極のアプローチ。


ところで、SQLObjectとSQLAlchemyの両方に対応しているのは良い点なのですが、O/Rマッパーの自動判定分岐が真偽反転していて、SQLObject使ってるのにSQLAlchemyのコードをはき出されて、ちょっと悩みました、ってことで、 `バグレポ`_ しました。片言の英語とコマンドラインとdiff貼り付けできっと通じる。

.. _`バグレポ`: http://trac.turbogears.org/ticket/1351


.. :extend type: text/html
.. :extend:



.. image:: 20070410_tgcrud.*
   :width: 33%


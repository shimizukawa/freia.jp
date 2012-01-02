:date: 2007-04-08 23:57:32
:categories: ['turbogears']
:body type: text/x-rst

=======================================
2007/04/08 TurboGearsのお手軽Controller
=======================================

*Category: 'turbogears'*

TurboGearsを使っていて最初に不満に思ったのは、crudフォームとしてcatwalkが提供されているものの、あれをそのまま実運用で使うことは出来ない＆カスタマイズが難しい、ということでした。Ploneほどのcrud機能は無くても良いので、Model定義すしただけで項目の一覧表示、追加、削除、編集、バリデーションが出来ればいいなあ、と思っていました。

色々調べて、DataGrid -> AjaxGrid -> TGFastData と順に使っていったのですが、TGFastDataでもまだ望む機能は満たされていませんでした（あとTGFastDataは0.9a6の時点からメンテナンスされていないようです）。そこで、TGFastDataをもうちょっと使いやすくした仕組みを作ってみました。名前は安直にtgdatacontroller。

tgdatacontrollerは、出来るだけ少ない実装で項目の一覧表示と各項目の編集を行うための枠組みです。たとえばグループの一覧表示と編集画面を用意するための最小のコードは以下のようになります。

.. code-block:: python

    class Group(DataControllerEx):
        sql_class = model.Group

また、フィールドの表示順を変更したり、表示する項目を限定する場合は以下の
ように記述します。

.. code-block:: python

    class Group(DataControllerEx):
        sql_class = model.Group
        form_fields = ('group_name', 'display_name', 'created',)

上記クラスはTurbuGearsのcontrollerとして作成されるので、通常のcontroller
と同様にcontroller.pyのRootクラスの属性に設定するなどして利用します。

まあ、あちこちバグがあるし、DataGrid,AjaxGrid,TGFastDataの方向性で育てていくのは、拡張性の面で限界があるので、ある程度まで形になったら、controllerじゃなくてwidgetにバラして再構築かなー。

SVNは以下のURLですが、easy_installには対応していません。

- http://svn.freia.jp/open/tgdatacontroller/

Screen Castも作ってみました。7分。微妙。YouTubeだと文字が潰れるよ

- http://devcamp.freia.jp/others/tgdatacontroller.wmv


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2007-04-15.0568224749
.. :title: Re:TurboGearsのお手軽Controller
.. :author: しみずかわ
.. :date: 2007-04-15 17:50:57
.. :email: 
.. :url: 
.. :body:
.. リポジトリのURLが変わりました。詳しくは以下を参照。
.. 
.. tgdatacontrollerをegg化
.. http://www.freia.jp/taka/blog/445
.. 

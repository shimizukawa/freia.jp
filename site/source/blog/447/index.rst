:date: 2007-04-16 00:02:19
:categories: ['Plone']
:body type: text/x-rst

=======================================
COREBlog2のカテゴリの関連づけと表示権限
=======================================

`PloneでReferenceのW/F状態による色分け`_ や `COREBlog2のオブジェクトの関連づけと表示権限`_ で行った対策で、COREBlog2のエントリが関連付いている画像などが非公開状態の場合に、赤文字で表示したり閲覧時に認証画面が出ないようにしたつもりだった。でも実はカテゴリも同じように対処が必要だったことが今日発覚。あたらしく追加したJavaScriptカテゴリを公開にするのを忘れていたようだ。

ということで、同じように対策してみた。対策内容は添付のpatchを参照のこと。

前回の対策と合わせて `COREBlog2 - Trac`_ に提案登録してみよう。


.. _`COREBlog2のオブジェクトの関連づけと表示権限`: http://www.freia.jp/taka/blog/431/
.. _`PloneでReferenceのW/F状態による色分け`: http://www.freia.jp/taka/blog/429
.. _`COREBlog2 - Trac`: http://coreblog.org/trac/coreblog2/


.. :extend type: text/html
.. :extend:

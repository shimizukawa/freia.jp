:date: 2007-03-08 23:58:23
:categories: ['Plone']
:body type: text/x-rst

=================================================================
2007/03/08 Trackback禁止エントリでTrackback通知メールを送信しない
=================================================================

`COREBlog2の各エントリのTrackback設定を一括変更する`__ で遭遇した問題についてコードを確認してみた。

.. __: http://www.freia.jp/taka/blog/410

.. epigraph::

  ところで、この方法でいじくったせいかわからないけど、TB禁止なエントリにTBを受けるとメールによる通知だけ届く現象に遭遇中。実際にTBは保存されていないので実害はないけれど、ちょっと気になる。明日調べてみよう。あと、Blogの設定でデフォルトTBステータスを設定しても反映されないような。まとめて明日チェック。

まず、TB禁止エントリへのTBでメールが通知されるのは ``COREBlog2\skins\COREBlog2\tbping.py`` でメールの送信を行ってからTBをエントリに追加する ``addTrackback2Entry`` を呼んでいて、ここでTB追加禁止がチェックされているからだった。つまりメールの送信をこの関数内で行うようにするか、関数の返値を見てメール送信するかどうかを判断すればよい。

次にBlogのデフォルトTBステータスが新規作成したエントリに反映されていない現象については、反映するように実装されてないからだった。そして `COREBlog2のTrac`_ を見てみたら報告があがっていた。未実装なのかな？

.. _`COREBlog2のTrac`: http://coreblog.org/trac/coreblog2/ticket/50


.. :extend type: text/x-rst
.. :extend:

とりあえず自分で使うのに不便なので実装してデフォルト値対応してみた。

.. code-block:: python

    --- COREBlog2/content/coreblogentry.py.orig	Sun Feb 25 03:02:45 2007
    +++ COREBlog2/content/coreblogentry.py	Fri Mar 09 00:12:52 2007
    @@ -197,6 +197,7 @@
         IntegerField('allow_comment',
             searchable=0,
    -        default = 2,
    +        default_method='getDefaultCommentStatus',
             widget=SelectionWidget(label='Comment status',
                 label_msgid='label_allow_comment',
                 description_msgid='help_allow_comment',
    @@ -207,7 +208,7 @@
     
         IntegerField('receive_trackback',
             searchable=0,
    -        default = 2,
    +        default_method='getDefaultTrackbackStatus',
             widget=SelectionWidget(label='Trackback status',
                 label_msgid='label_receive_trackback',
                 description_msgid='help_receive_trackback',
    @@ -324,6 +325,13 @@
         trackback_open = 2
         trackback_closed = 3
     
    +    def getDefaultTrackbackStatus(self):
    +        blog = self.blog_object()
    +        return blog.getReceive_trackback_default()
    +
    +    def getDefaultCommentStatus(self):
    +        blog = self.blog_object()
    +        return blog.getAllow_comment_default()
     
         def initializeArchetype(self, **kwargs):
             ATCTContent.initializeArchetype(self, **kwargs)

フィールドのdefault_method引数の使い方は `Archetypesマニュアル`_ に書いてあるけど、値にはstringを渡せと書いてあって、インスタンス作成後にcontextにbindして呼び出してくれる。あるいはcallableオブジェクトを設定してもちゃんと呼び出してくれる。

ところで、同じ物をCOREBlog2のTracにも貼っておこうと思ったのだけど、新しいチケットを発行できなかった。なんでだろう？MLの方で聞いてみよう。

.. _`Archetypesマニュアル`: http://plone.org/documentation/manual/archetypes-developer-manual/fields/fields-reference


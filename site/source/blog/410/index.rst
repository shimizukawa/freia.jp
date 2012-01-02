:date: 2007-03-08 01:49:34
:categories: ['Plone']
:body type: text/x-rst

==================================================
COREBlog2の各エントリのTrackback設定を一括変更する
==================================================

COREBlog2_ はトラックバックの受付と表示について、各エントリ毎に

- 追加不可/非表示 
- 追加可能/表示 
- 追加不可/表示

を選択できる。これは各エントリに保存されるので、後からUIで変更しようと思うと全部のエントリを一つ一つ変更していく事になってしまう。これではひたすら面倒なのでScript(Python)を書いて一括変更してしまえ、と。

.. _COREBlog2: http://coreblog.org/


.. :extend type: text/x-rst
.. :extend:
.. code-block:: python

    cb = context.blog
    entries = cb.objectValues(['COREBlogEntry'])
    print len(entries), 'entries'
    
    for ent in entries:
        ent.setReceive_trackback(3)
    
    return printed

でけた。

coreblogentry.pyのスキーマ定義を見るとentry_trackbacksというフィールドがある。

.. code-block:: python

    IntegerField('receive_trackback',
        searchable=0,
        default = 2,
        widget=SelectionWidget(label='Trackback status',
            label_msgid='label_receive_trackback',
            description_msgid='help_receive_trackback',
            i18n_domain='plone',),
        vocabulary=DisplayList(trackback_status),
        schemata='cbentry_extented_fields',
        ),

このフィールドが取り得る値はtrackback_statusで定義されていて、今回はTB禁止にしたいので3を設定すればよい、と。Archetypesではフィールドのsetter,getterメソッドは自動的に生成される。名前の生成規則は基本的に'get'+capitalize(フィールド名)とか'set'+capitalize(フィールド名)で作られるので、今回はsetReceive_trackbackがsetterメソッドになる。

ところで、この方法でいじくったせいかわからないけど、TB禁止なエントリにTBを受けるとメールによる通知だけ届く現象に遭遇中。実際にTBは保存されていないので実害はないけれど、ちょっと気になる。明日調べてみよう。あと、Blogの設定でデフォルトTBステータスを設定しても反映されないような。まとめて明日チェック。

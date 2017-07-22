:date: 2007-03-29 23:12:48
:categories: ['Plone']
:body type: text/x-rst

======================================================
2007/03/29 COREBlog2のオブジェクトの関連づけと表示権限
======================================================

`PloneでReferenceのW/F状態による色分け`_ の続き。色によるW/F状態の表示が出来るようになったので、次は ``非公開`` 状態のオブジェクトに関連づけされていても、(ログイン画面じゃなく)ページが正しく表示されるようにする。

関連づけの仕組みはCOREBlog2の実装ではなくPloneが標準で提供しているのだが（実際はArchetypes）、Ploneの ``関連するページ`` 表示では同じような問題はおきない。なぜか。まずはCOREBlog2のどこでUnauthorizedが発生するのかを調べるため、zope.confのVerboseSecurityを有効にして、ログイン画面が出る現象を再現させる。どうやらgetRefsByKind.pyで発生するようだ。

COREBlog2/skins/COREBlog2/getRefsByKind.py

.. code-block:: python

    for obj in context.getRefs('relatesTo'):

ここのgetRefs呼び出しでアクセス権の問題が起きる。
getRefs は Archetypes/Referenceable.py に実装があって、これはカタログからリファレンスを取得する。
カタログからの取得ではアクセス権のチェック等はされないので、呼出元のScript(Python)に戻るときに権限チェックが行われ、権限チェック中にUnauthorizedがraiseする。

ここでPloneの実装に戻って CMFPlone/skins/plone_content/document_relateditems.pt を見ると、getRefsではなく ``computeRelatedItems`` で取得しているのがわかる。computeRelatedItems の実装は CMFPlone/skins/plone_scripts/computeRelatedItems.py にあって、カタログを使わずに直接Referencesフィールドを参照して権限チェックもやっている。

そこでCOREBlog2のgetRefsByKind.pyを以下のように修正してみた。

.. code-block:: python

    #for obj in context.getRefs('relatesTo'):
    for obj in context.computeRelatedItems():

成功。

ToDo: 置き換えて機能的な変化が発生しないか？


.. _`PloneでReferenceのW/F状態による色分け`: http://www.freia.jp/taka/blog/429


.. :extend type: text/html
.. :extend:


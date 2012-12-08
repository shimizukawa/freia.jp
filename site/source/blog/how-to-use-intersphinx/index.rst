:date: 2012-12-08 18:30
:categories: ['Python', 'Sphinx', 'intersphinx']
:body type: text/x-rst

====================================================================
2012/12/08 intersphinxを使おう - #sphinxjp アドベントカレンダー2012
====================================================================

*Category: 'Python', 'Sphinx', 'intersphinx'*


`Sphinx Advent Calendar 2012`_ 8日目担当の清水川です。昨日は `@takanory`_ の `Sphinx Advent Calendar 7日目: 異なった環境で Sphinx と blockdiag とかを使う`_ でした。

おそらくみなさんはたくさんの人でリレーするこのアドベントカレンダーよりも `Sphinx Advent Calendar 2012 (全部俺)`_ の方が気になっていると思いますが、少しお付き合いください。

------

最近、Sphinx本体のCo-Maintainerになったので、Sphinxの実装コードを読んだり書いたりする機会が多くなりました。その関係でいままで使っていなかった便利な機能に気がついたり、問題解決のためにちょっとした拡張を書けるようになってきました。

で、今回のネタはintersphinxです。


intersphinxの使い方
=======================

intersphinxは他のSphinxドキュメントにリンクしやすくする拡張機能です。
Sphinxに同梱されていますが拡張扱いになっているので、conf.pyのextensionsに以下のように追加しないと使えません::

   extensions = ['sphinx.ext.intersphinx']

詳しくは公式ドキュメント [1]_ に書かれているので省略しますが、以下のように使えます。

example.rst::

   例1: 詳しくは :py:mod:`sphinx:sphinx.ext.intersphinx` を参照して下さい。

   例2: 例えば :ref:`sphinx:domains` にもリンクできます。

conf.py::

   extensions = ['sphinx.ext.intersphinx']
   intersphinx_mapping = {
       'sphinx': ('http://sphinx-users.jp/doc11', None),
   }



これをmake htmlでビルドすると以下のようにレンダリングされます:

   例1: 詳しくは :py:mod:`sphinx:sphinx.ext.intersphinx` を参照して下さい。

   例2: 例えば :ref:`sphinx:domains` にもリンクできます。


ローカルドキュメントにリンクするかのように、外部サイトにリンクしてタイトルも正しく表示出来ましたね。

intersphinxの仕組みとしては、 ``make html`` したときに必ず生成される ``objects.inv`` を http://sphinx-users.jp/doc11/objects.inv から取ってきてリンクの解決をしています。objects.invはインベントリ(inventory)と呼ばれるファイルで、名前付きのリンクターゲットが保存されています。

.. [1] :py:mod:`他のプロジェクトのドキュメントへのリンク <sphinx:sphinx.ext.intersphinx>`


Sphinx以外のドキュメントにintersphinxでリンクする
===================================================

例えばJavaのドキュメントがあったとします。そこに以下のように書いてリンクできると楽だよなーと思うわけです::

   外部のJavaのドキュメントに :ref:`javaapi:api1` これでリンクしたい

前述したように、intersphinxを使えば外部へのリンクを内部リンクのようにreSTに記述して生成することができますが、そのデータはobjects.inv等のインベントリを使って実現しています。ということは、それっぽいインベントリを用意出来ればSphinx的にはリンクを作れることになります。

といことで、 ``javaapi.inv`` を作ってみました。

.. code-block:: python

   # -*- coding: utf-8 -*-

   import zlib

   inventory_header = u'''\
   # Sphinx inventory version 2
   # Project: javaapi
   # Version: 2.0
   # The remainder of this file is compressed with zlib.
   '''.encode('utf-8')

   inventory_payload = u'''\
   api1 std:label -1 api.html#api1 API 1
   '''.encode('utf-8')

   # inventory_payload lines spec:
   #   name domainname:type priority uri dispname
   #
   # * `name`       -- fully qualified name
   # * `domainname` -- sphinx domain name
   # * `type`       -- object type specified by domain (ex. label, module)
   # * `uri`        -- relative uri with anchor
   # * `dispname`   -- name to display when searching/linking
   # * `priority`   -- how "important" the object is
   #                   (determines placement in search results)
   #
   #   - 1: default priority (placed before full-text matches)
   #   - 0: object is important (placed before default-priority objects)
   #   - 2: object is unimportant (placed after full-text matches)
   #   - -1: object should not show up in search at all

   inventory = inventory_header + zlib.compress(inventory_payload)
   open('javaapi.inv','wb').write(inventory)

これを実行すると ``javaapi.inv`` が生成されます。inventory_payloadのところでリンク先のデータが定義されているので、ここをどんどん書き足していけば、好きなリンクターゲットを作れるようになります。

作成したjavaapi.invはローカルに置く場合は以下のようにconf.pyを設定します。

conf.py::

   extensions = ['sphinx.ext.intersphinx']
   intersphinx_mapping = {
       'sphinx': ('http://sphinx-users.jp/doc11', None),
       'javaapi': ('http://api.example.com/', 'javaapi.inv'),
   }


リモートサーバーに置く場合は以下のように書きます。objects.invという名前でないのでちょっと長いですね。

conf.py::

   extensions = ['sphinx.ext.intersphinx']
   intersphinx_mapping = {
       'sphinx': ('http://sphinx-users.jp/doc11': None),
       'javaapi': ('http://api.example.com/',
                   'http://api.example.com/javaapi.inv'),
   }


.. note::

   ``domainname:type`` の部分は ``:ref:`` でリンクしたい場合は std:label にします。 ``:py:func`` でリンクしたい場合は ``py:function`` にします。このあたりはドメインの話なので、詳しくは :ref:`sphinx:domains` を参照して下さい。



ドキュメント内にリンクターゲットを作ってintersphinxでリンクする
==================================================================

intersphinxを活用する上で、今のSphinxにはちょっとした問題があります。

Problem
----------

intersphinxのための情報はすべて objects.inv に含まれていますが、ここに無名のリンクターゲットが含まれていません。

例えば index.rst が以下のように書かれているとします::

   .. _named-label:

   Welcome to spam's documentation!
   ================================

   .. _anon-label:

   ham! egg! spam!

これを :command:`make html` して生成した objects.inv は以下のようになります::

   u'std:label': {u'genindex': (u'spam', u'1.0', u'genindex.html#', u'Index'),
                  u'modindex': (u'spam',
                                u'1.0',
                                u'py-modindex.html#',
                                u'Module Index'),
                  u'named-label': (u'spam',
                                   u'1.0',
                                   u'index.html#named-label',
                                   u"Welcome to spam's documentation!"),
                  u'search': (u'spam', u'1.0', u'search.html#', u'Search Page')}

この objects.inv には 'anon-label' が含まれていないため、外部のSphinxからintersphinxを使ってこのラベルにリンクすることが出来ません。

Solution
-----------

この問題はいまSphinx本体で解決出来るのでは無いかと提案(`#1050`_, `#1052`_)が行われていますが、とりあえず新しいドメインを作って対処するコードを書いてみました。

.. _`#1050`: https://bitbucket.org/birkenfeld/sphinx/issue/1050/not-all-possible-reference-targets-are
.. _`#1052`: https://bitbucket.org/birkenfeld/sphinx/issue/1052/human-readable-version-of-objectsinv

AnonimousDomain (ext_anon_domain.py) は全てのラベルをobjects.invに保存します。

先の例に出したindex.rstであれば、objects.invに以下のようにターゲットが保存されます::

   u'anon:label': {u'anon-label': (u'spam',
                                   u'1.0',
                                   u'index.html#anon-label',
                                   u'-'),
                   u'named-label': (u'spam',
                                    u'1.0',
                                    u'index.html#named-label',
                                    u'-')},
   u'std:label': {u'genindex': (u'spam', u'1.0', u'genindex.html#', u'Index'),
                  u'modindex': (u'spam',
                                u'1.0',
                                u'py-modindex.html#',
                                u'Module Index'),
                  u'named-label': (u'spam',
                                   u'1.0',
                                   u'index.html#named-label',
                                   u"Welcome to spam's documentation!"),
                  u'search': (u'spam', u'1.0', u'search.html#', u'Search Page')}



実装コードは以下のようになります。

.. raw:: html

   <script src="https://gist.github.com/4181015.js?file=ext_anon_domain.py"></script>

.. raw:: html

   <script src="https://gist.github.com/4181015.js?file=conf.py"></script>

ただし一つ問題があって、対象のラベルにintersphinxでリンクする時にもこの拡張が必要になります。リンクは以下のように書けます。

.. code-block:: rst

   無名ラベルへのリンクを :anon:ref:`anon-label` このように書きます。

と言うことで、AnonimousDomainを作ってみましたが、使う方の準備がけっこう面倒くさいですね。他の拡張ドメインを使った場合にも同じ問題は起こるので、このあたりはSphinx本体でなんとかなると嬉しいのかもしれないですね。


最後に
=========

明日は `@tcsh`_ さんの回です。@tcshさんにはJUS勉強会でのSphinx発表の場を提供してもらったり、PyConJPで発表してもらったり、色々お世話になっております。明日よろしくおねがいします！

.. _`Sphinx Advent Calendar 2012`: http://connpass.com/event/1441/
.. _`Sphinx Advent Calendar 7日目: 異なった環境で Sphinx と blockdiag とかを使う`: http://takanory.net/takalog/1293
.. _`Sphinx Advent Calendar 2012 (全部俺)`: http://advent-calendar2012.usaturn.net/
.. _`@takanory`: https://twitter.com/takanory
.. _`@tcsh`: https://twitter.com/tcsh


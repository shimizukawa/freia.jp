:date: 2009-09-23 18:16:17
:categories: ['Plone']
:body type: text/x-rst

===================================================================
2009/09/23 reSTで書いたページをPlone3のPresentationモードで表示する
===================================================================

*Category: 'Plone'*

reStructuredText(reST)で書いたページを、 `Plone3に標準で組み込まれているPresentationモード`_ (Plone S5)で表示するのに色々はまったので、設定のポイントメモを書いておこうと思います。

# PloneS5って何？ -> see `Plone S5 - takanory.net`_

前提
-----

実行環境

:Plone: 3.3.1
:Zope: 2.10.8
:Python: 2.4.4
:OS: Windows7 32bit


reStructuredTextの設定値

:入力エンコード: utf-8
:出力エンコード: utf-8
:言語: ja (日本語)
:ヘッダーレベル: 1

reStructuredTextの設定値については、PloneS5で使われる値の設定場所があちこちに分散していてちょっと困りました。とりあえず怪しい箇所全部を書き換える前提でやってしまうのが無難。厳密には(★)を付けてるところが必須で、後はPlone3.3.1のPloneS5では使われていないはず...です。

zope.conf
----------
関連する設定のみ抜粋::

    default-zpublisher-encoding utf-8   (★)
    locale ja
    rest-header-level 1
    rest-input-encoding utf-8
    rest-output-encoding utf-8


buildoutでやってる場合は以下のように記載してbuildoutを再実行::

    zope-conf-additional =
        locale ja
        rest-header-level 1
        rest-input-encoding utf-8
        rest-output-encoding utf-8

localeをjaに設定すると色々影響するので、設定しない方が良い気がします。必須は★だけです。


Ploneの site_properties
------------------------
Ploneインスタンスの ``portal_properties/site_properties`` の項目から関連する設定のみ抜粋::

    default_language ja
    default_charset utf-8    (★)


default_charset はZMIでしか設定出来ないっぽいので、ZMI画面から設定してください。

なお、Plone3.3.1では ``CMFPlone/properties/default/propertiestool.xml`` でデフォルトがutf-8で定義されていて、zope.confの設定とかは見ていないようです。この値がPortalTransform等で使用されるrest_to_html変換時のinput/outputのエンコーディングとなります(多分)。

そしてzope.confのrest-input-encodingとrest-output-encodingは実行時も見ていません。完全に無視されるみたいです。


Ploneの portal_transforms
---------------------------
Ploneインスタンスの ``portal_transforms/rest_to_html`` の項目から関連する項目のみ抜粋::

    Initial Header Level: 1   (★)

これもZMIで設定します。デフォルトの2という値は、 ``PortalTransforms/transforms/rest.py`` で固定値で定義されていて、zope.confとかの設定は関係ないようです。

そしてzope.confのrest-header-levelは実行時も無視されるみたいです。だめじゃん。


reStructuredText文面の書き方
-------------------------------

後はreSTで文章を書けば良い、となれば苦労が無くて良いんですが、S5が以下のように認識するので、そのように出力される書き方をしないといけません。

:ページ区切り: h1かh2で認識する。h3はだめ。
:pタグは無視される: 表示したい文面は<li>か<dl>で表現する


reSTで、h2で節を区切る書き方
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
reSTはヘッダーレベルを自動的に調整して、最上位レベルが1つになるようにします沓そして最上位レベルが複数になると自動的に全てのレベルを1段落とすようになっています。つまり、::

    ==================
    1ページ目タイトル
    ==================

    文面......

    ==================
    2ページ目タイトル
    ==================

    文面......

と書くと、両方ともレベル2扱いになってしまい、レベル1が無いHTMLが出力される訳です。しかし都合の良いことに、Ploneのページタイトルがh1なので、結果的にはh1が1つ、レベル2(h2)が複数、という真っ当な出力ができあがります。

ちなみにレベル1を1つreST的に用意すると、ページタイトルの方のh1と合わせて２つになってしまい、スライド表示がおかしくなってしまう場合があります。さらにreSTでレベル1を用意すると(S5じゃない普通の)ページで表示したときにもh1が複数になってしまうので、レベル1は書かないのが無難でしょう。

ところでレベル2がh2になるのは、 `Ploneの portal_transforms`_ で初期レベルを1に設定しているからです。これがPloneの初期値だとレベル2=h3になってしまい、S5ではページ区切りとは見なされなくなってしまいます。


まとめ：初期レベルは1に設定し、reSTではレベル2で出力されるように書く


pタグは無視される
~~~~~~~~~~~~~~~~~~~

pタグは無視されます。以下のように書くと箇条書き部分しか表示されません::

    ページタイトル
    ---------------

    このページで説明したい概要文.....

    * 箇条書き１
    * 箇条書き２

    まとめの文章.......

プレゼンテーションモードのページには、HTML的には箇条書きの前後もpタグで出力されているのですが、JavaScriptの処理で無視されているようです。s5_slides.jsをざっと眺めただけではよく分からなかったので、そういうものだと思うことにします。とりあえずスライドのタイトル以外ではul,ol,imgは使えてる感じ。


ページの設定でプレゼンテーションモードをOnにする
---------------------------------------------------

ページの、編集タブ内にある設定タブで、プレゼンテーションモードをOnにします。これをOnにすると、ページを表示したときに ``プレゼンテーションモードでも利用可能`` というリンクが表示されるようになります。


以上でプレゼンモードが使えるようになったはず。 `プレゼンテーションモードがPlone3.0から標準になった`_ ため、PloneS5をインストールしなくても使えて楽なのですが、そもそも使いこなすのが微妙に難しい気がします。みんなreSTで書かずにWYSIWYGで書いてるんでしょうか...?


参考文献
-----------

最後に参考文献です。

* `Zope/Plone勉強会#3 - int neko`_ reSTのレベル設定
* `How can I change reStructuredText header levels? - Plone CMS: Open Source Content Management`_
* `S5 での文字化け解消 - Plone で文字化けした時は - - すちゃらか社員日記`_ 多分Plone2系
* `plone で shift_jis のサイトを作る(その2) - takanory.net`_ default_charset の説明の参考に
* `Plone S5 - Plone CMS: Open Source Content Management`_ Plone S5 配布(Plone2.x用)
* `Enfold Systems: Plone S5`_ Plone S5の本家(Plone2.x用)
* `S5: A Simple Standards-Based Slide Show System`_ S5の本家meyerwebのサイト. リファレンスとか


.. _`Plone S5 - takanory.net`: http://takanory.net/plone/products/plones5
.. _`S5: A Simple Standards-Based Slide Show System`: http://meyerweb.com/eric/tools/s5/
.. _`S5 での文字化け解消 - Plone で文字化けした時は - - すちゃらか社員日記`: http://d.hatena.ne.jp/claddvd/20061127/p1
.. _`Enfold Systems: Plone S5`: http://www.enfoldsystems.com/developer/software/plones5
.. _`plone で shift_jis のサイトを作る(その2) - takanory.net`: http://takanory.net/Zope/takanory/takalog/759/
.. _`How can I change reStructuredText header levels? - Plone CMS: Open Source Content Management`: http://plone.org/documentation/faq/how-can-i-change-restructuredtext-header-levels
.. _`Zope/Plone勉強会#3 - int neko`: http://intneko.net/page/20090905
.. _`プレゼンテーションモードがPlone3.0から標準になった`: http://plone.org/products/plone/features/3.0/new/presentation-mode-for-content
.. _`Plone3に標準で組み込まれているPresentationモード`: http://plone.org/products/plone/features/3.0/new/presentation-mode-for-content
.. _`Plone S5 - Plone CMS: Open Source Content Management`: http://plone.org/products/s5


.. :extend type: text/html
.. :extend:


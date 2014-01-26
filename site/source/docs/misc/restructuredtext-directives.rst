:orphan:

=======================================
[翻訳] reStructuredText ディレクティブ
=======================================

.. warning::

   このページの翻訳は以下のURLに統合されました。
   http://docutils.sphinx-users.jp/docutils/docs/ref/rst/directives.html


:著者: David Goodger
:問い合わせ: goodger@python.org
:リビジョン: $Revision: 3340 $
:更新日時: $Date: 2005-05-14 18:14:44 +0200 (Sat, 14 May 2005) $
:著作権: This document has been placed in the public domain.
:翻訳者: 清水川 貴之 shimizukawa at gmail.com
:原文: http://docutils.sourceforge.net/docs/ref/rst/directives.html

.. contents::

このドキュメントはreStructuredTextの文書解析器で実装されているディレクティブについて記述されています。

ディレクティブは以下の構文にで記述されます::

    +-------+-------------------------------+
    | ".. " | directive type "::" directive |
    +-------+ block                         |
            |                               |
            +-------------------------------+

ディレクティブは明示的な開始記号(ピリオド二文字とスペース一文字)で始まり、その後ろにディレクティブのタイプと二つのコロンが続きます(合わせて"ディレクティブマーカー"と言います)。ディレクティブブロックはディレクティブマーカーの直後に続く、インデントされた全ての行で構成されます。ディレクティブブロックの内部は複数の 引数・オプション(フィールドリスト)・コンテンツで構成されます。詳しい構文については、 `reStructuredText 言語仕様書`_ の `ディレクティブ`_ 節を参照してください。

後で述べる "doctree エレメント" (ドキュメントツリーエレメント名: XML DTD 標準記述子) リストが個々のディレクティブに対応します。エレメント階層の詳細については、 `The Docutils Document Tree`_ と `Docutils Generic DTD`_ XML ドキュメントタイプ定義 を参照してください。また、ディレクティブの実装の詳細については、 `reStructuredText ディレクティブの作り方`_ を参照してください。

.. _`ディレクティブ`: restructuredtext.html#directives
.. _`reStructuredText 言語仕様書`: restructuredtext.html
.. _The Docutils Document Tree: ../doctree.html
.. _Docutils Generic DTD: ../docutils.dtd
.. _reStructuredText ディレクティブの作り方:
   ../../howto/rst-directives.html


----------
 警告関係
----------

.. _attention:
.. _caution:
.. _danger:
.. _error:
.. _hint:
.. _important:
.. _note:
.. _tip:
.. _warning:

警告の仕様
============

:Directiveタイプ: "attention", "caution", "danger", "error", "hint",
                  "important", "note", "tip", "warning", "admonition"
:Doctreeエレメント: attention, caution, danger, error, hint, important,
                   note, tip, warning, admonition, title
:Directive引数: 無し
:Directiveオプション: 無し
:Directive本文: 本文エレメントとして解釈される

```警告``` (Admonitions) は "topics" の拡張版で、他のディレクティブの本文に記述することが出来ます。
大抵の ```警告``` はドキュメント内のオフセットブロックとして表示され、時には外枠や影付きで表示されます。表示されるタイトルは ```警告``` の種類によって決定されます。例えば::

    .. DANGER::
       Beware killer rabbits!

このディレクティブはおそらく以下のように表示されます::

    +------------------------+
    |        !DANGER!        |
    |                        |
    | Beware killer rabbits! |
    +------------------------+

以下の ```警告``` ディレクティブが実装されています。

- attention
- caution
- danger
- error
- hint
- important
- note
- tip
- warning

ディレクティブの直後に記述したテキスト(同じ行 And/Or 次の行以降のインデントされたテキスト)はディレクティブブロックとして解釈され、テキストは普通の本文エレメントとして解釈されます。
例えば、以下の "note" という ```警告``` ディレクティブは1つのパラグラフと2つのリストアイテムを含む1つのリストブロックとして解釈されます::

    .. note:: これは note `警告` です。
       これは最初のパラグラフの2行目です。

       - note は次行以降のインデントされた本文エレメントを含みます。
       - それはこのリストを含んでいます。


.. _admonition:

一般的な 警告
==============

:Directiveタイプ: "admonition"
:Doctreeエレメント: admonition, title
:Directive引数: 1つ必須 (警告のタイトル)
:Directiveオプション: 指定可能
:Directive本文: 本文エレメントとして解釈される

これは一般的なタイトル付き ```警告``` です。タイトルは書き手が任意に決めることが出来ます。

書き手が指定したタイトルも "class" 属性値として使用されます("admonition-" が接頭され、小文字に統一され、ローマ字・数字以外の文字はハイフンに変換されます)。
以下の ```警告``` の例は::

    .. admonition:: And, by the way...

       自分で警告を作ることも出来ます。

以下のドキュメントツリーに変換されます(pseudo-XML)::

    <document source="test data">
        <admonition class="admonition-and-by-the-way">
            <title>
                And, by the way...
            <paragraph>
                自分で警告を作ることも出来ます。

以下のオプションを使用出来ます:

``class`` : 文字列
    自動生成の "class" 属性を上書きします。 class_ ディレクティブを参照してください。


----------
 画像関係
----------

画像に関する二つのディレクティブ "image" と "figure" があります。


Image
=======

:Directiveタイプ: "image"
:Doctreeエレメント: image
:Directive引数: 1つ必須 (image URI)
:Directiveオプション: 指定可能
:Directive本文: 無し

"image" は単純な画像です::

    .. image:: picture.png

画像の参照先を示すURLをディレクティブの引数に指定する必要があり、これはハイパーリンクとして利用されます。URIはディレクティブ開始行と同じ行に記述するか、以下に示すようにインデントされたテキストブロックに空白行を挟まずに記述します。
もし、URIが複数行にまたがってしまった場合は、各行の行頭・行末の空白を除いて連結されます。

オプションとして、以下のフィールドリストに示す _`image options` を指定することが出来ます::

    .. image:: picture.jpeg
       :height: 100
       :width: 200
       :scale: 50
       :alt: alternate text
       :align: right

以下のオプションを使用出来ます:

``alt`` : 文字列
    代替テキスト: 短い画像の説明文。アプリケーションが画像を表示出来ない場合、あるいは音声読み上げに使用されます。

``height`` : 数値
    画像の縦幅をピクセルで指定し、予約領域や画像の縦方向の拡大縮小に使用されます。"scale" オプションと組み合わせて使用することが出来ます。例えば、heightに200、scaleに50が指定された場合、高さ100で拡大縮小無しと評価されます。

``width`` : 数値
    画像の横幅をピクセルで指定し、予約領域や画像の横方向の拡大縮小に使用されます。
    前述の "height" や "scale" と組み合わせて使用することが出来ます。

``scale`` : 数値
    縦横同比率で拡大縮小したい場合、パーセント("%"は記述しない/出来ない)で指定します。 "100" はフルサイズを意味し、"scale" が指定されない場合と等価になります。

    もし、"height" や "width" が指定されていない場合、PIL [#PIL]_ は画像ファイルから幅や高さを取得して使用します。

``align`` : "top", "middle", "bottom", "left", "center", "right"
    画像の配置はHTMLの ``<img>`` タグの "align" 属性として評価されます。"top", "middle", "bottom" の3つは縦方向の配置位置を(テキストのベースラインからの相対位置で)コントロールします（これらは画像がインラインで使用される場合にのみ有効です）。
    "left", "center", "right" の3つは横方向の配置位置をコントロールします。この指定は画像をfloat指定にし、文字列を回り込みさせます。これらの指定はブラウザや表示するソフトウェアによって表示方法が異なります。

``target`` : 文字列 (URI あるいは 参照名)
    画像をハイパーリンクとしてクリック可能にします。オプションの引数にはURI(絶対パス/相対パス)か、アンダースコアを接尾した参照名 (例: ``name_``) を指定出来ます。

``class`` : 文字列
    image エレメントに "class" 属性を指定します。 class_ ディレクティブを参照してください。


Figure
=======

:Directiveタイプ: "figure"
:Doctreeエレメント: figure, image, caption, legend
:Directive引数: 1つ必須 (image URI)
:Directiveオプション: 指定可能
:Directive本文: キャプションと凡例(オプション)として解釈される

"figure" は `image options`_ を含む `Image`_ データで構成され、単一パラグラフのキャプションと凡例を含めることが出来ます::

    .. figure:: picture.png
       :scale: 50
       :alt: map to buried treasure

       これはキャプションです(シンプルなパラグラフ).

       凡例は任意の要素で構成され、キャプションの後に書くことが出来ます。
       この例の場合、凡例はこのパラグラフと以下のテーブルで構成されます:

       +-----------------------+-----------------------+
       | 記号                  | 説明                  |
       +=======================+=======================+
       | .. image:: tent.png   | キャンプ場            |
       +-----------------------+-----------------------+
       | .. image:: waves.png  | 湖                    |
       +-----------------------+-----------------------+
       | .. image:: peak.png   | 山                    |
       +-----------------------+-----------------------+

キャプションパラグラフや凡例の前には空行が必要です。キャプションを書かずに凡例を書く場合は、キャプションの代わりに空のコメント ("..") を書きます。

"figure" ディレクティブは "image" ディレクティブの全てのオプションをサポートしています(`image options`_ を参照)。さらに以下のオプションを指定することが出来ます:

``figwidth`` : 数値 または "image"
    figureの最大幅をピクセルで記述します。または "image" を記述することも出来、この場合画像の幅が利用されます( 要 PIL [#PIL]_)。もし画像ファイルが見つからなかったり、必要なソフトウェアが提供されていない場合、このオプションは無効になります。

    "figure" Doctree エレメントの "width" 属性をセットしてください。

    このオプションは含まれる画像の伸縮を行いません。その用途には "width"
    `Image`_ オプションを以下のように使用してください::

        +---------------------------+
        |        figure             |
        |                           |
        |<------ figwidth --------->|
        |                           |
        |  +---------------------+  |
        |  |     image           |  |
        |  |                     |  |
        |  |<--- width --------->|  |
        |  +---------------------+  |
        |                           |
        |figureのキャプションはこの |
        |幅で折り返します。         |
        +---------------------------+

``figclass`` : 文字列
    figureエレメントの "class" 属性を指定します。 class_ ディレクティブを参照してください。

``align`` : "left", "center", "right"
    横方向の配置位置をコントロールします。この指定は画像をfloat指定にし、文字列を回り込みさせます。これらの指定はブラウザや表示するソフトウェアによって表示方法が異なります。


.. [#PIL] `Python Imaging Library`_.

.. _Python Imaging Library: http://www.pythonware.com/products/pil/


----------------
 本文エレメント
----------------

Topic
=====

:Directiveタイプ: "topic"
:Doctreeエレメント: topic
:Directive引数: 1つ必須 (topicタイトル)
:Directiveオプション: 指定可能
:Directive本文: トピックの本文として解釈される

トピックはタイトル付きのBlock Quote、あるいはセルフコンテインドでサブセクションを持たないセクションに似ています。"topic"ディレクティブをドキュメントの回り込み設定から独立したものとして使えます。トピックはセクションのどこにでも記述することが出来ます。本文エレメントとトピックはネストしたトピックを持ちません。

このディレクティブの唯一の引数は、トピックのタイトルになります。タイトルと本文の間は必ず1行空けてください。インデントされた後続の行は全てトピックの本文となり、本文エレメントとして解釈されます。例::

    .. topic:: トピックのタイトル

        後続のインデントされた行はトピック
        の本文を意味し、本文エレメントとして
        解釈されます。

以下のオプションを使用出来ます:

``class`` : 文字列
    topicエレメントの "class" 属性を指定します。 class_ ディレクティブを参照してください。


Sidebar
=======

:Directiveタイプ: "sidebar"
:Doctreeエレメント: sidebar
:Directive引数: 1つ必須 (sidebarタイトル)
:Directiveオプション: 指定可能
:Directive本文: Interpreted as the sidebar body.

Sidebars are like miniature, parallel documents that occur inside
other documents, providing related or reference material.  A sidebar
is typically offset by a border and "floats" to the side of the page;
the document's main text may flow around it.  Sidebars can also be
likened to super-footnotes; their content is outside of the flow of
the document's main text.

Sidebars may occur anywhere a section or transition may occur.  Body
elements (including sidebars) may not contain nested sidebars.

The directive's sole argument is interpreted as the sidebar title,
which may be followed by a subtitle option (see below); the next line
must be blank.  All subsequent lines make up the sidebar body,
interpreted as body elements.  For example::

    .. sidebar:: Sidebar Title
       :subtitle: Optional Sidebar Subtitle

       Subsequent indented lines comprise
       the body of the sidebar, and are
       interpreted as body elements.

以下のオプションを使用出来ます:

``subtitle`` : 文字列
    The sidebar's subtitle.

``class`` : 文字列
    sidebarエレメントの "class" 属性を指定します。 class_ ディレクティブを参照してください。


Line Block
==========

.. admonition:: Deprecated

   The "line-block" directive is deprecated.  Use the `line block
   syntax`_ instead.

   .. _line block syntax: restructuredtext.html#line-blocks

:Directiveタイプ: "line-block"
:Doctreeエレメント: line_block
:Directive引数: 無し
:Directiveオプション: 指定可能
:Directive本文: Becomes the body of the line block.

The "line-block" directive constructs an element where line breaks and
initial indentation is significant and inline markup is supported.  It
is equivalent to a `parsed literal block`_ with different rendering:
typically in an ordinary serif typeface instead of a
typewriter/monospaced face, and not automatically indented.  (Have the
line-block directive begin a block quote to get an indented line
block.)  Line blocks are useful for address blocks and verse (poetry,
song lyrics), where the structure of lines is significant.  For
example, here's a classic::

    "To Ma Own Beloved Lassie: A Poem on her 17th Birthday", by
    Ewan McTeagle (for Lassie O'Shea):

        .. line-block::

            Lend us a couple of bob till Thursday.
            I'm absolutely skint.
            But I'm expecting a postal order and I can pay you back
                as soon as it comes.
            Love, Ewan.

以下のオプションを使用出来ます:

``class`` : 文字列
    line_blockエレメントの "class" 属性を指定します。 class_ ディレクティブを参照してください。


.. _parsed-literal:

Parsed Literal Block
====================

:Directiveタイプ: "parsed-literal"
:Doctreeエレメント: literal_block
:Directive引数: 無し
:Directiveオプション: 指定可能
:Directive本文: Becomes the body of the literal block.

Unlike an ordinary literal block, the "parsed-literal" directive
constructs a literal block where the text is parsed for inline markup.
It is equivalent to a `line block`_ with different rendering:
typically in a typewriter/monospaced typeface, like an ordinary
literal block.  Parsed literal blocks are useful for adding hyperlinks
to code examples.

However, care must be taken with the text, because inline markup is
recognized and there is no protection from parsing.  Backslash-escapes
may be necessary to prevent unintended parsing.  And because the
markup characters are removed by the parser, care must also be taken
with vertical alignment.  Parsed "ASCII art" is tricky, and extra
whitespace may be necessary.

For example, all the element names in this content model are links::

    .. parsed-literal::

       ( (title_, subtitle_?)?,
         decoration_?,
         (docinfo_, transition_?)?,
         `%structure.model;`_ )

以下のオプションを使用出来ます:

``class`` : 文字列
    literal_blockエレメントの "class" 属性を指定します。 class_ ディレクティブを参照してください。


Rubric
======

:Directiveタイプ: "rubric"
:Doctreeエレメント: rubric
:Directive引数: 1つ必須 (rubric text).
:Directiveオプション: 指定可能
:Directive本文: 無し

..

     rubric n. 1. a title, heading, or the like, in a manuscript,
     book, statute, etc., written or printed in red or otherwise
     distinguished from the rest of the text. ...

     -- Random House Webster's College Dictionary, 1991

The "rubric" directive inserts a "rubric" element into the document
tree.  A rubric is like an informal heading that doesn't correspond to
the document's structure.

以下のオプションを使用出来ます:

``class`` : 文字列
    rubricエレメントの "class" 属性を指定します。 class_ ディレクティブを参照してください。


Epigraph
========

:Directiveタイプ: "epigraph"
:Doctreeエレメント: block_quote
:Directive引数: 無し
:Directiveオプション: 無し
:Directive本文: Interpreted as the body of the block quote.

An epigraph is an apposite (suitable, apt, or pertinent) short
inscription, often a quotation or poem, at the beginning of a document
or section.

The "epigraph" directive produces an "epigraph"-class block quote.
For example, this input::

     .. epigraph::

        No matter where you go, there you are.

        -- Buckaroo Banzai

becomes this document tree fragment::

    <block_quote class="epigraph">
        <paragraph>
            No matter where you go, there you are.
        <attribution>
            Buckaroo Banzai


Highlights
==========

:Directiveタイプ: "highlights"
:Doctreeエレメント: block_quote
:Directive引数: 無し
:Directiveオプション: 無し
:Directive本文: Interpreted as the body of the block quote.

Highlights summarize the main points of a document or section, often
consisting of a list.

The "highlights" directive produces a "highlights"-class block quote.
See Epigraph_ above for an analogous example.


Pull-Quote
==========

:Directiveタイプ: "pull-quote"
:Doctreeエレメント: block_quote
:Directive引数: 無し
:Directiveオプション: 無し
:Directive本文: Interpreted as the body of the block quote.

A pull-quote is a small selection of text "pulled out and quoted",
typically in a larger typeface.  Pull-quotes are used to attract
attention, especially in long articles.

The "pull-quote" directive produces a "pull-quote"-class block quote.
See Epigraph_ above for an analogous example.


.. _compound:

Compound Paragraph
==================

:Directiveタイプ: "compound"
:Doctreeエレメント: compound
:Directive引数: 無し
:Directiveオプション: 指定可能
:Directive本文: Interpreted as body elements.

(New in Docutils 0.3.6)

The "compound" directive is used to create a compound paragraph, which
is a single logical paragraph containing multiple physical body
elements such as simple paragraphs, literal blocks, tables, lists,
etc., instead of directly containing text and inline elements.  For
example::

    .. compound::

       The 'rm' command is very dangerous.  If you are logged
       in as root and enter ::

           cd /
           rm -rf *

       you will erase the entire contents of your file system.

In the example above, a literal block is "embedded" within a sentence
that begins in one physical paragraph and ends in another.

.. note::

   The "compound" directive is *not* a generic block-level container
   like HTML's ``<div>`` element.  Do not use it only to group a
   sequence of elements, or you may get unexpected results.

   If you happen to need a generic block-level container, please
   describe your use-case in an email to
   docutils-users@lists.sourceforge.net.

Compound paragraphs are typically rendered as multiple distinct text
blocks, with the possibility of variations to emphasize their logical
unity:

* If paragraphs are rendered with a first-line indent, only the first
  physical paragraph of a compound paragraph should have that indent
  -- second and further physical paragraphs should omit the indents;
* vertical spacing between physical elements may be reduced;
* and so on.

以下のオプションを使用出来ます:

``class`` : 文字列
    compoundエレメントの "class" 属性を指定します。 class_ ディレクティブを参照してください。


--------
 Tables
--------

Formal tables need more structure than the reStructuredText syntax
supplies.  Tables may be given titles with the table_ directive.
Sometimes reStructuredText tables are inconvenient to write, or table
data in a standard format is readily available.  The csv-table_
directive supports CSV data.


Table
=====

:Directiveタイプ: "table"
:Doctreeエレメント: table
:Directive引数: 1, optional (tableタイトル)
:Directiveオプション: 指定可能
:Directive本文: A normal reStructuredText table.

(New in Docutils 0.3.1)

The "table" directive is used to create a titled table, to associate a
title with a table::

    .. table:: Truth table for "not"

       =====  =====
         A    not A
       =====  =====
       False  True
       True   False
       =====  =====

以下のオプションを使用出来ます:

``class`` : 文字列
    tableエレメントの "class" 属性を指定します。 class_ ディレクティブを参照してください。


.. _csv-table:

CSV Table
=========

:Directiveタイプ: "csv-table"
:Doctreeエレメント: table
:Directive引数: 1, optional (tableタイトル)
:Directiveオプション: 指定可能
:Directive本文: A CSV (comma-separated values) table.

.. WARNING::

   The "csv-table" directive's ":file:" and ":url:" options represent
   a potential security holes.  They can be disabled with the
   "file_insertion_enabled_" runtime setting.

.. Note::

   The "csv-table" directive requires the ``csv.py`` module of the
   Python standard library, which was added in Python 2.3.  It will
   not work with earlier versions of Python.  Using the "csv-table"
   directive in a document will make the document **incompatible**
   with systems using Python 2.1 or 2.2.

(New in Docutils 0.3.4)

The "csv-table" directive is used to create a table from CSV
(comma-separated values) data.  CSV is a common data format generated
by spreadsheet applications and commercial databases.  The data may be
internal (an integral part of the document) or external (a separate
file).

Example::

    .. csv-table:: Frozen Delights!
       :header: "Treat", "Quantity", "Description"
       :widths: 15, 10, 30

       "Albatross", 2.99, "On a stick!"
       "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
       crunchy, now would it?"
       "Gannet Ripple", 1.99, "On a stick!"

Block markup and inline markup within cells is supported.  Line ends
are recognized within cells.

Working limitations:

* Whitespace delimiters are supported only for external CSV files.

* There is no support for checking that the number of columns in each
  row is the same.  However, this directive supports CSV generators
  that do not insert "empty" entries at the end of short rows, by
  automatically adding empty entries.

  .. Add "strict" option to verify input?

* Due to limitations of the CSV parser, this directive is not Unicode
  compatible.  It may also have problems with ASCII NUL characters.
  Accordingly, CSV tables should be ASCII-printable safe.

  .. Test with Unicode; see if that's really so.  "encoding" option?

以下のオプションを使用出来ます:

``class`` : 文字列
    tableエレメントの "class" 属性を指定します。 class_ ディレクティブを参照してください。

``widths`` : 数値 [, integer...]
    A comma- or space-separated list of relative column widths.  The
    default is equal-width columns (100%/#columns).

``header-rows`` : 数値
    The number of rows of CSV data to use in the table header.
    Defaults to 0.

``stub-columns`` : 数値
    The number of table columns to use as stubs (row titles, on the
    left).  Defaults to 0.

``header`` : CSV data
    Supplemental data for the table header, added independently of and
    before any ``header-rows`` from the main CSV data.  Must use the
    same CSV format as the main CSV data.

``file`` : string (newlines removed)
    The local filesystem path to a CSV data file.

``url`` : string (whitespace removed)
    An Internet URL reference to a CSV data file.

``encoding`` : name of text encoding
    The text encoding of the external CSV data (file or URL).
    Defaults to the document's encoding (if specified).

``delim`` : char | "tab" | "space"
    A one-character string used to separate fields.  Defaults to ``,``
    (comma).  May be specified as a Unicode code point; see the
    unicode_ directive for syntax details.

``quote`` : char
    A one-character string used to quote elements containing the
    delimiter or which start with the quote character.  Defaults to
    ``"`` (quote).  May be specified as a Unicode code point; see the
    unicode_ directive for syntax details.

``keepspace`` : flag
    Treat whitespace immediately following the delimiter as
    significant.  The default is to ignore such whitespace.

``escape`` : char
    A one-character string used to escape the delimiter or quote
    characters.  May be specified as a Unicode code point; see the
    unicode_ directive for syntax details.  Used when the delimiter is
    used in an unquoted field, or when quote characters are used
    within a field.  The default is to double-up the character,
    e.g. "He said, ""Hi!"""

    .. Add another possible value, "double", to explicitly indicate
       the default case?


List Table
==========

:Directiveタイプ: "list-table"
:Doctreeエレメント: table
:Directive引数: 1, optional (tableタイトル)
:Directiveオプション: 指定可能
:Directive本文: A uniform two-level bullet list.

(New in Docutils 0.3.8.  This is an initial implementation; `further
ideas`__ may be implemented in the future.)

__ http://docutils.sf.net/docs/dev/rst/alternatives.html#list-driven-tables

The "list-table" directive is used to create a table from data in a
uniform two-level bullet list.  "Uniform" means that each sublist
(second-level list) must contain the same number of list items.

Example::

    .. list-table:: Frozen Delights!
       :widths: 15 10 30
       :header-rows: 1

       * - Treat
         - Quantity
         - Description
       * - Albatross
         - 2.99
         - On a stick!
       * - Crunchy Frog
         - 1.49
         - If we took the bones out, it wouldn't be
           crunchy, now would it?
       * - Gannet Ripple
         - 1.99
         - On a stick!

以下のオプションを使用出来ます:

``class`` : 文字列
    tableエレメントの "class" 属性を指定します。 class_ ディレクティブを参照してください。

``widths`` : 数値 [integer...]
    A comma- or space-separated list of relative column widths.  The
    default is equal-width columns (100%/#columns).

``header-rows`` : 数値
    The number of rows of list data to use in the table header.
    Defaults to 0.

``stub-columns`` : 数値
    The number of table columns to use as stubs (row titles, on the
    left).  Defaults to 0.


----------------
 Document Parts
----------------

Table of Contents
=================

:Directiveタイプ: "contents"
:Doctreeエレメント: pending, topic
:Directive引数: One, optional: title.
:Directiveオプション: 指定可能
:Directive本文: 無し

The "contents" directive generates a table of contents (TOC) in a
topic_.  Topics, and therefore tables of contents, may occur anywhere
a section or transition may occur.  Body elements and topics may not
contain tables of contents.

Here's the directive in its simplest form::

    .. contents::

Language-dependent boilerplate text will be used for the title.  The
English default title text is "Contents".

An explicit title may be specified::

    .. contents:: Table of Contents

The title may span lines, although it is not recommended::

    .. contents:: Here's a very long Table of
       Contents title

Options may be specified for the directive, using a field list::

    .. contents:: Table of Contents
       :depth: 2

If the default title is to be used, the options field list may begin
on the same line as the directive marker::

    .. contents:: :depth: 2

以下のオプションを使用出来ます:

``depth`` : 数値
    The number of section levels that are collected in the table of
    contents.  The default is unlimited depth.

``local`` : flag (empty)
    Generate a local table of contents.  Entries will only include
    subsections of the section in which the directive is given.  If no
    explicit title is given, the table of contents will not be titled.

``backlinks`` : "entry" or "top" or "none"
    Generate links from section headers back to the table of contents
    entries, the table of contents itself, or generate no backlinks.

``class`` : 文字列
    topicエレメントの "class" 属性を指定します。 class_ ディレクティブを参照してください。


.. _sectnum:
.. _section-autonumbering:

Automatic Section Numbering
===========================

:Directiveタイプ: "sectnum" or "section-autonumbering" (synonyms)
:Doctreeエレメント: pending, generated
:Directive引数: 無し
:Directiveオプション: 指定可能
:Directive本文: 無し

The "sectnum" (or "section-autonumbering") directive automatically
numbers sections and subsections in a document.  Section numbers are
of the "multiple enumeration" form, where each level has a number,
separated by periods.  For example, the title of section 1, subsection
2, subsubsection 3 would have "1.2.3" prefixed.

The "sectnum" directive does its work in two passes: the initial parse
and a transform.  During the initial parse, a "pending" element is
generated which acts as a placeholder, storing any options internally.
At a later stage in the processing, the "pending" element triggers a
transform, which adds section numbers to titles.  Section numbers are
enclosed in a "generated" element, and titles have their "auto"
attribute set to "1".

以下のオプションを使用出来ます:

``depth`` : 数値
    The number of section levels that are numbered by this directive.
    The default is unlimited depth.

``prefix`` : string
    An arbitrary string that is prefixed to the automatically
    generated section numbers.  It may be something like "3.2.", which
    will produce "3.2.1", "3.2.2", "3.2.2.1", and so on.  Note that
    any separating punctuation (in the example, a period, ".") must be
    explicitly provided.  The default is no prefix.

``suffix`` : string
    An arbitrary string that is appended to the automatically
    generated section numbers.  The default is no suffix.

``start`` : 数値
    The value that will be used for the first section number.
    Combined with ``prefix``, this may be used to force the right
    numbering for a document split over several source files.  The
    default is 1.


.. _header:
.. _footer:

Document Header & Footer
========================

:Directive タイプs: "header" and "footer"
:Doctreeエレメント: decoration, header, footer
:Directive引数: 無し
:Directiveオプション: 無し
:Directive本文: Interpreted as body elements.

(New in Docutils 0.3.8)

The "header" and "footer" directives create document decorations,
useful for page navigation, notes, time/datestamp, etc.  For example::

    .. header:: This space for rent.

This will add a paragraph to the document header, which will appear at
the top of the generated web page or at the top of every printed page.

These directives may be used multiple times, cumulatively.  There is
currently support for only one header and footer.

.. note::

   While it is possible to use the "header" and "footer" directives to
   create navigational elements for web pages, you should be aware
   that Docutils is meant to be used for *document* processing, and
   that a navigation bar is not typically part of a document.

   Thus, you may soon find Docutils' abilities to be insufficient for
   these purposes.  At that time, you should consider using a
   templating system (like ht2html_) rather than the "header" and
   "footer" directives.

   .. _ht2html: http://ht2html.sourceforge.net/

In addition to the use of these directives to populate header and
footer content, content may also be added automatically by the
processing system.  For example, if certain runtime settings are
enabled, the document footer is populated with processing information
such as a datestamp, a link to `the Docutils website`_, etc.

.. _the Docutils website: http://docutils.sourceforge.net


------------
 References
------------

.. _target-notes:

Target Footnotes
================

:Directiveタイプ: "target-notes"
:Doctreeエレメント: pending, footnote, footnote_reference
:Directive引数: 無し
:Directiveオプション: 無し
:Directive本文: 無し

The "target-notes" directive creates a footnote for each external
target in the text, and corresponding footnote references after each
reference.  For every explicit target (of the form, ``.. _target name:
URL``) in the text, a footnote will be generated containing the
visible URL as content.


Footnotes
=========

**NOT IMPLEMENTED YET**

:Directiveタイプ: "footnotes"
:Doctreeエレメント: pending, topic
:Directive引数: None?
:Directiveオプション: Possible?
:Directive本文: 無し

@@@


Citations
=========

**NOT IMPLEMENTED YET**

:Directiveタイプ: "citations"
:Doctreeエレメント: pending, topic
:Directive引数: None?
:Directiveオプション: Possible?
:Directive本文: 無し

@@@


---------------
 HTML-Specific
---------------

Meta
====

:Directiveタイプ: "meta"
:Doctreeエレメント: meta (non-standard)
:Directive引数: 無し
:Directiveオプション: 無し
:Directive本文: Must contain a flat field list.

The "meta" directive is used to specify HTML metadata stored in HTML
META tags.  "Metadata" is data about data, in this case data about web
pages.  Metadata is used to describe and classify web pages in the
World Wide Web, in a form that is easy for search engines to extract
and collate.

Within the directive block, a flat field list provides the syntax for
metadata.  The field name becomes the contents of the "name" attribute
of the META tag, and the field body (interpreted as a single string
without inline markup) becomes the contents of the "content"
attribute.  For example::

    .. meta::
       :description: The reStructuredText plaintext markup language
       :keywords: plaintext, markup language

This would be converted to the following HTML::

    <meta name="description"
        content="The reStructuredText plaintext markup language">
    <meta name="keywords" content="plaintext, markup language">


Support for other META attributes ("http-equiv", "scheme", "lang",
"dir") are provided through field arguments, which must be of the form
"attr=value"::

    .. meta::
       :description lang=en: An amusing story
       :description lang=fr: Un histoire amusant

And their HTML equivalents::

    <meta name="description" lang="en" content="An amusing story">
    <meta name="description" lang="fr" content="Un histoire amusant">

Some META tags use an "http-equiv" attribute instead of the "name"
attribute.  To specify "http-equiv" META tags, simply omit the name::

    .. meta::
       :http-equiv=Content-Type: 文字列/html; charset=UTF-8

HTML equivalent::

    <meta http-equiv="Content-Type"
         content="text/html; charset=UTF-8">


Imagemap
========

**NOT IMPLEMENTED YET**

Non-standard element: imagemap.


---------------
 Miscellaneous
---------------

.. _include:

Including an External Document Fragment
=======================================

:Directiveタイプ: "include"
:Doctreeエレメント: depend on data being included
:Directive引数: 1つ必須.
:Directiveオプション: 指定可能
:Directive本文: 無し

.. WARNING::

   The "include" directive represents a potential security hole.  It
   can be disabled with the "file_insertion_enabled_" runtime setting.

   .. _file_insertion_enabled: ../../user/config.html#file-insertion-enabled

The "include" directive reads a reStructuredText-formatted text file
and parses it in the current document's context at the point of the
directive.  The directive argument is the path to the file to be
included, relative to the document containing the directive.  For
example::

    This first example will be parsed at the document level, and can
    thus contain any construct, including section headers.

    .. include:: inclusion.txt

    Back in the main document.

        This second example will be parsed in a block quote context.
        Therefore it may only contain body elements.  It may not
        contain section headers.

        .. include:: inclusion.txt

If an included document fragment contains section structure, the title
adornments must match those of the master document.

The text encoding of the master input source is used for included
files.

以下のオプションを使用出来ます:

``literal`` : flag (empty)
    The entire included text is inserted into the document as a single
    literal block (useful for program listings).

``encoding`` : name of text encoding
    The text encoding of the external data file.  Defaults to the
    document's encoding (if specified).


.. _raw:

Raw Data Pass-Through
=====================

:Directiveタイプ: "raw"
:Doctreeエレメント: raw
:Directive引数: One or more, required (output format types).
:Directiveオプション: 指定可能
:Directive本文: Stored verbatim, uninterpreted.  None (empty) if a
                    "file" or "url" option given.

.. WARNING::

   The "raw" directive represents a potential security hole.  It can
   be disabled with the "raw_enabled_" or "file_insertion_enabled_"
   runtime settings.

   .. _raw_enabled: ../../user/config.html#raw-enabled

.. Caution::

   The "raw" directive is a stop-gap measure allowing the author to
   bypass reStructuredText's markup.  It is a "power-user" feature
   that should not be overused or abused.  The use of "raw" ties
   documents to specific output formats and makes them less portable.

   If you often need to use the "raw" directive or a "raw"-derived
   interpreted text role, that is a sign either of overuse/abuse or
   that functionality may be missing from reStructuredText.  Please
   describe your situation in email to
   docutils-users@lists.sourceforge.net.

The "raw" directive indicates non-reStructuredText data that is to be
passed untouched to the Writer.  The names of the output formats are
given in the Directive 引数.  The interpretation of the raw data
is up to the Writer.  A Writer may ignore any raw output not matching
its format.

For example, the following input would be passed untouched by an HTML
Writer::

    .. raw:: html

       <hr width=50 size=10>

A LaTeX Writer could insert the following raw content into its
output stream::

    .. raw:: latex

       \setlength{\parindent}{0pt}

Raw data can also be read from an external file, specified in a
directive option.  In this case, the content block must be empty.  For
example::

    .. raw:: html
       :file: inclusion.html

以下のオプションを使用出来ます:

``file`` : string (newlines removed)
    The local filesystem path of a raw data file to be included.

``url`` : string (whitespace removed)
    An Internet URL reference to a raw data file to be included.

``encoding`` : name of text encoding
    The text encoding of the external raw data (file or URL).
    Defaults to the document's encoding (if specified).

.. _replace:

Replacement Text
================

:Directiveタイプ: "replace"
:Doctreeエレメント: 文字列 & inline elements
:Directive引数: 無し
:Directiveオプション: 無し
:Directive本文: A single paragraph; may contain inline markup.

The "replace" directive is used to indicate replacement text for a
substitution reference.  It may be used within substitution
definitions only.  For example, this directive can be used to expand
abbreviations::

    .. |reST| replace:: reStructuredText

    Yes, |reST| is a long word, so I can't blame anyone for wanting to
    abbreviate it.

As reStructuredText doesn't support nested inline markup, the only way
to create a reference with styled text is to use substitutions with
the "replace" directive::

    I recommend you try |Python|_.

    .. |Python| replace:: Python, *the* best language around
    .. _Python: http://www.python.org/


.. _unicode:

Unicode Character Codes
=======================

:Directiveタイプ: "unicode"
:Doctreeエレメント: 文字列
:Directive引数: One or more, required (Unicode character codes,
                      optional text, and comments).
:Directiveオプション: 指定可能
:Directive本文: 無し

The "unicode" directive converts Unicode character codes (numerical
values) to characters, and may be used in substitution definitions
only.

The arguments, separated by spaces, can be:

* **character codes** as

  - decimal numbers or

  - hexadecimal numbers, prefixed by ``0x``, ``x``, ``\x``, ``U+``,
    ``u``, or ``\u`` or as XML-style hexadecimal character entities,
    e.g. ``&#x1a2b;``

* **text**, which is used as-is.

Text following " .. " is a comment and is ignored.  The spaces between
the arguments are ignored and thus do not appear in the output.
Hexadecimal codes are case-insensitive.

For example, the following text::

    Copyright |copy| 2003, |BogusMegaCorp (TM)| |---|
    all rights reserved.

    .. |copy| unicode:: 0xA9 .. copyright sign
    .. |BogusMegaCorp (TM)| unicode:: BogusMegaCorp U+2122
       .. with trademark sign
    .. |---| unicode:: U+02014 .. em dash
       :trim:

results in:

    Copyright |copy| 2003, |BogusMegaCorp (TM)| |---|
    all rights reserved.

    .. |copy| unicode:: 0xA9 .. copyright sign
    .. |BogusMegaCorp (TM)| unicode:: BogusMegaCorp U+2122
       .. with trademark sign
    .. |---| unicode:: U+02014 .. em dash
       :trim:

以下のオプションを使用出来ます:

``ltrim`` : flag
    Whitespace to the left of the substitution reference is removed.

``rtrim`` : flag
    Whitespace to the right of the substitution reference is removed.

``trim`` : flag
    Equivalent to ``ltrim`` plus ``rtrim``; whitespace on both sides
    of the substitution reference is removed.



Class
=====

:Directiveタイプ: "class"
:Doctreeエレメント: pending
:Directive引数: One or more, required (class names / attribute
                      values).
:Directiveオプション: 無し
:Directive本文: 無し

The "class" directive sets a "class" attribute value on the first
immediately following non-comment element [#]_.  For details of the
"class" attribute, see `its entry`__ in `The Docutils Document Tree`_.
The directive argument consists of one or more space-separated class
names, which are converted to lowercase and all non-alphanumeric
characters are converted to hyphens.  (For the rationale, see below.)

__ ../doctree.html#class

Examples::

    .. class:: special

    This is a "special" paragraph.

    .. class:: exceptional remarkable

    An Exceptional Section
    ======================

    This is an ordinary paragraph.

The text above is parsed and transformed into this doctree fragment::

    <paragraph class="special">
        This is a "special" paragraph.
    <section class="exceptional remarkable">
        <title>
            An Exceptional Section
        <paragraph>
            This is an ordinary paragraph.

.. [#] To set a "class" attribute value on a block quote, the "class"
   directive must be followed by an empty comment::

       .. class:: highlights
       ..

           Block quote text.

   The directive doesn't allow content, therefore an empty comment is
   required to terminate the directive.  Without the empty comment,
   the block quote text would be interpreted as the "class"
   directive's content, and the parser would complain.

.. topic:: Rationale for Class Attribute Value Conversion

    Docutils identifiers are converted to conform to the regular
    expression ``[a-z](-?[a-z0-9]+)*``.  For CSS compatibility,
    identifiers (the "class" and "id" attributes) should have no
    underscores, colons, or periods.  Hyphens may be used.

    - The `HTML 4.01 spec`_ defines identifiers based on SGML tokens:

          ID and NAME tokens must begin with a letter ([A-Za-z]) and
          may be followed by any number of letters, digits ([0-9]),
          hyphens ("-"), underscores ("_"), colons (":"), and periods
          (".").

    - However the `CSS1 spec`_ defines identifiers based on the "name"
      token, a tighter interpretation ("flex" tokenizer notation
      below; "latin1" and "escape" 8-bit characters have been replaced
      with entities)::

          unicode     \\[0-9a-f]{1,4}
          latin1      [&iexcl;-&yuml;]
          escape      {unicode}|\\[ -~&iexcl;-&yuml;]
          nmchar      [-a-z0-9]|{latin1}|{escape}
          name        {nmchar}+

    The CSS1 "nmchar" rule does not include underscores ("_"), colons
    (":"), or periods ("."), therefore "class" and "id" attributes
    should not contain these characters.  They should be replaced with
    hyphens ("-").  Combined with HTML's requirements (the first
    character must be a letter; no "unicode", "latin1", or "escape"
    characters), this results in the ``[a-z](-?[a-z0-9]+)*`` pattern.

    .. _HTML 4.01 spec: http://www.w3.org/TR/html401
    .. _CSS1 spec: http://www.w3.org/TR/REC-CSS1



.. _role:

Custom Interpreted Text Roles
=============================

:Directiveタイプ: "role"
:Doctreeエレメント: None; affects subsequent parsing.
:Directive引数: Two; one required (new role name), one optional
                      (base role name, in parentheses).
:Directiveオプション: Possible (depends on base role).
:Directive本文: depends on base role.

(New in Docutils 0.3.2)

The "role" directive dynamically creates a custom interpreted text
role and registers it with the parser.  This means that after
declaring a role like this::

    .. role:: custom

the document may use the new "custom" role::

    An example of using :custom:`interpreted text`

This will be parsed into the following document tree fragment::

    <paragraph>
        An example of using
        <inline class="custom">
            interpreted text

The role must be declared in a document before it can be used.

The new role may be based on an existing role, specified as a second
argument in parentheses (whitespace optional)::

    .. role:: custom(emphasis)

    :custom:`text`

The parsed result is as follows::

    <paragraph>
        <emphasis class="custom">
            text

If no base role is explicitly specified, a generic custom role is
automatically used.  Subsequent interpreted text will produce an
"inline" element with a "class" attribute, as in the first example
above.

With most roles, the ":class:" option can be used to set a "class"
attribute that is different from the role name.  For example::

    .. role:: custom
       :class: special

    :custom:`interpreted text`

This is the parsed result::

    <paragraph>
        <inline class="special">
            interpreted text

.. _role class:

The following option is recognized by the "role" directive for most
base roles:

``class`` : 文字列
    Set a "class" attribute value on the element produced (``inline``,
    or element associated with a base class) when the custom
    interpreted text role is used.  If no Directive オプション are
    specified, a "class" option with the directive argument (role
    name) as the value is implied.  See the class_ directive above.

Specific roles may support other options and/or Directive 本文.
See the `reStructuredText Interpreted Text Roles`_ document for
details.

.. _reStructuredText Interpreted Text Roles: roles.html

Restructuredtext-Test-Directive
===============================

:Directiveタイプ: "restructuredtext-test-directive"
:Doctreeエレメント: system_warning
:Directive引数: 無し
:Directiveオプション: 無し
:Directive本文: Interpreted as a literal block.

This directive is provided for test purposes only.  (Nobody is
expected to type in a name *that* long!)  It is converted into a
level-1 (info) system message showing the directive data, possibly
followed by a literal block containing the rest of the directive
block.


..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:


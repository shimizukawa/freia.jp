:date: 2013-02-16 18:00
:tags: Python, Sphinx, textwrap

=======================================================
2013/02/16 Pythonのtextwrap.wrap()が日本語で崩れる問題
=======================================================

:py:func:`textwrap.wrap()` を使うとテキストを例えば70文字で折り返して整形
するといった事が出来ます。しかしこいつは **文字数** で折り返しするので、
日本語などの全角幅(fullwidth)な文字を与えると幅がぜんぜん揃わなくて
残念なことになってしまいます。

Sphinxの :command:`make text` でも内部で :py:mod:`textwrap` の実装を
使っているため、この問題が発生します。

Sphinx-1.1.3でSphinxのドキュメントを :command:`make text` すると英語の場合は
問題無く以下のように整形されます。

.. code-block:: rst

   reStructuredText Primer
   ***********************

   This section is a brief introduction to reStructuredText (reST)
   concepts and syntax, intended to provide authors with enough
   information to author documents productively.  Since reST was designed
   to be a simple, unobtrusive markup language, this will not take too
   long.

   See also:

      The authoritative reStructuredText User Documentation.  The "ref"
      links in this document link to the description of the individual
      constructs in the reST reference.


   Paragraphs
   ==========

   The paragraph (>>:duref:`ref <paragraphs>`<<) is the most basic block
   in a reST document.  Paragraphs are simply chunks of text separated by
   one or more blank lines.  As in Python, indentation is significant in
   reST, so all lines of the same paragraph must be left-aligned to the
   same level of indentation.

英語の場合は単語の区切りで改行するなどの調整もしてくれているので、
多少幅がガタついていますが、まあ綺麗に揃っています。

しかし日本語の場合は以下のようになってしまいます。


.. code-block:: text

   reStructuredText入門
   ******************

   このセクションは、reStructuredText(reST)の考え方や文法についての短いイントロダクションです。Sphinxユーザがドキュ
   メントを作成するために十分な情報を提供します。reSTはシンプルに設計された、控えめなマークアップ言語ですので、理解するのにそれほど時間はか
   からないでしょう。

   See also:

      本家 reStructuredTextユーザドキュメント
      このドキュメント中の参照リンクは、reSTのリファレンスの個々の要素の説明にリンクしています。


   段落(パラグラフ)
   =========

   段落(>>:duref:`ref <paragraphs>`<<)はreSTドキュメントにおける、もっとも基本的な要素です。段落は1行以上の
   空行で区切られた、シンプルなテキストの固まりです。 Pythonにおいてインデントが重要な意味を持つのと同様、reSTでもインデントは重要で
   す。同じ段落のすべての行は、インデントを同じ高さにそろえて、左揃えにしなければなりません。


数えてみると、半角全角関係なく文字数で70文字で改行されています。
タイトルの次の行の ``=`` 文字もタイトルの長さに合って欲しいところ
ですが、文字数は合ってても幅は合ってませんね。

上記の例では分かりませんが、英単語も空白無しで日本語文字と連続してしまうと、
単語の途中でも強制的に改行されます。これはひどい。

これだと色々悲しいので、python本体の :py:class:`textwrap.TextWrapper`
を継承して、多少修正して以下のように出力されるようにしました。

.. code-block:: text

   reStructuredText入門
   ********************

   このセクションは、reStructuredText(reST)の考え方や文法についての短いイ
   ントロダクションです。Sphinxユーザがドキュメントを作成するために十分な
   情報を提供します。reSTはシンプルに設計された、控えめなマークアップ言語
   ですので、理解するのにそれほど時間はかからないでしょう。

   See also:

     本家 reStructuredTextユーザドキュメント このドキュメント中の参照リン
     クは、reSTのリファレンスの個々の要素の説明にリンクしています。


   段落(パラグラフ)
   ================

   段落(>>:duref:`ref <paragraphs>`<<)はreSTドキュメントにおける、もっと
   も基本的な要素です。段落は1行以上の空行で区切られた、シンプルなテキス
   トの固まりです。 Pythonにおいてインデントが重要な意味を持つのと同様、
   reSTでもインデントは重要です。同じ段落のすべての行は、インデントを同じ
   高さにそろえて、左揃えにしなければなりません。


キレイ。


ということで、以下が拡張したTextWrapperの全コードです。

ポイントは、 ``_split()`` 関数と ``len()`` を使っている部分の差し替えです。
``_split()`` は元の実装では空白等で文字列を分割していたのですが、
全角文字の場合は1文字ずつ全部分割しました。 ``len()`` は文字数ではなく
幅を返す関数に差し替えました。この2つによって、
うまく70桁幅でそろえられるようになりました。


.. code-block:: python

   # -*- coding: utf-8 -*-
   import sys
   import textwrap
   import unicodedata
   from itertools import groupby

   #copy from docutils
   east_asian_widths = {'W': 2,   # Wide
                        'F': 2,   # Full-width (wide)
                        'Na': 1,  # Narrow
                        'H': 1,   # Half-width (narrow)
                        'N': 1,   # Neutral (not East Asian, treated as narrow)
                        'A': 1}   # Ambiguous (s/b wide in East Asian context,
                                  # narrow otherwise, but that doesn't work)

   #copy from docutils
   def column_width(text):
       """Return the column width of text.

       Correct ``len(text)`` for wide East Asian and combining Unicode chars.
       """
       if isinstance(text, str) and sys.version_info < (3,0):
           return len(text)
       combining_correction = sum([-1 for c in text
                                   if unicodedata.combining(c)])
       try:
           width = sum([east_asian_widths[unicodedata.east_asian_width(c)]
                        for c in text])
       except AttributeError:  # east_asian_width() New in version 2.4.
           width = len(text)
       return width + combining_correction


   class TextWrapper(textwrap.TextWrapper):
       """Custom subclass that uses a different word splitter."""

       def _wrap_chunks(self, chunks):
           """_wrap_chunks(chunks : [string]) -> [string]

           Original _wrap_chunks use len() to calculate width.
           This method respect to wide/fullwidth characters for width adjustment.
           """
           lines = []
           if self.width <= 0:
               raise ValueError("invalid width %r (must be > 0)" % self.width)

           chunks.reverse()

           while chunks:
               cur_line = []
               cur_len = 0

               if lines:
                   indent = self.subsequent_indent
               else:
                   indent = self.initial_indent

               width = self.width - column_width(indent)

               if self.drop_whitespace and chunks[-1].strip() == '' and lines:
                   del chunks[-1]

               while chunks:
                   l = column_width(chunks[-1])

                   if cur_len + l <= width:
                       cur_line.append(chunks.pop())
                       cur_len += l

                   else:
                       break

               if chunks and column_width(chunks[-1]) > width:
                   self._handle_long_word(chunks, cur_line, cur_len, width)

               if self.drop_whitespace and cur_line and cur_line[-1].strip() == '':
                   del cur_line[-1]

               if cur_line:
                   lines.append(indent + ''.join(cur_line))

           return lines

       def _break_word(self, word, space_left):
           """_break_word(word : string, space_left : int) -> (string, string)

           Break line by unicode width instead of len(word).
           """
           total = 0
           for i,c in enumerate(word):
               total += column_width(c)
               if total > space_left:
                   return word[:i-1], word[i-1:]
           return word, ''

       def _split(self, text):
           """_split(text : string) -> [string]

           Override original method that only split by 'wordsep_re'.
           This '_split' split wide-characters into chunk by one character.
           """
           split = lambda t: textwrap.TextWrapper._split(self, t)
           chunks = []
           for chunk in split(text):
               for w, g in groupby(chunk, column_width):
                   if w == 1:
                       chunks.extend(split(''.join(g)))
                   else:
                       chunks.extend(list(g))
           return chunks

       def _handle_long_word(self, reversed_chunks, cur_line, cur_len, width):
           """_handle_long_word(chunks : [string],
                                cur_line : [string],
                                cur_len : int, width : int)

           Override original method for using self._break_word() instead of slice.
           """
           space_left = max(width - cur_len, 1)
           if self.break_long_words:
               l, r = self._break_word(reversed_chunks[-1], space_left)
               cur_line.append(l)
               reversed_chunks[-1] = r

           elif not cur_line:
               cur_line.append(reversed_chunks.pop())


   MAXWIDTH = 70


   def fw_wrap(text, width=MAXWIDTH, **kwargs):
       w = TextWrapper(width=width, **kwargs)
       return w.wrap(text)


ということでSphinxの実装を差し替ました
https://bitbucket.org/birkenfeld/sphinx/commits/9869f4e 。
こんな感じでSphinxの実装・改善してるよ、ってことで。


:date: 2006-02-05 17:26:23
:categories: ['python']
:body type: text/x-rst

===========================================
2006/02/05 SilverCity-0.9.6がうまく動かない
===========================================

*Category: 'python'*

SilverCity-0.9.6がうまく動かない。
問題点をSourceForgeにバグ報告したので、次のバージョンでは直って欲しいな。


.. :extend type: text/x-rst
.. :extend:

0.9.6を以下のように実行するとexceptする。

.. code-block:: python

  >>> from StringIO import StringIO
  >>> out = StringIO()
  >>> from SilverCity import LanguageInfo
  >>> pgen = LanguageInfo.find_generator_by_name('python')()
  >>> pgen.generate_html(out,'import test')
  Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    File "/usr/local/lib/python2.4/site-packages/SilverCity/Python.py", line 60, in generate_html
      lexer.tokenize_by_style(buffer, self.event_handler)
    File "/usr/local/lib/python2.4/site-packages/SilverCity/Lexer.py", line 8, in tokenize_by_style
      call_back
  TypeError: expected sequence of 2 WordLists (1 provided)

調べてみたら、0.9.6で取り込んだscintillaのコードにpython-wrapperが対応できていないようだ。以下のように修正したところ、正しく動いているようだ。

SilverCity-0.9.6/PySilverCity/SilverCity/Python.py (13-15)の

.. code-block:: python

        self._keyword_lists = [
            WordList(Keywords.python_keywords)
                            ]

を以下のように修正。

.. code-block:: python

        self._keyword_lists = [
            WordList(Keywords.python_keywords),
            WordList(),
                            ]

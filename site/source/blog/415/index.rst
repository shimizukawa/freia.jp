:date: 2007-03-13 12:44:08
:tags: python
:body type: text/x-rst

===========================
2007/03/13 SilverCity-0.9.7
===========================

以前、 `SilverCity-0.9.6がうまく動かない`_ というエントリを書いたが、 `0.9.7`_ で修正されたようだ。去年の11月に `バグレポ`_ に対して「直したよ」という返答があったのだが、届いたメールが自宅メールサーバーに埋もれてしまっていた。

それはさておき、さっそく0.9.7を取得して以前と同じテストコードで動作確認してみる。

.. code-block:: python

    >>> from StringIO import StringIO
    >>> out = StringIO()
    >>> from SilverCity import LanguageInfo
    >>> pgen = LanguageInfo.find_generator_by_name('python')()
    >>> pgen.generate_html(out,'import test')
    >>> out.getvalue()
    '<span class="p_word">import</span><span class="p_default">&nbsp;</span><span class="p_identifier">test</span>'

うまくいった。

.. _`SilverCity-0.9.6がうまく動かない`: http://www.freia.jp/taka/blog/310
.. _`0.9.7`: http://sourceforge.net/project/showfiles.php?group_id=45693
.. _`バグレポ`: http://sourceforge.net/tracker/index.php?func=detail&aid=1424436&group_id=45693&atid=443739


.. :extend type: text/html
.. :extend:


:date: 2006-07-04 03:43:15
:categories: ['python']
:body type: text/x-rst

===================================================
2006/07/04 Python2.4.2と2.4.3でMIMETextの挙動が違う
===================================================

*Category: 'python'*

Zope2.9.3をいじってて気づいたんだけど、Python2.4.2と2.4.3とでemail.MIMEText.MIMETextクラスの挙動がちょっと違うっぽい。どう違うかというと、

.. code-block:: python

  Python 2.4.2 (#1, Jul  4 2006, 01:41:41)
  [GCC 3.4.2 [FreeBSD] 20040728] on freebsd5
  Type "help", "copyright", "credits" or "license" for more information.
  >>> from email.MIMEText import MIMEText
  >>> m = MIMEText('hello', 'plain', 'utf-8')
  >>> m.get_payload()
  'hello'

と

.. code-block:: python

  Python 2.4.3 (#1, Jul  4 2006, 01:43:57)
  [GCC 3.4.2 [FreeBSD] 20040728] on freebsd5
  Type "help", "copyright", "credits" or "license" for more information.
  >>> from email.MIMEText import MIMEText
  >>> m = MIMEText('hello', 'plain', 'utf-8')
  >>> m.get_payload()
  'aGVsbG8=\n'
  >>> import base64
  >>> base64.decodestring(m.get_payload())
  'hello'

という感じ。payloadがbase64エンコードされちゃってる。 ``エンコードは _charset 引数にもとづき暗黙のうちに行われる`` らしいので、Python2.4.3でこの暗黙の部分が何か変わったんだろうなあ‥‥。もっとも、m['Content-Transfer-Encoding']はPython2.4.2以前からbase64なので、2.4.3の方が正しいのかもしれない。これまでと挙動が違って困るけど。

`What's New in Python 2.4.3?`_ に ``emailモジュールをアップデートした`` という記述はあるけど、直接関連しそうな細目は載ってないんですよね‥‥。リリースノート眺めててもよく分からないので、MLで聞いてみようかな。

.. _`What's New in Python 2.4.3?`: http://www.python.org/download/releases/2.4.3/NEWS.txt

----

MIMETextの第二引数はsubtypeなので、 ``text`` じゃなくて ``plain`` と書くべきでした。Python-ml-jpで柴田さんにやんわりと正されてしまった‥‥しまったなぁ(--;

.. :extend type: text/html
.. :extend:

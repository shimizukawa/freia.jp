:date: 2009-10-17 14:21:05
:categories: ['python']
:body type: text/x-rst

========================================================
2009/10/17 emailモジュールの使い方サンプル #zopeplonedev
========================================================

第4回 Zope/Plone開発勉強会で、emailモジュールの話になったので、実験コードを書いてみた。

.. code-block:: python

  >>> from email.MIMEText import MIMEText
  >>> from email.Header import Header
  >>> def buildmail(charset, toaddrs, subject, message):
  ...   m_body = message.encode(charset, 'replace')
  ...   m_subject = subject
  ...   m_subject = Header(m_subject.encode(charset, 'replace'), charset)
  ...   m_from = 'foo@example.com'
  ...   m_to = ', '.join(toaddrs)
  ...   message = MIMEText(m_body, 'plain', charset)
  ...   message['Subject'] = m_subject
  ...   message['From'] = m_from
  ...   message['To'] = m_to
  ...   return message
  ...

上記の関数に渡すデータを用意。

::

  >>> text = u'にほんごにほんご'

iso-2022-jp でエンコードする例::

  >>> e = buildmail('iso-2022-jp', ['bar@example.com'], text, text)
  >>> print e.as_string()
  Content-Type: text/plain; charset="iso-2022-jp"
  MIME-Version: 1.0
  Content-Transfer-Encoding: 7bit
  Subject: =?iso-2022-jp?b?GyRCJEskWyRzJDQkSyRbJHMkNBsoQg==?=
  From: foo@example.co.jp
  To: bar@example.com
  
  $B$K$[$s$4$K$[$s$4(B

utf-8 でエンコードする例::

  >>> e = buildmail('utf-8', ['bar@example.com'], text, text)
  >>> print e.as_string()
  Content-Type: text/plain; charset="utf-8"
  MIME-Version: 1.0
  Content-Transfer-Encoding: 8bit
  Subject: =?utf-8?b?44Gr44G744KT44GU44Gr44G744KT44GU?=
  From: foo@example.co.jp
  To: bar@example.com

  にほんごにほんご

Subjectはbase64になってました。本文は指定した文字エンコードの生データですね。

ちなみに、上記コードは2006年にpython-mlに質問したときのコードです。懐かしい。
`[Python-ml-jp 3602] 2.4.3のMIMETextクラスのpayloadの持ち方 <http://www.python.jp/pipermail/python-ml-jp/2006-July/003595.html>`_


.. :extend type: text/html
.. :extend:


:date: 2007-02-25 11:10:00
:tags: Plone

=======================================
PloneのSMTP設定にGMailを指定
=======================================

最近、利用しているCATVインターネット接続でもOP25bが導入され、自宅サーバーのSMTPから自宅外へメール送信することが出来なくなってしまった。このサイトのPloneのSMTP設定もlocalhostを利用していたのだが、通知メールの受け取りを自宅外に設定できないのでは不便なので（というかGMailに転送したいので）、GMailのSMTPサーバーを指定してみた。

Plone サイト設定 -> メールの設定:

:SMTPサーバ: smtp.gmail.com
:SMTPポート: 587
:ESMTPユーザ名: xxxxxx@gmail.com
:ESMTPパスワード: xxxxxxxx

これであとはGMail側でPOPを利用する設定にしておけばメールが送信できる、はずだった。

実際に送ってみたところ、 ``メールを送ることができません: (8, 'EOF occurred in violation of protocol')``
というエラーが送信フォームに表示されてしまった。何だろう・・。
とりあえずこのエラーメッセージで検索してみると、PythonでProxy+SSL通信する例がたくさん見つかる。smtplib もキーワードに追加してみると、以下の内容が見つかった。

.. highlights::

  Most SSL servers and clients (primarily HTTP, but some SMTP as well) are
  broken in this regard: they do not properly negotiate TLS connection
  shutdown.  This causes one end or the other to notice an SSL protocol error.

  多くののSSLサーバーとクライアントの実装は仕様通りでなく、正しいTLS接続のシャットダウン処理が
  行われていない。この実装はSSLプロトコル上のエラーを引き起こす。

  -- `sslerror: (8, 'EOF occurred in violation of protocol') ???`__

.. __: http://mail.python.org/pipermail/python-list/2005-August/338280.html


他にこんな内容も見つかった。

.. highlights::

  As the error states, Google Domains closes the SSL SMTP connection 
  early, in violation of the TLS/SMTP protocol. Please contact Google to 
  fix their SMTP server.

  このエラーはGoogleがSSL SMTP接続を規定よりも早く閉じてしまっていて、これは
  TLS/SMTPプロトコルに反する。GoogleにSMTPサーバーを直すように言ってください。

  -- `[Zope] SecureMailHost Error`__

.. __: http://mail.zope.org/pipermail/zope/2007-February/170430.html


.. :extend type: text/x-rst
.. :extend:

そこで、smtp送信を行っているあたりのプログラム(SecureMailHost-1.0.4/mail.py[89-126])を抜粋してPythonの対話モードで試してみたところ、smtp接続を切る段階でたしかにエラーが発生してしまった。

.. code-block:: python

  >>> smtpserver = smtplib.SMTP('smtp.gmail.com',587)
  >>> smtpserver.ehlo()
  (250, 'mx.google.com at your service, [61.24.99.179]\nSIZE 20971520\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES')
  >>> smtpserver.starttls()
  (220, '2.0.0 Ready to start TLS')
  >>> smtpserver.ehlo()
  (250, 'mx.google.com at your service, [61.24.99.179]\nSIZE 20971520\n8BITMIME\nAUTH LOGIN PLAIN\nENHANCEDSTATUSCODES')
  >>> smtpserver.login('xxxxxxxx@gmail.com','xxxxxx')
  (235, '2.7.0 Accepted')
  >>> smtpserver.quit()
  Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    File "C:\develop\python24\lib\smtplib.py", line 712, in quit
      self.docmd("quit")
    File "C:\develop\python24\lib\smtplib.py", line 374, in docmd
      return self.getreply()
    File "C:\develop\python24\lib\smtplib.py", line 348, in getreply
      line = self.file.readline()
    File "C:\develop\python24\lib\smtplib.py", line 160, in readline
      chr = self.sslobj.read(1)
  socket.sslerror: (8, 'EOF occurred in violation of protocol')
  >>>

SecureMailHostで発生したこのExceptionはキャッチされていないため、エラーが画面に表示される。そこで、もうしょうがないので、smtpserver.quit()のあたりを以下のように書き換えて対処することにした。

.. code-block:: python

  try:
      smtpserver.quit()
  except socket.sslerror,e:
      pass

エラーの種類見てないけど、quitの時のエラーだし、まあいいか。


.. image:: 20070223_securemailhost.*
   :width: 33%


:date: 2007-10-28 01:55:13
:tags: python
:body type: text/x-rst

=============================================
2007/10/28 OP25b回避にGMailを利用 (on python)
=============================================

Python温泉の成果2。

以前 `PloneのSMTP設定にGMailを指定`_ というネタを書きましたが、ソースコードをPython一般で使えるように抽出してみました。以下のサンプルはパスワードが含まれてるので、実用のためにはそのへんをゴニョっとする必要があります。

.. code-block:: python

  #!/usr/local/bin/python
  # -*- coding: utf-8 -*-
  
  ID = 'xxxxxxx@gmail.com'
  PW = 'dummy'
  FROM = 'xxxxx@example.com'
  
  import smtplib
  
  def sendmail(toaddrs,subject,msg):
      if isinstance(toaddrs, basestring):
          toaddrs=[toaddrs]
      smtpserver = smtplib.SMTP('smtp.gmail.com',587)
      smtpserver.ehlo()
      smtpserver.starttls()
      smtpserver.ehlo()
      smtpserver.login(ID,PW)
  
      t=', '.join(toaddrs)
      msg='From: %s\nTo: %s\nSubject: %s\n\n%s' % (FROM,t,subject,msg)
      smtpserver.sendmail(FROM, toaddrs, msg)
      try:
          smtpserver.quit()
      except socket.sslerror,e:
          pass
  
  if __name__ == '__main__':
      sendmail('testaddr@example.com','subject','testmail')



.. _`PloneのSMTP設定にGMailを指定`: http://www.freia.jp/taka/blog/403?searchterm=gmail

.. :extend type: text/html
.. :extend:


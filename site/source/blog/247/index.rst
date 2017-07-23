:date: 2005-09-06 15:08:27
:tags: Plone

==============================================
Ploneのワークフローでメール通知する
==============================================

`ryouseiさんの資料`_ を横目で見つつ、 `[zope-users:04900] [Q] customize workflow with script`_ を参考にしながら作ってみました。
それにしても、スクリプトが受け取る引数の型がStateChangeInfoだとか、StateChangeInfo.objectが対象ページのインスタンスだとか、どうやって知るんだろう？自分は前述の資料とgrepで知りました。

以下、とりあえず動くスクリプトです。

.. _`[zope-users:04900] [Q] customize workflow with script`: http://ml.zope.jp/pipermail/zope-users/2004-May/004712.html
.. _`ryouseiさんの資料`: http://www.plone.jp/Members/ryousei/




.. :extend type: text/x-rst
.. :extend:

emailモジュールを使っているので、Script(Python)で使えるようにしておく必要があります。

.. code-block:: python

  ## Script (Python) "mail_notify"
  ##bind container=container
  ##bind context=context
  ##bind namespace=
  ##bind script=script
  ##bind subpath=traverse_subpath
  ##parameters=sci
  ##title=
  ##
  try:
      mail = container.MailHost

      hist = sci.getHistory()
      hist = hist[-1]
      obj = sci.object

      data = []
      data.append( "URL: " + obj.absolute_url() )
      data.append( "Date: " + str(sci.getDateTime()) )
      data.append( "Actor: " + hist['actor'])
      data.append( "Title: " + obj.title_or_id() )
      data.append( "Desc: " + obj.Description() )


      data = '\n'.join(data)

      from email.Header import Header
      title = Header(unicode(obj.title_or_id(),'utf-8').encode('iso-2022-jp','replace'), 'iso-2022-jp')

      msg = """\
  From: test@example.com
  To: test@example.com
  Subject: published: %s
  Content-Type: text/plain; charset="iso-2022-jp"

  Page published.

  %s
  """ % (title, data)

      msg = unicode(msg,'utf-8').encode('iso-2022-jp','replace')
      mail.send(msg)

  except:
      pass




:date: 2009-12-03 23:55:00
:categories: ['Zope', 'Plone']
:body type: text/x-rst

======================================================================
2009/12/03 COREBlog2をPlone3で動かすための修正: コメント時のメール送信
======================================================================

12/4修正。間違いが多かったため書き直しました。Plone3やZope2.10系の問題だと書いていたのですが、Zope2.9.10 + Plone-2.5.5でも発生します。

------------------------

`Plone-3.3.2 にアップグレードして公開`_ したときの課題からは抜けていたのですが（今日気づいた）、COREBlog2を setdefaultencoding('utf-8') 無しで動かしたとき、そのままではコメント時やトラックバック時にメール送信が行われない場合があります。

:対象: `COREBlog2_nightly.tgz`_ (2008/10時点)
:Plone: Plone-3.3.2
:Zope: Zope-2.10.9

.. _`Plone-3.3.2 にアップグレードして公開`: http://www.freia.jp/taka/blog/686
.. _`COREBlog2_nightly.tgz`: http://coreblog.org/junk_l/COREBlog2_nightly.tgz

以前の環境でエラー無くメール送信が行われていた理由は、 sitecustomize.py に ``sys.setdefaultencoding('uft-8')`` と書いていたためだと思います。今回の環境では sitecustomize.py 無しで動かそうとしているので、translateメソッドからUnicodeオブジェクトが返ってくるのと、REQUESTからの値を結合しようとしたときに、予期しないUnicodeDecodeErrorとなったためです。

という前置きはさておき、修正方法。

skins/COREBlog2/cbaddComment::

        to_addr   = context.getNotify_to()
        from_addr = context.getNotify_to()
      - msgbody = context.translate(msgid='comment_notify_body')
      + msgbody = context.translate(msgid='comment_notify_body').decode('utf-8')
        elements = {}
        for k in ('title','author','url','body'):
            if REQUEST.form.has_key(k):
                elements[k] = REQUEST.form[k]
            else:
                elements[k] = ''
        elements['post_ip'] = REQUEST.getClientAddr()
        elements['entry_url'] = context.absolute_url()
        msgbody = msgbody % (elements)
      - msgsubject = context.translate('comment_notify_title')
      + msgsubject = context.translate('comment_notify_title').decode('utf-8')
        mgsheader = """To: %s

同様に skins/COREBlog2/tbping も ``translate`` しているところを修正します。

これでコメントが正しくメール通知されるようになりました。


.. :extend type: text/x-rst
.. :extend:


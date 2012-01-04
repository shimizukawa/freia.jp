:date: 2006-06-14 00:20:28
:categories: ['Plone']
:body type: text/x-rst

======================================
2006/06/14 COREBlog2スパム対策(まとめ)
======================================

*Category: 'Plone'*

最近仕事の影響で **私** がかなり疎かになってしまっています。そんな中、 `takanory.netさんからtrackbackをもらった`_ のでこれに反応して、自分が行っているCOREBlog2スパム対策をまとめてみます。これを読めば一通り設定できるはず＞for 未来の自分

# 参考： `spamとの戦い（回顧編）`_

.. _`takanory.netさんからtrackbackをもらった`: http://takanory.net/
.. _`spamとの戦い（回顧編）`: http://www.freia.jp/taka/blog/306


.. :extend type: text/x-rst
.. :extend:

スパム対策共通BuzzWordチェックスクリプト
-----------------------------------------
`以前にblogに書いたスクリプト`_ と同一です。スパマーがこのエントリを見ているとは思いませんが、念のためbuzzwordは省略します。とはいえ、大抵のスパム投稿には ``url=`` か ``href`` が入っているので、この2つを設定しておけばほとんど防げると思います。

.. _`以前にblogに書いたスクリプト`: http://www.freia.jp/taka/blog/coreblog27c216613spam-filter

以下のコードをportal_skins/custom等に置きます。

.. code-block:: python

    ## Script (Python) "validateBuzzWords"
    ##bind container=container
    ##bind context=context
    ##bind namespace=
    ##bind script=script
    ##bind subpath=traverse_subpath
    ##parameters=text, moderated=True
    ##title=COREBlog2: buzzword checker
    ##
    buzz_words = (
      'casino',
    )
    
    try:
        if not moderated:
            return moderated
    
        s = str(text).lower()
        for w in buzz_words:
            if s.find(w) >= 0:
                moderated = False
                break
        else:
            moderated = True
    
    except:
        pass
    
    return moderated



コメントスパム対策
--------------------

まずはcbaddCommentの直接呼び出しを拒否するようにカスタマイズします。これが必要になるシーンは滅多にないとは思いますが、自分は喰らってしまったので対策しています。22行目～27行目が追加されています。

.. code-block:: python

    ## Controller Python Script "cbaddComment"
    ##bind container=container
    ##bind context=context
    ##bind namespace=
    ##bind script=script
    ##bind state=state
    ##bind subpath=traverse_subpath
    ##parameters=
    ##title=COREBlog2: modify: refuce direct access
    ##
    from Products.CMFPlone import transaction_note
    from Products.CMFCore.utils import getToolByName
    from Products.CMFPlone.utils import log
    
    cbtool = getToolByName(context, 'coreblog2_tool')
    
    REQUEST = context.REQUEST
    form = REQUEST.form
    RESPONSE = context.REQUEST.RESPONSE
    entry = context
    
    # refuse direct access.
    if script is REQUEST.get('PUBLISHED',None):
        RESPONSE.setStatus(403)
        return '403 Forbidden'
        #return RESPONSE.redirect('403 Forbidden', 403)
    
    if REQUEST.form.has_key('remember_cookie'):
        #Set cookie
        for key in ['author','email','url']:
            if REQUEST.form.has_key(key):
                REQUEST.RESPONSE.setCookie(key,REQUEST.form[key],
                            path='/'.join(context.blog_object().getPhysicalPath()),
                            expires='Sun, 01-Dec-2099 12:00:00 GMT')
    
    #Try to add comment
    entry.addComment2Entry(author=form['author'],email=form['email'],
                            url=form['url'],title=form['title'],
                            body=form['body'],REQUEST=REQUEST)
    
    #Send notify mail if need
    if context.getSend_comment_notification():
        try:
            to_addr   = context.getNotify_to()
            from_addr = context.getNotify_to()
            msgbody = context.translate('comment_notify_body')
            elements = {}
            for k in ('title','author','url','body'):
                if REQUEST.form.has_key(k):
                    elements[k] = REQUEST.form[k]
                else:
                    elements[k] = ''
            elements['post_ip'] = REQUEST.getClientAddr()
            elements['entry_url'] = context.absolute_url()
            msgbody = msgbody % (elements)
            msgsubject = context.translate('comment_notify_title')
            mgsheader = """To: %s
    From: %s
    Mime-Version: 1.0
    Content-Type: text/plain; Charset=utf-8
    
    """ % (to_addr,from_addr)
            cbtool.send_mail(mgsheader+msgbody, to_addr, from_addr, msgsubject)
        
        except Exception,e:
            log( 'COREBlog2/cbaddComment: '
                     'Some exception occured, %s' % e )
    
    #Set next action
    state.setNextAction('redirect_to:string:')
    
    #Display message for user
    state.setKwargs({'portal_status_message':'A comment successfully added.'})
    return state
    
    
    
    return state




validateCommentにBuzzWordをチェックするコードを追加しています。以下のカスタマイズでは、smapの傾向や元IP収集のためにBuzzWordに引っかかった場合に、投稿内容を管理者にメール送信し、投稿フォームにはエラーを表示して投稿自体はされないようにしています。

.. code-block:: python

    ## Controller Validator "validateComment"
    ##bind container=container
    ##bind context=context
    ##bind namespace=
    ##bind script=script
    ##bind state=state
    ##bind subpath=traverse_subpath
    ##parameters=
    ##title=COREBlog2: modify: add buzzword check
    ##
    from Products.CMFPlone import transaction_note
    REQUEST=context.REQUEST
    moderated = True
    
    reqs = ['title','body']
    
    #See setting and append required field list
    if context.getComment_require_author():
        reqs.append('author')
    
    if context.getComment_require_email():
        reqs.append('email')
    
    if context.getComment_require_url():
        reqs.append('url')
    
    for key in reqs:
        if REQUEST.has_key(key) and not REQUEST[key]:
            state.setError(key, 'Please enter a value', new_status='failure')
    
    for key in ['title', 'body', 'author', 'email', 'url']:
        if REQUEST.has_key(key):
            m = context.validateBuzzWords(REQUEST[key], True)
            if not m:
                state.setError(key, 'Please remove NG words.', new_status='failure')
                moderated = False
    
    #Try to send mail for Bad comment
    if not moderated:
        context.addCommentMail(
                            author=REQUEST['author'],email=REQUEST['email'],
                            url=REQUEST['url'],title=REQUEST['title'],
                            body=REQUEST['body'], moderated=moderated,
                            remoteip=REQUEST.getClientAddr())
    
    if state.getErrors():
        state.set(portal_status_message='Please correct the errors shown.')
    
    return state




BuzzWordコメント時のメール送信用スクリプトです。これはCOREBlog2がメール送信によるコメント通知をサポートする前に作ったものですが、アクセス元IPを通知してくれるあたりがスパム対策っぽい感じです。

.. code-block:: python

    ## Script (Python) "addCommentMail"
    ##bind container=container
    ##bind context=context
    ##bind namespace=
    ##bind script=script
    ##bind subpath=traverse_subpath
    ##parameters=author,email,url,title,body,moderated,remoteip='',message=''
    ##title=
    ##
    try:
        mailhost=getattr(context, \
                         context.superValues(['Secure Mail Host', 'Mail Host'])[0].id)
    except:
        raise AttributeError, "Mail Host object cant be found."
    
    
    mMsg = """To: %s
    From: %s
    Mime-Version: 1.0
    Content-Type: text/plain;
    
    Moderate : %s
    ManageURL: http://www.freia.jp/taka/blog/%s/entry_comments
    ViewURL  : http://www.freia.jp/taka/blog/%s
    RemoteIP : %s
    Author   : %s
    Title    : %s
    URL      : %s
    EMail    : %s
    EntryID  : %s
    Body     :
    %s
    
    Additional message:
    %s
    """
    
    try:
        to_addr   = "admin@example.jp"
        from_addr = "admin@example.jp"
        parent_id = context.getId()
    
        mTo   = to_addr
        mFrom = from_addr
        mSubj = 'blog: A comment %s' % (moderated and 'added!' or 'NEED MODERATE.')
        mMsg  = mMsg % (to_addr, from_addr, str(moderated), parent_id, parent_id, \
                        remoteip, author, title, url, email, parent_id, body, message )
    
        mailhost.send(mMsg, mTo, mFrom, mSubj)
    
    except:
        raise



トラックバックスパム対策
-------------------------

tbpingをカスタマイズして、validateBuzzWordsとスパム時のメール送信を呼び出すようにしています。

.. code-block:: python

    ## Script (Python) "tbping"
    ##bind container=container
    ##bind context=context
    ##bind namespace=
    ##bind script=script
    ##bind subpath=traverse_subpath
    ##parameters=
    ##title=Receive trackback: COREBlog2: modify: check buzzwords
    ##
    from Products.CMFCore.utils import getToolByName
    from Products.CMFPlone.utils import log
    
    cbtool = getToolByName(context, 'coreblog2_tool')
    
    REQUEST = context.REQUEST
    form = REQUEST.form
    RESPONSE = context.REQUEST.RESPONSE
    entry = context
    
    excerpt = ''
    if form.has_key('excerpt'):
        excerpt = form['excerpt']
    
    title = cbtool.convert_charcode(form['title'])
    blog_name = cbtool.convert_charcode(form['blog_name'])
    excerpt = cbtool.convert_charcode(excerpt)
    
    #Try to add trackback
    try:
        # !!!STAART modify by shimizukawa!!!
        moderated = True
        for text in [title, blog_name, excerpt]:
            m = context.validateBuzzWords(text, True)
            if not m:
                state.setError(key, 'Please remove NG words.', new_status='failure')
                moderated = False
    
        #Try to send mail for Bad comment
        if not moderated:
            context.addTrackbackMail(
                                title=title, url='',
                                blog_name=blog_name,
                                excerpt=excerpt,
                                moderated=moderated,
                                remoteip=REQUEST.getClientAddr(),
                                message='NEED MODERATE',)
            raise 'NEED MODERATE'
        # !!!END modify by shimizukawa!!!
    
        #Send notify mail if need
        if context.getSend_trackback_notification():
            try:
                to_addr   = context.getNotify_to()
                from_addr = context.getNotify_to()
                msgbody = context.translate('trackback_notify_body')
                elements = {}
                for k in ('blog_name','title','excerpt','url','excerpt'):
                    if form.has_key(k):
                        elements[k] = REQUEST.form[k]
                    else:
                        elements[k] = ''
                elements['post_ip'] = REQUEST.getClientAddr()
                elements['entry_url'] = context.absolute_url()
                msgbody = msgbody % (elements)
                msgsubject = context.translate('trackback_notify_title')
                mgsheader = """To: %s
    From: %s
    Mime-Version: 1.0
    Content-Type: text/plain; Charset=utf-8
    
    """ % (to_addr,from_addr)
                cbtool.send_mail(mgsheader+msgbody, to_addr, from_addr, msgsubject)
            except Exception,e:
                log( 'COREBlog2/tbping: '
                         'Some exception occured, %s' % e )
    
        entry.addTrackback2Entry(title=title,url=form['url'],\
                                blog_name=blog_name,excerpt=excerpt)
    
        return context.tbping_result(client=context,REQUEST=REQUEST,\
                                            error_code=0,message='Thanks :-)')
    except:
        return context.tbping_result(client=context,REQUEST=REQUEST,\
                                        error_code=1,message='Error occured!')



addCommentMailとほぼ同一のスクリプト。トラックバック用。芸のないコピペコード。

.. code-block:: python

    ## Script (Python) "addTrackbackMail"
    ##bind container=container
    ##bind context=context
    ##bind namespace=
    ##bind script=script
    ##bind subpath=traverse_subpath
    ##parameters=title,url,blog_name,excerpt,moderated,remoteip='',message=''
    ##title=
    ##
    try:
        mailhost=getattr(context, \
                         context.superValues(['Secure Mail Host', 'Mail Host'])[0].id)
    except:
        raise AttributeError, "Mail Host object cant be found."
    
    mMsg = """To: %s
    From: %s
    Mime-Version: 1.0
    Content-Type: text/plain;
    
    Moderate : %s
    ManageURL: http://www.freia.jp/taka/blog/%s/entry_trackbacks
    ViewURL  : http://www.freia.jp/taka/blog/%s
    RemoteIP : %s
    Title    : %s
    URL      : %s
    BlogName : %s
    EntryID  : %s
    Excerpt  :
    %s
    
    Additional message:
    %s
    """
    
    try:
        to_addr   = "admin@example.jp"
        from_addr = "admin@example.jp"
        parent_id = context.getId()
    
        mTo   = to_addr
        mFrom = from_addr
        mSubj = 'blog: A trackback %s' % (moderated and 'added!' or 'NEED MODERATE.')
        mMsg  = mMsg % (to_addr, from_addr, str(moderated), parent_id, parent_id, \
                        remoteip, title, url, blog_name, parent_id, excerpt, message )
    
        mailhost.send(mMsg, mTo, mFrom, mSubj)
    
    except:
        raise



ApacheのIPアドレス制限
-----------------------
ログの出力を標準のアクセスと別にしたり、アクセス時にZopeにアクセスに行かないように設定したりしてます。httpd.confの書き方を全然調査してないので冗長な感じです。あと本当はエラーページじゃなくて403を返すように設定したい。

.. code-block:: python

    SetEnvIf Remote_addr "(24\.244\.170\.180|81\.177\.8\.26)" spam1
    CustomLog /var/log/httpd/www.freia.jp-access.log combined env=!spam1
    CustomLog /var/log/httpd/www.freia.jp-access-spam1.log combined env=spam1
    ErrorLog /var/log/httpd/www.freia.jp-error.log

    RewriteEngine On

    # for spam filtering.
    RewriteCond %{REMOTE_HOST}  ^(24\.244\.170\.180|81\.177\.8\.26)
    RewriteRule ^/(.*) http://localhost:80/underconstruction/ [P,L]

    # rewrite standard zope server.
    RewriteRule ^/(.*) http://localhost:8080/VirtualHostBase/http/www.freia.jp:80/VirtualHostRoot/$1 [P,L]

上記のhttpd.conf、見やすくするためにIPアドレス制限を2つだけ書いていますが、本当は以下のIPを制限しています。

    24.244.170.180
    65.214.44.212
    66.246.218.107
    69.50.167.122
    81.177.7.108
    81.177.7.154
    81.177.7.37
    81.177.7.81
    81.177.8.26
    85.255.117.18
    194.117.134.72
    195.39.170.102
    200.79.91.5
    202.56.253.184
    209.190.4.10
    209.190.4.106
    209.67.219.178





.. :trackbacks:
.. :trackback id: 2006-06-27.0228277053
.. :title: Akismetを使ったトラックバック・スパム対策
.. :blog name: Weboo! Returns.
.. :url: http://yamashita.dyndns.org/blog/reject-trackback-spam-by-akismet
.. :date: 2006-06-27 23:20:23
.. :body:
.. いい加減にトラックバック・スパムがうざくなってきたので対策してみました。COREBlog2におけるコメント＆トラックバック・スパム対策に関しては、清水川さんが纏めてくれているので、それを参考にAkismetというWordPress標準の対策機能を使ってSP...
.. 
.. :trackbacks:
.. :trackback id: 2006-07-26.3118481816
.. :title: COREBlog2のコメントスパム・トラックバックスパム対策
.. :blog name: Triconf Blog
.. :url: http://triconf.net/blog/coreblog2306e30b330e130f330c830b930e030fb30c830e930c330af30c330af30b930e05bfe7b56
.. :date: 2006-07-26 16:18:32
.. :body:
..  いつかこういう日が来るとは思っていましたが、突如、COREBlog2に対して膨大な量のコメントスパムがつけられるようになってしまいました。 そこでGoogle神に問い合わせますと、以下の清水川さんの記事に行き当たりました。  COREBlog2スパム対策...
.. 

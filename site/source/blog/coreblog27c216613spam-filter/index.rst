:date: 2005-12-15 02:48:46
:categories: ['Plone']
:body type: text/x-rst

========================
COREBlog2簡易spam-filter
========================

コメント追加の許可設定の件を調べようと思ったら、コメント追加が可能になったとたんspamコメントが10件以上投稿されていた。ムカツク。とりあえず、COREBlog1のBuzzWordsチェック機構をCOREBlog2用に改造してチェックするようにしたので、これで様子見。

.. :extend type: text/x-rst
.. :extend:
追加コードは意外と少なくて、portal_skins/COREBlog2/validateCommentを以下のようにカスタマイズする。これでBuzzWordsに引っかかった項目がエラーとなって投稿できない。

::

    for key in ['title', 'body', 'author', 'email', 'url']:
        if REQUEST.has_key(key):
            m = context.validateBuzzWords(REQUEST[key])
            if not m:
                state.setError(key, 'Pleae remove NG words.', new_status='failure')
    
    if state.getErrors():

いちおうvalidateBuzzWordsも載せておく。これもportal_skins/custom等に置いて、引数textを取るようにしておく。今回の用途ではmoderated変数が用をなしていないけど、まぁいいか。

::

    buzz_words = (
      'casino',
      'poker',
    )
    
    moderated=True
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


:Trackbacks:
:TrackbackID: 2006-06-13.9575564577
:BlogName: takalog
:url: http://takanory.net/takalog/553
:date: 2006-06-13 23:29:18

==================================
COREBlog2 簡易 trackback spam 対策
==================================

 最近このサイトに大量の trackback spam が届くようになりました。  で、言及リンク付きかどうかチェックではじこうかと思っていたんですが、いろいろ問題があってできてませんでした。  そうは言っても spam は止まりません。COREB...


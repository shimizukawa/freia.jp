:date: 2005-10-11 23:00:34
:tags: Zope

==================================
2005/10/11 COREBlog1.2.1がリリース
==================================

`COREBlog1.2.1`_ がリリースされました。今回のリリースを境にメンテナンスモードに入ると言うことで、これまでの延長線上での機能追加はこれが最後になるようです。

ということで、さっそく今回のリリースで追加された **コメントやトラックバックの追加前にフックメソッドを呼び出す** 機能を使ってみました。


.. _`COREBlog1.2.1`: http://www.zope.org/Members/ats/COREBlog



.. :extend type: text/plain
.. :extend:

コメント追加前に *コメントスパム* の可能性があるかどうかをチェックして、
可能性がある場合は *要モデレート* 状態にします。

.. image:: coreblog_buzzwords
  :align: right

今回はとりあえずNGワードを含む投稿をチェックすることにします。
まず、 COREBlogインスタンスのmethodsフォルダ(以下blog/methods)のプロパティーに
``buzz_words`` という名前のプロパティーを ``lines`` 型で追加します。
そして、プロパティーの値として行単位でNGワードを追加します。

自分は最初はpoker等を対象にしていたのですが、最近はきりがなくなってきたので ``href``
をNGワードにしてしまいました。

次に、以下のPythonスクリプトを ``beforeAddComment`` という名前で blog/methods
フォルダに追加します。

.. code-block:: python

    ## Script (Python) "beforeAddComment"
    ##bind container=container
    ##bind context=context
    ##bind namespace=
    ##bind script=script
    ##bind subpath=traverse_subpath
    ##parameters=d
    ##title=
    ##
    try:
        if not d["moderated"]:
            return d

        buzz_words = container.getProperty("buzz_words")
        s = str(d).lower()
        for w in buzz_words:
            if s.find(w) >= 0:
                d["moderated"] = 0
                break
        else:
            d["moderated"] = 1
    
    except:
        pass
    
    return d

このへんのコードは `lirisさんの記事`_ から頂いたものをCOREBlog1.2.1用に軽く修正
しています。ありがとうございます。

同様に ``beforAddTrackback`` というスクリプトを用意すれば同じ事が出来ます。


.. figure:: coreblog_spams
  :align: left

  結果、こんな感じでコメントスパムがフィルタリングされています。
  チェックの付いていないやつがフィルタされたスパムです。
  
  ‥‥大杉。今日だけでコメントスパム投稿数 **100件** って何？

.. cssclass:: visualClear

.

.. _`lirisさんの記事`: http://www.liris.org/blog/626/





.. :comments:
.. :comment id: 2005-11-28.5215125905
.. :title: Re: COREBlog1.2.1がリリース
.. :author: setomits
.. :date: 2005-10-12 10:59:37
.. :email: 
.. :url: 
.. :body:
.. なるほど、 beforeAddComment はこうやって使うんですね。参考にさせてもらいます。
.. 
.. ところで d["moderated"] = 1 のとこの else のブロックのインデントがひとつ左にずれて見えるのは Safari だからかしらん。
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.5216275155
.. :title: Re: COREBlog1.2.1がリリース
.. :author: 清水川
.. :date: 2005-10-12 12:03:08
.. :email: 
.. :url: 
.. :body:
.. > ところで d["moderated"] = 1 のとこの else のブロックのインデントがひとつ左にずれて見えるのは Safari だからかしらん。
.. 
.. いえ、これはfor文に対するelseです。つまりfor文が回りきった場合のみ実行されてます。
.. 
.. でもよく考えるとbuzz_wordsに引っかからなかったら *放置* するのが正しい動作のような気が...。結果としてはelse節は無くても動作は同じですね(;-;
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.5217421897
.. :title: Re: COREBlog1.2.1がリリース
.. :author: setomits
.. :date: 2005-10-12 14:17:03
.. :email: 
.. :url: 
.. :body:
.. なるほど。
.. にあるあたりですね。
.. これまでこういう else の使い方をしたことがなかったので、ちょっとびっくりしました。
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.5218594889
.. :title: Re: COREBlog1.2.1がリリース
.. :author: shin
.. :date: 2005-10-13 12:49:10
.. :email: 
.. :url: 
.. :body:
.. はじめまして、shinと申します。plonifiedについて質問です。
.. COREBlog1.2 / COREBlog1.2.1 で
.. スキンをplonifiedに変更すると、
.. There is no setting in this skin.  
.. 確認すると、
.. Site Error
.. An error was encountered while publishing this resource. 
.. のエラーで、plonifiedスキン利用出来ないのですが。なぜでしょう。
.. defaultのスキンは、適用されます。
.. 
.. Apache/2.0.54 (Win32) DAV/2 mod_autoindex_color mod_ssl/2.0.54 OpenSSL/0.9.8 mod_jk2/2.0.4 PHP/5.0.4 SVN/1.2.3
.. 
.. Apache / zope 連携
.. 
.. Ploneバージョン概要
.. Plone 2.1, 
.. Zope (Zope 2.7.7-final, python 2.3.5, win32), 
.. 
.. 以上の件、宜しくお願い致します。
.. 
.. 
.. 
.. 
.. 
.. 
.. 
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.5219769054
.. :title: Re: COREBlog1.2.1がリリース
.. :author: 清水川
.. :date: 2005-10-13 15:10:03
.. :email: 
.. :url: 
.. :body:
.. plonifiedに変更したときに
..   「スキンの設定を編集してください。'(Blogのタイトル)'.」
..   There is no setting in this skin. 
.. と表示されるのは、plonifiedのskinに設定項目が無いためです。viewで表示すればちゃんとPloneに統合されて表示されませんか？
.. 
.. 表示されずに、後半にかかれているようなエラーが起きるのであれば、、、ちょっとわかりません。そこから先はここよりも、COREBlogかZopeのMLで聞かれるのが近道かも。
.. 
.. 
.. 
.. :trackbacks:
.. :trackback id: 2005-11-28.5220920963
.. :title: コメントスパム弾き実験のまとめ
.. :blog name: blogSetomits
.. :url: http://matatabi.homeip.net/blog/setomits/476
.. :date: 2005-11-28 00:48:42
.. :body:
.. これまで3度に渡って実験してきたコメントスパム弾き実験をまとめます。
.. 基本的には JavaScript
.. を無効にしている人にとっては、一旦有効にしてからリロードして...とめんどいし、そのハンドリングを考えるとめんどいので却下。
.. 具体的には時刻情報を埋め込んで、POSTされるときの時刻から許容できるずれ幅を超えていたらはねて...

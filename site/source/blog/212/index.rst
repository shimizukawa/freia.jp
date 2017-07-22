:date: 2005-05-21 01:34:39
:tags: Zope

===================================================
2005/05/21 ZPhotoSlidesメモリ・ディスク食い潰し問題
===================================================

最近ふと気が付くと Data.fs [1]_ が17GBにふくれあがっている事が何度かあった。Packさぼってたからかなー‥‥と思って1週間でPackすると6GBくらいになる。いくら何でもおかしい。

最近ふと気が付くとZopeの使用メモリ量が512MBを超えている。そして一部のページを表示するときにMemoryErrorが発生する。どうやらその一部のページというのはZPhotoSlidesコンテンツのようだ‥‥。

なんで写真ページを表示するだけでData.fsが150KB～500KBも増えるのか。そして、botのアクセスがなければここまで深刻な問題ではなかったのかもしれない。

とりあえずソースに以下の変更を加えて対処してみた。

.. code-block:: python

 rating.py: 75
    def showRatings(self):
        ''' return 1 if object use ratings '''
        if not self.isPrincipiaFolderish:
            if hasattr(self.aq_parent,'show_rating'):
 -               self.show_rating = self.aq_parent.show_rating
 +               return self.aq_parent.show_rating
        return self.show_rating

 ZPhoto.py: 593
                if(not REQUEST.cookies.has_key('visited'+str(self.getId()))):
 -                  self.viewed = self.viewed + 1
 +                  #self.viewed = self.viewed + 1
                    REQUEST.RESPONSE.setCookie('visited'+str(self.getId()),1)

 ZPhoto.py: 623
                if(not REQUEST.cookies.has_key('visited'+str(self.getId()))):
 -                  self.viewed = self.viewed + 1
 +                  #self.viewed = self.viewed + 1
                    REQUEST.RESPONSE.setCookie('visited'+str(self.getId()),1)

どうやら、ZPhotoインスタンスのフィールドを更新しているのが原因らしい。これがUndoに記録されるのかな？こんなの、Undo出来ないんだからUndoされなくてもいいのに‥‥。 [2]_

とりあえずよりよい対処法が見つかるまで、写真のアクセスカウントはしない方向で。というか、botのアクセスがカウントされるのってどうなのよ？

----------------------

.. [1] Zopeのユーザーデータが格納される仮想(?)ストレージ
.. [2] 勝手な憶測です。



.. :extend type: text/plain
.. :extend:


:date: 2006-03-31 02:11:26
:tags: Zope

==============================================
画像に文字列を埋め込むZope3アダプタ
==============================================

3月の `Zope3勉強会`_ で `俳写`_ をZope3でやってみたい、と言う案がさとうさんから出たので、とりあえず `画像と文字列を合成するAdapter`_ を作ってみました。

最初は、画像フィールドとテキストフィールドを表示時に毎回合成する新しいコンテンツタイプを作ったのですが、途中で、Adapterにすれば新しいコンテンツじゃなくても標準の画像(IImage)にAdaptできるという事に気づき路線変更。さらにEventとAnnotationを使って、画像オブジェクトの編集時のみ画像合成するようにしました。Ploneプロダクト作成の発想からZope3の発想にちょっとだけ切り替えられた気がします。

*# Imageクラスを拡張するという発想はかなり正しかったですよ＞さとうさん*

途中、間違ってAnnnotationに自分自身を格納しようとしてシリアライズ出来ないエラーに悩まされたり、Adapterのセキュリティープロクシ周りのzcmlの書き方に悩まされたりと、Zope3の最初の壁をまだ乗り越えられてない感じです。

.. _`Zope3勉強会`: http://qwik.jp/zope3study/
.. _`俳写`: http://www.50pa.com/haisya.html
.. _`画像と文字列を合成するAdapter`: http://qwik.jp/zope3study/53.html


.. :extend type: text/x-rst
.. :extend:



.. :comments:
.. :comment id: 2006-03-31.4919162786
.. :title: Re:画像に文字列を埋め込むZope3アダプタ
.. :author: masaru
.. :date: 2006-03-31 21:34:56
.. :email: 
.. :url: 
.. :body:
.. そのさとうさんって人アイディアだけじゃね？(￣ｍ￣)ぷっ
.. 
.. :comments:
.. :comment id: 2006-03-31.6710379116
.. :title: Re:画像に文字列を埋め込むZope3アダプタ
.. :author: しみずかわ
.. :date: 2006-03-31 22:11:11
.. :email: 
.. :url: 
.. :body:
.. じゃ、あとよろしく＞さとーさん
.. 

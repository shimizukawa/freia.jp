:date: 2005-02-21 09:01:53
:categories: ['Zope']
:body type: text/x-rst

====================================
2005/02/21 COREblog in Ploneフォルダ
====================================

*Category: 'Zope'*

Ploneへとりあえず移行しました。

COREblogのインスタンスをPloneフォルダに移動させたところ、

- 初期表示時にFormatが設定値にかかわらずPlainTextになる
- エントリのPreview時に本文が表示されない
- エントリのPreview時にFormat設定値がPlainTextにリセットされる

等々の問題があることが分かりました。が、とりあえずAddEntryは正しく動作しているようなので、このまま様子を見ながら運用してみたいと思います。



.. :extend type: text/plain
.. :extend:



.. :comments:
.. :comment id: 2005-11-28.4745408069
.. :title: Re: COREblog in Ploneフォルダ
.. :author: 清水川
.. :date: 2005-02-21 11:07:29
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. 追記： 環境依存の可能性は高いと思う。別環境で試してからMLに問い合わせてみよう……。
.. 
.. 
.. :Trackbacks:
.. :TrackbackID: 2005-11-28.4746544401
.. :title: うわ，ほんとだ(Re: COREBlog in Ploneフォルダ)
.. :BlogName: TRIVIAL TECHNOLOGIES
.. :url: http://coreblog.org/ats/576
.. :date: 2005-11-28 00:47:54
.. :body:
.. ん。早速試したところ，エントリの投稿時，デフォルトフォーマットが指定したとおりにならない。
.. 多分Ploneインスタンス上にあるattribute(Propertyかなにか)と，COREBlog上のPropertyが衝突して居るんだと思います。明示的にCOREBlogインスタンス上にあるPropertyから...
.. 
.. 
.. :Trackbacks:
.. :TrackbackID: 2005-11-28.4747493431
.. :title: なんか新しいPLONEとかいうXOOPSみたいなCMS・・・
.. :BlogName: レトロブログ - retroさんのブログ - RETRO-MANIA
.. :url: http://www.retro-mania.net/modules/weblog/details.php?blog_id=28
.. :date: 2005-11-28 00:47:54
.. :body:
.. PLONEっていうコミュニティサイト構築スクリプトを相棒がインストールしだしたので、興味しんしんで経過を見守っています。見た目は、なんとなくスマート。当サイトでも利用しているXOOPSの場合、各種モジュールを追加することによって、色々な機能を共通の言語で利用することができるのですが（たとえば　imgboard、blog、掲示板、フォーラム、ニュース、ヘッドライン、wiki、ゲームなど）このPLONEってのは、まだマイナーな代わりに、ひじょ〜〜にシンプル。そして、技術者いわく「軽い」そうです。今後、流行す...

:date: 2004-04-20 23:30:00
:tags: Zope, misc

===================================
COREBlogのStructuredText
===================================

ところで、COREBlogのStructuredTextがよく分かりません。URLリンクの指定の仕方とか、普通のStructuredTextと違うんでしょうか？

仕方がないので今はStructuredTextの中にbrとかhrefとか書いてます。めんどくさいなぁ。



.. :extend type: text/plain
.. :extend:



.. :comments:
.. :comment id: 2005-11-28.4224109314
.. :title: Re: COREBlogのStructuredText
.. :author: aihatena
.. :date: 2004-04-21 18:48:37
.. :email: 
.. :url: 
.. :body:
.. こうすんでない?
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4226095038
.. :title: Re: COREBlogのStructuredText
.. :author: 清水川
.. :date: 2004-04-21 18:58:25
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. "google"なら良いんだけど、"日本語"だとダメみたい。日本語のパースがうまくいってないな‥‥日本語関連のライブラリいじったから？
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4227418385
.. :title: Re: COREBlogのStructuredText
.. :author: aihatena
.. :date: 2004-04-21 19:21:47
.. :email: 
.. :url: 
.. :body:
.. ふむむ。。
.. あと Entry.py で
.. 
.. #Formats
.. format_plain = 0
.. format_stx = 1
.. format_html = 3
.. format_wiki = 2
.. 
.. なのに EntryPage ではWikiが無いのはなんでだろ。
.. 
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4229127086
.. :title: Re: COREBlogのStructuredText
.. :author: 清水川
.. :date: 2004-04-22 09:28:28
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. SettingFormに0,1,2しかoptionを書いてないからですね。理由は不明だけど。
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4230396370
.. :title: Re: COREBlogのStructuredText
.. :author: の
.. :date: 2004-05-20 11:01:20
.. :email: 
.. :url: 
.. :body:
.. 今更かもしれませんが、StructuredText で日本語が扱えないのは、 Zope の StructuredText の実装が腐ってるせいです（＾＾；
.. 
.. 
.. このへん参照。
.. 多分2.7でもまだ直ってない。
.. 
.. 2.7だとReStructuredTextが標準で入ったようだけど、そっちだとたしょうはましなのかな?
.. 使ったことないからわかんないや
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4231705946
.. :title: Re: COREBlogのStructuredText
.. :author: 清水川
.. :date: 2004-05-20 14:31:15
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. 情報ありがとうございます～。
.. おかげさまで、パッチを当てたら直りました。
.. 
.. パッチは以下のURLのを使いました。
.. 
.. 頂いたURLで語られている状態よりはなんぼかましになっているみたいですが、2.6→2.7では全く変わっていないようです。（おかげでパッチがそのまま適用できましたが‥‥）
.. 
.. reStructuredText については日本語で不自由した事は‥‥ちょっとあります(^^  
.. 
.. UTF-8を使っていると日本語の全角文字も1文字として数えてくれるのは良いのですが、テーブルを作るために列あわせをするときに半角・全角とも１文字で数えちゃうんですよね。これはZope-mlで相談したらパッチを作ってもらえました。
.. 

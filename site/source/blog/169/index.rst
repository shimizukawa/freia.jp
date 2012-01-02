:date: 2005-03-23 12:48:47
:categories: ['python', 'Programming']
:body type: text/x-rst

===========================
2005/03/23 pythonでHTML解析
===========================

会社の同僚が

  「Webサイトに定期的にアクセスして内容を解析して○○××を自動的に実行するプログラムを作りたい。
  Perlで作ろうと思うんだけど……」

という話をしていたので、Pythonを勧めてみた。ついでにサンプルコードを作ってみた。

myparser.py::

    from HTMLParser import HTMLParser
    
    class MyHTMLParser(HTMLParser):
        def handle_data(self, data):
            data = data.strip(" 　\t\r\n")
            if data:
                print 'Data: "%s"' % data
    
        def handle_starttag(self, tag, attrs):
            pass
            #print 'TagStart: "%s"' % tag
    
        def handle_endtag(self, tag):
            pass
            #print 'TagEnd: "%s"' % tag
    
    def main(url):
        import urllib
        data = urllib.urlopen( url )
        mp = MyHTMLParser()
        mp.feed( data.read() )
    
    
    if __name__ == "__main__":
        import sys
        url = "http://python.jp/"
        if len( sys.argv ) > 1:
            url = sys.argv[1]
    
        main(url)

これを引数無しで実行すると、python.jpのページが取れてきて以下のように表示される::

    Data: "Click"
    Data: "here"
    Data: "to get to the FrontPage."

超適当に作った割にはちゃんと動いたなぁ。



.. :extend type: text/plain
.. :extend:


.. :comments:
.. :comment id: 2005-11-28.4855949363
.. :title: Re: pythonでHTML解析
.. :author: uemura
.. :date: 2005-03-23 16:03:49
.. :email: makoto.uemura@gmail.com
.. :url: 
.. :body:
.. すみません、質問なのですが、
.. 
.. HTMLParserというかpythonで日本語を含むHPを解析しようと思うと
.. (たとえばunicode(data).encode("sjis")みたいな処理）
.. 失敗するのですが、どのような処理をしたらいいのでしょうか？
.. 
.. 
.. 
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4857113122
.. :title: Re: pythonでHTML解析
.. :author: 清水川
.. :date: 2005-03-24 00:03:46
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. すみません、pythonプロじゃないので全然詳しくないのですが、unicode(data) ってエンコード判別してくれるんでしょうか？APIマニュアル見た感じだと判別してくれないような気が‥‥。
.. 
.. とりあえず、HTTPレスポンスでContent-Typeを返してくれるサーバーの場合は以下のようにしてエンコードを取得することは出来ました。
.. 
..     import urllib
..     data = urllib.urlopen( url )
..     charset = data.headers.getparam('charset')
.. 
.. そして以下のようにして文字変換します。
.. 
..     data = unicode(data,charset).encode("sjis")
.. 
.. サーバーがContent-Typeをくれない場合はmeta タグのContent-Typeを見るとか、でしょうか‥‥？それもだめなら自動判別‥‥って、どうやるんだろう？
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4858298371
.. :title: Re: pythonでHTML解析
.. :author: uemura
.. :date: 2005-03-24 11:28:30
.. :email: makoto.uemura@gmail.com
.. :url: 
.. :body:
.. ありがとうございます。
.. 自動判別は難しそうですね。
.. 
.. こんな感じで
..     import urllib
..     data = urllib.urlopen( url )
..     charset = data.headers.getparam('charset')
..     print charset
..         charset = "sjis"  #本来ならここに自動判別のプログラムを入れる。
..     mp = MyHTMLParser()
..     mp.feed(unicode(data.read(),charset).encode("sjis") )
.. 
.. ある程度のものは読めるようになりました。
.. 
.. RSS,AtomのParserであるuniversal feed parser モジュールはこの辺もしっかりやってるんだろうなとソースを読んでみようかと思ったら発狂しそうになりました。
.. 
.. もうちょっといろいろ調べてみようかと思います。
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4859453562
.. :title: Re: pythonでHTML解析
.. :author: uemura
.. :date: 2005-03-24 14:24:29
.. :email: makoto.uemura@gmail.com
.. :url: 
.. :body:
.. なんどもすみません
.. 
..     import urllib
..     import pykf
..     cod = ("UNKNOWN","ASCLL","SJIS","EUC-JP","JIS","utf-8","UTF-16-LE","UTF-16-BE","ERROR")
..     data = urllib.urlopen( url )
..     urlstring = data.read()
..     mp = MyHTMLParser()
..     charset = cod[pykf.guess(urlstring)]
..     data = urllib.urlopen( url )
..     mp.feed(unicode(urlstring,charset).encode("sjis") )
.. 
.. PyKfモジュールで判定はできましたけど、
.. windowsでutf-8をSJISに変換するときにエラーが出るときがあります。
.. 
.. 難しいですね。
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4860618397
.. :title: Re: pythonでHTML解析
.. :author: 清水川
.. :date: 2005-03-24 22:42:26
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. > PyKfモジュールで判定はできましたけど、
.. 
.. おお！すばらしい！！参考にさせていただきます。
.. とはいえ、自動判別については、既存のブラウザでも完璧なのは無いですし、うまくいかなくてもしょうがない部分はありますね。
.. 
.. > windowsでutf-8をSJISに変換するときにエラーが出るときがあります。
.. 
.. SJISに無い文字が混ざっているとか？（あてずっぽう）
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4861761649
.. :title: Re: pythonでHTML解析
.. :author: i?
.. :date: 2005-03-25 09:38:27
.. :email: 
.. :url: 
.. :body:
.. ここの 683に、いくつかのencodingで変換試して
.. UnicodeExceptionの場合ハズレ、という方法が。
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4862902542
.. :title: Re: pythonでHTML解析
.. :author: 清水川
.. :date: 2005-03-25 23:21:51
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. > ここの 683に
.. 
.. それはよい方法だね！
.. 実際の所、pykfが無い環境で近似的にやるにはリーズナブルだなぁ。（pykf, 中で同じ方法でチェックしてたりして‥‥）
.. 
.. 
.. :comments:
.. :comment id: 2007-02-25.7602364260
.. :title: Re:pythonでHTML解析
.. :author: nagaetty
.. :date: 2007-02-25 23:12:42
.. :email: 
.. :url: http://www6.atwiki.jp/nagae_tatsua/pages/1.html
.. :body:
.. python勉強中のものです。大変参考になるソースをありがとうございます。
.. pykfのあるページが参照できなくなっているので、
.. http://www.python.jp/Zope/download/pythonjpdist
.. のWindowsインストーラを入手して、自分のページを参照してみました。
.. 
.. 
.. 
.. :comments:
.. :comment id: 2007-02-25.4961561563
.. :title: Re:pythonでHTML解析
.. :author: しみずかわ
.. :date: 2007-02-25 23:24:56
.. :email: 
.. :url: 
.. :body:
.. 各所で出てますが、webarchiveから入手できますよ～
.. 
.. http://web.archive.org/web/20060206123300/http://gembook.jp/tsum/page.pys?wiki=PyKf
.. 
.. あと、HTML解析については、PythonWorkshopで紹介されたBeautiful Soupが良いかもしれません。良い感じで手を抜けそうです。
.. 
.. http://www.python.jp/Zope/workshop/200612/index_html?pp=1
.. 
.. :Trackbacks:
.. :TrackbackID: 2005-11-28.4864045021
.. :title: Ploneの使い方
.. :BlogName: PukiWiki/TrackBack 0.1
.. :url: http://tokyo.atso-net.jp/sitedev/index.php?Plone%A4%CE%BB%C8%A4%A4%CA%FD
.. :date: 2005-11-28 00:48:06
.. :body:

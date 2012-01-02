:date: 2005-04-20 23:33:24
:categories: ['Zope', 'work']
:body type: text/x-rst

=======================
2005/04/20 会社の歓迎会
=======================

*Category: 'Zope', 'work'*

会社の歓迎会で「清水川さんってblog書いてますよね。会社名で色々情報集めてる時に見ました」とか言われてかなりびっくり。そういえば昔（２年くらい前？）は社名出してたなー、とか思ったり。

で、どのくらい検索で引っかかるのかと思ってgoogleで調べたところ、あんまり引っかからない。キーワードを色々変えてみたらやっと１件引っかかった、という程度でちょっと安心。

ところが、googleのリンク先がPloneに移行する前のURLだったため、リンク先に飛んでも昔の日記にアクセス出来ないことが判明。つまり::

  http://www.freia.jp/taka/diary/2004_03

というアドレスにアクセスしても、今上記のURLのコンテンツは::

  http://www.freia.jp/taka/taka_old/diary/2004_03

に移動してしまっているわけ。そこで、http://www.freia.jp/taka/ の位置に diary という名前の *Script(Python)* を作成して、スクリプトの中身を以下のように記述::

  request = container.REQUEST
  RESPONSE =  request.RESPONSE
  
  url = request.VIRTUAL_URL_PARTS[1]
  new_url = '/taka/taka_old/' + '/'.join( url.split('/')[1:] )
  
  RESPONSE.redirect( new_url )

これで旧URLでアクセスした人も新URLへ誘導出来る、という寸法。urlparseモジュールを使う方法もあるかも、と思いつつ使い慣れた方で書いてしまいました。（他にも正規置換とか決め打ち置換とか出来そうだけど）

*#しかし、C言語では書きたくないなー...*

*#というか会社名で検索した人向けに正しいURLに誘導するなよ＜俺*



.. :extend type: text/plain
.. :extend:


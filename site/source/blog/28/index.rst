:date: 2004-07-14 23:49:54
:tags: python, Programming

=============================
計算パズルとpython
=============================

`i? <http://www.freia.jp/aihatena/>`__ から計算パズルを出されました。10分くらい考えてみたのですが答えが出ず、悔しかったのでプログラム(python)で解いてみることにしました。

問題

  1, 1, 5, 8 の4つの数字を使って四則演算を行い、答えが10となる式を作れ。ただし、以下の条件を守ること。

    - 各数字を必ず１回ずつ使う

    - 単項のマイナス演算は不可

    - 二つの数字をくっつけて二桁にするのは不可



.. :extend type: text/structured
.. :extend:

pythonで計算するために、まずは逆ポーランド計算機を用意。これはgoogleで探したサイトから流用しました::

  import string
  stack = []
  for x in input:
      if x == '+':
          stack.append(stack.pop() + stack.pop())
      elif x == '-':
          stack.append(stack.pop(-2) - stack.pop())
      elif x == '*':
          stack.append(stack.pop() * stack.pop())
      elif x == '/':
          stack.append(stack.pop(-2) / stack.pop())
      else:
          stack.append(string.atof(x))
  return stack[-1]

へー、リスト型に対してpopが出来るんですね‥‥。pop_frontは無いのでしょうか？自分はpythonでプログラムを一から組んだことが無いので、どんなことが出来るのかすらよく分かっていません。

とりあえずそんな問題は棚上げにして、パズルを解くアルゴリズムを考えます。

逆ポーランド計算機に入れる計算式のパターンは以下で全てのようです(#=数字, o=演算子)::

  #,#,#,#,o,o,o
  #,#,#,o,#,o,o
  #,#,#,o,o,#,o
  #,#,o,#,#,o,o
  #,#,o,#,o,#,o

あとは、'#'に(1,1,5,8)の組み合わせを入れて、'o'に演算子の全組み合わせを入れて全パターン調べるだけです。とりあえずざくざくとプログラムを書いてみたところ、以下のようになりました::

  # n=num, s=sign(+-*/)
  pattern=[]
  pattern.append(['n','n','n','n','s','s','s'])
  pattern.append(['n','n','n','s','n','s','s'])
  pattern.append(['n','n','n','s','s','n','s'])
  pattern.append(['n','n','s','n','n','s','s'])
  pattern.append(['n','n','s','n','s','n','s'])
  
  num=('1','1','5','8')
  sign=('+','-','*','/')
  
  sign_pattern=[]
  for x in range(4):
    for y in range(4):
      for z in range(4):
        tmp = []
        tmp.append( sign[x] )
        tmp.append( sign[y] )
        tmp.append( sign[z] )
        sign_pattern.append( tmp )
  
  num_pattern=[]
  for x in range(4):
    for y in range(3):
      for z in range(2):
        num_copy=[i for i in num]
        tmp=[]
        tmp.append( num_copy.pop( -1-x ) )
        tmp.append( num_copy.pop( -1-y ) )
        tmp.append( num_copy.pop( -1-z ) )
        tmp.append( num_copy.pop() )
        num_pattern.append( tmp )
  
  for n in num_pattern:
    for s in sign_pattern:
      for p_set in pattern:
        nc=[i for i in n]
        sc=[i for i in s]
        input=[]
        for p in p_set:
          if p=='n':
            input.append( nc.pop() )
          else:
            input.append( sc.pop() )
        try:
          if context.rpn(input=input) == 10:
            return input
        except:
          pass
  
  return 'failed'

‥‥初めてC言語でプログラムを書いた頃のことを思い出してしまいました。何というか、とりあえず知っている書き方と本(今回はWeb)を調べて見つけた書き方で何とかしたという雰囲気がよく分かります‥‥。そこはかとなく恥ずかしい気もしますが、習作という事で日記掲載決定です。

次の目標は値のコピーの仕方を覚えることです。関数化するなどでアルゴリズムを見直す方が先という気もしますが、既に目的がすり替わってしまいました。いくらpythonがリテラル以外の代入がコピーではなく参照になるとはいえ、こんな書き方::

  num=['a','b','c','d']
  num_copy=[i for i in num]

をしなくてもコピーできるんじゃないでしょうか？というあたりが気になってしかたありません。

*# なんて事をしてるから引越準備が遅れるワケです。*




.. :comments:
.. :comment id: 2005-11-28.4320201680
.. :title: Re: 計算パズルとpython
.. :author: micro-8
.. :date: 2004-07-15 02:49:20
.. :email: 
.. :url: 
.. :body:
.. 切符の数字で遊ぶ奴みたいですね。
.. こんな理路整然と書いていけるんですね。すごい。
.. 
.. 覚えたての私が言うのもなんですが、配列の複製はこんな感じで書いていました。
.. 
.. >>> a0=['1','2','3']
.. >>> a1=a0
.. >>> a1[0]='*'
.. >>> a1
.. ['*', '2', '3']
.. >>> a2
.. ['1', '2', '3']
.. >>> a0
.. ['*', '2', '3']
.. 
.. でもやっていることはa2=[i for i in a0]と同じような気がしないでもないです。
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4321520347
.. :title: Re: 計算パズルとpython
.. :author: 清水川
.. :date: 2004-07-16 01:39:01
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. > こんな理路整然と書いていけるんですね。すごい。
.. 
.. (^^;;
.. 
.. 
.. なるほど、要素の部分集合の代入はコピーになるんですか。言われてみれば確かにその通りですね。部分集合が参照だった場合、参照元にappendやpopしたらおかしな事になってしまう。これは気づきませんでした（気づく気づかない以前にちゃんとリファレンス読まないと‥‥）。
.. 
.. > でもやっていることはa2=[i for i in a0]と同じような気がしないでもないです。
.. 
.. 内部的には多分同じなんだと思いますが、表面的には無駄にラムダを使ってるようにしか見えません。「要素の全コピーを簡潔に書きたい。そうだ、ラムダ式だ！」と、知識が偏っている結果の産物です(;-;
.. 
.. # STLを使っていた頃が懐かしい‥‥
.. 
.. ということで、基本を押さえておかないとちょっとしたことで詰まってしまう、という実例でした。

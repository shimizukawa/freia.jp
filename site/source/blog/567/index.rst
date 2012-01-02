:date: 2008-04-22 14:51:21
:categories: ['python']
:body type: text/x-rst

=============================
2008/04/22 Python riddle 1, 2
=============================

Pythonのマニュアルは大抵のことが載っているので、良く読め、という話なんだけど、
riddle的な要素を抽出してドリル形式にしたら、どこかで需要があるかもしれない（Python合宿とか）。
あるいはどこかにPythonのriddleを集めたサイトが既にあるかもしれない。

ということで、最近遭遇した小ネタ。

.. topic:: 問い1

    リストLが ``L = ['a','b','c','d','e','f']`` のように与えられたとき、
    以下のコードを出来るだけ短く書け

    | >>> a, b, c = L[:3]
    | >>> L = L[3:]


.. topic:: 問い2

    16bitの符号付き値Nの値として ``N = -100`` が与えられたとき、
    Nを16進数表現でprintするコードを書け。（出力例： ``0xff9c`` ）

    なおC言語では以下のように記述できる。

    short s = -100;
    printf("0x%hx\n", s);


参考サイト
----------
riddleでは無いな。。

- `The Python Challenge`_
- `ActiveState O'Reilly Python cookbook code samples ratings review`_

.. _`The Python Challenge`: http://www.pythonchallenge.com/
.. _`ActiveState O'Reilly Python cookbook code samples ratings review`: http://aspn.activestate.com/ASPN/Python/Cookbook/


.. :extend type: text/html
.. :extend:


.. :comments:
.. :comment id: 2008-05-16.0967177415
.. :title: Re:Python riddle 1, 2
.. :author: jack
.. :date: 2008-05-16 06:14:58
.. :email: 
.. :url: 
.. :body:
.. unpack代入に *args はつかえないよねぇ・・・どうやるんだろ
.. 
.. :comments:
.. :comment id: 2008-05-16.8508536106
.. :title: Re:Python riddle 1, 2
.. :author: しみずかわ
.. :date: 2008-05-16 12:17:33
.. :email: 
.. :url: 
.. :body:
.. > unpack代入に *args はつかえないよねぇ・・・どうやるんだろ
.. 
.. 回答はこちらに。。
.. http://d.hatena.ne.jp/Isoparametric/20080417/1208387767
.. 
.. :comments:
.. :comment id: 2008-05-20.0005221877
.. :title: Re:Python riddle 1, 2
.. :author: jack
.. :date: 2008-05-20 13:33:20
.. :email: 
.. :url: 
.. :body:
.. それでいいんだ。でも [::-1]もそうだけど、あまりやると可読性はもうひとつになるよね
.. 
.. :Trackbacks:
.. :TrackbackID: 2008-04-23.1537476563
.. :title: [Python][Mercurial]巡回
.. :BlogName: 常山日記
.. :url: http://d.hatena.ne.jp/johzan/20080423/1208881139
.. :date: 2008-04-23 01:19:15
.. :body:
..  ファイルを連結して標準出力に出力するPythonスクリプト Pythonで特定のディレクトリ以下のファイルとディレクトリを一覧・特定ディレクトリ以下を全削除 [Python]Mercurialのhgwebdir.cgiでsyntax highlightする。 Python riddle 1, 2 続・円の交点を求める　Brainstorm バ
.. 

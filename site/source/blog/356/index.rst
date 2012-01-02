:date: 2006-07-26 01:13:34
:categories: ['python']
:body type: text/x-rst

====================================
単語の出現回数をpythonでカウントする
====================================

今日の昼頃、このblogがコメントスパム攻撃を受けた。あとで調べたところ、約2時間に渡って1360 POST受けたようだ。ウチのサイトにそんなに集中攻撃してもおいしくないのに、と思いつつ、検索エンジンの性質と絡めて考えると、狙われるサイトの規模はあまり関係ないのかもしれない。

このblogはCAPTCHAを入れておらずbuzzwordチェックでスパム対策をしている。このためか、今回のような物量攻撃には弱いのかもしれない。POSTの半分がbuzzwordチェック抜けて来ちゃったし。やっぱりCAPTCHA導入しよう。

ここで、気分転換にコメントスパム内の頻出単語上位20位をカウントしてみる。来週、電通大からインターンシップの学生(3年生)がやってくるので、「ああ、一般教養のプログラミング課題はC言語で単語数カウントとかやったなぁ」と懐かしみつつ作成。Pythonは楽でいいなぁ。

今日のコメントスパムを全てspams.txtに保存して以下のコードを走らせる。

.. code-block:: python

    f = open('spams.txt')
    data = f.read()
    
    # counting
    words = {}
    for word in data.split():
        words[word] = words.get(word, 0) + 1
    
    # sort by count
    d = [(v,k) for k,v in words.items()]
    d.sort()
    d.reverse()
    for count, word in d[:20]:
        print count, word
    

んで、この結果の上位20位がこれ::

    722 neryuids
    146 link
    145 side
    139 effects
    123 and
    110 drug
    99 medication
    97 dosage
    82 generic
    73 tablet
    70 mg
    64 pregnancy
    63 information
    61 medicine
    59 online
    55 for
    54 acne
    53 vs
    45 withdrawal
    44 alcohol

一位の ``neryuids`` って何語？と思ってgoogleで検索したらTopが `takanory.net`_ さんで2位がウチというのがなんとも味わい深い（笑）。

.. _`takanory.net`: http://takanory.net/

.. :extend type: text/html
.. :extend:


.. :comments:
.. :comment id: 2006-07-26.4320337564
.. :title: Re:単語の出現回数をpythonでカウントする
.. :author: koma2
.. :date: 2006-07-26 11:53:53
.. :email: 
.. :url: 
.. :body:
.. 自分の日記でやったら、こんなんなりますた。
.. 
..   http://bloghome.lovepeers.org/daymemo2/20060726.html#p01
.. 
.. 結果を貼っつけようとしたら「NG word 消せやゴルァ」って言われてしまったので（苦笑）、
.. リンクだけで。
.. 
.. 
.. :comments:
.. :comment id: 2006-07-27.9622983619
.. :title: Re:単語の出現回数をpythonでカウントする
.. :author: takanori
.. :date: 2006-07-27 12:29:24
.. :email: 
.. :url: http://takanory.net
.. :body:
.. 「ｎｅｒｙｕｉｄｓ」で今検索したら、ランキングに変動がありました。
.. 2位がロバートさんのところで3位が skype の岩田さんのところになっています!!
.. 

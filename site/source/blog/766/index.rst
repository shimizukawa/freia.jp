:date: 2011-11-15 13:05:16
:categories: ['misc', 'Memo', 'python', 'Programming']
:body type: text/x-rst

=======================================================
2011/11/15 ANS-prog: pythonの-m指定で便利なモジュール類
=======================================================

*Category: 'misc', 'Memo', 'python', 'Programming'*

`ANS-prog`_ という日本版 `Stack Overflow`_ とでもいうべきサイトがあって、そこで色々な技術の質問をすると誰かが答えてくれる。「これはちょっとMLとかで質問するのは気が引ける」といった簡単な質問でもANS-progなら気軽に質問出来る気がする。MLと比べて便利なのは、Q&A集になることとや、良いAnswerを選んで「確定」できること、評価(カルマ)ポイントが貯まると **質問そのものを編集可能** なので質問になっていない質問を適切なQuestionに直せるところなど。

.. _`ANS-prog`: http://answer.pythonpath.jp/
.. _`Stack Overflow`: http://stackoverflow.com/

ということで、以下の質問を出してみた -> http://answer.pythonpath.jp/questions/506/python-m%%%%%%%%%-----------------------------------------------

Pythonは標準モジュールを-mに指定して実行するといろいろな機能を提供してくれるのが便利です。

現在のディレクトリをHTTPで公開する::

    $ python -m SimpleHTTPServer
    Serving HTTP on 0.0.0.0 port 8000 ...

対象スクリプトをステップ実行する::

    $ python -m pdb foo.py
    > d:\foo.py(1)<module>()
    (Pdb)

メールサーバーを立てる::

    $ python -m smtpd -d -n localhost:25
    PureProxy started at Tue Nov 15 12:45:38 2011
            Local addr: ('localhost', 25)
            Remote addr:('localhost', 25)

メールを送る::

    $ python -m smtplib
    From:

JSONをバリデーションしてprettyprintする (by Masaki Tsuchiya)::

    $ echo '{"json":"obj"}' | python -mjson.tool
    {
        "json": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -mjson.tool
    Expecting property name: line 1 column 2 (char 2)

他に、「普段こんな使い方をしていて便利だよ！」というモジュールがあったら教えてください。%%%%%%%%%-----------------------------------------------


ということで教えてください！ => http://answer.pythonpath.jp/questions/506/python-m

あと、みんなもちょっとした質問を書くと良いよ！


.. :extend type: text/x-rst
.. :extend:

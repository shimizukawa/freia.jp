:date: 2006-05-21 22:34:41
:categories: ['python', 'Programming']
:body type: text/x-rst

=====================================
2006/05/21 PythonのDocTestでお手軽TDD
=====================================

.. epigraph::

  『Python凄いんですか？』

  『詳しくは知らないんですが、doctestというのが凄そうです』

  -- `機械猫の日記 - 第15回XPJUGユーザ会`_ のコメント欄より


.. _`機械猫の日記 - 第15回XPJUGユーザ会`: http://d.hatena.ne.jp/kikaineko/20060520#p1

PythonのDocTestで手軽にUnitTestを書く事が出来ます。こいつの **凄い** ところは、

- 実装とドキュメントとテストが一カ所に集中する（生き別れない）
- テストコードが言語レベルでマニュアルとして利用される
- インタラクティブモード（対話コンソール）の内容を貼り付ければテストになる

というところです。まああんまり書きすぎると実装がドキュメント(UnitTest)に埋もれちゃう、という話もありますが、そのへんはバランスを取って書くということで。

それでは早速DocTestを書いてみます。(`vnc2swf - 画面録画ユーティリティ`_ を使ってFlash作ってみました)


.. _`vnc2swf - 画面録画ユーティリティ`: http://www.unixuser.org/~euske/vnc2swf/index-j.html

.. :extend type: text/x-rst
.. :extend:
コードだけだと分からないと思うので、使い方等、詳しくはFlashの方を見てください。

.. code-block:: python

    def add(x, y):
        """ return added value.
        
        add digits.
        
        >>> add(1, 2)
        3
        
        add strings.
        
        >>> add('abc', '123')
        'abc123'
        """
        return x + y
    
    def evens(digits):
        """ return even value's list.
    
        >>> evens([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        >>> evens([1, 3])
        []
        >>> evens(range(0, 10))
        [0, 2, 4, 6, 8]
    
        """
        return [x for x in digits if x%2==0]
    
    # make and return TestSuite for this module.
    def test_suite():
        import unittest
        from doctest import DocTestSuite
        return unittest.TestSuite(( # make test suite
            DocTestSuite('my_utils'), # register myself as test
            ))
    
    # This if statement is executed only when run this module as main module.
    if __name__ == '__main__':
        import unittest
        unittest.main(defaultTest='test_suite') # execute test.


.. :comments:
.. :comment id: 2006-05-21.3484458793
.. :title: Re:PythonのDocTestでお手軽TDD
.. :author: kikaineko
.. :date: 2006-05-21 22:49:08
.. :email: 
.. :url: 
.. :body:
.. さっそくフラッシュ拝見させていただきました。
.. これは凄いですね！！確かに対話モードで試してみて、それを貼り付けるってのはアリですよね！！
.. おーかっこいい！！
.. 
.. :comments:
.. :comment id: 2006-05-21.0364105491
.. :title: Re:PythonのDocTestでお手軽TDD
.. :author: 清水川
.. :date: 2006-05-21 23:17:16
.. :email: 
.. :url: 
.. :body:
.. 反応はやっ！（笑
.. 
.. 日本ではPythonって何？状態なので、こういう機能が意外と知られてないんですよね‥‥。実際便利ですよー。
.. 
.. :Trackbacks:
.. :TrackbackID: 2006-05-21.8311522462
.. :title: [ruby]RubyでDocTest
.. :BlogName: 機械猫の日記
.. :url: http://d.hatena.ne.jp/kikaineko/20060521#p1
.. :date: 2006-05-21 23:13:51
.. :body:
..  一昨日のXPユーザ会でpythonにDocTestなる非常にクールな機能があることを教えてもらった。 詳しくはこちら http://www.python.jp/doc/release/lib/module-doctest.html ↓こちらは清水川さんのフラッシュ付き解説 http://www.freia.jp/taka/blog/347 これならTDD×Rubyの迷
.. 
.. :Trackbacks:
.. :TrackbackID: 2006-05-22.8938078777
.. :title: [Python]PythonのDocTestはすごいらしい :-)
.. :BlogName: きむだらど〜日記
.. :url: http://d.hatena.ne.jp/afukui/20060522/1148267741
.. :date: 2006-05-22 12:18:14
.. :body:
..  XPJUGのユーザー会で清水川さんがid:kikainekoさんにその素晴らしさをレクチャーしていたみたい。(^_^) PythonのDocTestでお手軽TDD by 清水川さん http://www.freia.jp/taka/blog/347 Flushでも作成されていて、これを見るとよく分かりますね。 おー、かっこいい！関数内に
.. 

:date: 2007-08-03 11:01:33
:categories: ['python']
:body type: text/x-rst

================================================================
2007/08/03 Re: [Python] メソッドを一時的に変更する方法とその実例
================================================================

*Category: 'python'*

- `SumiTomohikoの日記 - [Python] メソッドを一時的に変更する方法とその実例`_

おー、なるほど！ ``self.bar = self.baz`` としてもクラス属性が上書きされる訳じゃなくてインスタンスの属性に設定されるだけだから、あとで ``del self.bar`` すれば元のクラス属性のbarが使われるようになるのか！ということは、これはメソッドでなくても同じ事ができるね。

.. topic:: Python2.4
  :class: dos

  | In [1]: class Foo(object):
  |    ...:     bar = 1
  |    ...:
  | 
  | In [2]: f = Foo()
  | 
  | In [3]: f.bar
  | Out[3]: 1
  | 
  | In [4]: f.bar = 10
  | 
  | In [5]: f.bar
  | Out[5]: 10
  | 
  | In [6]: del f.bar
  | 
  | In [7]: f.bar
  | Out[7]: 1

ちなみに ``Foo.bar = 5`` とかするとクラス属性が書き換わる。

.. _`SumiTomohikoの日記 - [Python] メソッドを一時的に変更する方法とその実例`: http://d.hatena.ne.jp/SumiTomohiko/20070802/1186075455


.. :extend type: text/html
.. :extend:

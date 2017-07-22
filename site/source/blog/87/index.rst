:date: 2004-12-10 01:10:19
:tags: python, misc

================================
2004/12/10 PythonCE for PocketPC
================================

帰りの電車の中で、PocketPCにインストールしたPythonをいじっていて遭遇したネタ。

Pytnonのコンソールを終了しようとして::

  >>> exit
  'Use Ctrl-Z plus Return to exit.'

ああ、そうか。Ctrl-Zだったっけ。そう言えばexit()とかquit()っていう関数はないのかな？::

  >>> exit()
  Traceback (most recent call last):
    File "<stdin>", line 1, in ?
  TypeError: 'str' object is not callable

ん？strオブジェクトは関数呼び出し出来ません？‥‥‥‥あーーー！つまり、exitっていうのはstr型の変数なんだ！きっとシステム起動時に exit = 'Use Ctrl-Z plus Return to exit.' ってやってるんだ！

いや、そんだけです。いまさらですかね？

ちなみに sys.exit() はありました。



.. :extend type: text/plain
.. :extend:



.. :comments:
.. :comment id: 2005-11-28.4573602342
.. :title: Re: PythonCE for PocketPC
.. :author: M.Shibata
.. :date: 2004-12-10 02:05:47
.. :email: nospam.mshibata@emptypage.jp
.. :url: http://www.emptypage.jp
.. :body:
.. ほんとだ！　Windows XP ですけど、
.. >>> type(exit)
.. 
.. って出ました。そういう実装だったとはまったく思いつきませんでした。目から鱗です。
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4574786898
.. :title: Re: PythonCE for PocketPC
.. :author: 清水川
.. :date: 2004-12-10 08:21:39
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. すんません、タグとして認識されちゃったみたいですね。
.. 
..   >>> teype(exit)
..   &lt;type 'str'&gt;
.. 
.. ですね

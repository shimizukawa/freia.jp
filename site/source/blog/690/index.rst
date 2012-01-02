:date: 2009-12-04 00:51:14
:categories: ['python']
:body type: text/x-rst

==================================================================
2009/12/04 Windowsでpyreadlineを使うとCtrl+H押下時にカーソルが進む
==================================================================

*Category: 'python'*

この問題はWindows上でIPythonを便利に使おうとすると発現するんじゃないかなと思います。必ず起きるのかどうかは知りませんが、この問題で困ったことがある人は自分以外に一人しか知らないので、レアな組み合わせなんでしょうね...。でももしかしたら `Zopeのdebugコンソールをipython化する`_ を見てやってみようという人が出てくるかも。

現象としては、Backspaceキー押下時にはちゃんとカーソルの前の文字が削除されてカーソルも1文字左に移動するのに、Ctrl+H押下時には、カーソルの前の文字は消えるもののカーソル自体は右に1つ進む、という状況になります。

この問題は以下のパッチで修正出来ます。Ctrl+H押下時にはBackspaceと同等に動作するように書き換えています::

  --- pyreadline/keysyms/keysyms.py.orig
  +++ pyreadline/keysyms/keysyms.py
  @@ -119,6 +119,10 @@
           char = chr(VkKeyScan(ord(char)) & 0xff)
       elif control:
           char=chr(keycode)
  +    if control and ord(char)==8 and keycode==72:
  +        keycode=8
  +        control=False
  +        state &= 0xfffffff7
       try:
           keyname=code2sym_map[keycode]
       except KeyError:


問題と解決方法は2年以上前に把握していたんですが、某所で書いたもののバグ報告していなかったので、 `IPython: Ctrl+H erase previous character, but cursor goes forward.`_ というタイトルでバグ報告してみました（ちょっと失敗してますが..）。こんなまずい英語でもpatchが付いてれば分かってくれるかなー。分かってくれると良いなー。

.. _`Zopeのdebugコンソールをipython化する`: http://www.freia.jp/taka/blog/688

.. _`IPython: Ctrl+H erase previous character, but cursor goes forward.`: https://bugs.launchpad.net/pyreadline/+bug/491941


.. :extend type: text/x-rst
.. :extend:



.. :comments:
.. :comment id: 2009-12-18.3903854584
.. :title: Re:Windowsでpyreadlineを使うとCtrl+H押下時にカーソルが進む
.. :author: 檜山正幸
.. :date: 2009-12-18 15:39:51
.. :email: m.hiyama@gmail.com
.. :url: http://d.hatena.ne.jp/m-hiyama/
.. :body:
.. 清水川さん、はじめまして。檜山と申します。
.. CatyというWebフレームワーク（http://d.hatena.ne.jp/m-hiyama/20091215/1260847179）に pyreadline を
.. 同梱して配布しております。
.. このパッチを適用した keysyms.py も付けたいのですが、いかがでしょう？
.. README にお名前とURL（http://www.freia.jp/taka/blog/690 ）も記載したいと思いますが、差し障りがございますでしょうか？
.. 
.. 
.. :comments:
.. :comment id: 2009-12-18.6137357278
.. :title: Catyへの添付OKです！
.. :author: しみずかわ
.. :date: 2009-12-18 17:40:15
.. :email: 
.. :url: 
.. :body:
.. 檜山さんこんにちは。CatyはBPStudyで聞きたかったんですが仕事が・・・＞＜
.. 
.. 添付はもちろんOKです。
.. 是非ご利用下さい。
.. 
.. 
.. :comments:
.. :comment id: 2009-12-21.7386887801
.. :title: パッチ使わせていただきます
.. :author: 檜山正幸
.. :date: 2009-12-21 08:12:19
.. :email: m.hiyama@gmail.com
.. :url: http://d.hatena.ne.jp/m-hiyama/
.. :body:
.. 清水川さん、
.. メールにてご返答申し上げましたが、こちらにも； ありがとうございます。
.. 
.. 
.. :comments:
.. :comment id: 2010-07-18.1172560530
.. :title: pyreadline-1.6対応
.. :author: しみずかわ
.. :date: 2010-07-18 13:58:37
.. :email: 
.. :url: 
.. :body:
.. 詳しくはこちら http://www.freia.jp/taka/blog/726
.. 

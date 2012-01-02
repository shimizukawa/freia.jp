:date: 2009-12-21 23:55:00
:categories: ['python']
:body type: text/x-rst

===================================
2009/12/21 pyreadlineのパッチを修正
===================================

*Category: 'python'*

`Windowsでpyreadlineを使うとCtrl+H押下時にカーソルが進む`_ というエントリに `檜山正幸のキマイラ飼育記`_ の檜山さんからコメントをもらって、その後メールで改善案と質問をもらいました。

::

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

* 質問: 上記のコードで state &= 0xfffffff7 のコードの意味は？
* 回答: わかりません＞＜

パッチだけだと分かりませんが、関数全体でこの行以降でstate変数を参照している箇所が無いのです＞＜ パッチを作ったのが2年以上前の事とはいえ、さすがにこれは意味がなさ過ぎる。反省。

他にメールで、Ctrl+Mについても、Ctrl+Hと同様な問題があるという指摘と改善パッチをもらってやりとりした結果、以下のようなパッチに生まれ変わりました::

  --- pyreadline/keysyms/keysyms.py.orig
  +++ pyreadline/keysyms/keysyms.py
  @@ -119,6 +119,9 @@
           char = chr(VkKeyScan(ord(char)) & 0xff)
       elif control:
           char=chr(keycode)
  +    if control and (ord(char),keycode) in ((8,72),(13,77)):
  +        keycode=ord(char)
  +        control=False
       try:
           keyname=code2sym_map[keycode]
       except KeyError:
  
このパッチは `IPython: Ctrl+H erase previous character, but cursor goes forward.`_ にもUpし直しておきました。檜山さん、ありがとうございました。

(このエントリは12/25に書きました)

.. _`Windowsでpyreadlineを使うとCtrl+H押下時にカーソルが進む`: http://www.freia.jp/taka/blog/690

.. _`檜山正幸のキマイラ飼育記`: http://d.hatena.ne.jp/m-hiyama/

.. _`IPython: Ctrl+H erase previous character, but cursor goes forward.`: https://bugs.launchpad.net/pyreadline/+bug/491941


.. :extend type: text/x-rst
.. :extend:


.. :comments:
.. :comment id: 2010-07-18.1278194579
.. :title: pyreadline-1.6対応
.. :author: しみずかわ
.. :date: 2010-07-18 13:58:47
.. :email: 
.. :url: 
.. :body:
.. 詳しくはこちら http://www.freia.jp/taka/blog/726
.. 

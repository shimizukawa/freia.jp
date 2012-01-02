:date: 2008-04-28 16:18:51
:categories: ['python']
:body type: text/x-rst

==================
Python riddle 3, 4
==================

riddleというか定石っぽいのを問題形式にしただけなんですが、そもそも定石というよりは最初に知ったときに「へー」って思ったことを書いてるだけなので、マニュアルとかPythonチュートリアルとかを読めばいくらでも作れそうな気がしてきた今日この頃。

と言い訳しつつ。

.. topic:: 問い3

    リストLが ``L = ['a','b','c','d',]`` のように与えられたとき、
    以下のプログラムをenumerateを使って書き直せ

    .. code-block:: python

      >>> for i in range(len(L)):
      ...     print 'L[%d] =' % i, L[i]

enumerateを使え、って、それはもうriddleじゃないような...

.. topic:: 問い4

    リストLが ``L = ['a','b','c','d',]`` のように与えられたとき、
    並びを逆順にする以下のプログラムを出来るだけ短く書け

    .. code-block:: python

      >>> L_tmp = []
      >>> for x in L:
      ...     L_tmp.insert(0, x)
      >>> L = L_tmp

出来るだけ短く、と言われても。これは分かる人には分かる系のあまりよくない出題。ちなみに、9文字で書けます。


.. :extend type: text/html
.. :extend:


.. :comments:
.. :comment id: 2008-05-16.4930890259
.. :title: Re:Python riddle 3, 4
.. :author: jack
.. :date: 2008-05-16 05:31:51
.. :email: 
.. :url: 
.. :body:
.. 3. は単なるenumerate の紹介では(^^;;
.. 4. は9文字だと reverse()じゃないのか・・・。じゃぁ、あれか。でも、reverse()ってしておくと思います。
.. 
.. :comments:
.. :comment id: 2008-05-16.4890911183
.. :title: Re:Python riddle 3, 4
.. :author: しみずかわ
.. :date: 2008-05-16 12:11:30
.. :email: 
.. :url: 
.. :body:
.. > 3. は単なるenumerate の紹介では(^^;;
.. 
.. うんｗ
.. 

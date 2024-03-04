:date: 2006-01-21 22:16:01
:tags: misc

===============================================
Zope-2.9.0にはInterfacesタブが！の嘘
===============================================

先日の `CMS/Blog EXchange2`_ で何人かの方に、「Zope-2.9.0にはInterfacesタブがある！」とか言って実際の表示とかまで見せたんですが、嘘でした。ごめんなさい o(_ _)o

実際には、 ZopePrototype_ というプロダクトを入れているために表示されているのでした。

このZopePrototypeプロダクト、巷で有名なPrototype.jsをZope2に導入するための簡単なプロダクトで、単にprototype.jsが同梱されているだけに近いのですが、プロダクトの作りがZope3のルールで書かれていているのが大きな特徴かもしれません。同梱されているREADME.txtには「Requires Zope 2.8.4 or +」と書かれています。

なお、同梱のEXAMPLE.txtに大きな嘘が含まれていて、Zope3を知らないと気づけない可能性があります。つまり、以下のように書いてもprototype.jsをロードすることは出来ないのです::

  <script type="text/javascript" src="/++resource++js/prototype.js"></script>

正しくは、次のように書く必要があります::

  <script type="text/javascript" src="/++resource++jsprototype/prototype.js"></script>
  あるいは
  <script type="text/javascript" src="/++resource++prototype.js"></script>

ちなみに、Zope3のような以下のような書き方は出来ませんでした。惜しい。

  <script type="text/javascript" src="/@@/jsprototype/prototype.js"></script>
  <script type="text/javascript" src="/@@/prototype.js"></script>

.. _`CMS/Blog EXchange2`: http://coreblog.org/jp/events/news/blog-cms-exchange-2
.. _ZopePrototype: http://www.zope.org/Members/fabiorizzo/zopeprototype



.. :extend type: text/x-rst
.. :extend:


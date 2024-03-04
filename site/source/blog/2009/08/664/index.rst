:date: 2009-08-07 23:08:57
:tags: Zope

==================================================
Zope-2.12.0b4リリースをeasy_installする
==================================================

Zope-2.12.0b4 が昨日8/6にリリースされました。 `アナウンスはこちら`_ 。 `Zope2.12はPyPIにも登録されている`_ ので、easy_installでインストールすることが出来るようになっています。ということで、さっそくやってみます。

.. topic:: Zope2をeasy_installする
  :class: dos

  | $ wget http://peak.telecommunity.com/dist/ez_setup.py
  | $ python ez_setup.py
  | $ easy_install virtualenv
  | $ virtualenv zope2120
  | $ cd zope2120
  | $ bin/activate
  | 
  | $ easy_install Zope2 
  | $ bin/mkzopeinstance -d inst1 -u admin:admin
  | 
  | $ cd inst1
  | $ bin/runzope

やりました。とっても簡単ですね。

`Zope-2.12.0b2 がWindowsでは壊れたrunzope.batを生成する問題`_ で書いた問題も解消されていて、zopectlも使えるようになり、Python2.4/.5/.6 で動作します。すばらしい！ Awesome!

.. _`アナウンスはこちら`: http://mail.zope.org/pipermail/zope-dev/2009-August/037373.html
.. _`Zope2.12はPyPIにも登録されている`: http://pypi.python.org/pypi/Zope2
.. _`Zope-2.12.0b2 がWindowsでは壊れたrunzope.batを生成する問題`: http://www.freia.jp/taka/blog/638


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2009-10-02.8594846045
.. :title: virtualenv の activate
.. :author: しみずかわ
.. :date: 2009-10-02 10:44:24
.. :email: 
.. :url: 
.. :body:
.. $ bin/activate
.. 
.. の部分はbash系の場合
.. 
.. $ source bin/activate
.. 
.. にする必要があります。
.. Windowsでnyacus使ってる場合は直実行でもsourceでもだめです。残念。

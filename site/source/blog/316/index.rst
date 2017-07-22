:date: 2006-02-23 01:32:38
:tags: Zope

==============================================
2006/02/23 ZopeProductのテストを実行してみよう
==============================================

ZopeのProductには大抵testsディレクトリが付属していて、そのProductの機能が正しく動作するかどうかのテストを行うことが出来る。

Zope2.7, 2.8系では ``zopectl test`` と実行すれば全Productのtestsが実行されたのだけど、Zope2.9.0ではtest.pyが無いため動作しない。また、そもそもWindows環境ではzopectlが使えない。ということで、こういう環境でテストを実行するためには環境変数等、それなりの環境を用意してテストを実行してあげないといけない。とりあえず一つのプロダクトのテストを実行するには、以下のようにする(例はWindowsの場合)。

1. runzope の中の環境変数設定をコピーしてDOS窓で実行する
2. 目的のプロダクトのtestsディレクトリに移動する
3. ``%PYTHON% runalltests.py`` を実行する

これでうまくいけば以下のような結果が表示される。


.. :extend type: text/x-rst
.. :extend:


.. topic:: runalltests.py
  :class: dos

  | C:> @set PYTHON=C:\Python24\python24.exe
  | C:> @set ZOPE_HOME=C:\Zope-2.9.0
  | C:> @set INSTANCE_HOME=C:\zope290instance
  | C:> @set SOFTWARE_HOME=C:\Zope-2.9.0\lib\python
  | C:> @set CONFIG_FILE=C:\zope290instance\etc\zope.conf
  | C:> @set PYTHONPATH=%SOFTWARE_HOME%
  |
  | C:> %PYTHON% runalltests.py
  | SOFTWARE_HOME: C:\Zope-2.9.0\lib\python
  | INSTANCE_HOME: C:\zope290instance
  | Loading Zope, please stand by 
  |
  | 中略
  |
  | ----------------------------------------------------------------------
  | Ran 11 tests in 1.781s
  |
  | OK

中略の部分にたくさんのDeprecationWarningが出るけど、気にしない方向で。

ということで、 `最小Procutにもテストコード`_ を書いてみた。framework.py, runalltests.py は Zope-2.9.0/lib/python/Testing/ZopeTestCase/ からのもらいもの。実行には `PloneTestCase`_ とPlone-2.1.2が必要。


.. _`最小Procutにもテストコード`: http://svn.freia.jp/open/ATCTSmallSample/trunk/tests/
.. _`PloneTestCase`: http://plone.org/products/plonetestcase


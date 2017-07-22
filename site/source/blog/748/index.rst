:date: 2011-01-23 18:00:49
:tags: python, testing, gae

===========================================================================
2011/01/23 GAE/py + NoseGAEでUnitTestするときにimportエラーになる場合の対策
===========================================================================

Google App Engine/Python での開発中にUnitTestを行うためには、データストアが使えるように環境を整えてくれる NoseGAE_ プラグインを使ってnoseでテストする方法があります。データストアの環境を整えてくれるオプション ``--with-gae`` をつけてテストするだけなのですが、ここで以下のようなエラーが出る場合があります。

::

  File "/path/to/index.py", line 4, in <module>
    from google.appengine.ext import webapp
  ImportError: No module named ext

NoseGAEでのテスト時以外にはこの問題は発生しないのですが、自分の環境ではなぜかテスト中だけ発生してしまいました。昨日の `(第4回)Python mini Hack-a-thon`_ で `@aodag`_ と話をして色々調べてみたところ、以下のことがわかりました。

* 本番のGAE環境ではsocketなどの一部ライブラリは利用できない
* NoseGAEはそういったパッケージを使えないようにしてくれる(sandbox機能)
* そのためにsys.modulesをゴニョゴニョしている
* 何か壊してるっぽい>< やめて！
* `--without-sandbox` オプションをつけること問題を回避出来る！

--without-sandbox オプションをつけると、GAEで使えないはずのライブラリが使用できてしまいますが、まあそのへんは自分で気をつけることにします。テスト出来ることの方が重要だしね。

この現象と対策は以下の環境で確認しました。

:Python: 2.5.x
:Nose: 1.0.0
:NoseGAE: 0.1.7
:GAE: 1.4.1



べつの話題として、テスト毎にデータストアを初期状態に戻してくれたり、fixtureデータを読み込んでくれたり、といったテスト環境の整備をパッケージ提供している人がまだ居ないようなので、この分野を整備して公開、だれかしてくれないかなぁ‥‥。

.. _`@aodag`: http://twitter.com/aodag
.. _`(第4回)Python mini Hack-a-thon`: http://atnd.org/events/10194


.. _NoseGAE: http://pypi.python.org/pypi/NoseGAE

.. :extend type: text/x-rst
.. :extend:


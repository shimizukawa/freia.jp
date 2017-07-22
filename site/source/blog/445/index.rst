:date: 2007-04-15 17:50:16
:tags: python, turbogears
:body type: text/x-rst

==================================
2007/04/15 tgdatacontrollerをegg化
==================================

easy_install
-------------

`TurboGearsのお手軽Controller`_ で公開したTGDataControllerをegg化してみました。あと公開URLを変更しました。以下のURLからeasy_installで手軽にインストールできるようになっています。

- TGDataController: http://svn.freia.jp/open/tg/TGDataController/trunk
- 利用サンプルアプリ: http://svn.freia.jp/open/tg/TGDataController/trunk/tgdatacontroller/sample/todo

easy_installでインストールする場合は以下のように実行します。

.. Topic:: easy_install
  :class: dos

  | C:> easy_install http://svn.freia.jp/open/tg/TGDataController/trunk


dependency
-----------
eggの依存情報のところに, ``"SQLObject == bugfix, >=0.7.5,<=0.7.99"`` という記述を入れています。SQLObject-0.8系は動作確認してません。あと、SQLAlchemyには対応していません。


egg化
------
プロダクトをegg対応するには、基本的にdistutils用のsetup.pyを作るのとほぼ同じようにsetup.pyを書けばいいようだ。 `TurboGearsのsetup.py`_ を参考にして必要なパラメータをsetup関数に指定。あとはpython環境にsetuptoolsがインストールされていれば、以下のようにコマンドを実行してeggファイルを作ることが出来るようになる。

.. Topic:: bdist_egg
  :class: dos

  | C:> python setup.py bdist_egg

- 参考: `setuptools - The PEAK Developers' Center`_


.. _`TurboGearsのお手軽Controller`: http://www.freia.jp/taka/blog/437
.. _`TurboGearsのsetup.py`: http://svn.turbogears.org/trunk/setup.py
.. _`setuptools - The PEAK Developers' Center`: http://peak.telecommunity.com/DevCenter/setuptools


.. :extend type: text/html
.. :extend:


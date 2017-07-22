:date: 2014-7-10 22:00
:tags: Python, PEP-0426, metadata2.0, setuptools, pip, wheel

====================================================================
2014/07/10 PEP-0426 Environment Markers の調査
====================================================================

.. contents::
   :local:


動機
======

Pythonのパッケージを開発していると、色々なところに依存パッケージの情報を各必要があります。setup.pyに書いたり、requirements.txtに書いたり、tox.iniに書いたり。

例えば以下のような例:

setup.py:

.. code-block:: python

   requires = []
   extras_require = {}

   if sys.version_info < (2, 6) or (3, 0) <= sys.version_info < (3, 3):
       requires.append('Jinja2>=2.3,<2.7')
   else:
       requires.append('Jinja2>=2.3')

   if sys.version_info < (2, 6):
       extras_require['transifex'] = ['transifex_client==0.8']
   else:
       extras_require['transifex'] = ['transifex_client']

   setup(
       ...
       install_requires=requires,
       extras_require=extras_require,
   )


tox.ini:

.. code-block:: ini

   [testenv:py25]
   deps=
       transifex-client==0.8
       {[testenv]deps}

   [testenv:py26]
   deps=
       transifex-client
       {[testenv]deps}

   [testenv:py27]
   deps=
       transifex-client
       {[testenv]deps}


依存バージョンの指定などをsetup.pyとtox.iniの両方に書いてしまっています。似たような事を書きつつ、うまくまとめて書くことが出来ない訳ですが、Environment Markersを使用することで今後解決出来るかもしれません。

Environ Makerの仕様(PEP426より抜粋)
========================================

.. raw:: html

   <script src="https://gist.github.com/shimizukawa/f853a231a99f8bacea74.js"></script>



Environment Markersを使ったextras_requireの例
=================================================

最初の例を書き換えてみました。

setup.py:

.. code-block:: python

   requires = []
   extras_require = {
       ':python_version <= "2.5" or python_version in "3.0,3.1,3.2"': [
           'Jinja2>=2.3,<2.7',
       ],
       ':python_version in "2.6,2.7" or python_version >= "3.3"': [
           'Jinja2>=2.3',
       ],
       'transifex': [
           'transifex_client',
       ],
       'transifex:python_version <= "2.5"': [
           'transifex_client==0.8',
       ],
   }

   setup(
       ...
       install_requires=requires,
       extras_require=extras_require,
   )


tox.ini:

.. code-block:: ini

   [testenv:py25]
   deps=
       deps=-e.[transifex]
       {[testenv]deps}

   [testenv:py26]
   deps=
       deps=-e.[transifex]
       {[testenv]deps}

   [testenv:py27]
   deps=
       deps=-e.[transifex]
       {[testenv]deps}


とりあえず依存バージョンの指定はsetup.pyに集中させることができました。


まとめ
=======

残念ながらこの仕組みはpip-1.5.6ではまだ動作しません。このため、配布物に使うことは出来ないわけですが、今後主流になるwheelパッケージではこの書き方を使うのが一般的になると思います。

今の時点でもテストだけならpipではなくeasy_installを使えば良いので、今のうちに extras_require の書き方も併用しておいて、あちこちにバージョンや依存の面倒な記述を書かなくて済むようにしておこう・・・と思ったのですが、easy_installだとwheelのインストールに対応していないため、インストール時間がかかるし逆に不便になるような気もします。

早いところpipでEnvironment Markersを使えるようになると良いですね。


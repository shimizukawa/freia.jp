:date: 2009-07-30 23:16:59
:categories: ['python', 'Programming']
:body type: text/x-rst

=============================================================
2009/07/30 buildoutで開発 番外編: eggにrevision番号が付かない
=============================================================

eggのファイル名は例えば wsgiapp-0.1dev_r10-py24.egg となっていて、各種設定から自動的に適切な名前が付けられるようになっている。簡単にまとめると以下のような感じ:

:wsgiapp: パッケージ名。setup.pyのname引数
:0.1: バージョン番号。setup.pyのversion引数
:dev: タグ。setup.cfgのegg_infoセクションのtag_buildの値
:r10: リビジョン。setup.cfgのegg_infoセクションのtag_svn_revisionがtrueの場合に自動設定
:py24: Pythonのバージョン。インタプリタバージョンが自動取得される

これらのうち、リビジョン番号は ``setup.cfgでtag_svn_revisionがtrue`` でかつ、 ``svnクライアントのversion <= 1.5`` でないと正しく設定されない。

前者は仕様なので、setup.cfgが無かったら作成して、[egg_info]セクションにtag_svn_revision = true と書いておけば良い。ちなみにsetup.cfgはsetup.pyのデフォルト引数を定義しておけるファイル。egg_infoセクションに何が書けるかは、 ``python setup.py egg_info --help`` で表示されるOptions項を見よう。

後者はsetuptools-0.6c9がsvn-1.6系の新しいクライアントに対応出来てないため。svnコマンドが1.6系の状態で 'easy_install' や 'setup.py bdist_egg' を実行すると以下のようにエラーが表示される（がr0として処理が継続する）。

.. topic:: easy_install
  :class: dos

  | > easy_install ....
  | ...
  | unrecognized .svn/entries format; skipping .
  | unrecognized .svn/entries format in
  | ...

.. topic:: setup.py bdist_egg
  :class: dos

  | > python setup.py bdist_egg
  | ...
  | unrecognized .svn/entries format; skipping .
  | ...
  | unrecognized .svn/entries format in
  | ...


今は.svn/entriesを解析して取得していて、上記のようになってしまうのは.svn/entriesのフォーマット解析に失敗しているため。同じ理由で、.svnじゃなくて_svnに管理情報を格納するように設定している場合(TortoiseSVN等)にもr0になってしまう。今後はどのバージョンのsvnクライアントでも動作するように ``svn info --xml`` で情報を取得するようになるらしい(Issue64_, Issue79_)。

とりあえずsetuptools-0.6c9を使ってeggを作ったり、リポジトリから直接easy_installする場合はsvnクライアントを1.5系にして.svnに管理情報を保存する設定になっていればOK。


参考
------
- Issue64_ (Subversion 1.6 entries format 'unrecognized')
- Issue79_ (SVN Entries parsing should use local svn command for implementation)


.. _`eggの作り方が分からない`: http://www.freia.jp/taka/blog/655
.. _`buildoutで開発1: WSGIアプリをeggで作る`: http://www.freia.jp/taka/blog/659
.. _`buildoutで開発2: buildoutで環境を整える`: http://www.freia.jp/taka/blog/660
.. _`buildoutで開発3: easy_install できるように公開する`: http://www.freia.jp/taka/blog/661

.. _Issue64: http://bugs.python.org/setuptools/issue64
.. _Issue79: http://bugs.python.org/setuptools/issue79


.. _`zc.buildoutを使ったプロジェクト管理`: http://nagosui.org/Nagosui/Docs/tutorial/managing-projects-with-zcbuildout/tutorial-all-pages
.. _`Managing projects with Buildout`: http://plone.org/documentation/tutorial/buildout/tutorial-all-pages
.. _`Using z3c packages,...`: http://www.ibiblio.org/paulcarduner/z3ctutorial/introduction.html
.. _`Zope 3の入門にはz3cのチュートリアルがおすすめ`: http://blog.livedoor.jp/matssaku/archives/50500810.html

.. _`pypi`: http://pypi.python.org/simple/
.. _`http://svn.zope.org/repos/main/`: http://svn.zope.org/repos/main/
.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
.. _`zc.recipe.egg`: http://pypi.python.org/pypi/zc.recipe.egg
.. _`zc.recipe.testrunner`: http://pypi.python.org/pypi/zc.recipe.testrunner
.. _`z3c.recipe.egg`: http://pypi.python.org/pypi/z3c.recipe.egg
.. _`Zope 3 Package Guide`: http://wiki.zope.org/zope3/Zope3PackageGuide
.. _`mr.developer`: http://pypi.python.org/pypi/mr.developer
.. _`mod_wsgiはGoogleCode`: http://code.google.com/p/modwsgi/

.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-09)`: http://d.hatena.ne.jp/SumiTomohiko/20070609/1181406701
.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-22)`: http://d.hatena.ne.jp/SumiTomohiko/20070622/1182537643
.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-23)`: http://d.hatena.ne.jp/SumiTomohiko/20070623/1182602060
.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-24)`: http://d.hatena.ne.jp/SumiTomohiko/20070624/1182665330

.. _`Making your package available for EasyInstall`: http://peak.telecommunity.com/DevCenter/setuptools#making-your-package-available-for-easyinstall
.. _`Sumiさんの日本語訳`: http://d.hatena.ne.jp/SumiTomohiko/20070623/1182602060

.. _`how to run your own private PyPI (Cheeseshop) server << Fetchez le Python`: http://tarekziade.wordpress.com/2008/03/20/how-to-run-your-own-private-pypi-cheeseshop-server/
.. _`EggBasket`: http://www.chrisarndt.de/projects/eggbasket/


.. :extend type: text/html
.. :extend:


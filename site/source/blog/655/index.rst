:date: 2009-07-06 12:54:14
:categories: ['Zope', 'python']
:body type: text/x-rst

==================================
2009/07/06 eggの作り方が分からない
==================================

*Category: 'Zope', 'python'*

``eggの作り方`` で検索したら、イースターエッグとスクランブルエッグの作り方が分かりました。本当に(略

目的はbuildoutに対応したパッケージを作ることなんだけど、覚える順番があって、先が長い。

* distutilsを知る
* setuptoolsを知る
* buildoutを知る
* recipeを知る
* Pasteを知る

しかも、それぞれの段階の中に、「使える」「作れる」「開発を回せる」の3カテゴリがある気がする。つまり、easy_installコマンドは使えても、easy_install対応したパッケージを作ったり、そのパッケージをソースリポジトリからチェックアウトした状態を維持して開発を回したりテストしたり、ということをするにはどういう手順でやればいいのかが分からない。これら全体を網羅したドキュメントって英語でも見つからないんだよね...。

とりあえず、distutilsの段階については、py2exeとかいじってた時期に理解しているので、setuptools関連のドキュメントを読みまくることにする。


* `EasyInstall - The PEAK Developers' Center`_
* `setuptools - The PEAK Developers' Center`_
* `[Python] setuptools - SumiTomohikoの日記 (2007-06-09)`_
* `[Python] setuptools - SumiTomohikoの日記 (2007-06-22)`_
* `[Python] setuptools - SumiTomohikoの日記 (2007-06-23)`_
* `[Python] setuptools - SumiTomohikoの日記 (2007-06-24)`_

SumiTomohikoさん、和訳ありがとう！

.. _`EasyInstall - The PEAK Developers' Center`: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _`setuptools - The PEAK Developers' Center`: http://peak.telecommunity.com/DevCenter/setuptools
.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-09)`: http://d.hatena.ne.jp/SumiTomohiko/20070609/1181406701
.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-22)`: http://d.hatena.ne.jp/SumiTomohiko/20070622/1182537643
.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-23)`: http://d.hatena.ne.jp/SumiTomohiko/20070623/1182602060
.. _`[Python] setuptools - SumiTomohikoの日記 (2007-06-24)`: http://d.hatena.ne.jp/SumiTomohiko/20070624/1182665330


.. :extend type: text/html
.. :extend:

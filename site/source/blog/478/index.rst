:date: 2007-08-18 18:54:50
:categories: ['python']
:body type: text/x-rst

====================
pywin32でSysTrayIcon
====================

keyowrd: systray tasktray trayicon タスクトレイ トレイ アイコン. (自分でこのエントリを見つけやすいように追加 2008/11/18)

pythonでタスクトレイにアイコンを表示して常駐する処理を書くためにpywin32を使うと楽に出来るかな、と思いググってみたら、いきなり見つけてしまった。夏休みの自由研究、終ー了ー。

- `Small Values of Cool: Windows system tray icons with Python`_
- `SysTrayIcon.py`_ (ソースコード)

昔Cで書いたシステムトレイアイコン用Pythonモジュールを久しぶりに引っ張り出してきたものの、例外処理があまくて常用するのは危険な感じ。システムトレイ領域にファイルをドラッグアンドドロップ出来るようになってたり、意欲的というかちょっと危ないことをしているせいで、冷害が発生するとshellごと死ぬ。危ない。ビルドにVisualStudioが必要だったりするのも、ハードルが高いかも。

http://svn.freia.jp/open/trayicon/


.. _`Small Values of Cool: Windows system tray icons with Python`: http://www.brunningonline.net/simon/blog/archives/001835.html
.. _`SysTrayIcon.py`: http://www.brunningonline.net/simon/blog/archives/SysTrayIcon.py.html


.. :extend type: text/html
.. :extend:

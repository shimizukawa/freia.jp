:date: 2008-02-17 02:00:33
:tags: python

===========================================================
2008/02/17 svn for win32コマンドの文字化け対策でpysvn落ちる
===========================================================

Windows Vista に乗り換えてから、必要に応じて環境を再構築しているわけですが、今日はsvn.exe周りではまりました。今日のはVista関係ないんだけど、再構築はなかなか大変。

`svn-win32-1.4.6.zip`_ をインストールしてWindowsのコマンドラインでsvnコマンドを使えるようにしたところ、日本語メッセージが化けてしまいました。対策は `コマンドプロンプトでsvnコマンドの文字化け`_ に載っていたので、さっそくregeditを起動して::

  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor

に文字列値としてAutoRunを作って値に::

  set APR_ICONV_PATH=<Subversionをインストールしたパス>\iconv

を設定。たしかに文字化けは解消されました。が、Python2.4.4とpy24-pysvn-svn140-1.5.0-742の組み合わせで以下を実行したところ、pythonが落ちました。

.. code-block:: python

    import pysvn
    client = pysvn.Client()

とりあえずしょうがないのでレジストリを元に戻しましたが、なんで落ちるかな...。メッセージ化けてもたいして問題ないのでいいんだけど。


.. _`コマンドプロンプトでsvnコマンドの文字化け`: http://blog.noworks.net/uma/archives/000909.html

.. _`svn-win32-1.4.6.zip`: http://subversion.tigris.org/servlets/ProjectDocumentList?folderID=8100&expandFolder=8100&folderID=8100


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2008-02-17.6535378958
.. :title: Re:svn for win32コマンドの文字化け対策でpysvn落ちる
.. :author: 常山
.. :date: 2008-02-17 03:47:34
.. :email: 
.. :url: 
.. :body:
.. なるほど、Instant Djangoでもsvn-win32-1.4.6を使っていたので
.. svn updateに失敗したようですね。
.. 原因が分かりました。
.. ありがとうございます:)
.. 
.. :trackbacks:
.. :trackback id: 2008-02-17.5025776344
.. :title: [Python]巡回
.. :blog name: 常山日記
.. :url: http://d.hatena.ne.jp/johzan/20080217/1203186472
.. :date: 2008-02-17 03:28:24
.. :body:
..  svn for win32コマンドの文字化け対策でpysvn落ちる Pythonで全角から半角への変換 Cygwin SQLAlchemy Install Puzzler Pythonの多次元リストをどのように作るべきか Python でsnmp　プリンタの印刷カウント監視 nkf Python Windows で nkf pythonを使う Python MySQL 文字
.. 

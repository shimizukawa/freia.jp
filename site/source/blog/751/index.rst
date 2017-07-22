:date: 2011-04-12 11:15:00
:categories: ['python', 'sphinx']
:body type: text/x-rst

==================================================================================
2011/04/12 CentOS-5.5(i386, x86_64)でblockdiagを使って日本語入り画像を生成する手順
==================================================================================

大人気 blockdiag_ の環境構築にみんなはまっているようなので、CentOS-5.5で blockdiag_ 環境を構築する最短？っぽい手順をまとめてみました。

.. _blockdiag: http://tk0miya.bitbucket.org/blockdiag/build/html/examples.html

::

    yum install python-setuptools python-imaging fonts-japanese
    touch /usr/lib/python2.4/site-packages/PIL-1.1.5.egg-info
    easy_install blockdiag

これで動くようになります。easy_installの代わりにpipでも同様です。

みんながはまっているのは、python-imaging をyumでインストールしてもしなくても、 ``easy_install blockdiag`` したときにPIL-1.1.7がインストールされてしまい、このときにPILがインストールに失敗したり、png生成非対応状態でインストールされてしまうというあたりのようです。

そこで、前述の手順では ``touch ... PIL-1.1.5.egg-info`` してPILがインストールされてるという状態をeasy_installコマンド(python setup.py installでも同様)に教えてあげています。っていうバッドノウハウです。


念のため、以下のように出力のテストもやっておきましょう::

    wget http://pypi.python.org/packages/source/b/blockdiag/blockdiag-0.7.7.tar.gz
    tar zxf blockdiag-0.7.7.tar.gz
    cd blockdiag-0.7.7/examples
    blockdiag simple.diag
    blockdiag -f /usr/share/fonts/ja/TrueType/kochi-gothic-subst.ttf multibyte.diag

blockdiagに動作確認コマンドとか欲しいですね。

4/13追記
------------

CentOS-5.6でも同じ手順でOKだったみたいです。

  @togakushi: @shimizukawa 教えてもらった手順で CentOS5.6 環境であっさり動かせました！あざっす！

  -- http://twitter.com/togakushi/statuses/57774840882536448


.. :extend type: text/x-rst
.. :extend:


:date: 2009-01-22 01:25:18
:tags: Zope

===============================================
2009/01/22 和訳 [Zope-dev] Plans for Zope 2.12 
===============================================

このエントリはZope-dev に流れた以下のメールの和訳です。

http://mail.zope.org/pipermail/zope-dev/2009-January/034150.html

------------

Hi there,

やあみんな。

based on an earlier Zope 2.12 thread

このメールは最近のZope 2.12についてのスレッドを元にしています。

http://mail.zope.org/pipermail/zope-dev/2008-October/033572.html

I propose that we get out an alpha version of Zope 2.12 by end
of February.

Zope 2.12 のαバージョンを2月末までにリリースする提案をしたいと思う。

http://mail.zope.org/pipermail/zope-dev/2008-October/033572.html

Major changes:

主な変更点:


- dropping Python 2.4 support officially (Python 2.4 is no longer officially supported by the Python developers so we can not safely support it)

- Python 2.4 の公式サポートを終了。(Python 2.4 は既にPython開発者たちの公式サポートが行われていないので我々もちゃんとサポート出来ない)



- focus on Python 2.6 support for the final release (although there are  still some tests failing - more than with Python 2.5). Possibly  focus on Python 2.5 support for the alpha phase. Not sure if we want to support Python 2.5 and 2.6 officially at the same time.  With the current classification of Python versions within the  configure script I would suggest::

    TARGET=Python 2.6.X
    ACCEPTABLE=Python 2.5

  Python 2.4.X would be basically not acceptable but could be used  at your own risk using the --with-python option.

- 最終リリースでは Python 2.6 のサポートにフォーカスする。  (とは言えまだ多くのテストが失敗している - Python 2.5 よりも)  出来るならα版ではPython 2.5 のサポートにフォーカスしよう。  Python 2.5 と 2.6 を同時に公式サポート出来るかどうかは今のところ分からない。  今のところ configure スクリプトの Pythonバージョンについての設定は以下のようにしたいと思っている::

    TARGET=Python 2.6.X
    ACCEPTABLE=Python 2.5

  Python 2.4.X は基本的に許容外だけど、 --with-python オプションで指定は出来る。ただし、自己責任で。



- complete eggification (apparently pretty much done)

- 完全にegg化 (見たところ大体出来てる)


- reducing Zope 3 dependencies (apparently pretty much done)

- Zope 3 への依存を削減 (見たところ大体出来てる)


- removing  ZClasses completely

- ZClass関連の完全削除


- ship with ZODB 3.9 (currently in alpha stage)

- ZODB 3.9 を同梱 (現在はα版)


Rough edges/open points I encountered so far:

今のところ遭遇している問題(Rough edges/open ponts)

- RestrictedPython security audit: such an audit has been made  by Stefan and Sidnei. I am not qualified to speak about the  correctness of the audit. I assume they know what they were  doing. Unless objections one might consider this issue as  resolved - if not, please speak up.

- RestrictedPython セキュリティー監査: これは Stefan と Sidnei  によって作られています。私はこの話題について口を挟めるほどの適任ではありません。私は彼らが何をしていたかを多分知っています。  その問題に反論がないのであれば解決と見なしたい。そうでないなら、議論を再開して。


- creation of some skripts e.g. "mkzeoinstance" when easy_install-ing the Zope 2 source distro does not seem to work or it is still  missing

- "mkzeoinstance" などの幾つかのスクリプトはeasy_installでZope2をインストールしたときに正しく動作しない、あるいはインストールされないように見える。


- how do to a "traditional" SVN checkout of the Zope 2 and the related Zope 3 modules? The Zope2.buildout maintains its dependencies through  a KGS - the old-style SVN checkout uses svn:external. I think there  is a need for having both and don't know of a save way for keeping  the svn:externals and the KGS in sync (without additional manual  effort).

- どうやってZope2と、関連するZope3のモジュールを "従来の" SVN チェックアウトで出来るようにするか？ Zope2.buildout はKGS(Known Good Set)を通じて関連づけられているし、従来のSVNチェックアウトは svn:external によって、関連づけられている。両方とも維持する必要があると考えているが、 svn:externals と KGS を同期しつつ保持しておく(追加の努力無しでの)方法が分からない。

Andreas


.. :extend type: text/html
.. :extend:


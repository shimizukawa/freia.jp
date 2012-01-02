:date: 2011-12-09 23:00:00

=============================================================================
2011/12/09 Windowsのコンソールで PagerExtension が動作しない問題を追いかける
=============================================================================

`Mercurial Advent Calendar 2011`_ が実施されるということで、忙しいのにエントリーしてしまった9日目担当の清水川です。勢い大事ね。どこかから結婚式レポート書けとか聞こえてきますが、それはまた近いうちに。

.. _`Mercurial Advent Calendar 2011`: http://partake.in/events/902cd6d9-0215-4ea3-b51f-b8ff32e56426

さて、この記事書き始めた時点で担当日の23時20分を過ぎてる訳ですが、間に合うんでしょうか？

私の.hgrc
===========

とりあえず.hgrcを晒しておきます。Windowsで使っているのでそこかしこにWindows向けの記述がありますが大して設定はしていませんね::

   [ui]
   username = Takayuki SHIMIZUKAWA
   merge = winmergeu
   editor = "C:\Program Files\vim73\vim.exe"

   [tortoisehg]
   vdiff = winmergeu
   tabwidth = 4
   editor = C:\Program Files\vim73\gvim.exe
   fontcomment = メイリオ,10,-1,5,50,0,0,0,0,0
   fontlist = メイリオ,9,-1,5,50,0,0,0,0,0
   fontlog = メイリオ,10,-1,5,50,0,0,0,0,0
   fontoutputlog = メイリオ,8,-1,5,50,0,0,0,0,0

   [alias]
   pp = pull -u
   pr = pull --rebase
   ba = branches -a

   [extensions]
   rebase =
   graphlog =
   transplant =
   mq =
   record =
   histedit = C:\Users\taka\hg\hg_histedit.py


Pager拡張 on Windows
=====================

Windows向けネタということで、Windowsのコンソールでhgコマンドを使う上で便利になるようにPager拡張(PagerExtension_)をWindowsで使うためのhackを書こうと思ったのですが、結局うまく動作しませんでした。

.. _PagerExtension: http://mercurial.selenic.com/wiki/PagerExtension

Pager拡張は、画面スクロールしてしまうような長い出力(``hg log`` とか)をページング表示できるようにする機能です。Unixなどでは .hgrc (Mercurial.ini) に以下のように書いて有効にします。

::

   [pager]
   pager = LESS='FSRX' less

   [extensions]
   pager =

詳しい使い方は PagerExtension_ に書いてありますが、これはWindowsではうまく動作しません。 ``pager = LESS='FSRX' less`` の部分を ``pager = more`` と書いたりvim.exeを指定してみたりいろいろやってみたのですがうまくいきません。以下のようにエラーが表示されるばかりです::

   C:\\Project\\sphinx-doc\\sphinx-jp> hg log
   ** unknown exception encountered, please report by visiting
   **  http://mercurial.selenic.com/wiki/BugTracker
   ** Python 2.6.6 (r266:84297, Aug 24 2010, 18:13:38) [MSC v.1500 64 bit (AMD64)]
   ** Mercurial Distributed SCM (version 2.0)
   ** Extensions loaded: rebase, graphlog, transplant, mq, record, histedit, pager

(ああ、この記事の締め切りまであと30分です)

PagerExtension はどこにあるの？
================================

私の環境ではTortoiseHGをインストールしてパスを通してコンソールからhgコマンドを使用しています。TortoiseHGのインストール先にはhg.exeなどと一緒にlibrary.zipが置かれていて、Pythonのコードはすべてこの中に入っています。Mercurialの拡張系はこのzipの中のhgextディレクトリに入っているので、.hgrcの [extensions] セクションの pager = というのはつまりここにある pager.pyo を有効にしているわけですね。

::

   C:\Develop\TortoiseHg\library.zip
      + hgext
        + pager.pyo

拡張子 pyo は最適化されたバイトコードなのでこれを読んでもよくわかりません。library.zipにはpager.pyは入っていなかったので、pager.pyを読みたければ別途ソースコードを入手する必要があります。 

で、このpager.pyを入手して、夕食前に30分ほど眺めていたのですが、拡張の作法とかよくわからないので、結局よくわかりませんでした。


WindowsではPager拡張は動作しないのか？
=======================================

ちょっとGoogleで検索してみたところ、 http://mercurial.selenic.com/bts/issue1677 にIssueが上がっており、2011/6/5に「MLでレビューしてほしい」というコメントがありますが、MLの方では http://www.selenic.com/pipermail/mercurial/2011-June/038602.html のようにレビュー依頼のメールが投稿されたまま誰も見てくれていないようです。

誰かパッチ動作確認してあげればいいのにね、と思いつつ、Windowsのコンソール向けの修正パッチなんて需要が少ないのでしょう。しょうがないですね。自分も時間がとれないので・・ね。

(締め切りまであと3分!)


まとめ
========
つかれました。眠いです。

明日は、10日目担当 @gab_km さん、よろしくお願いします。

追記(12/09 24:40)
=======================
前述のpatchはMercurial-1.6の頃のものだったので2.0.1向けに書き直して以下に置きました。
まだ動作が怪しいのでもうちょっと直そうかな・・そのうち・・・

https://gist.github.com/1452023

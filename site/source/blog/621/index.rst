:date: 2009-01-25 16:36:44
:tags: Programming, Windows

===================================================================================
cmd.exe代替アプリckwの改造版をさらに改造してconfig切り替え機能を付けたい
===================================================================================

ckwはputtyライクなwindowでdos窓操作ができるアプリです。nyacusと組み合わせるとかなりunixっぽくなります。ckw について詳しくは `ckwとnyacusとztop`_ とか `cmd.exeを超便利にする ckw 0.8.10 を改造した。`_ を参照ください。

で。

ckw ではAllocConsoleを使ってコンソールWindowを作成しつつ、非表示にしている処理があって、これが元ソースやmod2ではVistaでうまく働かずDOS窓とckw窓が両方起動するという問題があった。これをﾅﾝﾄｶしようと思って色々みていたら既に解決されている方がいて、その修正を取り込んだ版がうまく動作した。

* `ckw 0.8.10 改造版を更に改造した（修正しただけ）`_

でもって、先日Plone研究会でsvnコマンドの使い方をプロジェクタしたときに、動的に画面表示のフォントサイズなどを切り替えられたら便利だろうなと思って、今朝の３時から明け方７時過ぎまでコードを改造して、とりあえずタイトルバーの右クリックに切り替えメニューを追加するところまで実装した。内部的には指定された*.cfgを読み込むところまで作ったので、あとはサイズなどをWindowに適用すれば動く・・・かな？

*# exeと同じファイル名のcfgを用意しておけばそれを読み込んでくれるので、そっちを起動すればいいんだけどね・・・。*


さて、複数人の人たちが独自に修正を入れているckw, そろそろCodeReposとかGoogleCodeとかにコードを置くべきだろうか...。


.. _`ckwとnyacusとztop`: http://www.freia.jp/taka/blog/526
.. _`cmd.exeを超便利にする ckw 0.8.10 を改造した。`: http://d.hatena.ne.jp/hideden/20071115/1195229532
.. _`ckw 0.8.10 改造版を更に改造した（修正しただけ）`: http://blogs.wankuma.com/shuujin/archive/2008/10/15/158825.aspx



.. :extend type: text/html
.. :extend:



.. :trackbacks:
.. :trackback id: 2009-07-12.4853193075
.. :title: Tools@System
.. :blog name: @note (PukiWiki/TrackBack 0.4)
.. :url: http://redpanda.sakura.ne.jp/wiki/note/index.php?Tools%40System
.. :date: 2009-07-12 13:54:46
.. :body:
.. CommandPrompt    cmd.exe代替アプリckwの改造版をさらに改造してconfig切り替え機能を付けたい - 清水川Web    Bookmarks    cmd.exe代替アプリckwの改造版をさらに改造してconfig切り替え機能を付けたい - 清水川Web Mobile Orz: フォルダの使用量を可視化するソフトを...
.. 

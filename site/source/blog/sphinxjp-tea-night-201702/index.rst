:date: 2017-02-09 23:55
:categories: ['Sphinx']
:body type: text/x-rst

=============================================
2017/02/09 Sphinx Tea Night 2017.02 #sphinxjp
=============================================

*Category: 'Sphinx'*

`Sphinx Tea Night 2017.02`_ に参加しました。


.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash">#sphinxjp</a> Tea Night にキター (@ ガスト 市ヶ谷駅前店 in 新宿, 東京都, 東京都) <a href="https://t.co/lARd5z1cjt">https://t.co/lARd5z1cjt</a> <a href="https://t.co/w1IpuHQTJ5">pic.twitter.com/w1IpuHQTJ5</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/829650402278776833">2017年2月9日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

:参加者: @usaturn, @jbking, @shimizukawa

`2014年1月から開催しているTea Night <https://sphinxjp.connpass.com/event/4639/>`_ も4年目に突入。ほぼ出席してるので、30回ちょっと参加してるかな。場所は、市ヶ谷のガスト。12月までは市ヶ谷のデニーズでやってたけれど、デニーズが閉店してしまったので数件隣のガストで開催しているけど、ものすごい混んでて15分待ちとかなのであまりよくない。良い場所があれば教えてください。できればドリンクバーがあるところで。

話したこと.

* MacではTexLive使えないの？(@usaturn) -> TexLiveにMac向けサポートを付けたのがMacTeXだった。
* http://sphinx-users.jp はどこでホスティングしてるの？(@usaturn) -> S3
* S3ってサイトのホスティングできるんだ！(@usaturn) -> はい
* Sphinx 1.3, 1.4, 1.5 リリースのトピックってなんだっけ？(@usaturn)

  Sphinx-1.3 のトピックス

  - Python 2.5, 3.1, 3.2 のサポート終了
  - Python 3.4 サポートの追加
  - docutils 0.11 未満のサポート終了
  - docutils 0.12 のサポート追加
  - sphinx.ext.oldcmarkup 拡張の削除
  - "default"テーマを"classic"テーマに名前変更
  - 拡張追加: sphinx.ext.napoleon
  - テーマ追加: alabaster (新しいデフォルト), sphinx_rtd_theme, bizstyle
  - ビルダー追加: applehelp
  - 図表番号機能追加: 図、テーブル、コードブロックに自動採番
  - any ロール追加: 任意のドメインの任意の型を自動的にみつけてクロスリンク
  - ``:caption:`` オプションを code-block, literalinclude, toctree ディレクティブに追加
  - sphinx-quickstart コマンドラインにオプションを追加し、非対話モードを追加
  - 14の言語でステミングをサポート
  - i18nの改善: moファイルの自動コンパイル、uid計算をデフォルトで無効化、翻訳可能な範囲を拡大
  - 並列ビルドの改善

  Sphinx-1.4のトピックス

  - I18N: 画像ファイルの多言語化: language と figure_language_filename 設定
  - Config: suppress_warnings でwarningを選択的に抑制
  - Directive: glossaryディレクティブに索引キーを指定可能
  - Directive: imgmath (pngやsvgで数式出力, 従来のpngmathは非推奨に).
  - Builder: XeTeX と LuaTeXをサポート
  - Builder: ``dummy`` ビルダー追加: 文法チェック用
  - Builder: EPUB 3ビルダー追加 (experimental)
  - Search: 中国語の検索インデックス
  - Search: 日本語分かち書きアルゴリズムとしてJanomeを選択可能
  - Search: 日本語のsplitterをカスタマイズ可能に
  - Domain: cpp ドメインの改善
  - Ext: GitHub Pagesへドキュメントを公開する sphinx.ext.githubpages を追加
  - Ext: セクション名にリンクできる sphinx.ext.autosectionlabel を追加
  - API: Sphinx.add_source_parser() 追加: recommonmark 等を設定して任意のテキストをSphinxソースに利用可能
  - 画像サイズを取得するために imagesize パッケージを使用し、PIL/Pillowがなくても動作します

  Sphinx-1.5のトピックス

  - Python 2.6, 3.3 のサポート終了
  - IE 6-8, Opera 12.1x, Safari 5.1+ サポートの終了(jQueryを1.11.0から3.1.0へ変更)
  - Sphinx-1.6で削除される非推奨関数等の利用時にwarningを出力
  - sphinx-quickstart: Makefile/make.bat の内容がシンプルになった(make-mode)
  - sphinx-quickstart: ``--extensions`` オプションの追加(拡張の有効化指定)
  - Builder: latexビルダー周りの大幅な改修
  - Builder: 日本語のPDFもlatexpdfで生成できるようになった
  - Builder: epubビルダーはepub3を生成（従来の実装はepub2ビルダーへ改名）
  - Builder: linkcheck用の ``tls_verify``, ``tls_cacerts`` 設定の追加
  - Domain: cpp ドメインの改善


やったこと.

* `Sphinxをはじめよう`_ の改訂作業

  改訂しようという話が進んでいるので、原稿の確認と自分の担当範囲の整理をしました。

  `2013年9月のPyCon JP`_ に合わせて初版リリース、 `2015年11月のSphinxCon JP`_ に合わせて改版をしたこの本もそろそろアップデートが必要な時期ですね、ということで。

* http://docs.sphinx-usres.jp/robots.txt を置いてドメインを検索から除外

  本家サイト http://www.sphinx-doc.org/ja/stable に日本語訳を相乗りしています。
  このため、sphinx-users.jpドメインでSphinxドキュメントの日本語訳を置く必要はなくなりました。
  ということで、検索されないようにdisallwoしました。

  @jbking が「"Sphinx 多言語" でGoogle検索すると古いドキュメント(docs.sphinx-users.jp)がヒットするのが困る」と言うので、サクッと対応しました。

* http://sphinx-usres.jp/robots.txt を置いて/doc10, /doc11を検索から除外

  既にSphinx-1.5まで進んでいるので、いまさら1.0や1.1のドキュメントはあってもしょうがないですね。ということで検索されないようにdisallwoしました。
  docs.sphinx-uesrs.jp の件で思い付いてついでに実施。



.. _Sphinx Tea Night 2017.02: https://sphinxjp.connpass.com/event/48841/
.. _Sphinxをはじめよう: http://www.oreilly.co.jp/books/9784873116488/
.. _2013年9月のPyCon JP: http://apac-2013.pycon.jp/index.html
.. _2015年11月のSphinxCon JP: https://sphinxjp.connpass.com/event/22024/

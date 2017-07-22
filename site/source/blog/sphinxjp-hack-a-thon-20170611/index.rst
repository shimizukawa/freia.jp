:date: 2017-06-11 16:30
:categories: ['Sphinx']
:body type: text/x-rst

=====================================================
2017/06/11 Sphinx+翻訳 hack-a-thon 2017.06 #sphinxjp
=====================================================

`Sphinx+翻訳 hack-a-thon 2017.06`_ に参加しました。

.. raw:: html

   <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">Sphinx+翻訳 Hack-a-thonの様子です。おやつたっぷり <a href="https://twitter.com/hashtag/sphinxjp?src=hash">#sphinxjp</a> (@ タイムインターメディア in 新宿区, 東京都) <a href="https://t.co/APG1ZcrvFC">https://t.co/APG1ZcrvFC</a> <a href="https://t.co/Qy1Z05jNj1">pic.twitter.com/Qy1Z05jNj1</a></p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/873797354024992768">2017年6月11日</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


:参加者: @tk0miya(会長), @shimizukawa(会計), @k9waffy, nskgch, @henrich, @usaturn

今回は、イベントを公開したのが前日の土曜深夜1時なのに、6人も集まってびっくり。


みんながやったこと
=====================

.. figure:: todo.*
   :width: 500

* @tk0miya: Sphinxのバグつぶしをしてました。いくつか閉じられそうなIssueを閉じたり、更新したりしました。なかなかチケットが減りません。Issue+PR 618件あって泣きたいです。
* @k9waffy: Sphinxの多言語化機能をSD誌読みながらためしてみてました。Zanataを使ってみたらけっこう使いやすいので、これはこれで試して行ってみたい。
* @shimizukawa: 某エキPy2の翻訳を進めてました。あと、GitLabのCIとホスティングを試しました。
* nskgch: Sphinxドキュメントの翻訳を引き続きやってました。未翻訳のところをやっていたので、あまり進みませんでした。
* やまね(@henrich): Debian PolicyをdocbookからSphinxへ。ひたすら以降をやってました。来週のDebianの勉強会でこの成果を発表して、他のデベロッパーも巻き込んでいきたいです。
* @usaturn: Sphinxをはじめよう、の改訂に向けて自分の担当範囲でやるべきことを列挙したり、着手したりしてました。


自分がやったこと
==================

* エキPy2の翻訳が遅れているので、翻訳を進めました。

  * Sphinx + 翻訳 Hack-a-tho なので、翻訳するのは正しい。
  * 覚えた: "rule of thumb" で "経験則"
  * 覚えた: "be only a .." で "..に過ぎない"

* GitLabのCIとホスティングを試してみた

  * GitLabのCIとホスティングを使ってみました。
  * SphinxのHTMLをビルドして公開するのはとても簡単
  * 手順をまとめました http://sphinx-users.jp/cookbook/hosting/index.html#gitlab-pages

  .. raw:: html

     <blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/sphinxjp?src=hash">#sphinxjp</a> SphinxのビルドとホスティングをGitLabでやる手順についてまとめました <a href="https://t.co/c7VpHa91YZ">https://t.co/c7VpHa91YZ</a><br>プライベートリポジトリからのHTML限定公開…はできなかった(´･ω･`)</p>&mdash; Takayuki Shimizukawa (@shimizukawa) <a href="https://twitter.com/shimizukawa/status/873804150944944129">2017年6月11日</a></blockquote>
     <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


.. _Sphinx+翻訳 hack-a-thon 2017.06: https://sphinxjp.connpass.com/event/59558/


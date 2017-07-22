:date: 2007-04-13 22:06:24
:tags: javascript
:body type: text/x-rst

=================================================
2007/04/13 FirefoxのCopyURL+をIEとOperaにも欲しい
=================================================

FirefoxのCopyURL+を使うと、ページのURLとタイトルをクリップボードにコピーしてくれる。たとえばこのサイトのトップページで行うと以下のような文字列がクリップボードに保存される::

  最近の清水川Web — 清水川Web 
  http://www.freia.jp/taka

これがあると他の人にURLを伝えるときにタイトル付きなのでわかりやすい。あとメモをに書き写すときとかblogに引用元のURLを書くときとか。

これをIEやOperaでも出来るといいなあ、と思ってGoogleで探して、欲しい物に一番近いコードをbookmarkletとして改造してみた。引用元は `最速インターフェース研究会 :: Firefoxでテキストをクリップボードにコピーする方法`_ 。

Opera用::

  javascript:(function(text){var swf_data = "http://ma.la/setClipboard.swf";var tmp = document.createElement("div");tmp.innerHTML = '<embed src="'+swf_data+'" FlashVars="code='+encodeURI(text)+'" width="0" height="0"></embed>';with(tmp.style){position ="absolute";left = "-10px";top  = "-10px";visibility = "hidden";};document.body.appendChild(tmp);setTimeout(function(){document.body.removeChild(tmp)},1000);})(document.title+"\n"+location.href)


最近はJavaScriptにも以前より慣れたとはいえ、Opera用は自力では作れなかったなぁ。OperaではJavaScriptでクリップボードを操作する方法が無い(と思う)ので、Flashを経由してクリップボードに保存しているようだ。上記のコードをそのまま使うと、Flashファイルをma.laドメインに取りに行くので、アクセスログに色々残る可能性あり。自分のサーバー等にコピーして利用するか、引用元サイトで第3の方法として提示されている外部Flashファイルを使わない方法にチャレンジする必要がある。

ところで、IEのJavaScriptはクリップボード操作ができるので、以下のコードで動作する。

IE用::

  javascript:(function(text){clipboardData.setData("Text",text);})(document.title+'\n'+location.href);


そうだ、reStructuredText用に、出力文字列を以下のようにしてみようかな::

  `最近の清水川Web — 清水川Web`_
  .. _`最近の清水川Web — 清水川Web`: http://www.freia.jp/taka



.. _`最速インターフェース研究会 :: Firefoxでテキストをクリップボードにコピーする方法`: http://la.ma.la/blog/diary_200601100445.htm


.. :extend type: text/html
.. :extend:


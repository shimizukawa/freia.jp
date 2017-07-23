:date: 2007-01-27 03:13:25
:tags: Zope

==============================
Zope-2.10.2リリース
==============================

Zope-2.10.2がリリースされましたので `CHANGES.TXT`_ を翻訳して `zope.jpサイト`_ においておきました。しかし、Trackerとか実装コードの変更とかを見てやっと書いてあることが翻訳できました。そんな感じなので、翻訳した文面を見ても「で、何が直ったの？」という感じです。きっと分かる人には分かるんでしょう。

ちょっとだけ補足すると、、、

Zope-2.10.0からZopePateTemplateの実装がZope3ベースになった影響で、日本語文字列を含むPateTemplateのZMIでの保存時にエラーが発生して保存できない問題が起きていました。これが修正されました。Zope3のAdapterの仕組みを使って修正されており、UnicodeEncodingConflictResolverというやつを切り替えて、エンコード変換エラー時の挙動をカスタマイズ出来るようになったようです。

あと、既存エンコードをon-the-flyで変換するとも書いてあります。変換元エンコードは環境変数ZPT_REFERRED_ENCODINGに設定しておく必要がありそう。この環境変数にshift-jisと設定しておけば、古いZPTインスタンスが内部にshift-jis等で文字列を保持していても、動的に（表示時ではないみたい）Unicodeに変換してくれる仕組みのようです。

おまけ。同梱されるZope3が3.3.1になりましたが、Zope-3.3.1はまだリリースされていないような気がします。

----

そうそう、内部がUnicodeになった、という文面を見てふと思いついて実験してみました。

::

  management_page_charset:  utf-8
  default-zpublisher-encoding:  shift-jis

こんな設定にすると、ZMIはutf-8で公開ページはshift-jisに！でも ``～`` が正しくマッピングされなくて化けました(笑)。こんな変な設定はするなと言うことで。


.. _`CHANGES.TXT`: http://www.zope.org/Products/Zope/2.10.2/CHANGES.txt
.. _`zope.jpサイト`: http://zope.jp/download/zope/releases/2.10.2/


.. :extend type: text/html
.. :extend:


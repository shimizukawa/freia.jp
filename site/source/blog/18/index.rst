:date: 2004-06-11 00:51:21
:tags: Zope, python

================================
2004/06/11 Plone2.03も日本語がっ
================================

会社の上司にZopeを紹介してみました。紹介と言っても業務ではなくプライベート
の範疇で、ですが。で、Zopeを簡単に強力に使う手段として "Plone":plone.jp 
（ZopeのProduct）を勧めてみました。Ploneで構築されているサイトの例としては
 `沖縄ITポータル <http://okiit.okihawk.org/>`__ が有名らしいのでついでに実例と
言うことで紹介しました。

ところで、個人的にはPloneもCMFも使ったこともないしよく分からないというのが
実情だったので、紹介しておいて知らないというのもなぁ‥‥ということで
Windows版の2.03をインストールして軽くさわってみました。



.. :extend type: text/structured
.. :extend:

Windows版、楽でイイですね。やっぱり最初の1ステップは楽な方が人に勧めるのに
抵抗がなくて良いと思います。

それはさておき、とりあえずデフォルトのトップページを日本語にしてみよう、と
思って::

  "沖縄ITポータル":http://okiit.okihawk.org/

と書いてみたのですが、リンクになってくれません。しかし、
:doc:`先日の件 <../4/index>` もあり、すぐに ZopeのStructuredTextが腐っ
てるんだ！と思いつき、さくっと対応できました。

パッチは
`ここ <http://sukima.ddo.jp/Plone/Members/yusei/Download/Zope-2.6-StructuredText.patch/file_view>`__
のを当てて、修正したpyファイルを手動で再コンパイル。再コンパイルの方法は、
pythonのMLで教えてもらった方法で手軽に(?)行いました::

  > cd (ploneインストールフォルダ)\Zope\lib\python\StructuredText
  > (ploneインストールフォルダ)\python\python.exe
  --python起動--
  >>> import DocumentClass
  >>> import STletters
  >>> (Ctrl-Zで終了)

ところで、このコンパイル方法って本当に手軽なのでしょうか？pycが無い場合は自
動的にコンパイルして生成してくれる方法がありそうな気がします。



:date: 2005-01-17 22:38:57
:categories: ['WZ', 'python']
:body type: text/x-rst

================================
2005/01/17 WZの色分け for python
================================

*Category: 'WZ', 'python'*

負けました。＜挨拶

`Whining Express`_ より::

  WZ PYTHON SCRIPT EDITOR
  ご参考までに。Pythonスクリプトを、僕はこんな感じの文書の設定で表示させています。

きめ細かい設定してるなぁ‥‥。自分の場合はというと

色分け::

  rear(use=1;rgb="0x0080FF";atr=0): #
  area(use=1;rgb="0xFFFF00";atr=0;flag=2): " " \"
  area(rgb="0xFFFF00"): ' ' \'
  words(use=1;rgb="0x00FF00";atr=0): if else elif endif
  reword(rgb="0x00FFFF";atr=0;re=1): 0x[0-9a-fA-F]+
  reword(use=1;rgb="0x00FFFF";atr=0;re=2): <(\d+)>
  words(use=1;rgb="0x00FF00";atr=0): and class def except exec float for from import in int is lambda list not or pass print raise return self str try tuple False None True
  chars(rgb="0xFF0000";atr=2): \(kata)

見出し３::

  ^\s*def\s+(\w[\w\d_]*).*

このくらいしか設定してませんわ。早速利用させてもらいましょうかね。


.. _`Whining Express`: http://www.emptypage.jp/whining/2005-01-16.html




.. :extend type: text/plain
.. :extend:


:date: 2004-04-23 23:54:44
:tags: Zope, Memo

=======================================
2004/04/23 COREblogにおける日本語の問題
=======================================

`COREblog <http://coreblog.org/>`__ は標準では検索機能が使えません。 `HowTo <http://coreblog.org/howtos/>`__ に使えるようにするための手順は載っていますが、それだけでは日本語の検索がうまくいきません。原因はパーサーが日本語をパース出来ないところにあります。（自分の環境固有の話かもしれませんが‥‥）


.. :extend type: text/plain
.. :extend:

そこで、 `mojix <http://mojix.org/>`_ 氏作の `MJSplitter <http://zope.org/Members/mojix/MJSplitter/>`_ を導入します。このプロタクトは、形態素解析器 `MeCab <http://chasen.aist-nara.ac.jp/~taku/software/mecab/>`_ を用いて日本語を解析し、カタログ化するZCTextIndexのパーサーとして機能します。

MJSplitter_ を手順に従ってインストールすると、ZCTextIndexのWord SplitterとしてMJSplistterを選択できるようになります。COREblogフォルダのcontentsタブでlexiconオブジェクトを削除して、lexiconという名前でZCTextIndexを追加後、EntryタブでRecatalogすると日本語を含むカタログが生成されます。

自分の環境は以下ような感じです。

- UTF-8
- `Zope2.7.0 <http://zope.org/Products/Zope/2.7.0>`__
- `COREblog0.61b <http://coreblog.org/>`__
- `MeCab0.76 <http://chasen.aist-nara.ac.jp/~taku/software/mecab/src/>`__
- `ipadic2.5.1 <http://chasen.aist-nara.ac.jp/stable/ipadic/>`__
- `MeCab-python-bindings0.76 <http://chasen.aist-nara.ac.jp/~taku/software/mecab/bindings/>`__
- `JapaneseCodec1.4.10 <http://www.python.jp/pub/JapaneseCodecs/JapaneseCodecs-1.4.10.tar.gz>`__


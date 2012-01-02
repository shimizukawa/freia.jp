:date: 2004-09-10 00:52:19
:categories: ['Programming']
:body type: text/x-rst

===================================
2004/09/10 ドキュメント自動生成計画
===================================

仕事のプロジェクトで、慢性的に人手が足りていません。そこで、ドキュメントは出来るだけ自動生成にしようと画策しています。

今のところ、 doxygen_ と CUnit_ を使用して以下のドキュメントが自動生成されています。

- APIリファレンス
- 単体テスト項目書
- 単体テスト成績書

会社のモノを勝手に公開するわけにはいかないので、残念ながら成果物を掲載することは出来ないのですが、生成手順についてメモしておきます。

.. _doxygen: http://www.doxygen.org/
.. _CUnit: http://cunit.sourceforge.net/



.. :extend type: text/x-rst
.. :extend:
APIリファレンス
---------------
::

  doxygen_ → html → HTML Help

htmlからWindowsのHTMLHelp形式にするためには、MicrosoftのサイトからHTML Help Workshopをダウンロードしてインストールしておく必要があります。あとはdoxyfileにGENERATE_HTMLHELP = YES と記述して、関連する項目(コンパイラのパス等)を設定するだけで、doxygenが自動的に生成してくれます。

ただし、あまり見やすいヘルプは作ってくれません。自分は、@mainpage と @defgroup を使って、提供機能からAPIを引けるように工夫してみました。


単体テスト項目書
----------------
::

  doxygen_ → XML → 自作XSLTと結合して HTML

GENERATE_XML = YES とすることで、 doxygen_ はXMLを出力してくれます。そこで、XMLに自作のXSLTを結合させて、自動生成のHTML(HTMLHelp)よりも見やすく作ってみました。XMLとXSLTの結合には `Apache XML project`_ の xt を使用しました。

`xt導入`_ には若干手間取りましたが、googleで見つけたサイトで手順が書かれていたので、すんなりと導入することが出来ました。‥‥が、IE6.0の出力結果と微妙に違うようです。

実はHTMLに変換した理由は別にあって、WordでHTMLを読み込ませて、Wordファイルとして提出するためだったりします。別にWordじゃなくても‥‥とか思うんですけどねぇ。


単体テスト成績書
----------------
::

  CUnit_ → XML → 自作XSLTと結合して HTML

CUnit_ もXMLを出力することが出来るので、これもXSLTを用意しました。項目書と成績書の両方ともXMLなのだから、もう一工夫すれば項目書にテスト結果も載せることが出来ると思います。今回は時間が無いので、これは次回の課題としておきます(^^;

今後の自動生成
----------------
次は、後日メンテ用の内部設計書ですかね。あと、コマンド一発で

1. VSSからソース取得
2. VC++でコンパイル
3. テスト実行
4. ドキュメント生成(doxygen,xt)
5. ドキュメントアップロード

とかやってみたいですね。

.. _doxygen: http://www.doxygen.org/
.. _CUnit: http://cunit.sourceforge.net/
.. _`Apache XML project`: http://xml.apache.org/
.. _`xt導入`: http://www.dabesa.org/xml-tips/xslt.html




.. :comments:
.. :comment id: 2005-11-28.4481052000
.. :title: Re: ドキュメント自動生成計画
.. :author: うっちー
.. :date: 2005-06-08 15:34:14
.. :email: hse_uchiyama@access.co.jp
.. :url: 
.. :body:
.. 突然質問して申し訳ありません。
.. うっちーと申します。
.. 
.. CUnitを使用しようとして、セットアップしていますが、
.. うまくいきません。
.. 
.. Visual Studio 6.0で、CUnit.dswを開いて、
.. ビルドしようとしていますが、
.. CUnitはライブラリまで作成できますが、
.. BasicTestでリンク中外部シンボルは未解決とのエラーになってしまいます。
.. 
.. セットアップの方法が分かるでしたら、
.. 教えていただけないでしょうか？
.. 宜しくお願いいたします。
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4482233834
.. :title: Re: ドキュメント自動生成計画
.. :author: 清水川
.. :date: 2005-06-09 00:15:30
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. > CUnitはライブラリまで作成できますが、
.. > BasicTestでリンク中外部シンボルは未解決とのエラーになってしまいます。
.. 
.. こんにちは^^
.. 
.. 多分、ライブラリと利用側とのコンパイルオプションが異なっているために外部リンケージが見つからないのだと思います。
.. CUnit のコード生成のオプションはシングルスレッド(/ML)なので、利用側のオプションが一致しているか確認してみてください。異なっていた場合、利用側を合わせるのか、ライブラリ側を変えるのかは必要に応じて決めればいいと思います。
.. 
.. 
.. 
.. :Trackbacks:
.. :TrackbackID: 2005-11-28.4483404550
.. :title: [プログラミング]
.. :BlogName: きまぐれのらねこにっき
.. :url: http://d.hatena.ne.jp/sakuneko/20051109#p3
.. :date: 2005-11-28 00:47:28
.. :body:

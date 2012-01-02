:date: 2004-08-12 00:30:13
:categories: ['WZ']
:body type: text/x-rst

====================
python編集用WZマクロ
====================

WZ使いの `M.Shibataさん`_ のサイトで `python編集用WZマクロの試作品`_ が掲載されていました。

自分の環境(WZ5.01C)ではif文の":"補完やdef文の"()"補完などは動作しましたが、残念ながらEnter入力時などのインデント関係はうまく動作しませんでした。設定の関係でしょうか？

ソースをざっと眺めて、拡張子が"py"であるか文書の設定が"python"であれば動作するらしいことは分かりました。全部の処理は追いませんでしたが、とりあえず一カ所だけ。
":"にカーソルを合わせた状態でEnterを入力したときに *pyeditInsertReturn()* 関数で *fIncreaseIndent* がfalseになっているため、次の処理が行われないようです。

普段 Zope_ 上から ExternalEdit_ でpythonを編集することが多いので、実用できるようになればかなり楽が出来そうです。とりあえず草葉の陰から勝手に期待しておくことにします（笑）。

*# それにしてもWZマクロ関連は半年以上触ってないなぁ‥‥*

.. _`M.Shibataさん`: http://www.emptypage.jp/
.. _`python編集用WZマクロの試作品`: http://www.emptypage.jp/whining/2004-08-11.html
.. _Zope: http://zope.jp/
.. _ExternalEdit: http://www.zope.org/Members/Caseman/ExternalEditor/




.. :extend type: text/plain
.. :extend:

:date: 2009-08-07 23:08:52
:categories: ['Event', 'Zope', 'Plone', 'web']
:body type: text/x-rst

==============================================================
2009/08/07 Zope Essentials 7 で Deliverance の紹介を聞いてきた
==============================================================

昨日8/6に、 `Zope Essentials 7を開催します`_ 、に、行ってきました。ニュージーランドでPloneで仕事をしているTim Knappさんがメイントーカーで、 Deliverance_ について話してくれました。余談ですが、Timさんは `Buildout and Plone`_ というプレゼンも書いていたりします(buildout.orgに載ってます)。

Deliveranceとは:

  Deliverance は、デザイン用にHTMLを準備し、バックエンドにおいたPloneなどの動的サーバから、XML定義を元にページを生成する仕組みです。 Ploneへの標準導入が進められており、既にplone.orgサイトでは使われています。 とかく、PloneのSkin(テーマ)開発には学習コストがかかると言われています。それの軽減のためにも、Deliveranceが注目を集めています。

自分の理解は、XPathで位置指定するHTML変換Proxy。で、２つのHTML（変換もとページと、テーマ用HTML）を用意して変換ルールを書けば、変換された結果がブラウザに届きます。この技術はWebデザイナーさんが（Ploneのような）WebサーバーへのHTML組み込み方法を知らなくてもデザイン適用出来るところがミソかなとおもいます。 OSWD_ で配布されているデザインテンプレートも簡単にPloneに適用出来たらしい。

以下、当日のTwitterメモ(`#ze7`_ 一部加筆修正)。

- DeliveranceはXPathでルール書いておいてコンテンツ変換するProxy/WSGI 
- 指定XPathの前追加(prepend), 後追加(append), 削除(drop), 差し替え(replace)が出来る 
- XPath指定したエレメントの属性にだけ作用させることも可能 
- Deliveranceを紹介してるTimはまだDeliveranceを仕事で使ってない。たまたま機会がなかった 
- Deliveranceプレゼン資料 http://tinyurl.com/deliverance-preso-jp 
- Plone&Deliverance using Repoze http://www.sixfeetup.com/blog/2009/4/27/deploying-plone-and-zine-together-with-deliverance-using-repoze 
- Buildout for Plone 3 with deliverance on WSGI http://lichota.pl/blog/buildout-for-plone-3-with-deliverance-on-wsgi 
- A jquery-like library for python http://pypi.python.org/pypi/pyquery 
- zenich: deliveranceうまく使えば html/css とアプリケーション開発とコンテンツ作成をうまく切り分けて開発効率を上げられるのでは。
- 回答: Open Source Web Design (OSWD) のデザインをDeliveranceの勉強しながら数時間でPloneサイトに適用出来た 
- takanory: Deliverance 使うんだったら proxy でやったほうがいいらしい 
- @takanory PloneをWSGIで動くようにセットアップしたり,buildoutに設定するより分かりやすいかと思って言ってみました >最初はproxyがよい 
- Delivarance を単体のProxyとしてセットアップする方法 http://deliverance.openplans.org/quickstart.html


実際の使い方とかは、そのうちbuildoutで開発するネタの一部で書こうと思います。


.. _`Buildout and Plone`: http://www.buildout.org/screencasts.html
.. _`Zope Essentials 7を開催します`: http://zope.jp/events/zopeessentials/7/zope-essentials-7
.. _Deliverance: http://deliverance.openplans.org/index.html
.. _OSWD: http://www.oswd.org/
.. _`#ze7`: http://twitter.com/#search?q=%23ze7


.. :extend type: text/html
.. :extend:


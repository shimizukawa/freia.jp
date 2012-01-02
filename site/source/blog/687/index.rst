:date: 2009-12-01 23:55:00
:categories: ['Plone']
:body type: text/x-rst

========================================================
COREBlog2をPlone3で動かすための修正: portletのカレンダー
========================================================

`Plone-3.3.2 にアップグレードして公開`_ したときの課題として、 "COREBlog2のカレンダー表示が月変更出来ない" というものがありました。これを修正する方法が分かりました。

:対象: `COREBlog2_nightly.tgz`_ (2008/10時点)
:Plone: Plone-3.3.2

.. _`Plone-3.3.2 にアップグレードして公開`: http://www.freia.jp/taka/blog/686
.. _`COREBlog2_nightly.tgz`: http://coreblog.org/junk_l/COREBlog2_nightly.tgz


まず原因ですが、COREBlog2のポートレット表示用カレンダーは ``skins/COREBlog2/portlet_coreblogcalendar.pt`` というテンプレートで表示されます。ここで表示対象月を決めている変数が year, month なのですが、この変数の初期化時に ``options/year`` に年が設定されていないため、現在の日付を元にカレンダー表示されてしまっているようです。ここで使われている options 変数は  ``skins/COREBlog2/archives.py`` の最終行で cbarchive_view.pt に渡されていますが、これがどうやらportletには渡ってこないようです。（どこかにこの仕様変更について情報がないか探してみたのですが、見あたりませんでした）

この問題の修正の方針は3つあります。

1. Plone3向けのportletを書く
2. portlet_coreblogcalendar.pt 内でoptionsに頼らずにyear,monthを取得する
3. archives.py でrequest変数にyear,monthを設定しておいてportlet_coreblogcalendar.ptで使う

今回は2の方法で対応してみます。



.. :extend type: text/x-rst
.. :extend:
2. portlet_coreblogcalendar.pt 内でoptionsに頼らずにyear,monthを取得する
----------------------------------------------------------------------------

まず、 portlet_coreblogcalendar.pt をカスタマイズフォルダ(portal_skins/custom)に複製します。そして以下のように修正します::

     tal:define="DateTime python:modules['DateTime'].DateTime;
                 current python:DateTime();
    -            yearmonth here/getYearAndMonthToDisplay;
    -            year options/year | python:yearmonth[0];
    -            month options/month | python:yearmonth[1];
    +            yearmonth python:here.cbcalendar_date() or here.getYearAndMonthToDisplay();
    +            year python:yearmonth[0];
    +            month python:yearmonth[1];
                 prevMonthTime python:here.getPreviousMonth(month, year);
                 nextMonthTime python:here.getNextMonth(month, year);

次に、上記の書き換えで呼び出されることになった cbcalendar_date はまだどこにも存在していないので、このスクリプトを用意します。portal_skins/customフォルダで "Script(Python)" を新規追加して、名前を 'cbcalendar_date' として以下の内容を記載します。

.. code-block:: python

  request = container.REQUEST
  sub_traverse = request.ACTUAL_URL[len(request.URL):].strip('/').split('/')
  isArchive = request.URL.split('/')[-1] == 'archives' and sub_traverse

  if isArchive:
      yearmonth = [
          int(sub_traverse[0]),
          int(sub_traverse[1]),
      ]
      return yearmonth

  else:
      return None

これでカレンダーを次月、前月に遷移できるようになると思います。



.. :comments:
.. :comment id: 2009-12-03.3357855840
.. :title: Re:COREBlog2をPlone3で動かすための修正: portletのカレンダー
.. :author: akiko
.. :date: 2009-12-03 09:48:57
.. :email: 
.. :url: 
.. :body:
.. コメントを書いた後に発見しました。
.. （すごい！）
.. ありがとうございます、早速自分のサイトでも試してみます！
.. 
.. 
.. :comments:
.. :comment id: 2010-06-30.1763376748
.. :title: Re:COREBlog2をPlone3で動かすための修正: portletのカレンダー
.. :author: akiko
.. :date: 2010-06-30 14:19:37
.. :email: 
.. :url: 
.. :body:
.. Plone3.3.5にしたら、WARNINGが出て、カレンダーポートレットの描画もうまくできませんでした。
.. 
.. yearmonth python:here.cbcalendar_date() or here.getYearAndMonthToDisplay();
.. を、
.. yearmonth python:here.cbcalendar_date() or context.restrictedTraverse('@@calendar_view').getYearAndMonthToDisplay();
.. に変えてみたら、動くようになりました。
.. 
.. また、前後の月は、下記のようにしてみました。
.. prevMonthTime python:context.restrictedTraverse('@@calendar_view').getPreviousMonth(month, year);
.. nextMonthTime python:context.restrictedTraverse('@@calendar_view').getNextMonth(month, year);
.. 
.. 正しいのかどうかは判らないのですが...。

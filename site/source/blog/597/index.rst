:date: 2008-07-07 00:52:05
:categories: ['misc', 'Programming']
:body type: text/x-rst

========================================
Ruby on Rails 逆引きクイックリファレンス
========================================

ずっとerattaだと思ってました。errataでした。エラッタじゃなくてイラータの方が発音近いですかね。

- `Ruby on Rails 逆引きクイックリファレンス Rails 2.0対応`_

6章の「ビルド・テスト・運用」から読み始めてとてもわくわくした本です。 `先日お会いした大場さん`_ も著者のお一人。

18ページめの「Ruby on Railsでの開発に必要となる背景技術」に40項目近い項目があるあたりに
「この本ではこのへんは説明しないぞ！」という主張がある感じ？Webアプリを正しく書くのってかなりの範囲の知識がいるんですね :-)

達人プログラマーを書いたDave ThomasとDHHの `RailsによるアジャイルWebアプリケーション開発 第2版`_ もそのうち読んでみたい。

.. _`Ruby on Rails 逆引きクイックリファレンス Rails 2.0対応`: http://www.amazon.co.jp/dp/4839928266/freiaweb-22
.. _`RailsによるアジャイルWebアプリケーション開発 第2版`: http://www.amazon.co.jp/dp/4274066967/freiaweb-22
.. _`先日お会いした大場さん`: http://www.freia.jp/taka/blog/569

::

    P148, Q052:
        4つめのサンプルコード,2行目:
            誤: article
            正: project

    P262, Q101:
        2つめのサンプルコード,5行目:
            誤: min
            正: average

    P263, Q101:
        1つめのサンプルコード,5行目:
            誤: min
            正: sum

    P300, Q118:
        1つめと2つめのサンプルコードが逆

    P322, Q127:
        P321までの関連名はemployeesだったが、P322の2つ目3つ目では
        work_place_costsという名前になっている。
        1つめのWorkPlaceモジュールではemployeesという名前で参照
        しようとしている。

    P325, Q128:
        5つめのサンプルコード,3行目,インデントがずれている

    P328, Q129:
        下から2行目:
            誤: has_and.belongs_to.many
            正: has_and_belongs_to_many

    P348, Q138:
        3つめのサンプルコード,行末のダブルクォートが抜けている

    P354, Q141:
        本文5行目:
            誤: --skip- migration
            正: --skip-migration

    P382, Q151:
        4つめのサンプルコード:
            誤: alert(page.....
            正: page.alert(page....

    P383, Q151:
        3つめのサンプルコードの前の行:
            誤: Form.Element.serializeは(element)次の...
            正: Form.Element.serialize(element)は次の...

    P402, Q161:
        最初の表題（画像の次）:
            誤: _place_editing
            正: in_place_editing

    P526, INDEX:
        executeは241ページを指しているが、241にexecute文が無い。
        正しくは348ページ?


.. :extend type: text/html
.. :extend:


.. :comments:
.. :comment id: 2008-07-09.3929346804
.. :title: Re:Ruby on Rails 逆引きクイックリファレンス
.. :author: koichiro
.. :date: 2008-07-09 11:43:14
.. :email: 
.. :url: http://ko.meadowy.net/~koichiro/diary/
.. :body:
.. 正誤をまとめていただき感謝です。お陰でとても楽をさせてもらいました^^;
.. こちらの正誤表に反映して公開しました。ありがとうございます！
.. http://everyleaf.com/railsbook
.. 
.. 
.. :comments:
.. :comment id: 2008-07-21.5207947955
.. :title: Re:Ruby on Rails 逆引きクイックリファレンス
.. :author: しみずかわ
.. :date: 2008-07-21 04:35:21
.. :email: 
.. :url: 
.. :body:
.. P304, Q119:
..     関連の図の中でDeliveryクラスにoffice_idがあるが、正しくはorder_id.

:date: 2007-12-31 14:57:16
:categories: ['Memo', 'database']
:body type: text/x-rst

=========================================
2007/12/31 Oracle10gをWindowsに入れてみる
=========================================

*Category: 'Memo', 'database'*

Oracle10gは開発や評価用に無料で使用することが出来るので、WindowsXPなノートPCに入れてみた。

インストーラを入手する
----------------------

インストーラはOTN(Oracle Technology Network)から入手できるけど、なぜか `日本語のOTNサイト`_ では入手できないらしいので `英語のOTNサイト`_ から入手することにします。英語サイトからダウンロードするためには無料のアカウント登録が必要です。ところで、OperaだとなぜかBASIC認証が表示されてしまい、取得したID/PWを入れてもだめだったので、IE7でダウンロードしました。

Googleで検索すると、英語サイトでなら無料で入手できる、という話はほとんど見つからない。けっこう有名な話だと思ってたんだけどなあ。

.. _`日本語のOTNサイト`: http://otn.oracle.co.jp/software/products/database/#db10g
.. _`英語のOTNサイト`: http://www.oracle.com/technology/software/products/database/index.html


インストールする
----------------

ダウンロードした 10201_database_win32.zip を展開してsetup.exeを実行すると初期インスタンスの作成まで行ってくれます。が、今までOracleを触ったことがなかったので、いろんな用語がよくわからない。インスタンスとサービスとSIDとあとなんだっけ？SIDって何？とりあえず実験用なのでそのへんよくわかんなくてもまあいいか。

:port: 1521
:SID: testdb
:共通PW: test


ユーザーを追加する
------------------

インストール後に、スタートメニューからSQLPlusを起動して、Databaseに接続します。

:ユーザー名: system
:パスワード: test
:ホスト文字列: (空白)

ホスト文字列って何だろう。とりあえず空白でよいらしい。ユーザー名 system はインストール時に必ず用意される物らしい。ログインしたら以下のコマンドで通常利用用のユーザーを追加する::

  create user foo identified by foopw;
  grant connect, resource to foo;

grantで何を許可するのが一番良いのかまだよく分かってないけど、fooユーザーがこれでテーブル作成等もできるので良いことにしておく。多分ちゃんと仕事で使うためにはこんなんじゃ駄目だと思うけど。


DBを使う
--------

まだ繋いでないので何とも。Pythonから使うにはcxOracleかな。

マニュアルを読む
----------------

森の中のようだ‥‥。なかなか目的の情報にたどり着けないし、今どの辺を読んでるのかも分からなくなってきた。

- `OTN Japan - ドキュメント : Oracle Database 10g`_


.. _`OTN Japan - ドキュメント : Oracle Database 10g`: http://otn.oracle.co.jp/document/products/oracle10g/


.. :extend type: text/html
.. :extend:



.. :comments:
.. :comment id: 2008-01-01.4001269165
.. :title: Re:Oracle10gをWindowsに入れてみる
.. :author: ocs
.. :date: 2008-01-01 00:03:21
.. :email: 
.. :url: 
.. :body:
.. ＞ホスト文字列
.. 別ホストのOracleインスタンスに繋ぎにいく時に使います。
.. 
.. ＞grantで何を許可するのが一番良いのか
.. とりあえず connect, resource だけで良いんじゃないですかね。
.. 
.. ＞ドキュメント
.. Oracleのドキュメントは分かりにくいですよ。。。
.. どれ読めばいいのかも良く分からないですし。
.. 
.. 自分は、リファレンスとして使うことがほとんどだった気がします。
.. 
.. :comments:
.. :comment id: 2008-01-01.1920506749
.. :title: Re:Oracle10gをWindowsに入れてみる
.. :author: しみずかわ
.. :date: 2008-01-01 10:49:53
.. :email: 
.. :url: 
.. :body:
.. > ocsさん
.. 
.. おお、わざわざフォローどうもです。あのドキュメントで迷子になるのが自分だけじゃないというのが分かって安心しましたｗ
.. 

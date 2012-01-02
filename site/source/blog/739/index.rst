:date: 2010-09-30 19:40:00
:categories: ['Event', 'python']
:body type: text/x-rst

====================================================
2010/09/30 BPStudy#37 に参加しました 夜のDjango + LT
====================================================

*Category: 'Event', 'python'*

`BPStudy#37`_ に参加してきました。
いつも通り走り書きメモです。

.. _`BPStudy#37`: http://atnd.org/events/8025

今回のネタは"夜のDjango"と"LT"。LTは初の試み？前回の `beproud-bot君`
の紹介もLTっぽかったよね。そこからの発展かな？

第一部「やっぱりDjango ja night」
------------------------------------------------------

* 発表
    * `@feiz`_, http://d.hatena.ne.jp/feiz/
    * `@tokibito`_, http://d.hatena.ne.jp/nullpobug/
    * `@IanMLewis`_, http://www.ianlewis.org/jp/
    * `@torufurukawa`_, http://oldriver.org/
    * `@shin_no_suke`_, http://www.facebook.com/profile.php?id=651258640

.. _`@feiz`: http://twitter.com/feiz
.. _`@tokibito`: http://twitter.com/tokibito
.. _`@IanMLewis`: http://twitter.com/IanMLewis
.. _`@torufurukawa`: http://twitter.com/torufurukawa
.. _`@shin_no_suke`: http://twitter.com/shin_no_suke


Djangoとは (`@feiz`_)
~~~~~~~~~~~~~~~~~~~~~~~
* 開発サーバーが入ってるのでApache無くても起動出来る
* モデルは継承できる. personモデルがbuchoモデルを継承とか
* ViewはPythonの関数だったりClassだったりするのが問題かも
* 汎用Viewがある
* URLディスパッチ (Controllerに相当?)
    * 設定次第でURLの逆引きが出来る（名前からURL生成）
* Template(HTMLと変数埋め込み)で使うタグやフィルタはカスタム可能
    * Templateの継承もあるよ, 普通のincludeには戻れん
* Admin: モデルに2,3行定義を書くときれいな管理画面が自動生成される
* なぜDjangoなのか
    * スピード
        * Admin の存在が大きい
        * 充実したライブラリ群
    * 安定性
        * バグがあんまり無い(full-stackの利点)
        * 後方互換がしっかりしてる
    * etc.
        * Python製
        * コミュニティーの愛を感じる

Django1.2の新機能 (`@feiz`_)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* マルチDB対応
    * DB設定の複数定義、切り替え
    * Routerを定義すると読み書きするDBを適切に切り替え出来る、らしい
* Templateのifブロックの書き方が変わった
    * ifnotequals -> if xx != yy
* Object-level Permission

Django1.3で予定されている新機能 (`@feiz`_)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* #14130 Catching ImportError in manage.py considered dangerous
    * manage.py でアプリロード中にraiseするとアプリロードが自動キャンセルされる
    * 握りつぶされると何が起きてるか分からない！
    * やっと直ります
* #12982 Pony:cache.get_or_set()
    * django.core.cache.cache にget or set

feizへの質問
~~~~~~~~~~~~~~
* DRYって何ですか？
    * Don't Repeat Yourself です


実開発に使えるDjangoの機能 (`@tokibito`_)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
資料: http://tokibito.orz.hm/presentation/9/ (上下左右キーで操作)

* tokibito でぐぐれ
* Djangoフォーム
    * （実際のform自動生成のためのコードを紹介）
    * selectプルダウンとか入力ボックスとか
    * バリデーションの指定と自動チェックとか
    * gettextで自動的に日本語表示, カスタマイズも可能
    * Widgetの例。チェックボックスとか,デフォルト表示とか
    * Templateでフォームを使う例
    * clean_xxx でフィールドの入力をバリデーションする
        * 検証の最後に呼ばれる
        * Form全体のクリーニング
        * 複数の入力項目からしか検証できないコードを書く
    * validator
        * Django1.2から関数で値をチェックできるようになった
    * ModelからFormを生成する
    * 細かいカスタマイズはDjangoのコード読んで、やる

* django.utils
    * Django内部で使われてるモジュール
    * SortedDict
        * 2.6ならOrderedDictを使うのが良いんじゃない
    * force_unicode
    * format
    * timesince
    * functional
        * wraps, lazy, memoize, ...
    * safe_join
        * 親より上のパスへのアクセスはエラーにするとか
    * ほかにもいっぱいあります


Djangoアプリの実践的設計手法 (`@IanMLewis`_)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* アプリの構成を覚えよう
    * そもそもDjangoアプリは何？
        * models.pyのあるPythonモジュール。
        * Pony
            * 子供が「子馬が欲しい！」と言うけどなかなか子馬はあげられない
            * 欲しいもの、プレゼントの理想の形
            * MLで、こんな機能が欲しい！ということが実現される
    * （色々アプリの構成の説明）

* アプリを細かく分けよう
    * Reusable Apps (巨大なCoreを細かいAppsに分けた)
        * 会員と会員登録と会員プロフィールと...を別アプリで実装
        * 今は標準アプリが20個以上に分割されている
        * INSTALLED_APPS が長くなぎすぎるんじゃないか！？
            * どうでもいい！
        * まじで James Bennettさんの発表をみてください！

* アプリはAPIを作ろう
    * モデルのクエリを直接使わない。チームにAPIを提供する(api.pyを作る)
    * クラス、関数、モデルメソッド、デコレータ、ミドルウェア、シグナル

Djangoによる開発のテスト (`@torufurukawa`_)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
資料: http://www.slideshare.net/torufurukawa/django-5323190

なんらかの理由でテストコードが必要。

* manage.py test
    * from django.test import TestCase
    * （テストの実装についてコード紹介）
    * database作成とか自動でやってくれる

* Fixtures
    * testdata.json
    * DBからjsonにdumpできる `python manage.py dumpdata`

* Client
    * Viewレベルのテストを支援するClient

buchoへの質問
~~~~~~~~~~~~~~~
* DjangoのClientテストはページ遷移も出来る？
    * できます by bucho

* Djangoでnoseやpy.testなどの最近のテストツールも使えますか？
    * 使えるはずですが...
    * DjangoのFixturesも使える？ -> どうだろう
    * Django的にはフレームワーク内に収まるように使うのが基本


Djangoの嵌りどころ、使用の注意点（アンチパターン） `@shin_no_suke`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
資料: http://www.slideshare.net/bpstudy/bpstudy-37-djagno-tips

* app
    * 再利用（笑）
        * 日実用的な再利用性
    * appの分け方
        1. 再利用できるか
        2. 機能ごと

* settings
    * settings.py
    * settings_dev.py
    * settings_production.py
    * settings_bucho.py

* 論理削除・(非)公開データの扱い
    * 表示用と管理用のモデル定義を分ける(論理削除データの扱いのため)

* O/R Mapper
    * （聞き逃した）

* cron + djangoadmin.py
    * 便利

* middlewareでの例外注意
    * メールでのエラー通知が飛ばない

* BP社で利用しているオープンなApps
    * mysql_replicated
        * 参照先DB切り替え
        * 海外の人が作ったヤツをforkして改造してます
    * django_extensions
    * django-bpmobile

* 複数のDjangoサイトの運用の例
    * monjudoh.com, monjudoh.jp という2サイトある場合
    * settings.py を分けてそれぞれ定義する,Viewも分ける

* Django admin画面の活用
    * ちょっとカスタマイズして使ってます
    * 非常に便利。これだけでもDjangoの意味がある

しみずかわメモ
~~~~~~~~~~~~~~~~~~
* newforms, oldforms っていう名前は微妙じゃないか？
* 疑問, Django template のifnotequalsの変更はJinja2から取り込んだ？
* `@tokibito`_ のプレゼンがs6だ！
* Djangoフォームのコード例はschemaベースの自動フォーム生成を知らないとピンと来ないかも
* Djangoはいつかzope3に到達する気がする。語弊あるけど。
* DjangoのFixturesはjsonで用意する
    * Railsはyaml、Djangoはjson。趣味嗜好としては逆だよなぁ
* DjangoとRailsの用語比較
    * `manage.py test` <-> `rake test`
    * `Fixtures` <-> `Fixtures`
    * `Client` <-> `integration test`


第二部「LT大会」
------------------------------------------------------

LTのメモは省略しまーす

@yuroyoro「MIrah」
~~~~~~~~~~~~~~~~~~~~
jvm上で動くRubyっぽい性的過多漬け言語 Mirahを紹介

@akisutesama「Objective-CはLLです（キリッ」
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@akisutesama はLLを使えないのでObjective-CをLLだと言い切るLTでした


第三部「懇親会」
-----------------
「やっぱりDjango ja naiyo」 by @aodag の予定。



.. :extend type: text/x-rst
.. :extend:


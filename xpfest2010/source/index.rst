Pythonで アジャイル 開発サイクル 2010ver.
=========================================

.. todo:: 白背景にして、とらドラ！的に「ぱいそん！」を右下に配置、を検討

.. todo:: 幕間に、みのりんを入れる。実行委員長へのリスペクト。

.. todo:: S6をsphinx拡張にする

.. todo::
    img タグをslimbox対応にする

.. :日時: 2010/9/4(土)
.. :話す人: 清水川 貴之
.. :時間: 50分


今日は
-------

  アジャイル開発をやっていると欲しくなる自動化ツール類を全てPythonでそろえてみよう！

という話をします。


.. raw:: html

    <script>
    s6.page({
        styles: {
            p: {textAlign: 'right', margin:'0'},
            blockquote: {fontSize: '140%'}
        }
    });
    </script>


そのまえに...
--------------

そのまえに...

.. raw:: html

    <script>
    s6.page({
        styles: {
            h2: {display:'none'},
            p: {fontSize:'150%', textAlign:'center', margin:'30% auto'}
        }
    });
    </script>



自己紹介1: 清水川 貴之
-----------------------
* `http://清水川.jp/ <http://清水川.jp/>`_
  `@shimizukawa <http://twitter.com/shimizukawa>`_
* お仕事:
   * 6月からフリーランス
* コミュ:
   * Zope/Plone系, Sphinx系, pyspa系, XP系
* 言語:
   * Python, Rails, 昔はC/8086とか

.. raw:: html

    <script>s6.page({effect: 'fadeScaleFromUpTransparent'});</script>

.. todo::
    名刺の画像を入れる？



自己紹介2: 最近やってること
----------------------------
* Deliverance / xdv
   * Webフレームワークのテンプレを書き換えずにデザイン適用
   * 複数のフレームワークをまたがって同じデザインに

詳しくは `http://縮.jp/一点 <http://縮.jp/一点>`_ で！

.. todo::
    * 文字で説明してもわからん！絵を出せ
    * xdvトップページに画像で簡単なイメージを伝える

.. raw:: html

    <script>s6.page({effect: 'fadeScaleFromUpTransparent'});</script>


自己紹介3: 翻訳本を出しました
------------------------------
* エキスパートPythonプログラミング
   * アスキー・メディアワークス
   * B5変 (416ページ)
   * 3780円

.. figure:: epp.jpg

.. raw:: html

    <script>s6.page({effect: 'fadeScaleFromUpTransparent'});</script>

自己紹介3: 翻訳本を出しました.
------------------------------
エキPythonの概要

* 1章: 環境別インストール
* 2章: リスト内包表記, デコレータ
* 3章: メタクラス, デスクリプタ
* 4章: 良い名前を選ぶ
* 5,6章: アプリ作成とパッケージング
* 7章～11章: ずっとXP的な話
* 12～15章: 最適化,デザパタ,日本語

.. figure:: epp.jpg

.. raw:: html

    <script>
    s6.page({
        styles: {
            'div/img': {opacity:'0.5'},
            'p': {marginTop:'0.1em',marginBottom:'0.1em'},
            'ul': {marginTop:'0.1em'},
            'ul/li': {display: 'none'}
        },
        actions: [
            ['ul/li[0]', 'fade in', '0.3'],
            ['ul/li[1]', 'fade in', '0.3'],
            ['ul/li[2]', 'fade in', '0.3'],
            ['ul/li[3]', 'fade in', '0.3'],
            ['ul/li[4]', 'fade in', '0.3'],
            ['ul/li[5]', 'fade in', '0.3'],
            ['ul/li[6]', 'fade in', '0.3'],
        ]
    });
    </script>

自己紹介3: 翻訳本を出しました..
-------------------------------
エキPythonの概要

* 1章: 環境別インストール
* 2章: リスト内包表記, デコレータ
* 3章: メタクラス, デスクリプタ
* 4章: 良い名前を選ぶ
* 5,6章: アプリ作成とパッケージング
* 7章～11章: ずっとXP的な話
* 12～15章: 最適化,デザパタ,日本語

今日はこのへんの話をします。

.. figure:: epp.jpg

.. raw:: html

    <script>
    s6.page({
        styles: {
            'div/img': {opacity:'0.5'},
            'p[0]': {marginTop:'0.1em',marginBottom:'0.1em',visibility:'hidden'},
            'p[1]': {marginTop:'-3em', display:'none'},
            'ul': {marginTop:'0.1em'},
            'ul/li': {visibility: 'hidden',color:'orange'},
            'ul/li[5]': {visibility: 'visible'}
        },
        actions: [
            ['ul', 'move', '0.3', [0,0],[0,-32]],
            ['p[1]', 'fade in', '0.3']
        ]
    });
    </script>



XPとワタシ
-------------
XPとの出会いは2002年頃、当時は組み込み開発へのxUnit適用と継続的インテグレーションを実践していました。2003年頃からZope, 2005年からPythonを使い始めましたが、それ以降もUnitTestや自動化といったことを続けています。

.. raw:: html

    <script>
    s6.page({
        styles: {
            p: {fontSize:'60%'}
        }
    });
    </script>

.. todo:: ここを埋める

幕間
-----

.. todo:: みのりん


アジャイルに必要な自動化
--------------------------

* テストの自動化
* 環境構築の自動化
* 継続的インテグレーションの実施
* ドキュメント生成の自動化

まずはソースコード管理から
---------------------------

何を自動化するにしてもコード管理は必須！

* VCS (Version Controll System)
* ソースコード等の履歴を管理
* 全ての自動化の基盤

.. todo::
    VCSのみのブロック図

VCS: 中央集権 vs 分散
----------------------

* 中央集権と言えば: cvs, svn
* 分散と言えば: hg, bzr, git

中央集権と分散, どっちがいいの？

* サーバー不要の **分散** が超おすすめ

VCS: 使ってみよう1
-------------------

* インストール
    * :command:`easy_install mercurial`
* 初期化
    * :command:`hg init`
* 複製
    * :command:`hg clone`

SCM: 使ってみよう2
-------------------

* 画面閲覧 & リポジトリ公開
    * :command:`hg serve`

.. todo::
    ここに画面イメージ


環境構築って何？
-----------------
プログラムはVCSから入手するだけで動くものはほとんどありません。

* 関連プログラムの入手, 配置
* パスの設定, スクリプトの設置
* 環境設定ファイルの配置, 変更


環境構築の自動化
-----------------
.. Pythonのデファクトスタンダードとして :command:`easy_install` があります。

.. :command:`easy_install mercurial` のように1コマンドで済む場合もありますが、大抵、インストール後の手順がたくさん **手順書** に書かれているものと思います。

* **環境構築手順書** ってありますよね
* プログラムインストールから設定まで全く引っかからずに5分で出来ますか？
* buildout で自動化しましょう！

zc.buildout
------------

* buildout.cfg というini形式のファイルで全て自動化
* 右の例はZopeとPloneを自動インストールしてプラグインも入れます

.. todo:: 以下のiniを画像にして表示

.. code-block:: ini

    [buildout]
    parts = zope2 instance
    extends = http://dist.plone.org/release/3.3.4/versions.cfg
    versions = versions

    find-links =
        http://dist.plone.org/release/3.3.4
        http://download.zope.org/ppix/
        http://download.zope.org/distribution/
        http://effbot.org/downloads

    eggs =
        Plone
        Products.PloneFlashUpload
        Products.PloneSlimbox
        Products.ATGoogleMap

    [zope2]
    recipe = plone.recipe.zope2install
    fake-zope-eggs = true
    additional-fake-eggs = ZODB3
    url = ${versions:zope2-url}

    [instance]
    recipe = plone.recipe.zope2instance
    zope2-location = ${zope2:location}
    eggs = ${buildout:eggs}
    user = admin:admin
    http-address = 8080

.. raw:: html

    <script>
    s6.page({
        styles: {
            ul: {width:'50%'}
        }
    });
    </script>


zc.buildout の実行例
---------------------
.. code-block:: bash

    $ hg clone http://xxxxx/ .
    $ ls
    bootstrap.py   buildout.cfg
    $ python bootstrap.py
    $ bin/buildout

これでZope/Ploneのインストールと環境構築が完了しました！

zc.buildout デモ
-----------------

.. todo:: デモ？

zc.buildoutで構築する環境の例
-------------------------------

* Zope/Plone のインストール、プラグイン設定、テスト環境
* Google App Engine の開発、テスト、デプロイ環境
* nginx, varnish のビルド、インストール、設定


ユニットテスト
---------------

* Python標準のunittestライブラリ
* Nose や py.test などの高機能版
* PySpec (RSpecのpython版)
    * 実行委員長 @shibukawa 作


PythonのDocTest
----------------
* 機能の説明文章がそのままテストになるスグレモノ


PythonのDocTest.
------------------
.. code-block:: python

    def add(x, y):
        """ 二つの値を足します。

        >>> add(1, 2)
        3
        """
        return x + y


PythonのDocTest .
-----------------
* 機能の説明文章がそのままテストになるスグレモノ
* 実際にテストを動かしているところを見てみます


PythonのDocTest-2
------------------

.. raw:: html

    <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,29,0" id=""> 
    <param name="movie" value="_static/20060521_doctest.swf"><param name="quality" value="high"><param name="menu" value="false"><param name="loop" value="1"><embed src="_static/20060521_doctest.swf"loop="1" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" menu="false"></embed></object>

.. raw:: html

    <script>
    s6.page({
        styles: {
            h2: {display:'none'},
            object: {width:'100%', height:'100%'},
            'object/embed': {width:'100%', height:'100%'}
        }
    });
    </script>

PythonのDocTest..
-----------------
* 機能の説明文章がそのままテストになるスグレモノ
* 実際にテストを動かしているところを見てみます
    * 続きは **DocTest TDD** で検索！


ここでおしらせです
-------------------
毎月勉強会などをやってます。

* `Sphinx+翻訳ハッカソン <http://atnd.org/events/7475>`_ (9/5)
* `エキPy読書会02 <http://atnd.org/events/6954>`_ (9/7)
* `Python mini Hack-a-thon <http://atnd.org/events/7474>`_ (9/25)

9月はほぼ埋まってしまいました><

.. raw:: html

    <script>s6.page({effect: 'slide'});</script>

    <script>
    s6.page({
        styles: {
            'ul': {display:'none'},
            'p[1]': {display:'none'}
        },
        actions: [
            ['ul', 'fade in', '0.3'],
            ['p[1]', 'fade in', '0.3']
        ]
    });
    </script>


下書き２
--------

* 継続的インテグレ―ション
    * 自動テストサーバー Buildbot
* 課題管理システム
    * Wiki + 課題 + コード = Trac
* ドキュメンテーション
    * Sphinx

.. raw:: html

    <script>s6.page({effect: 'slide'});</script>


質問タイム？
-------------

.. raw:: html

    <script>
    s6.page({
        styles: {
            h2: {fontSize:'150%',textAlign:'center',margin:'30% auto'}
        }
    });
    </script>



おまけ
-------
今日のプレゼンテーションは

* Sphinx
* S6 (c) 2007 Cybozu Labs, Inc.

で作成しました。


まとめ
-------

MercurialHG, Bazaar, PyPI, setuptools, easzy_install, zc.buildout, Paver, Nose, py.test, Buildbot, Trac, Sphinx, ...

* 続きは懇親会、または勉強会で！

ご清聴ありがとうございました


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


.. .. raw:: html
.. 
..     <script>
..     s6.page({
..         styles: {
..             h1: {color: '#FF0000'}
..         }
..         actions: [
..             ['h2', 'fade in', '0.4'],
..             ['p', 'move', 0.4, [0, 45], [-8, 45]]
..         ]
..     });
..     </script>


.. .. raw:: html
..
..     <address>清水川 貴之</address>

.. このページの短縮URLは `http://縮.jp/一燃 <http://縮.jp/一燃>`_ です。

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


下書き１
--------

* XPやアジャイルに必要な自動化
* まずソースコード管理
    * 中央集権(svn) vs 分散リポジトリ(hg)
* 環境自動構築・構成管理
    * buildout
* ユニットテスト
    * Nose や py.test



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



まとめ
------

MercurialHG, Bazaar, PyPI, setuptools, easzy_install, zc.buildout, Paver, Nose, py.test, Buildbot, Trac, Sphinx, ...

* 続きは懇親会、または勉強会で！

ご清聴ありがとうございました


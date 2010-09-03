Pythonで アジャイル 開発サイクル 2010ver.
=========================================

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


...
----

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


自己紹介2: 翻訳本を出しました
------------------------------
* エキスパートPythonプログラミング
   * アスキー・MW
   * B5変 (416ページ)
   * 3780円

.. figure:: epp.jpg

.. todo::
    img タグをslimbox対応にする

.. raw:: html

    <script>s6.page({effect: 'fadeScaleFromUpTransparent'});</script>


自己紹介3: 最近やってること
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


プロフィール
-------------
XPとの出会いは2002年頃、当時は組み込み開発へのxUnit適用と継続的インテグレーションを実践していました。2003年頃からZope, 2005年からPythonを使い始めましたが、それ以降もUnitTestや自動化といったことを続けています。


ここでおしらせです
-------------------
毎月勉強会などをやってます。

* Sphinx+翻訳ハッカソン `(9/5) <http://atnd.org/events/7475>`_
* エキPy読書会02 `(9/7) <http://atnd.org/events/6954>`_
* Python mini Hack-a-thon `(9/25) <http://atnd.org/events/7474>`_

続きはATNDで！

.. raw:: html

    <script>s6.page({effect: 'slide'});</script>


.. セッション概要
.. ---------------
.. 
.. * エキスパートPythonプログラミングの概要(目次)
.. * 中央集権 vs 分散リポジトリ
.. * 構成管理
.. * ユニットテスト
.. * 継続的インテグレ―ション
.. * ドキュメンテーション
.. * まとめ
..     * エキスパートPythonプログラミングの概要(目次)
..     * 続きはエキPy読書会で！
..     * お仕事のご相談など


ところでXPって
---------------

5つの価値ってありますよね



タイトル未定
--------------
この発表では、以下の内容について話していきます。

* 分散バージョン管理
* 構成管理
* ユニットテスト
* 継続的インテグレ―ション

上記などを用いた開発サイクルについて、それぞれPythonのツール群(MercurialHG,buildout, Buildbot, Noseなど)の活用方法をお話します。


中央集権 vs 分散リポジトリ
---------------------------


構成管理
---------


ユニットテスト
--------------


継続的インテグレ―ション
-------------------------


ドキュメンテーション
---------------------

まとめ
------

* エキスパートPythonプログラミングの概要(目次)
* 続きはエキPy読書会で！
* お仕事のご相談など


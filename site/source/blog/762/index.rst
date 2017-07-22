:date: 2011-09-06 00:50:00
:tags: Programming, Windows, ruby
:body type: text/x-rst

================================================
2011/09/06 Rubyのrcov-0.9.8 for Windows のビルド
================================================

WindowsのRubyで rcov_ を使用するには一般的には http://rubyforge.org/frs/?group_id=1750&release_id=16551 にあるようなビルド済みバイナリを使用しますが、rcov-0.8.1.2以降はビルド済みのものが提供されていないので、自分でビルドする必要があります。Windowsではコンパイル環境があってもはまったので、バインディングビルド手順をメモしておきます(完成物はこちら:  :download:`rcov-0.9.10-x86-mswin32-60.gem`)。

.. _rcov: http://mecab.sourceforge.net/

ビルド手順
--------------

この記事で対象にしているバージョン

* WindowsXP, 7 (95以降共通と思われる)
* ActiveRuby-1.8.7-p300
* rcov-0.9.10
* VisualStudio 6

環境の用意
~~~~~~~~~~~~
Windowsを用意します。そこにRuby-1.8.7(ActiveRuby), VisualStudio6 をインストールしておきます。

gemからコンパイル済みのgemパッケージを作るRubyGemsプラグイン `gem-compile`_ をインストールします::

    C:\> gem install gem-compile

.. _`gem-compile`: http://d.hatena.ne.jp/viver/20100404/p1


Rubyのext.hを書き換え
~~~~~~~~~~~~~~~~~~~~~~~

環境の問題かもしれませんが、VisualStudio6でrcovをビルドしようとすると、以下のようなエラーが発生します::

  ライブラリ rcovrt-i386-mswin32.lib とオブジェクト rcovrt-i386-mswin32.exp を作成中
  callsite.obj : error LNK2001: 外部シンボル "_ruby_frame" は未解決です
  rcovrt.obj : error LNK2001: 外部シンボル "_ruby_frame" は未解決です
  rcovrt.so : fatal error LNK1120: 外部参照 1 が未解決です。
  NMAKE : fatal error U1077: 'cl' : リターンコード '0x2'
  Stop.

そこで調べてみると `RUBYFORGEのフォーラム`_ で情報が見つかったので、Ruby本体の ``C:\ruby-1.8\lib\ruby\1.8\i386-mswin32\env.h``  を以下のように書き換えます::

    - extern struct FRAME {
    + extern __declspec(dllimport) struct FRAME {


.. _`RUBYFORGEのフォーラム`: http://rubyforge.org/forum/forum.php?thread_id=45666&forum_id=16394


rcov-0.9.10.gem から rcov-0.9.10-x86-mswin32-60.gem を作成
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

http://rubygems.org/gems/rcov から rcov-0.9.10.gem を取得してコマンドラインで以下のように変換します::

  C:\>gem compile rcov-0.9.10.gem
  WARNING:  no rubyforge_project specified
    Successfully built RubyGem
    Name: rcov
    Version: 0.9.10
    File: rcov-0.9.10-x86-mswin32-60.gem

これで rcov-0.9.10-x86-mswin32-60.gem が作成出来ました。

完成物と変更を加えたファイルを公開しておきます。ライセンスなどは元のrcovのものに従います。

* :download:`rcov-0.9.10-x86-mswin32-60.gem`


.. :extend type: text/x-rst
.. :extend:



.. :comments:
.. :comment id: 2011-09-06.2078596857
.. :title: 誤字 Re:Rubyのrcov-0.9.8 for Windows のビルド
.. :author: you_tomita
.. :date: 2011-09-06 16:47:02
.. :email: you.tomita@gmail.com
.. :url: 
.. :body:
.. 通りすがりですが、
.. 
.. 「環境の問題化も」→「環境の問題かも」
.. 
.. :comments:
.. :comment id: 2011-09-06.0725862509
.. :title: Re:誤字
.. :author: しみずかわ
.. :date: 2011-09-06 17:51:21
.. :email: 
.. :url: 
.. :body:
.. > 「環境の問題化も」→「環境の問題かも」
.. 
.. ありがとう！直しました。
.. 

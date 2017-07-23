:date: 2004-12-05 01:35:03
:tags: Zope, python

==================================
Python2.4をインストール
==================================

`Python2.4`_ が出たのでサーバーのPythonをアップデートしてみた。同時にZopeを2.7.3 [1]_ にアップデート。そしたらZopeが起動しなくなったのでエラーメッセージを確認したところ::

  no module rotor

とのエラーが。たしかにpython2.4のリリースノートに以下の一文が::

  The mpz, rotor, and xreadlines modules have been removed.

COREBlogのソースを確認してみたところ、rotorを使っているのはMoblog等でパスワードをエンコードするためらしい。とりあえず自分はMoblog機能を使っていないのでrotor周りをコメントアウトし、パスワードチェックは常に失敗するように書き換えて対処した（間違ってるとアブナイのでコードは載せません）。

ということで、メジャーバージョンアップ [2]_ はもっと慎重にやらなければと思った今日この頃。

.. [1] Zope2.7.4β1がもう出てるけど。
.. [2] 2.3から2.4はメジャーなのか、マイナーなのか‥‥
.. _`Python2.4`: http://www.python.jp/Zope/PyLog//1101828863/index_html



.. :extend type: text/plain
.. :extend:



.. :comments:
.. :comment id: 2005-11-28.4553909100
.. :title: Re: Python2.4をインストール
.. :author: 清水川
.. :date: 2004-12-05 18:22:41
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. 同じところではまった方発見。Trackbackしてみました。
.. 
.. 
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4555062652
.. :title: Re: Python2.4をインストール
.. :author: yasiyasi
.. :date: 2004-12-06 09:18:39
.. :email: 
.. :url: http://yasi.minidns.net/blog/
.. :body:
.. 　当方とはちょっと動きが違ったみたいですね。
.. 
.. 　当方の場合、Python2.4にする前からZope2.7.3を使っていたのですが、この場合Python2.4にすると、ZopeもPloneも動いたけれど、COREBlogだけはプロダクトの読み込みがうまくいかず、blogインスタンスに「壊れてるよ」アイコンが表示されていました。
.. 
.. 　Zopeも起動しなくなったのは、なぜなんでしょうかね？
.. 
.. 
.. :comments:
.. :comment id: 2005-11-28.4556228428
.. :title: Re: Python2.4をインストール
.. :author: 清水川
.. :date: 2004-12-07 00:43:00
.. :email: taka@freia.jp
.. :url: 
.. :body:
.. > Zopeも起動しなくなったのは、なぜなんでしょうかね？
.. 
.. Pythonと同時にZopeもVerUpしたので*.pycが無効になって、起動時のProductコンパイルで引っかかった‥‥とか？
.. 
.. 
.. :trackbacks:
.. :trackback id: 2005-11-28.4557388537
.. :title: FreeBSDでのPythonとZopeとの関係修復の状況
.. :blog name: YasiYasi's Blog
.. :url: http://yasi.minidns.net/blog/117
.. :date: 2005-11-28 00:47:35
.. :body:
.. 　FreeBSDの最新版portsでPython 2.4が標準とされた影響で、Python
.. 2.3を前提としているZope関連のportsが広く悪影響を受けている（COREBlogの例その１（私）、その２（清水川記さん）、ZMｙSQLDAの例（あくまでも　ん？不定期ログさん））件ですが、修正されつつあります。
.. #
.. ということなので、atsさんのCOREBlog改良はFreeBSDは気にしなくても大丈夫かと。
.. 　まず、ZopeのportsがPython
.. 2.3を使うように、すでに修正されました。
.. ...

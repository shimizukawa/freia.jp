:date: 2005-06-02 01:14:34
:tags: python, Zope
:body type: text/x-rst

=========================
2005/06/02 ZrstAmazon構想
=========================

TRIVIAL TECHNOLOGIESで公開されている `ZopeでSyntax Coloring`_ を元ネタに SilverCityDocument_ というPlone用のプロダクトを先日作ってみました。さっそくたかのりさんが `使用レポート`_ を書いてくれています。

.. highlights::

  インストールするときに気になった点として、SilverCityDocument-0.0.5.tgz を解凍して Zope サーバを再起動すると「skins ディレクトリが無いよ」とエラーがでていました。そこで、Products/SilverCityDocument ディレクトリの下に skins ディレクトリを作成して、plone サイトにインストールしなおしました。

  -- `SilverCityDocument をインストール - takanory.net`_

おや。だめじゃん(苦笑)。多分、skin無いのに以下のようなコードがあるのがいかんのだと思います。

.. code-block:: python

    install_subskin(self, out, GLOBALS)

これは、次の機会になおします。というかBlogに書いて以来手をつけてないのですが...今ちょっと別のことやってて...。


.. _`ZopeでSyntax Coloring`: http://coreblog.org/ats/640
.. _SilverCityDocument: http://www.freia.jp/taka/memo/plone/silvercitydocument/
.. _`使用レポート`: http://takanory.net/takalog/219
.. _`SilverCityDocument をインストール - takanory.net`: http://takanory.net/takalog/219



.. :extend type: text/x-rst
.. :extend:

ZSilverCity のソースコードを読んでもう一つ、 **docutilsのdirectiveを使えばISBNコードを入れるだけでAmazonのデータを引っ張って来る仕掛けを作れるんじゃないかなぁ** というのを思い付きました。

早速、 pyamazon_ でデータを引っ張ってくる amazon-block directive を作ってみたところ、それなりに動くモノが出来ました。ZSilverCityと比べると、AmazonのIDとか設定が必要なので、もうちょっとコード書かないといけないです。

くわしくは ZrstAmazon_ のページを作ったのでそちらへどうぞ。


.. _pyamazon: http://www.josephson.org/projects/pyamazon/
.. _ZrstAmazon: http://www.freia.jp/taka/memo/zope/zrstamazon/




.. :trackbacks:
.. :trackback id: 2006-09-24.8441435501
.. :title: ZrstAmazon4公開します
.. :blog name: SiteBites Blog
.. :url: http://sitebites.homeip.net/blog/147
.. :date: 2006-09-24 23:40:44
.. :body:
.. 清水川さんがつくられた ZrstAmazon の改変版を公開します。
.. 概要 pyAmazon に依存していたのを pyAWS
.. ベースで手を入れた自前モジュールに変更。Amazon E-Commerce
.. Service(ECS)のAPI Version 2006-09-13
.. に準拠(しているはず)。もっとも、pyAmazonベースのオリジナルでも古いAPIで動作はしているみたいです。
.. オプションに次が指定可能: :image: 清水川さんがつくられた
.. ZrstAmazon の改変版を公開します。 概要 pyAmazon
.. に依存していたのを pyAWS
.. ベースで手を入れた自前モジュールに変更。Amazon E-Commerce
.. Service(ECS)のAPI Version 2006-09-13
.. に準拠(しているはず)。もっとも、pyAmazonベースのオリジナルでも古いAPIで動作はしているみたいです。
.. オプションに次が指定可能: :image:
.. 

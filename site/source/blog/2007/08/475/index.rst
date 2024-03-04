:date: 2007-08-03 13:51:13
:tags: web

==================================
某宅配伝票問い合わせPHP
==================================

某宅配伝票問い合わせページのURLが以下のようになっていた。

  http://example.com/list.php?denpyo[0]=123456789

GETで配列指定してるんだけど、PHPだとこういう事が出来るのか‥‥というか安全なんだろうか？

ZopeだとDTMLで

.. code-block::

  <input name="hoge:list" ...>
  <input name="hoge:list" ...>
  <input name="hoge:list" ...>

としておくと、各入力をリストにしてくれる仕組みがあるけど、上記のPHPのGETだと ``0`` というマジックナンバーが出現しているのが気になる。ググってみたらPHP関連のページで普通に紹介されてるなあ。


.. :extend type: text/html
.. :extend:


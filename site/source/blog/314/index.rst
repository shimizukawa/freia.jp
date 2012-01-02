:date: 2006-02-21 01:10:00
:categories: ['Zope']
:body type: text/x-rst

=========================================================
2006/02/21 なぜZSQLMethodの返値はdict準拠じゃないのだろう
=========================================================

今日コードを書いていてZSQLMethodの返値がどんな型なのか気になった。

例えば、ZSQLMethodに値を渡す場合、キーワード引数にする必要があるので

.. code-block:: python

  kwargs = {
    'id': 10,
    'name': 'hoge',
    'age': 20,
  }
  zsqlmethod_update(**kwargs)

とか書くことが多い。さらに、取得したレコードの値を書き換えて書き戻すような場合、

.. code-block:: python

  records = zsqlmethod_select()

  r = records[0]
  # update record data here.
  r['name'] = 'fuga'
  r['age'] = 30

  zsqlmethod_update(**r)

とやりたいところだけど、zsqlmethodの返値は辞書型じゃないのでこんな事は出来ない(キーワード引数に展開されない)。結局、

.. code-block:: python

  records = zsqlmethod_select()

  r = records[0]
  keys = records.names()
  dict_r = dict(zip(keys,list(r)))

  # update record data here.
  dict_r['name'] = 'fuga'
  dict_r['age'] = 30

  zsqlmethod_update(**r)

こんなコードになってしまった。

こんなコードになってしまってから、返値の型が書かれている Zope-2.8.5/lib/python/Shared/DC/ZRDB/Results.py をぼーっと眺めていたら、 ``dictionaries`` とかいうMethodがある。なんだコレ使えばいいんだ‥‥。

dict準拠じゃないけどdictには変換できる。その心は‥‥返値がいきなりdict準拠だと書き換え可能だから‥‥かな？


.. :extend type: text/x-rst
.. :extend:

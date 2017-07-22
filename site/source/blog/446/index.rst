:date: 2007-04-15 22:07:13
:categories: ['Pattern', 'python', 'turbogears']
:body type: text/x-rst

=====================================
2007/04/15 FormEncodeで複合validation
=====================================

TurboGearsのサンプルコードで、validatorの設定方法やvalidators.Schemaを使ったTableFormのvalidationの例はけっこうたくさん見つかるが、複数の条件でバリデーションを行う方法については日本語の情報があまり見つからなかった。FormEncodeのマニュアルを眺めてみたら発見したので、以下使い方。

.. code-block:: python

    # AND operation
    validator = validators.All(validators.String(), validators.NotEmpty())

    # OR operation
    validator = validators.Any(validators.URL(), validators.Email())

PloneのArchetypesの場合は ``validators = (...)`` という感じに複数設定する前提の設計になっているけど、FormEncodeの場合はcompositeパターンで構築されている。利用する立場ではどっちでも良いけど、validatorを書く立場の場合は後者の方が使いやすい気がする。なんとなく。

.. :extend type: text/html
.. :extend:


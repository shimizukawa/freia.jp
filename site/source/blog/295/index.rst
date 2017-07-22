:date: 2006-01-04 16:00:00
:tags: python
:body type: text/x-rst

=====================================================
2006/01/04 pythonで辞書に構造体っぽくアクセスするメモ
=====================================================

(2009/3/24 追記)

あるライブラリの関数で引数objに、obj.yearとかobj.monthとかでアクセスする関数があって、テスト用にこのobjをでっち上げる必要が出てきました。素直に書くと

.. code-block:: python

  class MockData:
    year = 2000
    month = 1

  obj = MockData()

というふうに書かないといけないのですが、このMockを使うのはunittestの中なので、以下のようにして使いたいと思いました。

.. code-block:: python

  obj = {'year':2000, 'month':1}

ということで、これを実現するために以下のようなクラスを用意してみました。

.. code-block:: python

  class DictMapper(dict):
      def __getattr__(self, name):
          try:
              attr = super(DictMapper, self).__getattr__(name)
          except:
              if not self.has_key(name):
                  raise AttributeError,name
              attr = self.get(name)
          return attr

  obj = DictMapper({'year':2000, 'month':1})

激しく既出の予感。あともっと簡単な方法がありそうな予感。

------------------

2009/3/24 追記

今日,使いたくなって DictWrapper で検索して見つからなかったので、 DictWrapper でも検索されるようにコメントしておく。

それはそれとして手元に__setattr__してる版が見つかった。あと__getattr__で辞書に無い値にアクセスしたときにNoneを返しているあたりRubyっぽい感じで緩い。__getattr__は属性値があればメソッド呼び出されないので、上記エントリに書いていたsuper(...)は不要だった。

.. code-block:: python

 class DictMapper(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
    def __setattr__(self, name, value):
        self[name] = value

 In [1]: obj = DictMapper({'year':2000, 'month':1})
 In [2]: obj.keys()
 Out[2]: ['year', 'month']
 In [3]: obj.keys
 Out[3]: <built-in method keys of DictMapper object at 0x02444A48>
 In [4]: obj.keys = 1
 In [5]: obj.keys
 Out[5]: 1


.. :extend type: text/x-rst
.. :extend:



.. :comments:
.. :comment id: 2006-01-05.4431619861
.. :title: Re:pythonで辞書に構造体っぽくアクセスするメモ
.. :author: chewganabira
.. :date: 2006-01-05 00:44:03
.. :email: 
.. :url: http://kariyushi.plala.jp/chewganabira
.. :body:
.. このエントリを読んだ**瞬間**、Martin Fowlerの論文"To Be Explicit"のことを思い出しました。
.. 
.. http://martinfowler.com/ieeeSoftware/explicit.pdf
.. 
.. 
.. :comments:
.. :comment id: 2006-01-05.8320619570
.. :title: Re:pythonで辞書に構造体っぽくアクセスするメモ
.. :author: 清水川
.. :date: 2006-01-05 10:17:13
.. :email: 
.. :url: 
.. :body:
.. おお、早速読んでみます。
.. とりあえずExcite翻訳にかけたら、著者名が「マーチン野鳥捕獲者」と‥‥
.. 

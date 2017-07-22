:date: 2005-11-03 19:33:14
:tags: Zope, python
:body type: text/x-rst

====================================================
2005/11/03 Python2.3から2.4でmarshal形式データが変更
====================================================

Python2.4で動かしているZopeのgadflyで保存したデータファイルをPython2.3で動かしているZopeでロードしようとしたら、フォーマット異常でロードできませんでした。調べてみたところPython2.4でmarshalモジュールの保存フォーマットが変更になっていました。

gadflyのデータファイルの変換方法について `gadflyのデータフォーマット`_ にまとめてみました。

.. _`gadflyのデータフォーマット`: http://www.freia.jp/taka/memo/zope/gadflyfile

以下のコードで、Python2.3と2.4で作ったmarshalの出力ファイルを相互に読み込ませてみたところ、2.3で作ったファイルは2.4で読み出せるようです。



.. :extend type: text/x-rst
.. :extend:

.. code-block:: python

    import marshal
    import sys

    sv = ''.join([str(x) for x in sys.version_info[0:3]])

    a = [1, 2.3, 'abc', u'uni', (4,5), {6:'7'}]

    marshal.dump(a, file( 'marshal_'+sv+'.msl', 'w'))

    import glob
    gl = glob.glob('./*.msl')
    for f in gl:
        print '%s loading...' % f,
        try:
            marshal.load(file(f,'r'))
            print 'OK'
        except:
            print 'NG'

実行するとこんな感じです。

.. topic:: 実行してみた
  :class: dos

  | C:> python23 marshaltest.py
  | .\marshal_235.msl loading... OK
  | .\marshal_242.msl loading... NG
  | 
  | C:> python24 marshaltest.py
  | .\marshal_235.msl loading... OK
  | .\marshal_242.msl loading... OK
  

リリースノート等にこのフォーマット変更は書かれていませんでしたが、 `Python2.4のライブラリリファレンス`_ には関係ありそうな変更を発見しました。

まぁ、永続化のためにmarshal使うな、って書いてあるのでこの影響を受ける人はほとんどいないはず...。

.. _`Python2.4のライブラリリファレンス`: http://docs.python.org/lib/module-marshal.html



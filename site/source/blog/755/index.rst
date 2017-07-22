:date: 2011-05-01 15:49:47
:categories: ['python']
:body type: text/x-rst

=================================================
2011/05/01 buchoを2to3でPython2/3両対応にするメモ
=================================================

`bucho-0.1.0`_ for Python2/3

最近Python3対応パッケージがぼちぼち出始めているみたいで、4/30に `zc.buildout-2.0.0a`_ もリリースされました。そこで、お試しにインストール出来そうなPython3向けパッケージを探してみたけどあんまり見つからなかったので、 bucho_ をPython3対応してみました。

`pyreadline を2to3でPython2/3両対応にするメモ`_ ではまった経験を元に、サクサク対応を進めていきます。


.. _`pyreadline を2to3でPython2/3両対応にするメモ`: http://www.freia.jp/taka/blog/753
.. _`zc.buildout-2.0.0a`: http://pypi.python.org/pypi/zc.buildout/2.0.0a1
.. _bucho: http://pypi.python.org/pypi/bucho
.. _`bucho-0.1.0`: http://pypi.python.org/pypi/bucho/0.1.0

Python3対応メモ
----------------

例によって、とりあえず2to3変換してみます。 ``python32 c:\Develop\Python32\Tools\Scripts\2to3.py bucho`` という感じでオプション無しで実行して、まずは変換差分を確認。

.. code-block:: python

    --- bucho/__init__.py	(original)
    +++ bucho/__init__.py	(refactored)
    @@ -1,6 +1,6 @@
     # encoding: utf-8
     import json
    -import urllib
    +import urllib.request, urllib.parse, urllib.error
     
     # these methods are exposed to Internet by wsgi.py
     __all__ = ['show', 'latest_status', 'all_status', 'torumemo']
    @@ -152,14 +152,14 @@
     def latest_status():
         """Print latest bucho's tweet.
         """
    -    url = urllib.urlopen('http://twitter.com/statuses/user_timeline/torufurukawa.json')
    +    url = urllib.request.urlopen('http://twitter.com/statuses/user_timeline/torufurukawa.json')
         tof = json.loads(url.read())
         return tof[0]['text']
     
     def all_status():
         """Print all bucho's tweet.
         """
    -    url = urllib.urlopen('http://twitter.com/statuses/user_timeline/torufurukawa.json')
    +    url = urllib.request.urlopen('http://twitter.com/statuses/user_timeline/torufurukawa.json')
         tof = json.loads(url.read())
         for t in tof:
             return t['text']
    --- bucho/command.py	(original)
    +++ bucho/command.py	(refactored)
    @@ -62,7 +62,7 @@
     for name in ['show', 'latest_status', 'all_status', 'torumemo']:
         def makecmd(n):
             def f(self, arg):
    -            print(getattr(bucho, n)())
    +            print((getattr(bucho, n)()))
                 return 0
             return f
         setattr(BuchoCmd, "do_" + name, makecmd(name))
    @@ -73,8 +73,8 @@
             if options is None:
                 options = BuchoOptions()
             c = cmdclass(options)
    -    except Exception, e:
    -        print e
    +    except Exception as e:
    +        print(e)
             return
     
         if options.args:
    --- bucho/wsgi.py	(original)
    +++ bucho/wsgi.py	(refactored)
    @@ -1,4 +1,4 @@
    -import urlparse
    +import urllib.parse
     import bucho
     
     
    @@ -11,8 +11,8 @@
     """
     
     def wsgi_app(environ, start_response):
    -    split_result = urlparse.urlsplit(environ['PATH_INFO'])
    -    paths = filter(None, split_result[2].split('/'))
    +    split_result = urllib.parse.urlsplit(environ['PATH_INFO'])
    +    paths = [_f for _f in split_result[2].split('/') if _f]
         headers = [('Content-Type', 'text/plain')]
     
         if not paths:


buchoはスレンダーなのであまり変換は多くありませんでしたが、実際に動かしてみると全然言うことを聞いてくれません。bucho, 見た目ほど単純ではないっぽい。

といことで、以下、はまったところをメモ。

printがbytesを受け付けない
----------------------------

Python2のUnicode文字列で、実行環境のコンソールに出力出来ない文字を含んでいる場合、 ``print value`` で出力出来ない場合があるので、以下のようにごまかすことがあります(良い代案募集):

.. code-block:: python

    print value.encode(sys.stdout.encoding, 'replace')

しかしPython3のprint()にbytesを渡すと以下のようにreprした結果が出力されてしまいます。

`Python2` の場合:

.. code-block:: python

    >>> print(b'bucho')
    bucho
    >>> print(u'部長'.encode(sys.stdout.encoding))
    部長

`Python3` の場合:

.. code-block:: python

    >>> print(b'bucho')
    b'bucho'
    >>> print('部長'.encode(sys.stdout.encoding))
    b'\xe9\x83\xa8\xe9\x95\xb7'

とはいえ、Unicodeオブジェクトのままprintに渡してしまうと環境依存で出力出来ない文字に遭遇したときにUnicodeEncodeErrorになってしまうので、以下のようにして回避しました(ほんと、良い代案募集):

.. code-block:: python

    bucho_encoding = sys.stdout.encoding
    if not bucho_encoding:
        bucho_encoding = 'utf-8'

    value = value.encode(bucho_encoding, 'replace')
    value = value.decode(bucho_encoding, 'replace')
    print(value)


なお、 `エキスパートPythonプログラミング`_ の日本語版で追加されたUnicode章(Appendix A)でこのあたりについて詳しく触れています (sys.stdout.buffer.writeでbytesを書き出せる (407ページ)、sys.stdout.encodingはファイルにリダイレクトしたときにNoneになるのでlocale.getpreferredencoding()を代わりに使う (399ページ)、など)。

.. _`エキスパートPythonプログラミング`: http://www.amazon.co.jp/dp/4048686291/freiaweb-22

wsgirefのappサンプルが動かない
-------------------------------

`Python-3.2のWSGIアプリケーションのサンプルコード`_ のアプリ部分を抜き出すと以下のように書かれていましたが、残念ながらこのままでは動きません。

.. code-block:: python

    def simple_app(environ, start_response):
        setup_testing_defaults(environ)

        status = b'200 OK'
        headers = [(b'Content-type', b'text/plain; charset=utf-8')]

        start_response(status, headers)

        ret = [("%s: %s\n" % (key, value)).encode("utf-8")
               for key, value in environ.items()]
        return ret

status は str 型でなければいけません。headersに設定するkey/valueもstr型でなければいけません。returnする値はbytesのリストなので、これは上記の記述で問題ありませんが、別のサンプルでは ``return b"Hello World"`` って書いてあってこれは ``return [b"Hello World"]`` じゃないとNGでした。

...というような事をつぶやいたらところ、 @methane からコメントを頂きました:

.. highlights::

    それは、この間PEP3333とかで結論が出た話で、ドキュメントの更新が間に合って
    ないみたいですね。
    statusとheaderは両方共str型で、latin-1でエンコードして出力されるはずです。

    -- @methane http://twitter.com/methane/status/64516507572510720

なるほどー。とりあえず似たような報告は上がってなかったので http://bugs.python.org/issue11968 に超適当な報告をあげておきました。


.. _`Python-3.2のWSGIアプリケーションのサンプルコード`: http://docs.python.org/py3k/library/wsgiref.html#wsgiref.util.setup_testing_defaults


json.loads()はbytesを受け付けない
----------------------------------
以下のコードは `Python2` で動作します:

.. code-block:: python

    url = urllib.urlopen('http://twitter.com/statuses/user_timeline/torufurukawa.json')
    tof = json.loads(url.read())

しかし、これを単純に2ty3しただけの以下のコードは `Python3` で動作しません:

.. code-block:: python

    url = urllib.request.urlopen('http://twitter.com/statuses/user_timeline/torufurukawa.json')
    tof = json.loads(url.read())

原因は、json.loads()はstrを期待しているのに、url.read()の返値がbytesだったためです。ということで、Python3で動作させるために以下のように書き換えました:

.. code-block:: python

    url = urllib.request.urlopen('http://twitter.com/statuses/user_timeline/torufurukawa.json')
    tof = json.loads(url.read().decode('ascii'))

さすがにasciiは手を抜きすぎか。 ``url.headers['content-type']`` のcharsetを見てdecodeしないとだめか。めんどくさいな。

2to3対応setup.py
------------------

最後に、Python2/3両対応にするためにsetup.pyに手を加えます。

.. code-block:: python

    import setuptools
    extra = {}

    if sys.version_info >= (3, 0):
        if not getattr(setuptools, '_distribute', False):
            raise RuntimeError(
                    'You must installed `distribute` to setup bucho with Python3')
        extra.update(
            use_2to3=True
        )


    setuptools.setup(
        name = 'bucho',
        ....
        **extra
        )

.. ***

とりあえず今日のまとめ
-----------------------

* buchoは手強い
* `bucho-0.1.0`_ リリース (ロゴがPython3だ！)



.. :extend type: text/x-rst
.. :extend:


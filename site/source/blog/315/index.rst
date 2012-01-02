:date: 2006-02-22 01:30:00
:categories: ['Zope', 'python']
:body type: text/x-rst

======================================
2006/02/22 ZopeTestBrowserを使ってみる
======================================

*Category: 'Zope', 'python'*

Zopeから独立したPythonパッケージとして使える ZopeTestBrowser-1.0.0 を使ってみようとしたら、依存してるモジュールが多かったのでどうしたもんかと色々調べてみたら、Zope-2.9.0にふつーに入ってた。Zope2.9.0ではZope3の色々な機能が使えるようになっている。zope.testbrowser もそのうちの一つで、UnitTestコードを書くときにこれがあるとテストの幅が広がるんじゃないかと思う。

ちなみに、ZopeTestBrowser-1.0.0ではGenerator式が使われてるので、そのままではPython-2.3系で動作しない。もしかしたら、ちょっと書き換えたら動くかもしれない。しかしPython-2.3系で使えないと現行のZope用UnitTestに使おうと思うとネックになるかもしれない。

とりあえず気を取り直して、チュートリアルに従ってPythonのコンソールから以下のように動かしてみた。


.. :extend type: text/x-rst
.. :extend:

.. topic:: Python
    :class: dos

    | >>> from zope.testbrowser.browser import Browser
    | >>> browser = Browser()
    | >>> browser.open('http://localhost:8080/')
    | >>> browser.url
    | 'http://localhost:8080/'
    | >>> '<title>TopPage</title>' in browser.contents
    | True
    | >>> browser.isHtml
    | True
    | >>> browser.title
    | 'TopPage'
    | >>> print browser.headers
    | Server: Zope/(Zope 2.7.7-final, python 2.3.5, win32) ZServer/1.1
    | Date: Tue, 21 Feb 2006 15:15:12 GMT
    | Content-Length: 572
    | Connection: close
    | Content-Type: text/html; charset=utf-8
    | >>> browser.headers['content-type']
    | 'text/html; charset=utf-8'
    | >>> browser.reload()
    | >>> link = browser.getLink('Hello')
    | >>> link
    | <Link text='Hello' url='http://localhost:8080/subfolder/hello_html'>
    | >>> link.text
    | 'Hello'
    | >>> link.tag
    | 'a'
    | >>> link.url
    | 'http://localhost:8080/subfolder/hello_html'
    | >>> link.attrs
    | {'href': 'subfolder/hello_html'}
    | >>> link.click()
    | >>> browser.url
    | 'http://localhost:8080/subfolder/hello_html'

他に、Formへの入力とかいろいろあり。Basic認証とかもできるらしい。詳しくは `zope/testbrowser/README.txt`_ を参照のこと。（リンク先はZope3のもの。Zope2.9.0のと同じ。）

`DevCamp2006w`_ 向けにUnitTestを調べてたはずなのに、今回はコレは使えないかも。残念。

.. _`zope/testbrowser/README.txt`: http://svn.zope.org/Zope3/trunk/src/zope/testbrowser/README.txt?rev=41673&view=markup
.. _`DevCamp2006w`: http://coreblog.org/camp/2006w/%%%%%%%%%-------

追記: 「UnitTestコードを書くときにこれがあるとテストの幅が広がるんじゃないかと思う。」と思ったけど、ZopeUnitTest中のインスタンスにhttpアクセスできないので、そう言う用途には使えないかも。じゃあZope-2.9.0のzope.testbrowserはどういう時に使うんだろう？要調査。

追記2: Zope/lib/python/zope はZope-2.8系から入っている。zope.testbrowserは2.9.0から。

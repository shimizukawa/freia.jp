:date: 2007-07-20 02:26:59
:categories: ['python', 'turbogears']
:body type: text/x-rst

=======================================
TurboGearsのVirtualHost化ではまりまくる
=======================================

今日はTurboGearsのアプリをmod_proxyの陰で動かし、VirtualHostで任意のパス以下に配置しようとしてはまりまくってました。

たとえば http://example.com/myapp/ がTurboGearsアプリのルートになる場合、TurboGearsのプログラム上やテンプレート上には"myapp"は書かずに、cfgに ``server.webpath="myapp"`` と書けばそれでOK！...と思ってました。それでは、はまり度の軽い方から並べてみます。

  1. server.webpath="/myapp", base_url_filter.on = True をcfgに書く
  2. テンプレート内のパスは ${tg.url('/hoge')}のようにtg.urlでくるむ
  3. リダイレクトは turbogears.redirect('hoge') ではなく turbogears.redirect('/hoge')と書く

(1),(2)は基本、(3)は知らないと悩むことになりそう。redirect('hoge')だと http://example.com/hoge にリダイレクトされます。redirect('/hoge')ならちゃんと http://example.com/myapp/hoge にリダイレクトされます。

  4. base_url_filter.use_x_forwarded_host = False を明示的に指定する
  5. base_url_filter.base_url = "http://example.com/myapp" のようにmyappまで書く

(4),(5)は本当にこれで正しいのかアヤシイです。でもこうしないと http://example.com/myapp/hoge にアクセスしたときに http://example.com/hoge/ にリダイレクトされてしまいます。cherrypyはControllerオブジェクトにアクセスしたときはURL末尾に"/"が付くようにリダイレクトしようとします。しかし、リダイレクトのURL生成ではturbogearsのredirectやurl関数のようにmyappを考慮してくれません。この対処のため(4)で実サーバーURLの自動的検出をOFFにし、(5)でURLをmyapp付きで与えることにより、強制的にbase_urlを指定します。

いや、指定します、とか書いてますが、本当にこれでいいんだろうか‥‥。日英両方の文献を見てもこういう例が見あたらない気がします。みんなmod_pythonでやってて問題にならないからかな？

まとめ.

- prod.cfg

.. code-block:: xml

    server.webpath="/myapp"
    base_url_filter.on = True
    base_url_filter.use_x_forwarded_host = False
    base_url_filter.base_url = "http://example.com/myapp"

- httpd_tg.conf

.. code-block:: xml

  <VirtualHost *:80>
    ServerName example.com
    RewriteEngine On
    RewriteRule ^/myapp(/.*|$) http://localhost:8080$1 [P,L]
  </VirtualHost>

- 参考文献

  - `TurboGears1.0.2.2をmod_pythonで起動する - the technote`_
  - `SumiTomohikoの日記 - [TurboGears] redirect関数の引数にurl関数の戻り値を与えてはならない。`_
  - `turbogears   apache(mod_proxy) (yamakk blog)`_
  - `1.0/BehindApache - TurboGears Documentation`_

.. _`TurboGears1.0.2.2をmod_pythonで起動する - the technote`: http://luna.loop-net.co.jp/blog/htanaka/2007/06/22/1182448638466.html
.. _`SumiTomohikoの日記 - [TurboGears] redirect関数の引数にurl関数の戻り値を与えてはならない。`: http://d.hatena.ne.jp/SumiTomohiko/20070218/1171791817
.. _`turbogears   apache(mod_proxy) (yamakk blog)`: http://yamakk.infogami.com/blog/mod_proxy
.. _`1.0/BehindApache - TurboGears Documentation`: http://docs.turbogears.org/1.0/BehindApache


.. :extend type: text/html
.. :extend:

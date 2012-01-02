:date: 2009-12-08 23:55:00
:categories: ['web']
:body type: text/x-rst

=========================================
sidebarとfooter付きLiquidページのHTML練習
=========================================

Sphinx_ のデザインを参考に、sidebarとfooterのあるLiquidなWebページを作る練習をしてみました。

.. _Sphinx: http://sphinx.shibu.jp/

HTMLコーディングはそれなりにちゃんと出来る方（遅いけど）だとは思うのですが、Liquid（画面幅に合わせてサイト幅が広がるデザイン）なページにサイドバーとフッターがある場合に自然にレイアウトすることが出来ませんでした。

それっぽいレイアウトとしては、サイドバーを左にfloatさせて、本文をabsoluteでleft位置をサイドバーの幅の分指定するという方法です。この方法は画面幅に合わせて本文部分の幅が可変になるものの、absoluteを使ってしまっているので、本文部分の高さがサイドバーよりも長くなってもfooterの縦位置はサイドバーの直下に張り付いたままになってしまったわけです。って、文字だけで説明してもわからんなあ。

ま、フッターの位置は本文・サイドバーどちらかの長い方の下（＝ページの最下端）に配置したいということです。

ということで、以下がうまくいったHTMLとCSSの例です。

.. code-block:: xml

  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      <title>Liquid Layout Test</title>
      <style type="text/css">
  <!--
  #header {
      background-color: #888;
      padding: 2px;
      height: 50px;
  }
  #navigation {
      background-color: #666;
      padding: 2px;
      height: 1em;
  }
  #document {
  }
  #documentwrapper {
      background-color: #eee;
      float: left;
  }
  #bodywrapper {
      background-color: #999;
      margin: 0 0 0 200px;
  }
  #body {
      background-color: #888;
      padding: 10px;
  }
  #sidebarwrapper {
      background-color: #bbb;
      width: 200px;
      float: left;
      margin-left: -100%;
  }
  #sidebar {
  }
  #footer1 {
      background-color: #666;
      padding: 2px;
      height: 1em;
  }
  #footer2 {
      background-color: #444;
      padding: 2px;
      height: 2em;
  }
  .clearer {
      clear: both;
  }
  -->
      </style>
    </head>
    <body>
      <div id="header">Header</div>
      <div id="navigation">Navigation</div>
      <div id="document">
        <div id="documentwrapper">
          <div id="bodywrapper">
            <div id="body">Body Body Body Body ... Body Body </div>
          </div>
        </div>
        <div id="sidebarwrapper">
          <div id="sidebar">Sidebar Sidebar ... Sidebar Sidebar</div>
        </div>
        <div class="clearer"></div>
      </div>
      <div id="footer1">Footer1</div>
      <div id="footer2">Footer2</div>
    </body>
  </html>


CSS部分を見ると分かりますが、 ``margin-left: -100%;`` という怪しい記述が。なるほど！これで幅のあるサイドバーの論理的な存在を画面外に追い出しつつ、同じエレメントを ``float:left`` にすることで画面内の左に乗るようにしているのか！思いついたヤツの頭はオカシイに違いない！

とりあえずここ3年くらいの疑問が解けた。ていうかよく見るCSSハックとかも好んで使いたくはないけど、こんな裏技もいやだ（笑）%%%%%%%%%------

あ、これ ``ネガティブマージン`` って言うんだ。理解してから検索するとすぐに例が見つかるという...。 chikin & egg pattern ですね。



.. :extend type: text/x-rst
.. :extend:

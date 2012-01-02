:date: 2009-06-28 21:38:09
:categories: ['Zope', 'python', 'pyspa']
:body type: text/x-rst

=======================================================
2009/06/28 [pyspa5] Zope3を最小構成でmod_wsgi動作させる
=======================================================

*Category: 'Zope', 'python', 'pyspa'*

pyspa5の成果２。

:やりたいこと: Zope3を軽い構成でmod_wsgiで起動できるようになると小規模なシーンで使いやすい
:前提条件1: mod_wsgi で起動する(Zope3をServer起動しない)
:前提条件2: zopeパッケージは出来るだけ削減する
:前提条件3: 軽く動作する

最近はZope3もegg化が進んでいて、Zope2/Ploneユーザーとしてはとってもわかりにくくなってしまったんだけど、mod_wsgiで接続して出来るだけ軽く動作するツールを作りたいというシーンではとてもやりやすくなってきている。ということで、問い合わせフォームを動作させるだけの軽いzope3 wsgi環境を作ろうと思ったんだけど、情報があちこちに分散していてまとまっていない、ということが分かった。

曰く:
* WSGIで動作させるためにPasteScript, PasteDeployを使う
* Zope3 は mod_wsgi で呼び出せるようになっている
* mod_wsgi アプリケーションの作り方
* paster serve paste.ini でサーバー起動出来る

じゃあ、Zope3をmod_wsgiに接続して、非サーバー起動で動作させるにはどうすれば良いのか？（どこかに書いてたら誰か教えてください）

とりあえず zope.paste をeasy_installして、mod_wsgiの設定で接続先となるapplication関数を自分でzope.pasteのコードを読んで用意すれば起動できた。以下がapplication関数の実装:

.. code-block:: python

  from paste.deploy import loadapp
  from zope.interface import implements
  from zope.app.wsgi import interfaces
  
  class PasteApplication(object):
      implements(interfaces.IWSGIApplication)
  
      def __init__(self, name):
          # `name` that gets passed here is something like:
          # <utility_name>:<host>:<port> for zope.app.twisted, and just
          # <utility_name> for zope.app.server. Extract just the utility
          # name.
          name = name.rsplit(':', 2)[0]
          # XXX There's no way currently to find out where our
          # INSTANCE_HOME is, so assume the cwd is the INSTANCE_HOME.
          path = r'C:\Project\zope2instances\wsgi\zope-paste'
          self.wsgi_app = loadapp('config:etc/paste.ini',
                                  name, relative_to=path)
  
      def __call__(self, environ, start_response):
          """See zope.app.wsgi.interfaces.IWSGIApplication"""
          return self.wsgi_app(environ, start_response)
  
  application = PasteApplication('main')

  
paste.iniとかData.fsの場所とかはとりあえず適当だけど、これでWindows7上で、apache2->mod_wsgi->zope3がちゃんと動作した。あとでabでベンチマーク取ってみよう。

（あとでまとめる：zope3をwsgiで動作させる一連の手順）

.. :extend type: text/html
.. :extend:

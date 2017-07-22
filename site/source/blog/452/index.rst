:date: 2007-04-22 01:03:38
:tags: Zope, Plone
:body type: text/x-rst

====================================================
2007/04/22 InstanceManagerでZope/Plone環境自動構築 2
====================================================

コマンド一発でZopeのインスタンスを作り、Ploneのtgzを展開し、svnからソースコード取ってきて、zopeを起動してploneのインスタンスを作ってプロダクトの追加までやってくれる便利なライブラリ、instance managerの設定についてのメモです。インストールについては `InstanceManagerでZope/Plone環境自動構築`_ を見てください。

ではさっそく、userdefaults.py の中身について。


.. _`InstanceManagerでZope/Plone環境自動構築`: http://www.freia.jp/taka/blog/451


.. :extend type: text/x-rst
.. :extend:


.. code-block:: python

  python = 'python2.4'
  zope_version = '2.9.7'
  
  zope_location_template = '%(user_dir)s/zope/Zope-%(zope_version)s'
  zope_instance_template = '%(user_dir)s/instances/%(project)s'
  archive_basedir_template = '%(user_dir)s/download/'
  archivebundle_basedir_template = '%(user_dir)s/download/'
  symlink_basedir_template = '%(user_dir)s/svn/'
  symlinkbundle_basedir_template = '%(user_dir)s/svn/'
  
  development_machine = True
  user = 'admin'
  password = 'admin'
  port = '8080'
  ftp_port = None

  plone_site_name = 'portal'

このへんが共通設定かな、という感じでコメントに書かれていた説明を解読しつつ設定してみました。

上記の設定に従って、利用するZopeを~/zope/以下に適切な名前でインストールしておく必要があります。上記の例なら ~/zope/Zope-2.9.7 が必要です。また、tgzファイル置き場として~/download を、svnのチェックアウトコード置き場として~/svn/を使用するように指定しているので、それぞれディレクトリを作成しておきましょう。

userdefaults.pyはあくまで共通設定なので、これを設定しただけでは環境を構築することは出来ません。ということで次に環境構築用の設定を作成します。環境構築設定を記述するファイルとして、~/.instancemanager フォルダに<projectnamem>.pyを作成します。projectnameは好きに付けて良いので今回はtestproj.pyとします。

.. code-block:: python

  zope_version = '2.9.7'
  development_machine = True
  
  symlink_sources = [
      {'source':'ATCTSmallSample',
       'pylib':False,
       'develop':False,
       'droplist':(),
       'url':'http://svn.freia.jp/open/ATCTSmallSample/trunk'
      },
      {'source':'ATBookshelf',
       'pylib':False,
       'develop':False,
       'droplist':(),
       'url':'http://svn.freia.jp/open/ATBookshelf/trunk'
      },
      {'source':'ATExtFlash',
       'pylib':False,
       'develop':False,
       'droplist':(),
       'url':'http://svn.freia.jp/open/ATExtFlash/trunk'
      },
  ]
  
  archivebundle_sources = [
      {'source': 'Plone-2.5.2-1.tar.gz',
       'develop':False,
       'droplist':('Five'), # drop Five from this bundle
       'url':'http://plone.googlecode.com/files/Plone-2.5.2-1.tar.gz'
      },
  ]
  
  main_products = [
      'ATBookshelf',
      'ATCTSmallSample',
      'ATEventRegistry',
      'ATExtFlash',
  ]
  

これで設定が出来ました。では早速実行してみましょう。

.. topic:: instancemanager fresh
    :class: dos

    % instancemanager fresh testproj

このツール、エラーが起きても止まらずに最後まで走ってしまうので、うまく動いて居なそうな場合は-vオプションを付けて出力されるログをよく観察する必要があります。エラーが起きなければ、8080ポートでZopeが動いているはずです。

InstanceManagerは、このほかにも以下のような機能があります。

- ZEO環境の構築
- テストの実施
- Data.fsの定期的なバックアップ
- Data.fsのPack
- zope.confの設定
- GenericSetupとの連携
- Zope3での使用

機能豊富です。ていうかGenericSetupまで入ってるし。

しかし、内部のコードはsvn,tar,unzipなどをos.system等で呼び出していて、Windowsで動かすには障害が多そうな感じです。特にzopectlコマンドはWindowsでは使えないので、quickinstaller呼び出しやtestの実行はうまく動きません。今のところUnixでつかえ、という感じなのかな。

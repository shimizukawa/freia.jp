=============================================
Deliverance 環境構築 easy_install のみ使用編
=============================================

.. warning::
    本ドキュメントはxdvがリリースされる前の2009年9月時点のものであり、
    コードなどは書かれてる通りの手順ではうまく動かないと思います。

このドキュメントは、ほぼ素の状態のPython環境でDeliveranceを使い始めるための手順を記載しています。

なお、Pythonはインストール済みで、実行ファイルへのパスが通っている状態にしておいてください。また、以下のコマンドの最初のいくつかはPython環境にインストールを行うので、その部分はsudoコマンドを書いてあります。

仮想環境にインストールする
---------------------------

素のPython環境を想定し、必要なパッケージを導入します。
次に、Python仮想環境を作ります。

::

  $ wget http://peak.telecommunity.com/dist/ez_setup.py
  $ python ez_setup.py
  $ easy_install virtualenv
  $ virtualenv deliv


次に仮想環境を有効にして、仮想環境内にdeliveranceをインストールします。
deliveranceは未リリースの0.3版を使用したいので、Subversionリポジトリパスを指定してインストールすることにします。
また、設定ファイルのテンプレート生成のためにPasteScriptをインストールします。

::

  $ cd deliv
  $ source bin/activate
  $ easy_install "lxml==2.2.2"
  $ easy_install http://codespeak.net/svn/z3/deliverance/trunk
  $ easy_install PasteScript

上記で "lxml==2.2.2" としているのは、この記事を書いた時点では、配布サイトで2.2.3以降はコンパイル済みのeggが登録されていなかったためです。

最後にDeliveranceの設定ファイルをテンプレートから生成します。

::

  $ paster create --list-templates
  Available templates:
    basic_package:      A basic setuptools-enabled package
    deliverance:        Basic template for a deliverance-proxy setup
    deliverance_plone:  Plone-specific template for deliverance-proxy
    paste_deploy:       A web application deployed through paste.deploy
  
  $ paster create -t deliverance Deliv1
  Selected and implied templates:
    deliverance#deliverance  Basic template for a deliverance-proxy setup
  
  Variables:
    egg:      Deliv1
    package:  deliv1
    project:  Deliv1
  Enter host (The host/port to serve on) ['localhost:8000']:
  Enter proxy_url (The main site to connect/proxy to) ['http://localhost:8080']: http://twitter.com/
  Enter proxy_rewrite_links (Rewrite links from sub_host?) ['n']: y
  Enter password (The password for the deliverance admin console) ['']: admin
  Enter theme_url (A URL to pull the initial theme from (optional)) ['']:
    :
    :
  Creating .\Deliv1\theme
  Creating .\Deliv1\theme/theme.html
  Creating .\Deliv1\theme\style.css

とりあえずここで何も考えずに Deliverance を起動してみます。

::

  $ deliverance-proxy Deliv1/etc/deliverance.xml
  To see logging, visit http://localhost:8000/.deliverance/login
      after login go to http://localhost:8000/?deliv_log
  serving on http://127.0.0.1:8000


Deliveranceが http://localhost:8000/ で起動しました。
先のテンプレ作成時に proxy_url に http://twitter.com/ を指定していたので、ブラウザで http://localhost:8000/ にアクセスするとtwitterサイトが表示されるはずです。
この状態のままthemeファイルや変換ルールを変更して、ブラウザをリロードすることで少しずつ表示を変えることが出来ます。


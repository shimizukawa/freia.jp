:date: 2009-09-05 15:19:55
:categories: ['python']
:body type: text/x-rst

==================================================================
2009/09/05 buildoutで開発 番外編2: buildoutでDeliverance環境を作る
==================================================================

*Category: 'python'*

`Zope/Plone勉強会3`_ でDeliverance環境を作った手順をまとめてみました。
とりあえず環境を作りたい！という人向け。

ちなみにDeliveranceについては以下を参照ください。

- `Deliveranceとは - CMSコミュニケーションズ[Zope/Plone]`_
- `Getting All Your Web Apps To Wear The Company Brand (JP)`_ (日本語)
- `Deliverance v0.3 documentation`_

環境を作る
------------

とりあえずVirtualEnv環境を作ります。PythonとVirtualEnvは入っている前提で。

.. topic:: virtualenv & install
  :class: dos

  | > cd c:/project/buildout
  | > virtualenv deliv
  | > cd deliv
  | > bin/activate
  | > easy_install zc.buildout
  | > mkdir deliv1
  | > cd deliv1



deliv1フォルダにbuildout.cfgを書きます::

    [buildout]
    parts = deliverance

    # mr.developer
    extensions = mr.developer
    sources = sources
    auto-checkout = deliverance

    [deliverance]
    recipe = zc.recipe.egg
    eggs =
        deliverance
        PasteScript
        PasteDeploy

    [sources]
    deliverance = svn http://codespeak.net/svn/z3/deliverance/trunk


buildoutを実行します。

.. topic:: buildout
    :class: dos

    | > buildout
    | ...
    | Installing deliverance.
    | Generated script '..deliv1\\bin\\deliverance-proxy'.
    | Generated script '..deliv1\\bin\\deliverance-speed'.
    | Generated script '..deliv1\\bin\\deliverance-static'.
    | Generated script '..deliv1\\bin\\deliverance-handtransform'.
    | Generated script '..deliv1\\bin\\deliverance-tests'.
    | Generated script '..deliv1\\bin\\paster'.


Deliveranceの設定ファイル等をPasterで自動生成します。

.. topic:: paster crate --list-templates
    :class: dos

    | > bin/paster.exe create --list-templates
    | Available templates:
    |   basic_package:      A basic setuptools-enabled package
    |   deliverance:        Basic template for a deliverance-proxy setup
    |   deliverance_plone:  Plone-specific template for deliverance-proxy
    |   paste_deploy:       A web application deployed through paste.deploy

.. topic:: paster create -t deliverance
    :class: dos

    | > bin/paster.exe create -t deliverance
    | Selected and implied templates:
    |   deliverance#deliverance  Basic template for a deliverance-proxy setup
    |
    | Enter project name: DelivTest
    | Variables:
    |   egg:      DelivTest
    |   package:  delivtest
    |   project:  DelivTest
    | Enter host (The host/port to serve on) ['localhost:8000']:
    | Enter proxy_url (The main site to connect/proxy to) ['http://localhost:8080']:
    | Enter proxy_rewrite_links (Rewrite links from sub_host?) ['n']:
    | Enter password (The password for the deliverance admin console) ['']: admin
    | Enter theme_url (A URL to pull the initial theme from (optional)) ['']: theme
    | Creating template deliverance
    | Creating directory .\\DelivTest
    | ...


できました。現時点のファイル構成::

  c:\\Project\\buildout\\deliv\
    +--bin
    |  +-- deliverance-handtransform-script.py
    |  +-- deliverance-handtransform.exe
    |  +-- deliverance-proxy-script.py
    |  +-- deliverance-proxy.exe
    |  +-- deliverance-speed-script.py
    |  +-- deliverance-speed.exe
    |  +-- deliverance-static-script.py
    |  +-- deliverance-static.exe
    |  +-- deliverance-tests-script.py
    |  +-- deliverance-tests.exe
    |  +-- develop-script.py
    |  +-- develop.exe
    |  +-- paster-script.py
    |  +-- paster.exe
    |
    +--DelivTest
    |  +--etc
    |  |  +-- deliv-users.htpasswd
    |  |  +-- deliverance.xml
    |  |  +-- supervisor.d
    |  |  +-- supervisord.conf
    |  +--logs
    |  +--theme
    |  |  +-- style.css
    |  |  +-- theme.html
    |  +--var
    |
    +--develop-eggs
    +--parts
    +--src
        +--deliverance
            + deliveranceのソースコード


**【注意】ここで、Windowsの人はDeliveranceの不具合修正が必要かも.** `ここからパッチを取得してください`_


Deliveranceを設定する
-----------------------

Deliveranceのコンフィグファイル ``DelivTest/etc/deliverance.xml``
をちょっと書き換えます。

1. htpasswd形式のファイルがめんどくさいので、管理画面のID/PWを直接指定します
2. proxy先をgoogleにしてみます
3. rule設定として、styleを全部削除してみます

deliverance.xml::

  <ruleset>
    <server-settings>
      <server>localhost:8000</server>
      <execute-pyref>true</execute-pyref>
      <dev-allow>127.0.0.1</dev-allow>
      <dev-user username="admin" password="admin" />
    </server-settings>
  
    <proxy path="/_theme">
      <dest href="{here}/../theme" />
    </proxy>
  
    <proxy path="/">
      <dest href="http://www.google.co.jp" />
    </proxy>
  
    <theme href="/_theme/theme.html" />
  
    <rule>
      <drop content="//head/style" />
      <replace content="children:body" theme="children:#content" nocontent="abort" />
    </rule>
  </ruleset>


実行
------

起動します。

.. topic:: deliverance-proxy.exe etc/deliverance.xml
    :class: dos

    | > pwd
    | c:\Project\buildout\deliv\deliv1\DelivTest
    |
    | > ../bin/deliverance-proxy.exe etc/deliverance.xml
    | To see logging, visit http://localhost:8000/.deliverance/login
    |     after login go to http://localhost:8000/?deliv_log
    | serving on http://localhost:8000


ブラウザで ``http://localhost:8000/`` にアクセスすると、
へんなGoogleの画面になるはず。

あとはtheme.htmlの書き方とか、ruleの書き方を勉強してカスタマイズするべし。

- `Deliverance v0.3 documentation`_
- `Deliverance Configuration`_

.. _`Deliverance v0.3 documentation`: http://deliverance.openplans.org/index.html
.. _`Deliverance Configuration`: http://deliverance.openplans.org/configuration.html
.. _`Zope/Plone勉強会3`: http://zope.jp/events/zope-plone-sprint-tokyo-3/
.. _`Deliveranceとは - CMSコミュニケーションズ[Zope/Plone]`: http://www.cmscom.jp/blog/232
.. _`Getting All Your Web Apps To Wear The Company Brand (JP)`: http://www.slideshare.net/knappt/getting-all-your-web-apps-to-wear-the-company-brand-jp
.. _`ここからパッチを取得してください`: https://projects.openplans.org/deliverance/ticket/13 


.. :extend type: text/html
.. :extend:

:date: 2009-11-24 21:35:00
:categories: ['Zope', 'Plone']
:body type: text/x-rst

===============================================
2009/11/24 Plone-3.3.2 にアップグレードして公開
===============================================

一つ前のエントリ `清水川Webを Plone-2.5.2-1 から Plone-3.3.2 にアップグレード`_ の手順ほぼそのままでアップグレードがうまくいったので、今朝方切り替えました。とりあえず見た目はなんにも変わりませんが、そのへんはそのうち。

.. _`清水川Webを Plone-2.5.2-1 から Plone-3.3.2 にアップグレード`: 685


続きは以下から。


.. :extend type: text/x-rst
.. :extend:

移行後の後始末
----------------------

起動中に PlacelessTranslationService が以下のようなメッセージを表示する::

   2009-11-23 13:39:23 INFO PlacelessTranslationService You have a stale entry for 'Products.CacheSetup' in your ZMI Products section.You should consider removing it.

既に削除されたプロダクトがZMIのControl_panel/Productsに残っているので、手動で削除する。今回の対象は以下の通り::

   CMFContentPanels
   CMFContentPanelsCB2Viewlet
   CMFSquidTool
   CacheSetup
   CallProfiler
   DDocument
   ExtImageDirective
   FCKeditor
   Hotfix_20060705
   Hotfix_20070320
   MJSplitter
   PloneErrorReporting
   PloneHotfix20060410
   PloneHotfix20060518
   PloneJSOrder
   PloneSVNView
   PloneTranslations
   VerboseSecurity
   WingDBG
   ZWeatherApplet
   ZopeTutorial


portal_skinsに残ってしまっている古いProductのskinを削除
-------------------------------------------------------

Ploneのページを表示するとコンソールに以下のように表示される::

   Products/CMFCore/DirectoryView.py:497: UserWarning:
   DirectoryView contentpanels refers to a non-existing path
   'Products.CMFContentPanels:skins/contentpanels'

同様に表示されれる以下のフォルダをportal_skinsから削除::

   'Products.CMFContentPanels:skins/contentpanels'
   'Products.CMFContentPanels:skins/cp_viewlets'
   'Products.CMFContentPanelsCB2Viewlet:skins/cp_cb2_viewlets'
   'PloneErrorReporting/skins/plone_error_reporting'


実行中に表示されるerrorを修正する
----------------------------------

CMFContentPanelsやPloneSVNViewをアンインストールせずに削除したため、portal_typesなどに情報が残っている。これを削除。
今回は portal_types にあった以下のフォルダを削除した::

   ContentPanels
   SVN View

また、portal_quickinstallerにある削除したはずのプロダクトを手動削除した::

   CMFContentPanels
   CMFContentPanelsCB2Viewlet
   PloneErrorReporting
   PloneJSOrder
   PloneSVNView


この流れで、 portal_javascripts と portal_css を確認したところ、リソースが無くなっている項目がいくつかあったので、手動削除した。


使われてないと思われるプロダクトを削除
---------------------------------------

ZMIのfindタブを使えば、特定のコンテンツタイプがDB内に存在するか調べることが出来る(一部例外あり)。これで例えばCOREBlogは全部COREBlog2に移行済みのはずだけど残ってないかな？といった状況で探すことが出来る。

今回探したもの::

   COREBlog           -> 実験用オブジェクト有り
   ATExtFlash         -> 無し
   CMFDynamicDocument -> 無し
   SilverCityDocument -> 無し
   ZAmazon            -> 実験用オブジェクト有り

しかし、上記で「無し」になっているインスタンスは実在しているのに、なぜか検索に出てこない。Zopeのdebugコンソールで起動してオブジェクト種別で検索する方法もあるけど、今回は1,2カ所くらいでしか使用していないことが分かっているので手動で対応した。

::

   COREBlog           -> 実験用オブジェクト有り -> 削除
   ATExtFlash         -> 無し -> 実際は有り -> そのまま使用
   CMFDynamicDocument -> 無し -> 実際は有り -> 削除
   SilverCityDocument -> 無し -> 実際は有り -> 削除
   ZAmazon            -> 実験用オブジェクト有り -> 削除


あと ejSplitter は以前 CJKSplitter に移行していたので、 portal_catalog の indexes で ZCTextIndex で参照されていないことを確認した上でcontentsタブでlexiconを削除。

最後にプロダクトを削除::

   $ sudo -u www rm -Rf CMFDynamicDocument
   $ sudo -u www rm -Rf FSCounter
   $ sudo -u www rm -Rf SilverCityDocument
   $ sudo -u www rm -Rf ZAmazon
   $ sudo -u www rm -Rf ejSplitter


products内の古いプロダクトをbuildoutへの記載に移行してupgradeする
--------------------------------------------------------------------------

いくつかのプロダクトがPyPIで提供されているので、buildout.cfgに記載しproductsから削除してバージョンアップすることにする。
目的のプロダクトがPyPIで提供されているかどうかを調べるためには http://pypi.python.org/simple/ を見表示してブラウザの検索機能を使うと早い。

:ATAlbumViewEx:
   Ploneのサムネイル表示で画像をlightbox表示するプロダクト。
   PyPIの Products.PloneSlimbox に移行。

:LDAPMultiPlugins:
   PyPIの Products.LDAPMultiPlugins に移行。

:LDAPUserFolder:
   PyPIの Products.LDAPUserFolder に移行。

:jaMailHost:
   とりあえずjaMailHostは削除。smtpにGMailを使用しているが問題なさそう。
   PyPIの c2.patch.plone3mail を使うべきか要検討。


上記を行う前に、LDAP認証関連が含まれているので、念のため Data.fs をpackしてバックアップしておいた。

Zopeを停止して、 buildout.cfg の eggs に以下を追記::

   eggs =
       Products.LDAPMultiPlugins
       Products.LDAPUserFolder
       Products.PloneSlimbox

移行したプロダクトを削除、 bin/buildout 実行、起動::

   $ cd products
   $ sudo -u www rm -Rf LDAPMultiPlugins
   $ sudo -u www rm -Rf LDAPUserFolder
   $ cd ..
   $ sudo -u www -H bin/buildout -v
   $ sudo -u www -H bin/instance fg

実はbuildout中に python-ldap-2.3.10 のビルド中に `LDAP_OPT_X_TLS_NEWCTX の問題`_ で止まってしまったけど、ググってコード書き換えてeggを手動で作成して解決したりなどした。

.. _`LDAP_OPT_X_TLS_NEWCTX の問題`: http://www.mail-archive.com/python-ldap-dev@lists.sourceforge.net/msg00717.html


もしかしたら役に立つかも知れない情報１
------------------------------------------

このサイトで使用していたプロダクトのバージョン

========================== ============ ============= ========================
Product name               Plone-2.5.2  Plone-3.3.2   Plone-3.3.2
========================== ============ ============= ========================
ATAlbumViewEx              0.2.1        ->            -> PloneSlimbox へ移行
ATBookshelf                0.0.2        ->            自作:どうしよう
ATExtFlash                 0.1          ->            自作:要Plone3対応
AdvancedQuery              0.6          plone include
CJKSplitter                0.7.3        ->            ->
CMFContentPanels           2.3          removed       removed
CMFContentPanelsCB2Viewlet svn          removed       removed
CMFDynamicDocument         1.1.2        ->            removed
COREBlog                   1.21         removed       removed
COREBlog2                  0.9b         9.83b         ->
CallProfiler               1.4(w/fixes) removed       removed
FSCounter                  1.4.0        ->            removed
Hotfix_20070320            20070320     removed       removed
ImageTag_CorePatch         0.3          ->            (need remove)
LDAPMultiPlugins           1.1          ->            pypi 1.8
LDAPUserFolder             2.6          ->            pypi 2.13
LocalFS                    1.7-andreas  ->            ->
MultiPatch                 2005/2/20    ->            (need modify)
MyScriptModules            2007/2/25    ->            (need modify)
PloneSlimbox               x            x             0.6
PloneFlashUpload           x            x             1.3b1
QuickImporter              0.2          ->            ->
SilverCityDocument         0.0.5        ->            removed
WingDBG                    WingIDE2.0.2 removed       removed
ZAmazon                    0.1          ->            removed
ZSilverCity                0.2-mod      ->            ->
ZWeatherApplet             1.51         removed       removed
ZWiki                      0.47.0       ->            (need update)
ZrstAmazon                 0.0.1        ->            自作:このまま
ZrstIFrame                 0.1          ->            自作:このまま
ejSplitter                 0.5.0        ->            removed
jaMailHost                 0.4.4        ->            removed
========================== ============ ============= ========================



もしかしたら役に立つかも知れない情報２
------------------------------------------

このサイトの環境を用意する ``buildout.cfg`` ::

  [buildout]
  parts =
      zope2
      productdistros
      instance
      zeoserver
      zopepy
  
  # Change the number here to change the version of Plone being used
  extends = http://dist.plone.org/release/3.3.2/versions.cfg
  versions = versions
  
  # Add additional egg download sources here. dist.plone.org contains archives
  # of Plone packages.
  find-links =
      http://dist.plone.org/release/3.3.2
      http://download.zope.org/ppix/
      http://download.zope.org/distribution/
      http://effbot.org/downloads
  
  # Add additional eggs here
  eggs =
      Products.LDAPMultiPlugins
      Products.LDAPUserFolder
      Products.PloneFlashUpload
      Products.PloneSlimbox
      Products.LinguaPlone
  
  # Reference any eggs you are developing here, one per line
  # e.g.: develop = src/my.package
  develop =
  
  
  
  [settings]
  effective-user = www
  http-port = 8180
  zeo-port = 8181
  initial-user = admin:admin
  
  
  
  [zope2]
  # For more information on this step and configuration options see:
  # http://pypi.python.org/pypi/plone.recipe.zope2install
  recipe = plone.recipe.zope2install
  fake-zope-eggs = true
  additional-fake-eggs =
      ZODB3
  url = ${versions:zope2-url}
  location = /usr/local/www/Zope210
  
  
  # Use this section to download additional old-style products.
  # List any number of URLs for product tarballs under URLs (separate
  # with whitespace, or break over several lines, with subsequent lines
  # indented). If any archives contain several products inside a top-level
  # directory, list the archive file name (i.e. the last part of the URL,
  # normally with a .tar.gz suffix or similar) under 'nested-packages'.
  # If any archives extract to a product directory with a version suffix, list
  # the archive name under 'version-suffix-packages'.
  [productdistros]
  # For more information on this step and configuration options see:
  # http://pypi.python.org/pypi/plone.recipe.distros
  recipe = plone.recipe.distros
  urls =
  nested-packages =
  version-suffix-packages =
  
  [instance]
  # For more information on this step and configuration options see:
  # http://pypi.python.org/pypi/plone.recipe.zope2instance
  recipe = plone.recipe.zope2instance
  zope2-location = ${zope2:location}
  user = ${settings:initial-user}
  http-address = ${settings:http-port}
  
  # If you want Zope to know about any additional eggs, list them here.
  # This should include any development eggs you listed in develop-eggs above,
  # e.g. eggs = Plone my.package
  eggs =
      Plone
      ${buildout:eggs}
      
  
  # If you want to register ZCML slugs for any packages, list them here.
  # e.g. zcml = my.package my.other.package
  zcml =
  
  products =
      ${buildout:directory}/products
      ${productdistros:location}
  
  effective-user = ${settings:effective-user}
  
  # for zeo
  zeo-client = true
  zeo-address = ${zeoserver:zeo-address}
  zeo-client-cache-size = 300MB
  
  zodb-temporary-storage =
      <zodb_db temporary>
        <zeoclient>
          server ${zeoserver:zeo-address}
          storage temp
          name zeostorage
          var ${buildout:directory}/var/filestorage
        </zeoclient>
        mount-point /temp_folder
        container-class Products.TemporaryFolder.TemporaryContainer
      </zodb_db>
  
  
  [zeoserver]
  recipe = plone.recipe.zope2zeoserver
  zope2-location = ${zope2:location}
  eggs = ${buildout:eggs}
  effective-user = ${settings:effective-user}
  zeo-address = 127.0.0.1:${settings:zeo-port}
  zeo-conf-additional =
       %import tempstorage
       <temporarystorage temp>
           name temp storage for sessioning
       </temporarystorage>
  
  
  [zopepy]
  # For more information on this step and configuration options see:
  # http://pypi.python.org/pypi/zc.recipe.egg
  recipe = zc.recipe.egg
  eggs = ${instance:eggs}
  interpreter = zopepy
  extra-paths = ${zope2:location}/lib/python
  scripts = zopepy



移行後のデザイン適用
-------------------------

* Plone3.3の流儀でheader/footer/cssのデザイン適用をやりなおした
* COREBlog2のportletをクラシックポートレットとして手動で適用
* エレメントの構成が一部変わっていたのでcssを数カ所修正


今後の作業
--------------

いくつかの問題を修正しなくてはいけない。

* COREBlog2のカレンダー表示が月変更出来ない
* ZWikiページが見れない
* 本棚ページの詳細が見れない
* ATExtFlashをPlone3対応しないといけない

あとは未来への展望

* Deliveranceかcollective.xdvでデザイン適用する
* plone.app.blob 導入で高速化(?)
* CacheFo 導入で高速化
* Vernish 導入で高速化


.. :comments:
.. :comment id: 2009-12-03.4889273535
.. :title: Re:Plone-3.3.2 にアップグレードして公開
.. :author: akiko
.. :date: 2009-12-03 08:44:50
.. :email: akiko@kk.iij4u.or.jp
.. :url: 
.. :body:
..  清水川さま、こんにちは。 
.. Ploneに関わってから、ずっとこちらを参考にさせていただいております。 
.. Ploneのアップグレードの記事も、大変参考になります。ありがとうございます。 
.. ※コメントのテスト用に再度投稿させていただきます。
.. （不要でしたら、削除いただければ幸いです）
.. 
.. 実は、今朝同僚のCOREBlog2のデータを移行したのですが、やはりカレンダーが前後に切り替わってくれません。 
.. 私自身の分は、先行してテストしていたんですが、 Plone3.2, Plone3.3でも動かない状態です。 
.. instance.log に、DEBUGの情報が出ているので、このあたりなんだろうな....とは思っていますが、手が出せません(^^; 
.. -------------- 
.. 2009-11-27T10:11:02 INFO Plone Debug: The getPreviousMonth script is deprecated and will be removed in Plone 4.0. Use the getPreviousMonth method of the @@calendar_view view instead. 
.. -------------- 
.. 
.. Plone3は、インストーラーにまかせて作ってしまい、buildoutのこととかまったく理解していなかったので、意外に苦労しています。
.. 今の環境を、ちゃんと理解したうえで作り直したいと思っているので、buildoutの設定なども、大変参考になりました。
.. 
.. 
.. なお、varnishはわたしも入れてみました。
.. でも、なにやらイタズラもあって、一筋縄ではいきません...。
.. 

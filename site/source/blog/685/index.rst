:date: 2009-11-23 02:10:30
:categories: ['Plone']
:body type: text/x-rst

======================================================================
2009/11/23 清水川Webを Plone-2.5.2-1 から Plone-3.3.2 にアップグレード
======================================================================

このサイトの Plone を `Plone 2.5.2-1` から `Plone 3.3` にアップグレードしようと先月からチャレンジしていましたが、ついに成功したのでその手順を深い考察などせずにそのまんま公開します。「すくなくともうちのサイトはこれでうまくいきました」的な内容なので、もしかしたら、あんまり役に立たないかも知れません。

なお、まだ「試行錯誤した結果うまくいった」状態で、デザインなどもリセットしてしまったので、本インスタンスにアップグレードを適用してサイト公開するのはもうちょっと先になりそうです。

詳細は以下の通り。


.. :extend type: text/x-rst
.. :extend:

Zope 2.9.7 -> 2.10.9
---------------------
Plone3系にするにはZope-2.10.xが必要なので、先にZope本体のバージョンを上げておく。

from::

        Plone 2.5.2,
        CMF-1.6.2,
        Zope (Zope 2.9.7-final, python 2.4.4, freebsd7),
        Five 1.3.8,
        Python 2.4.4 (#2, Oct 26 2008, 05:45:29) [GCC 4.2.1 20070719 [FreeBSD]],
        PIL 1.1.6

to::

        Plone 2.5.2,
        CMF-1.6.2,
        Zope (Zope 2.10.9-final, python 2.4.4, freebsd7),
        Five 1.5.6,
        Python 2.4.4 (#2, Oct 26 2008, 05:45:29) [GCC 4.2.1 20070719 [FreeBSD]],
        PIL 1.1.6


Plone 2.5.2-1 -> 2.5.5
-----------------------

なんにも問題無かったはず。省略して 2.5.2 -> 3.1.7 にしても良いかも。


Plone 2.5.5 -> 3.1.7
---------------------

Plone3系にアップグレード。Plone-3.2系はtgzパッケージ配布からbuildoutに切り替わっているので、tgzパッケージでアップグレードできるのは3.1.7まで。とりあえずここまでは従来のアップグレード手順で上げてしまうことにする。

ProductsをPlone-3.1.7に更新して起動すると、importエラーがたくさん発生する。
ここでこのエラーに対応するため、Plone以外に入れているプロダクトのソースコード改造を実施。

* 複数のプロダクトで、 ``Products.CMFCore.CMFCorePermissions`` が見つからないエラーがボロボロと出てきたので、 Products.CMFCore.permissions に置き換えた。こんなかんじ::

   -from Products.CMFCore.CMFCorePermissions import View,ListFolderContents,\
   +from Products.CMFCore.permissions import View,ListFolderContents,\


* ``Products.CMFCore.WorkflowCore.WorkflowAction`` が見つからない。使わないように改造してみた::

   -from TAL.TALDefs import TALESError
   +#from TAL.TALDefs import TALESError
   +from zope.tal.taldefs import TALExpressionError as TALESError
    from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl
    from Products.CMFCore.PortalContent import PortalContent
   -from Products.CMFCore.PortalContent import NoWL, ResourceLockedError
   -from Products.CMFCore.WorkflowCore import WorkflowAction
   +from Products.CMFCore.PortalContent import ResourceLockedError
   +NoWL = 0

   そして実際にWorkflowActionを使ってる行で...

   -    setFormat = WorkflowAction(setFormat)
   +    #setFormat = WorkflowAction(setFormat)

   これは移行後にどうするか考えよう...


* Products.PluggableAuthService.utils.implementedBy が無い::

   -from Products.PluggableAuthService.utils import implementedBy
   +from zope.interface import implementedBy   


起動できるようになったので portal_migration をdry-runすると、なんか `PT:Document` がアップグレード出来ないと言われる::

   2009-11-22 21:24:50 INFO Plone
   Attempting to upgrade from: 2.5.5
   2009-11-22 21:24:50 ERROR Plone
   Upgrade aborted
   2009-11-22 21:24:50 ERROR Plone
   Error type: zExceptions.BadRequest
   2009-11-22 21:24:50 ERROR Plone
   Error value: The id "PT:Document" contains characters illegal in URLs.
   2009-11-22 21:24:50 ERROR Plone
     File "/usr/local/www/ZFreia_taka/Plone-3.1.7/Products/CMFPlone/MigrationTool.py", line 210, in upgrade
       newv, msgs = self._upgrade(newv)

   2009-11-22 21:24:50 ERROR Plone
     File "/usr/local/www/ZFreia_taka/Plone-3.1.7/Products/CMFPlone/MigrationTool.py", line 321, in _upgrade
       res = function(self.aq_parent)

   2009-11-22 21:24:50 ERROR Plone
     File "/usr/local/www/ZFreia_taka/Plone-3.1.7/Products/CMFPlone/migrations/v3_0/alphas.py", line 100, in three0_alpha1
       migrateOldActions(portal, out)

   2009-11-22 21:24:50 ERROR Plone
     File "/usr/local/www/ZFreia_taka/Plone-3.1.7/Products/CMFPlone/migrations/v3_0/alphas.py", line 425, in migrateOldActions
       portal.portal_actions._setObject(category, ActionCategory(id=category))

   2009-11-22 21:24:50 ERROR Plone
     File "/usr/local/www/Zope210/lib/python/OFS/ObjectManager.py", line 315, in _setObject
       v = self._checkId(id)

   2009-11-22 21:24:50 ERROR Plone
     File "/usr/local/www/Zope210/lib/python/OFS/ObjectManager.py", line 83, in checkValidId
       raise BadRequest, (

   2009-11-22 21:24:50 INFO Plone
   End of upgrade path, migration has finished
   2009-11-22 21:24:50 ERROR Plone
   The upgrade path did NOT reach current version
   2009-11-22 21:24:50 ERROR Plone
   Migration has failed
   2009-11-22 21:24:50 INFO Plone
   Dry run selected, transaction aborted

そこで、portal_contentpanelsをuninstallしようとしたらそれもエラーになったので、まあいいや、と思ってportal/portal_contentpanelsを削除。本番では事前にCMFContentPanelsをアンインストールしておきたい。改めてdry-runを実行したところうまくいったっぽい::

   Plone Migration Tool at  /freia/taka/portal_migration
   Result of the attempt...

   Dry run selected.
   Starting the migration from version: 2.5.5
   Attempting to upgrade from: 2.5.5
   Registered tools as utilities.
   Migrated old actions to new actions stored in portal_actions.
   Added navtree.css to the registry
   Added invisibles.css to the registry
   Added forms.css to the registry
   Added 'default_contenttype' property to site_properties.
   Added 'forbidden_contenttypes' property to site_properties.
   Added Markup Settings to the control panel
   Added markup configlet icon to actionicons tool.
   Updated actions i18n domain attribute.
   Updated type informations i18n domain attribute.
   Upgraded the ATContentTypes tool.
   Installed CMFDiffTool.
   Installed CMFEditions.
   Converted legacy portlets at the portal root
   NOTE: You may need to convert other portlets manually.
   - to do so, click "manage portlets" in the relevant folder.
   Added 'calendar' icon to actionicons tool.
   Added calendar settings to the control panel
   Removed the Plone Tableless skin
   Upgrade to: 3.0-alpha1, completed
   Attempting to upgrade from: 3.0-alpha1
   Registered tools as utilities.
   Removed generated.css from the registry
   Added form_tabbing.js to portal_javascipt
   Registered kss mimetype
   Registered kss resources
   Added missing skins to Plone Default
   Succesfully migrated portal to KSS
   Registered redirector utility
   Added content rules action to object category
   Added reader and editor roles
   Ensured references to folder_localrole_form point to @@sharing now
   Updated RTL.css expression.
   Upgrade to: 3.0-alpha2, completed
   Attempting to upgrade from: 3.0-alpha2
   Registered tools as utilities.
   Added 'Maintenance' to the control panel
   Added 'maintenance' icon to actionicons tool.
   Added 'number_of_days_to_keep' property to site properties
   Added 's5_presentation' action to actions tool.
   Added 's5_presentation' icon to actionicons tool.
   Added in css and js for table of contents
   Added input-label.js to portal_javascipt
   Updated member management security
   Added Plone Session Plugin.
   Added 'filter' icon to actionicons tool.
   Added 'security' icon to actionicons tool.
   Registered content rules storage utility
   Added 'Content Rules Settings' to the control panel
   Added 'Content Rules Settings' icon to actionicons tool.
   Added html filter settings to the control panel
   Added security settings to the control panel
   Added 'enable_sitemap' property to site properties
   Use ++resource++kukit-src.js instead of ++resource++kukit.js
   Set 'full' compression on ++resource++kukit-src.js
   Created RAMCache ResourceRegistryCache for ResourceRegistry output
   Associated portal_css with ResourceRegistryCache
   Associated portal_javascripts with ResourceRegistryCache
   Set 'full-encode' compression on cssQuery.js
   Removed folder_contents_hideAddItems.js from portal_javascripts.
   Added webstats.js to portal_javascipts
   Added 'webstats_js' property to site properties
   Added object_provides index to portal_catalog
   Removed the mystuff user action
   Added 'external_links_open_new_window' property to site properties
   Added Types Settings to the control panel
   Added types configlet icon to actionicons tool.
   Added workflow intranet_workflow
   Added workflow intranet_folder_workflow
   Added workflow one_state_workflow
   Added workflow simple_publication_workflow
   Added 'many_groups' property to site properties
   Replaced obsolete PlonePAS version of plone tool with the normal one.
   Registered plone.app.i18n utilities.
   Installed PloneLanguageTool.
   Added 'email_charset' property to the portal.
   Upgrade to: 3.0-beta1, completed
   Attempting to upgrade from: 3.0-beta1
   Registered tools as utilities.
   Changed the order of action providers.
   Added unlockOnFormUnload.js to portal_javascripts
   Removed object_tabs action category.
   Removed global action category.
   Removed empty default_charset portal property
   Added automatic group PAS plugin
   Removed 's5_presentation' action from actions tool.
   Removed 's5_presentation' icon from actionicons tool.
   Associated portal_kss with ResourceRegistryCache
   Updated kss javascript resource ++resource++kukit-src.js, to disable kss for anonymous.
   Added kss resource at_experimental.kss, disabled by default.
   Added kss resource plone_experimental.kss, disabled by default.
   Removed properties action from type CMF Image
   Removed properties action from type CMF Document
   Removed properties action from type CMF Favorite
   Removed properties action from type CMF Link
   Removed properties action from type CMF News Item
   Removed properties action from type CMF File
   Removed properties action from type Wiki Page
   Removed properties action from type SilverCityDocument
   Removed properties action from type ATBookshelfItem
   Removed properties action from type ATBookshelf
   Removed properties action from type DynamicDocument
   Removed properties action from type ContentPanels
   Removed properties action from type ATExtFlash
   Removed properties action from type COREBlog2
   Removed properties action from type COREBlogComment
   Removed properties action from type COREBlogTrackback
   Removed properties action from type COREBlogCommentFolder
   Removed properties action from type COREBlogCategory
   Removed properties action from type COREBlogCategoryFolder
   Removed properties action from type COREBlogEntry
   Removed properties action from type ATPathCriterion
   Removed properties action from type ATBooleanCriterion
   Removed properties action from type Image
   Removed properties action from type Topic
   Removed properties action from type ATSelectionCriterion
   Removed properties action from type Large Plone Folder
   Removed properties action from type Document
   Removed properties action from type ATSimpleStringCriterion
   Removed properties action from type ATCurrentAuthorCriterion
   Removed properties action from type ATDateCriteria
   Removed properties action from type Favorite
   Removed properties action from type Event
   Removed properties action from type ATReferenceCriterion
   Removed properties action from type ATSimpleIntCriterion
   Removed properties action from type ATListCriterion
   Removed properties action from type Folder
   Removed properties action from type Link
   Removed properties action from type News Item
   Removed properties action from type File
   Removed properties action from type ATDateRangeCriterion
   Removed properties action from type ATSortCriterion
   Removed properties action from type ATRelativePathCriterion
   Removed properties action from type ATPortalTypeCriterion
   Upgrade to: 3.0-beta2, completed
   Attempting to upgrade from: 3.0-beta2
   Registered tools as utilities.
   Removed explicit references to sharing action
   Upgrade to: 3.0-beta3, completed
   Attempting to upgrade from: 3.0-beta3
   Registered tools as utilities.
   Updated kss javascript resources, to enable the use of production and development versions.
   Upgrade to: 3.0-rc1, completed
   Attempting to upgrade from: 3.0-rc1
   Added text_web_intelligent mime type to registry
   Added intelligenttext to html transform to registry
   Added html to intelligenttext transform to registry
   Upgrade to: 3.0-rc2, completed
   Attempting to upgrade from: 3.0-rc2
   Upgrade to: 3.0, completed
   Attempting to upgrade from: 3.0
   Upgrade to: 3.0.1, completed
   Attempting to upgrade from: 3.0.1
   Upgrade to: 3.0.2, completed
   Attempting to upgrade from: 3.0.2
   Upgrade to: 3.0.3, completed
   Attempting to upgrade from: 3.0.3
   Added new CMFEditions modifiers
   Upgrade to: 3.0.4, completed
   Attempting to upgrade from: 3.0.4
   Registered tools as utilities.
   Upgrade to: 3.0.5, completed
   Attempting to upgrade from: 3.0.5
   Upgrade to: 3.0.6, completed
   Attempting to upgrade from: 3.0.6
   Installed plone.browserlayer
   Installed plone.portlet.static
   Installed plone.portlet.collection
   Migrated portlet types to support multiple portlet manager interfaces.
   Removed doubly registered GenericSetup import steps: toolset rolemap componentregistry
   Removed doubly registered GenericSetup export steps: componentregistry step_registries rolemap toolset
   Reinstalled CMFPlacefulWorkflow
   Deactivated original 'local_roles' plugin
   - Activating: local_roles borg_localroles activated.
   Upgrade to: 3.1-beta1, completed
   Attempting to upgrade from: 3.1-beta1
   Upgrade to: 3.1-rc1, completed
   Attempting to upgrade from: 3.1-rc1
   Upgrade to: 3.1, completed
   Attempting to upgrade from: 3.1
   Upgrade to: 3.1.1, completed
   Attempting to upgrade from: 3.1.1
   Upgrade to: 3.1.2, completed
   Attempting to upgrade from: 3.1.2
   Upgrade to: 3.1.3, completed
   Attempting to upgrade from: 3.1.3
   Upgrade to: 3.1.4, completed
   Attempting to upgrade from: 3.1.4
   Upgrade to: 3.1.5, completed
   Attempting to upgrade from: 3.1.5
   Upgrade to: 3.1.5.1, completed
   Attempting to upgrade from: 3.1.5.1
   Upgrade to: 3.1.6, completed
   Attempting to upgrade from: 3.1.6
   Upgrade to: 3.1.7, completed
   Attempting to upgrade from: 3.1.7
   Migration completed at version 3.1.7.
   End of upgrade path, migration has finished
   Your ZODB and Filesystem Plone instances are now up-to-date.
   Dry run selected, transaction aborted
   Return

最後に aborted になっているのはdry-runをしたため。それでは改めて本実行::


   Plone Migration Tool at  /freia/taka/portal_migration
   Result of the attempt...

   Starting the migration from version: 2.5.5
   Attempting to upgrade from: 2.5.5
   Registered tools as utilities.
   Migrated old actions to new actions stored in portal_actions.
   Added navtree.css to the registry
   Added invisibles.css to the registry
   Added forms.css to the registry
   Added 'default_contenttype' property to site_properties.
   Added 'forbidden_contenttypes' property to site_properties.
   Added Markup Settings to the control panel
   Added markup configlet icon to actionicons tool.
   Updated actions i18n domain attribute.
   Updated type informations i18n domain attribute.
   Upgraded the ATContentTypes tool.
   Installed CMFDiffTool.
   Installed CMFEditions.
   Converted legacy portlets at the portal root
   NOTE: You may need to convert other portlets manually.
   - to do so, click "manage portlets" in the relevant folder.
   Added 'calendar' icon to actionicons tool.
   Added calendar settings to the control panel
   Removed the Plone Tableless skin
   Upgrade to: 3.0-alpha1, completed
   Attempting to upgrade from: 3.0-alpha1
   Registered tools as utilities.
   Removed generated.css from the registry
   Added form_tabbing.js to portal_javascipt
   Registered kss mimetype
   Registered kss resources
   Added missing skins to Plone Default
   Succesfully migrated portal to KSS
   Registered redirector utility
   Added content rules action to object category
   Added reader and editor roles
   Ensured references to folder_localrole_form point to @@sharing now
   Updated RTL.css expression.
   Upgrade to: 3.0-alpha2, completed
   Attempting to upgrade from: 3.0-alpha2
   Registered tools as utilities.
   Added 'Maintenance' to the control panel
   Added 'maintenance' icon to actionicons tool.
   Added 'number_of_days_to_keep' property to site properties
   Added 's5_presentation' action to actions tool.
   Added 's5_presentation' icon to actionicons tool.
   Added in css and js for table of contents
   Added input-label.js to portal_javascipt
   Updated member management security
   Added Plone Session Plugin.
   Added 'filter' icon to actionicons tool.
   Added 'security' icon to actionicons tool.
   Registered content rules storage utility
   Added 'Content Rules Settings' to the control panel
   Added 'Content Rules Settings' icon to actionicons tool.
   Added html filter settings to the control panel
   Added security settings to the control panel
   Added 'enable_sitemap' property to site properties
   Use ++resource++kukit-src.js instead of ++resource++kukit.js
   Set 'full' compression on ++resource++kukit-src.js
   Created RAMCache ResourceRegistryCache for ResourceRegistry output
   Associated portal_css with ResourceRegistryCache
   Associated portal_javascripts with ResourceRegistryCache
   Set 'full-encode' compression on cssQuery.js
   Removed folder_contents_hideAddItems.js from portal_javascripts.
   Added webstats.js to portal_javascipts
   Added 'webstats_js' property to site properties
   Added object_provides index to portal_catalog
   Removed the mystuff user action
   Added 'external_links_open_new_window' property to site properties
   Added Types Settings to the control panel
   Added types configlet icon to actionicons tool.
   Added workflow intranet_workflow
   Added workflow intranet_folder_workflow
   Added workflow one_state_workflow
   Added workflow simple_publication_workflow
   Added 'many_groups' property to site properties
   Replaced obsolete PlonePAS version of plone tool with the normal one.
   Registered plone.app.i18n utilities.
   Installed PloneLanguageTool.
   Added 'email_charset' property to the portal.
   Upgrade to: 3.0-beta1, completed
   Attempting to upgrade from: 3.0-beta1
   Registered tools as utilities.
   Changed the order of action providers.
   Added unlockOnFormUnload.js to portal_javascripts
   Removed object_tabs action category.
   Removed global action category.
   Removed empty default_charset portal property
   Added automatic group PAS plugin
   Removed 's5_presentation' action from actions tool.
   Removed 's5_presentation' icon from actionicons tool.
   Associated portal_kss with ResourceRegistryCache
   Updated kss javascript resource ++resource++kukit-src.js, to disable kss for anonymous.
   Added kss resource at_experimental.kss, disabled by default.
   Added kss resource plone_experimental.kss, disabled by default.
   Removed properties action from type CMF Image
   Removed properties action from type CMF Document
   Removed properties action from type CMF Favorite
   Removed properties action from type CMF Link
   Removed properties action from type CMF News Item
   Removed properties action from type CMF File
   Removed properties action from type Wiki Page
   Removed properties action from type SilverCityDocument
   Removed properties action from type ATBookshelfItem
   Removed properties action from type ATBookshelf
   Removed properties action from type DynamicDocument
   Removed properties action from type ContentPanels
   Removed properties action from type ATExtFlash
   Removed properties action from type COREBlog2
   Removed properties action from type COREBlogComment
   Removed properties action from type COREBlogTrackback
   Removed properties action from type COREBlogCommentFolder
   Removed properties action from type COREBlogCategory
   Removed properties action from type COREBlogCategoryFolder
   Removed properties action from type COREBlogEntry
   Removed properties action from type ATPathCriterion
   Removed properties action from type ATBooleanCriterion
   Removed properties action from type Image
   Removed properties action from type Topic
   Removed properties action from type ATSelectionCriterion
   Removed properties action from type Large Plone Folder
   Removed properties action from type Document
   Removed properties action from type ATSimpleStringCriterion
   Removed properties action from type ATCurrentAuthorCriterion
   Removed properties action from type ATDateCriteria
   Removed properties action from type Favorite
   Removed properties action from type Event
   Removed properties action from type ATReferenceCriterion
   Removed properties action from type ATSimpleIntCriterion
   Removed properties action from type ATListCriterion
   Removed properties action from type Folder
   Removed properties action from type Link
   Removed properties action from type News Item
   Removed properties action from type File
   Removed properties action from type ATDateRangeCriterion
   Removed properties action from type ATSortCriterion
   Removed properties action from type ATRelativePathCriterion
   Removed properties action from type ATPortalTypeCriterion
   Upgrade to: 3.0-beta2, completed
   Attempting to upgrade from: 3.0-beta2
   Registered tools as utilities.
   Removed explicit references to sharing action
   Upgrade to: 3.0-beta3, completed
   Attempting to upgrade from: 3.0-beta3
   Registered tools as utilities.
   Updated kss javascript resources, to enable the use of production and development versions.
   Upgrade to: 3.0-rc1, completed
   Attempting to upgrade from: 3.0-rc1
   Added text_web_intelligent mime type to registry
   Added intelligenttext to html transform to registry
   Added html to intelligenttext transform to registry
   Upgrade to: 3.0-rc2, completed
   Attempting to upgrade from: 3.0-rc2
   Upgrade to: 3.0, completed
   Attempting to upgrade from: 3.0
   Upgrade to: 3.0.1, completed
   Attempting to upgrade from: 3.0.1
   Upgrade to: 3.0.2, completed
   Attempting to upgrade from: 3.0.2
   Upgrade to: 3.0.3, completed
   Attempting to upgrade from: 3.0.3
   Added new CMFEditions modifiers
   Upgrade to: 3.0.4, completed
   Attempting to upgrade from: 3.0.4
   Registered tools as utilities.
   Upgrade to: 3.0.5, completed
   Attempting to upgrade from: 3.0.5
   Upgrade to: 3.0.6, completed
   Attempting to upgrade from: 3.0.6
   Installed plone.browserlayer
   Installed plone.portlet.static
   Installed plone.portlet.collection
   Migrated portlet types to support multiple portlet manager interfaces.
   Removed doubly registered GenericSetup import steps: toolset rolemap componentregistry
   Removed doubly registered GenericSetup export steps: componentregistry step_registries rolemap toolset
   Reinstalled CMFPlacefulWorkflow
   Deactivated original 'local_roles' plugin
   - Activating: local_roles borg_localroles activated.
   Upgrade to: 3.1-beta1, completed
   Attempting to upgrade from: 3.1-beta1
   Upgrade to: 3.1-rc1, completed
   Attempting to upgrade from: 3.1-rc1
   Upgrade to: 3.1, completed
   Attempting to upgrade from: 3.1
   Upgrade to: 3.1.1, completed
   Attempting to upgrade from: 3.1.1
   Upgrade to: 3.1.2, completed
   Attempting to upgrade from: 3.1.2
   Upgrade to: 3.1.3, completed
   Attempting to upgrade from: 3.1.3
   Upgrade to: 3.1.4, completed
   Attempting to upgrade from: 3.1.4
   Upgrade to: 3.1.5, completed
   Attempting to upgrade from: 3.1.5
   Upgrade to: 3.1.5.1, completed
   Attempting to upgrade from: 3.1.5.1
   Upgrade to: 3.1.6, completed
   Attempting to upgrade from: 3.1.6
   Upgrade to: 3.1.7, completed
   Attempting to upgrade from: 3.1.7
   Migration completed at version 3.1.7.
   End of upgrade path, migration has finished
   Your ZODB and Filesystem Plone instances are now up-to-date.

うぉ、成功した！
しかしPloneのViewで表示しようとしたらエラー::

   2009-11-22 21:38:13 ERROR Zope.SiteErrorLog 1258893493.510.109067702822 http://192.168.1.2:8980/freia/taka/folder_listing
   Traceback (innermost last):
     Module ZPublisher.Publish, line 119, in publish
     Module ZPublisher.mapply, line 88, in mapply
     Module ZPublisher.Publish, line 42, in call_object
     Module Shared.DC.Scripts.Bindings, line 313, in __call__
     Module Shared.DC.Scripts.Bindings, line 350, in _bindAndExec
     Module Products.CMFCore.FSPageTemplate, line 216, in _exec
     Module Products.CMFCore.FSPageTemplate, line 155, in pt_render
     Module Products.PageTemplates.PageTemplate, line 98, in pt_render
     Module zope.pagetemplate.pagetemplate, line 117, in pt_render
      - Warning: Macro expansion failed
      - Warning: exceptions.KeyError: 'kss_generic_macros'
     Module zope.tal.talinterpreter, line 271, in __call__
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 891, in do_useMacro
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 536, in do_optTag_tal
     Module zope.tal.talinterpreter, line 521, in do_optTag
     Module zope.tal.talinterpreter, line 516, in no_tag
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 957, in do_defineSlot
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 536, in do_optTag_tal
     Module zope.tal.talinterpreter, line 521, in do_optTag
     Module zope.tal.talinterpreter, line 516, in no_tag
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 861, in do_defineMacro
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 957, in do_defineSlot
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 536, in do_optTag_tal
     Module zope.tal.talinterpreter, line 521, in do_optTag
     Module zope.tal.talinterpreter, line 516, in no_tag
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 536, in do_optTag_tal
     Module zope.tal.talinterpreter, line 525, in do_optTag
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 949, in do_defineSlot
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 861, in do_defineMacro
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 536, in do_optTag_tal
     Module zope.tal.talinterpreter, line 521, in do_optTag
     Module zope.tal.talinterpreter, line 516, in no_tag
     Module zope.tal.talinterpreter, line 346, in interpret
     Module zope.tal.talinterpreter, line 870, in do_useMacro
     Module zope.tales.tales, line 696, in evaluate
      - URL: file:/usr/local/www/ZFreia_taka/Plone-3.1.7/Products/CMFPlone/skins/plone_content/folder_listing.pt
      - Line 19, Column 8
      - Expression: <PathExpr standard:u'here/kss_generic_macros/macros/generic_title_view'>
      - Names:
         {'container': <PloneSite at /freia/taka>,
          'context': <PloneSite at /freia/taka>,
          'default': <object object at 0x80110f200>,
          'here': <PloneSite at /freia/taka>,
          'loop': {},
          'nothing': None,
          'options': {'args': ()},
          'repeat': <Products.PageTemplates.Expressions.SafeMapping object at 0x81433eea8>,
          'request': <HTTPRequest, URL=http://192.168.1.2:8980/freia/taka/folder_listing>,
          'root': <Application at >,
          'template': <FSPageTemplate at /freia/taka/folder_listing>,
          'traverse_subpath': [],
          'user': <PloneUser 'taka'>}
     Module zope.tales.expressions, line 217, in __call__
     Module Products.PageTemplates.Expressions, line 155, in _eval
     Module zope.tales.expressions, line 124, in _eval
     Module Products.PageTemplates.Expressions, line 82, in boboAwareZopeTraverse
     Module OFS.Traversable, line 301, in restrictedTraverse
     Module OFS.Traversable, line 284, in unrestrictedTraverse
      - __traceback_info__: ([], 'kss_generic_macros')
   KeyError: 'kss_generic_macros'

kss_generic_macros が無いというようなエラーが出ているけど、まじめに追いかけると時間がかかりそう。多分デザインカスタマイズしてるどこかがまずいんだろうと当たりを付けて、portal_skinsのプロパティーでPloneDefaultにskinを切り替え。これでPloneサイトを表示出来るようになった。デザインカスタマイズを別名で作っておいてよかったー。

Plone-3.1.7 -> 3.3.1
---------------------

3.1.7がとりあえず動いてるっぽいので、そのまま3.3.1へUpgradeを進める。Plone-3.2以降にするにはbuildout化したほうが今後のためにも良いので、 plone.jp や takanory.net などを参考に、buildoutでのインストール、ZopeSkelを使ったPlone3をセットアップする方法などを練習しておく。十分理解できたので本番更新に着手。

まず3.3.1用に新しいディレクトリを作成。そこにZopeSkelで作っておいたbuildout.cfgとbootstrap.pyを持って行く。

buildout.cfg::

   [buildout]
   parts =
       zope2
       productdistros
       instance
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

   # Reference any eggs you are developing here, one per line
   # e.g.: develop = src/my.package
   develop =


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
   user = admin:admin
   http-address = 8980

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

   [zopepy]
   # For more information on this step and configuration options see:
   # http://pypi.python.org/pypi/zc.recipe.egg
   recipe = zc.recipe.egg
   eggs = ${instance:eggs}
   interpreter = zopepy
   extra-paths = ${zope2:location}/lib/python
   scripts = zopepy

書き換えた箇所は、ploneのバージョン値を3.3.1から3.3.2にしたくらい。

buildout実行::

   $ sudo -u www -H python bootstrap.py
   $ sudo -u www -H bin/buildout -v

既存のProductsを移行::

   $ sudo -u www mkdir products
   $ sudo -u www cp -R ../old/Products/* products

移行しなくて良さそうなプロダクトを削除::

   $ sudo -u www rm -Rf products/AdvancedQuery
   $ sudo -u www rm -Rf products/CallProfiler
   $ sudo -u www rm -Rf products/Hotfix_20070320
   $ sudo -u www rm -Rf products/WingDBG

既存のvarを移行::

   $ sudo -u www cp ../old/var/Data.fs var/filestorage/
   $ sudo -u www cp ../old/var/counter* var/filestorage/

起動::

   $ sudo -u www -H bin/instance fg


ここでエラーが発生。

エラー１: pymeterが無い -> 呼出元を削除::

   $ sudo -u www rm -Rf Products/ZWeatherApplet

エラー２: .python-egg/ を作れない::

   The following error occurred while trying to extract file(s) to the Python egg
   cache:

     [Errno 13] Permission denied: '/nonexistent'

   The Python egg cache directory is currently set to:

     /nonexistent/.python-eggs

   Perhaps your account does not have write access to this directory?  You can
   change the cache directory by setting the PYTHON_EGG_CACHE environment
   variable to point to an accessible directory.

自分の環境(FreeBSD)のwwwはHOMEが/nonexistentだったので、これをvipwコマンドで/usr/local/wwwに変更。対応方法としてPYTHON_EGG_CACHE環境変数を使う方法もあるけど、rc.dで起動する時のことを考えて...いやrc.dでの起動スクリプトに環境変数設定すればいいのか？まあいいや。

HOME=/usr/local/www/ でここにwwwが書き込み権限のある状態にして再度起動::

   $ sudo -u www -H bin/instance fg


起動したのでmigration実行. 3.1.7 -> 3.3.2 ::

   Plone Migration Tool at  /freia/taka/portal_migration
   Result of the attempt...

   Dry run selected.
   Starting the migration from version: 3.1.7
   Attempting to upgrade from: 3.1.7
   Upgrade to: 3.2a1, completed
   Attempting to upgrade from: 3.2a1
   Upgrade to: 3.2rc1, completed
   Attempting to upgrade from: 3.2rc1
   Upgrade to: 3.2, completed
   Attempting to upgrade from: 3.2
   Upgrade to: 3.2.1, completed
   Attempting to upgrade from: 3.2.1
   Upgrade to: 3.2.2, completed
   Attempting to upgrade from: 3.2.2
   Upgrade to: 3.2.3, completed
   Attempting to upgrade from: 3.2.3
   Upgrade to: 3.3b1, completed
   Attempting to upgrade from: 3.3b1
   Upgrade to: 3.3rc1, completed
   Attempting to upgrade from: 3.3rc1
   Upgrade to: 3.3rc2, completed
   Attempting to upgrade from: 3.3rc2
   Upgrade to: 3.3rc3, completed
   Attempting to upgrade from: 3.3rc3
   Upgrade aborted
   Error type: exceptions.AttributeError
   Error value: 'NoneType' object has no attribute 'strip'
   File "/var2/www/ZFreia_taka/eggs/Plone-3.3.2-py2.4.egg/Products/CMFPlone/MigrationTool.py", line 210, in upgrade newv, msgs = self._upgrade(newv)
   File "/var2/www/ZFreia_taka/eggs/Plone-3.3.2-py2.4.egg/Products/CMFPlone/MigrationTool.py", line 321, in _upgrade res = function(self.aq_parent)
   File "/var2/www/ZFreia_taka/eggs/Plone-3.3.2-py2.4.egg/Products/CMFPlone/migrations/v3_3/__init__.py", line 12, in three3_rc3_three3_rc4 cookCSSRegistries(portal)
   File "/var2/www/ZFreia_taka/eggs/Plone-3.3.2-py2.4.egg/Products/CMFPlone/migrations/v3_3/__init__.py", line 25, in cookCSSRegistries resource.getCookedExpression()
   File "/var2/www/ZFreia_taka/eggs/Products.ResourceRegistries-1.5.3-py2.4.egg/Products/ResourceRegistries/tools/BaseRegistry.py", line 115, in getCookedExpression expr = Expression(self._data['expression'])
   File "/var2/www/ZFreia_taka/eggs/Products.CMFCore-2.1.2-py2.4.egg/Products/CMFCore/Expression.py", line 37, in __init__ if text.strip():
   End of upgrade path, migration has finished
   The upgrade path did NOT reach current version
   Migration has failed
   Dry run selected, transaction aborted

またエラー！

今度のエラーはResourceRegistries関連らしい。これはResourceRegistries/tools/BaseRegistryのgetCookedExpressionメソッド実装を見ないと分からない。

BaseRegistry.py の getCookedExpression::

    security.declarePublic('getCookedExpression')
    def getCookedExpression(self):
        # Automatic inline migration of expressions
        if 'cooked_expression' not in self._data:
            expr = Expression(self._data['expression'])
            self._data['cooked_expression'] = expr
        return self._data['cooked_expression']

これを見ると self._data['expression'] が None を返しているために Expression クラスインスタンスの作成で失敗しているようだ。じゃあ self._data['expression'] のデフォルト値は何が適切かというと、 BaseRegistry.py の __init__ を見る限り、以下のように''で良いらしい::

    def __init__(self, id, **kwargs):
        self._data = PersistentMapping()
        ...
        expression = kwargs.get('expression', '')
        self.setExpression(expression)

ということで、115行目を以下のように書き換えてマイグレーションすることにした::

    def getCookedExpression(self):
        # Automatic inline migration of expressions
        if 'cooked_expression' not in self._data:
            self.setExpression(self._data['expression'] or '')
        return self._data['cooked_expression']


再起動してもっかいマイグレーション(dry-run)::


   Plone Migration Tool at  /freia/taka/portal_migration
   Result of the attempt...

   Dry run selected.
   Starting the migration from version: 3.1.7
   Attempting to upgrade from: 3.1.7
   Upgrade to: 3.2a1, completed
   Attempting to upgrade from: 3.2a1
   Upgrade to: 3.2rc1, completed
   Attempting to upgrade from: 3.2rc1
   Upgrade to: 3.2, completed
   Attempting to upgrade from: 3.2
   Upgrade to: 3.2.1, completed
   Attempting to upgrade from: 3.2.1
   Upgrade to: 3.2.2, completed
   Attempting to upgrade from: 3.2.2
   Upgrade to: 3.2.3, completed
   Attempting to upgrade from: 3.2.3
   Upgrade to: 3.3b1, completed
   Attempting to upgrade from: 3.3b1
   Upgrade to: 3.3rc1, completed
   Attempting to upgrade from: 3.3rc1
   Upgrade to: 3.3rc2, completed
   Attempting to upgrade from: 3.3rc2
   Upgrade to: 3.3rc3, completed
   Attempting to upgrade from: 3.3rc3
   Upgrade to: 3.3rc4, completed
   Attempting to upgrade from: 3.3rc4
   Upgrade to: 3.3rc5, completed
   Attempting to upgrade from: 3.3rc5
   Upgrade to: 3.3, completed
   Attempting to upgrade from: 3.3
   Upgrade to: 3.3.1, completed
   Attempting to upgrade from: 3.3.1
   Upgrade to: 3.3.2, completed
   Attempting to upgrade from: 3.3.2
   Migration completed at version 3.3.2.
   End of upgrade path, migration has finished
   Your ZODB and Filesystem Plone instances are now up-to-date.
   Dry run selected, transaction aborted


成功した！本実行::

   Plone Migration Tool at  /freia/taka/portal_migration
   Result of the attempt...

   Starting the migration from version: 3.1.7
   Attempting to upgrade from: 3.1.7
   Upgrade to: 3.2a1, completed
   Attempting to upgrade from: 3.2a1
   Upgrade to: 3.2rc1, completed
   Attempting to upgrade from: 3.2rc1
   Upgrade to: 3.2, completed
   Attempting to upgrade from: 3.2
   Upgrade to: 3.2.1, completed
   Attempting to upgrade from: 3.2.1
   Upgrade to: 3.2.2, completed
   Attempting to upgrade from: 3.2.2
   Upgrade to: 3.2.3, completed
   Attempting to upgrade from: 3.2.3
   Upgrade to: 3.3b1, completed
   Attempting to upgrade from: 3.3b1
   Upgrade to: 3.3rc1, completed
   Attempting to upgrade from: 3.3rc1
   Upgrade to: 3.3rc2, completed
   Attempting to upgrade from: 3.3rc2
   Upgrade to: 3.3rc3, completed
   Attempting to upgrade from: 3.3rc3
   Upgrade to: 3.3rc4, completed
   Attempting to upgrade from: 3.3rc4
   Upgrade to: 3.3rc5, completed
   Attempting to upgrade from: 3.3rc5
   Upgrade to: 3.3, completed
   Attempting to upgrade from: 3.3
   Upgrade to: 3.3.1, completed
   Attempting to upgrade from: 3.3.1
   Upgrade to: 3.3.2, completed
   Attempting to upgrade from: 3.3.2
   Migration completed at version 3.3.2.
   End of upgrade path, migration has finished
   Your ZODB and Filesystem Plone instances are now up-to-date.

成功！

サイト設定画面の表示::

   Plone 3.3.2
   CMF 2.1.2
   Zope (Zope 2.10.9-final, python 2.4.4, freebsd7)
   Python 2.4.4 (#2, Oct 26 2008, 05:45:29) [GCC 4.2.1 20070719 [FreeBSD]]
   PIL 1.1.6



まとめ
--------

* 使っていないプロダクトはアップグレード前に外しておく
   * CMFContentPanels (Plone3系で非対応? 要アップグレード前アンインストール)
   * AdvancedQuery (Plone本体に入ってた)
   * CallProfiler (本番環境にはいらない)
   * WingDBG (本番環境にはいらない)
   * ZWeatherApplet (以前 COREBlog1と連携して使っていた)
* 残すプロダクトは必要に応じてソース改造が必要(import元の変更など)
* カスタマイズしたskinは一度捨てる方向で(楽なので).
* Products.ResourceRegistries/tools/BaseRegistryの改造が必要.

* 残件、次の作業
   * productsにコピーした古いプロダクトをbuildoutへの記載に移行してupgradeする
   * 不要になったProductsを削除して/Control_Panel/Productsから削除する



.. :comments:
.. :comment id: 2010-03-23.4837853974
.. :title: Re:清水川Webを Plone-2.5.2-1 から Plone-3.3.2 にアップグレード
.. :author: marcellobs
.. :date: 2010-03-23 23:28:04
.. :email: mbsalgueiro@linuxmail.org
.. :url: www.tranqueira.net/weblog
.. :body:
.. Hi, thanks for the post, this post help me with migration from plone 3.0.6 to 3.3.4 and work fine
.. for me this tick! =)
.. This is a bug from portal_migration!? Did you ask this for plone developer community??
.. 
.. thanks,
.. 
.. Marcello.
.. 
.. :comments:
.. :comment id: 2010-03-24.6510330749
.. :title: Re:清水川Webを Plone-2.5.2-1 から Plone-3.3.2 にアップグレード
.. :author: shimizukawa
.. :date: 2010-03-24 02:00:51
.. :email: 
.. :url: 
.. :body:
.. It's happy that my article was helpful for you :-)
.. 
.. > This is a bug from portal_migration!?
.. 
.. Probably, Expression class doesn't assume None value.
.. (not a portal_migration's bug)
.. 
.. > Did you ask this for plone developer community??
.. 
.. No, I didn't do it.
.. 
.. 
.. 報告する時間が欲しい...

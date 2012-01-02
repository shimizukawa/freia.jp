:date: 2005-11-30 23:02:12
:categories: ['Plone']
:body type: text/x-rst

=====================================
2005/11/30 Plone2.1.1のフォルダで写真
=====================================

*Category: 'Plone'*

aihatenaの猫を世話することに‥‥ってこれも9月の写真。ヨドバシ秋葉オープンの翌日だったかな。

ZPhotoSlidesを改良して使うよりもPlone2.1系のフォルダを使った方が問題が少なそうだったので乗り換えてみました。ZPhotoSlidesから乗り換えて良くなった点と悪くなった点があるけど、標準フォルダ機能だと考えると良くできていると思う。少なくとも、自分の使い方の範囲では乗り換えに耐えられる。

良くなった点
------------
- WebDAVやFTPで一気にアップロード出来る
- メモリリークが起きない
- Plone2.1の作法で作られているのでカスタマイズがしやすい

悪くなった点
------------
- ZODBの外に保存できない
- 概要や名前の修正を一つ一つやるのがめんどくさい(フォルダViewからは出来ない)
- 多くの機能が減った(スライドショーとか)が、もともと使わないので...

変わらない点
-------------
- 写真の並び替えが大変

ATFolderで写真、の先人の方々
---------------------------

- `plone 2.1 の「写真アルバム」ビューは結構いいかも — takanory.net`_
- `Plone 2.1のアルバムビューをカスタマイズ — Central Core : coreblog.org`_

.. _`plone 2.1 の「写真アルバム」ビューは結構いいかも — takanory.net`: http://takanory.net/takalog/374
.. _`Plone 2.1のアルバムビューをカスタマイズ — Central Core : coreblog.org`: http://coreblog.org/ats/customizing-plone-album-view


.. :extend type: text/x-rst
.. :extend:
ZPhotoSlidesからATFolderへ変換
------------------------------
以下はPlone2.1.1上でZPhotoSlidesからATFolder/ATImageに変換した時に使ったスクリプト。
一応必要そうなデータは変換できるはず。でもプロパティーとかに値が設定してある場合はそれも変換するコードを追加しないといけない。使い方は省略する方向で。

.. code-block:: python

    ## Script (Python) "folder_converter"
    ##bind container=container
    ##bind context=context
    ##bind namespace=
    ##bind script=script
    ##bind subpath=traverse_subpath
    ##parameters=src, dest
    ##title=

    request = container.REQUEST
    
    def convert_image(src_obj, dest_container):
        id = callable(src_obj.id) and src_obj.id() or src_obj.id
        dest_container.invokeFactory(type_name='Image', id=id)
        obj = dest_container[id]
    
        kwargs = {
            'title': src_obj.title,
            'content_type': src_obj.content_type,
            'precondition':'',
            'filedata':src_obj.data,
        }
    
        obj.manage_edit(**kwargs)
        obj.setDescription(src_obj.description)
    
        print id, 'converted.'
        return printed
    
    def convert_atfolder(src_obj, dest_container):
        id = callable(src_obj.id) and src_obj.id() or src_obj.id
        dest_container.manage_addFolder(id, src_obj.title)
        obj = dest_container[id]
        print "'%s'" % src_obj.Description(),
        obj.setDescription( src_obj.Description() )
        obj.indexObject()
        print 'converted.'
        print convert_folder(src_obj, obj)
        return printed
    
    def convert_folder(src_container, dest_container):
    
        for obj in src_container.objectValues():
            id = callable(obj.id) and obj.id() or obj.id
            print 'converting.. ', id, "(%s)" % obj.meta_type,
    
            if obj.meta_type in ('ATFolder',):
                print convert_atfolder(obj, dest_container)
    
            elif obj.meta_type in ('CMF ZPhoto','ZPhoto',):
                print convert_image(obj, dest_container),
    
            elif obj.meta_type in ('CMF ZPhotoSlides',
                                   'CMF ZPhotoSlides Folder',
                                   'ZPhotoSlides',
                                   'ZPhotoSlides Folder',):
                dest_container.manage_addFolder(id, obj.title)
                sub_dest = dest_container[id]
                sub_dest.setDescription( obj.description )
                sub_dest.indexObject()
                print 'converted.'
                print convert_folder(obj, sub_dest)
    
            else: # copy for unknown
                o = src_container.manage_copyObjects(id)
                dest_container.manage_pasteObjects(o)
                dest_container[id].indexObject()
                print '%s copied.' % id
    
        return printed
    
    print 'make "%s"' % dest
    src_container =  container[src]
    container.manage_addFolder(dest)
    dest_container = container[dest]
    dest_container.setDescription( src_container.Description() )
    print convert_folder(src_container, dest_container),
    
    print 'done'
    return printed

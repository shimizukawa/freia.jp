## Script (Python) "folder_converter"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=src, dest
##title=
##
request = container.REQUEST

def convert_ddocument(src_obj, dest_container):
    id = callable(src_obj.id) and src_obj.id() or src_obj.id
    dest_container.invokeFactory(type_name='Document', id=id)
    obj = dest_container[id]

    obj.setDescription(src_obj.Description())
    obj.setTitle(src_obj.Title())
    obj.setText(src_obj.text)
    obj.setFormat(src_obj.Format())
    obj.indexObject()

    print id, 'converted.'
    return printed


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

def convert_atfile(src_obj, dest_container):
    id = callable(src_obj.id) and src_obj.id() or src_obj.id
    dest_container.invokeFactory(type_name='File', id=id)
    obj = dest_container[id]

    kwargs = {
        'title': src_obj.title,
        'content_type': src_obj.content_type,
        'precondition':'',
        'filedata':src_obj.data,
    }

    obj.manage_edit(**kwargs)

    obj.setDescription(src_obj.Description())
    #obj.setTitle(src_obj.Title())
    #obj.setFormat(src_obj.Format())
    obj.indexObject()

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

def convert_atlink(src_obj, dest_container):
    id = callable(src_obj.id) and src_obj.id() or src_obj.id
    dest_container.invokeFactory(type_name='Link', id=id)
    obj = dest_container[id]
    obj.setTitle(src_obj.Title())
    obj.setDescription( src_obj.Description() )
    obj.indexObject()
    print 'converted.'
    return printed

def convert_atdocument(src_obj, dest_container):
    id = callable(src_obj.id) and src_obj.id() or src_obj.id
    dest_container.invokeFactory(type_name='Document', id=id)
    obj = dest_container[id]
    obj.setTitle(src_obj.Title())
    obj.setDescription( src_obj.Description() )
    obj.setFormat(src_obj.Format())
    obj.setText(src_obj.getRawText())
    obj.indexObject()
    print 'converted.'
    return printed

def convert_folder(src_container, dest_container):

    for obj in src_container.objectValues():
        id = callable(obj.id) and obj.id() or obj.id
        print 'converting.. ', id, "(%s)" % obj.meta_type,

        if obj.meta_type in ('ATFolder',):
            print convert_atfolder(obj, dest_container)

        elif obj.meta_type in ('CMF ZPhoto','ZPhoto','Image', 'ATImage'):
            print convert_image(obj, dest_container),

        elif obj.meta_type in ('CMF ZPhotoSlides', 'CMF ZPhotoSlides Folder', 'ZPhotoSlides', 'ZPhotoSlides Folder',):
            dest_container.manage_addFolder(id, obj.title)
            sub_dest = dest_container[id]
            sub_dest.setDescription( obj.description )
            sub_dest.indexObject()
            print 'converted.'
            print convert_folder(obj, sub_dest)

        elif obj.meta_type in ('ATFile',):
            print convert_atfile(obj, dest_container)

        elif obj.meta_type in ('ATLink',):
            print convert_atlink(obj, dest_container)

        elif obj.meta_type in ('ATDocument',):
            print convert_atdocument(obj, dest_container)

        elif obj.meta_type in ('DDocument',):
            print convert_ddocument(obj, dest_container)

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

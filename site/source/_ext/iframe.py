import docutils.parsers.rst

def iframe(name, arguments, options, content, lineno,
           content_offset, block_text, state, state_machine):
    """
    The iframe directive for docutils,
    The sintax is following::

    .. iframe:: http://example.jp/iframeurl.html
      :width: 200
      :height: 200

    """
    try:
        src = arguments[0]
    except IndexError:
        src = options['src']

    values = {
        'src': src,
        'width': options.get('width', 200),
        'height': options.get('height', 200),
    }

    html = '<iframe src="%(src)s" frameborder="0" scrolling="no" width="%(width)s" height="%(height)s" marginwidth="0" marginheight="0"></iframe>\n' % values
    raw = docutils.nodes.raw('',html, format = 'html')
    return [raw]

iframe.arguments = (0,2,1)
iframe.options = {'width' : docutils.parsers.rst.directives.unchanged,
                  'height' : docutils.parsers.rst.directives.unchanged,}
iframe.content = 1

def setup(app=None):
    # Simply importing this module will make the directive available.
    docutils.parsers.rst.directives.register_directive( 'iframe', iframe )
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

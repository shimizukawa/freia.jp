import io
import csv


def parse_meta_tags(tags):
    for tags in csv.reader(io.StringIO(tags), skipinitialspace=True):
        return tags


def html_page_context(app, pagename, templatename, context, doctree):
    if not doctree:
        return

    try:
        tags = context['meta']['tags']
    except KeyError:
        pass
    else:
        context['meta']['tags'] = parse_meta_tags(tags)


def setup(app):
    app.connect('html-page-context', html_page_context)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

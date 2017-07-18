# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.abspath('.'), '_ext'))

# -- Extensions -----------------------------------------------------
import sphinx_bootstrap_theme
extensions = [
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.seqdiag',
    'sphinx.ext.todo',
    'iframe',
    'ogtag',
    'sphinxcontrib.feed',
    'sphinx.ext.intersphinx',
]

# for sphinx.ext.todo plugin
todo_include_todos = True

# for tkinter.ext.disqus plugin
#disqus_shortname = 'shimizukawa'

# site url
og_site_url = 'http://www.freia.jp/taka/'
og_twitter_site = '@shimizukawa'

# for sphinxcontrib.feed plugin
feed_title = u"清水川Web"
feed_base_url = 'http://www.freia.jp/taka'
feed_description = u'清水川Webは、Python関連の技術的な事についての個人的メモや、清水川の日々の雑記を公開しています。'
feed_filename = 'rss.xml'
feed_limit = 10

# for intersphinx
intersphinx_mapping = {
   'sphinx': ('http://www.sphinx-doc.org/ja/stable', None),
   'py': ('http://docs.python.jp/2/', None),
   'py2': ('http://docs.python.jp/2/', None),
   'py3': ('http://docs.python.jp/3/', None),
}

# -- General configuration -----------------------------------------------------

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = '清水川Web'
copyright = 'Takayuki SHIMIZUKAWA'
version = release = ''
language = 'ja'
exclude_trees = []
pygments_style = 'sphinx'
# exclude_patterns = ['blog/1*', 'blog/2*', 'blog/3*', 'blog/4*', 'blog/5*', 'blog/6*', 'blog/7*', 'blog/8*', 'blog/9*']


# -- Options for HTML output ---------------------------------------------------
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    'navbar_title': "清水川Web",
    'navbar_sidebarrel': False,
    'navbar_pagenav': False,
    'navbar_fixed_top': "false",
    'source_link_position': "footer",
    'bootswatch_theme': "flatly",
}
html_sidebars = {
    'index': ['relations.html', 'books.html'],
    '**': ['relations.html', 'localtoc.html', 'books.html'],
}

html_title = project
html_static_path = ['_static']
html_use_modindex = False
#html_search_options = {'type': 'sphinx.search.ja.JanomeSplitter'}
html_experimental_html5_writer = True

# -- setup --

from sphinx.environment.adapters.toctree import TocTree


def _get_local_toctree(app, docname, collapse=True, **kwds):
    if 'includehidden' not in kwds:
        kwds['includehidden'] = False
    toctree = TocTree(app.env).get_toctree_for(docname, app.builder, collapse, **kwds)
    return toctree


def add_context(app, pagename, templatename, context, doctree):
    context['toctree_node'] = lambda **kw: _get_local_toctree(app, pagename, **kw)
    context['render_partial'] = app.builder.render_partial


def setup(app):
    app.add_stylesheet('css/freia.css')
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')

    app.connect('html-page-context', add_context)

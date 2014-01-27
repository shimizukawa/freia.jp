# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.abspath('.'), '_ext'))

# -- Extensions -----------------------------------------------------
extensions = [
        'sphinxcontrib.blockdiag',
        'sphinxcontrib.seqdiag',
        'sphinx.ext.todo',
        'iframe',
        #'sphinxfeed',
        'sphinxcontrib.feed',
        #'tinkerer.ext.blog',
        #'tinkerer.ext.disqus',
        'sphinx.ext.intersphinx',
        ]

# for sphinx.ext.todo plugin
todo_include_todos = True

# for tkinter.ext.disqus plugin
#disqus_shortname = 'shimizukawa'

# for sphinxcontrib.feed plugin
feed_title = u"清水川Web"
feed_base_url = 'http://www.freia.jp/taka'
feed_description = u'清水川Webは、Python関連の技術的な事についての個人的メモや、清水川の日々の雑記を公開しています。'
feed_filename = 'rss.xml'
feed_count = 10

# for intersphinx
intersphinx_mapping = {
   'sphinx': ('http://docs.sphinx-users.jp/', None),
   'py': ('http://docs.python.jp/2/', None),
}

# -- General configuration -----------------------------------------------------

templates_path = ['_templates']
source_suffix = '.rst'
#source_encoding = 'utf-8'
master_doc = 'index'
project = u'清水川Web'
copyright = u'Takayuki SHIMIZUKAWA'
version = '1.0'
release = '1.0'
language = 'ja'
#today = ''
#today_fmt = '%B %d, %Y'
#unused_docs = []
exclude_trees = []
#default_role = None
#add_function_parentheses = True
#add_module_names = True
#show_authors = False
pygments_style = 'sphinx'
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------
html_theme = 'LoadFoo'
#html_theme_options = {}
html_theme_path = ['_themes']
html_title = project #If None, it defaults to "<project> v<release> documentation".
#html_short_title = None
#html_logo = None
#html_favicon = None
html_static_path = ['_static']
#html_last_updated_fmt = '%b %d, %Y'
html_use_smartypants = False
#html_sidebars = {}
#html_additional_pages = {}
#html_use_modindex = True
#html_use_index = True
#html_split_index = False
#html_show_sourcelink = True
#html_use_opensearch = ''
#html_file_suffix = ''

# -- Options for LaTeX output --------------------------------------------------
#latex_paper_size = 'letter' #('letter' or 'a4').
#latex_font_size = '10pt' # The font size ('10pt', '11pt' or '12pt').
latex_documents = [
  ('index', 'shimizukawa-web.tex', u'Shimizukawa web',
   u'Takayuki SHIMIZUKAWA', 'manual'),
]
#latex_logo = None
#latex_use_parts = False
#latex_preamble = ''
#latex_appendices = []
#latex_use_modindex = True


# -- Options for Epub output ---------------------------------------------------
epub_title = project
epub_author = u'Takayuki SHIMIZUKAWA'
epub_publisher = u'Takayuki SHIMIZUKAWA'
epub_copyright = u'Takayuki SHIMIZUKAWA'
epub_language = 'ja'
#epub_scheme = ''
#epub_identifier = ''
#epub_uid = ''
#epub_pre_files = []
#epub_post_files = []
#epub_exclude_files = []
epub_tocdepth = 3


# -- setup --

def setup(app):
    app.add_stylesheet('freia.css')
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')

# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.abspath('.'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary']
autosummary_generate = True
master_doc = 'index'

project = u'issue1444'
copyright = u'2014, issue1444'
version = release = 'issue1444'

exclude_patterns = ['_build']

html_theme_options = {
    'collapsiblesidebar': True,
}

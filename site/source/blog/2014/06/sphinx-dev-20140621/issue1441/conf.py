# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath('.'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary']
master_doc = 'index'
project = u'issue1441'
version = release = 'issue1441'

exclude_patterns = ['_build']
html_theme = 'default'

autosummary_generate = True
autodoc_default_flags = ['members']

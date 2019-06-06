# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import os
import sys
from configparser import RawConfigParser
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.abspath('_ext'))

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',    
    'sphinx.ext.intersphinx',
    #'doc_extensions',
    #'sphinx_tabs.tabs',
    #'sphinx-prompt',
    #'recommonmark',
    #'notfound.extension',
]
templates_path = ['_templates']

source_suffix = ['.rst', '.md']

master_doc = 'index'
project = u'Methpype'
copyright = '2019, Life Epigenetics'
author = 'Life Epigenetics'
version = '1.0'
release = version
exclude_patterns = []
default_role = 'obj'
intersphinx_mapping = {
    'python': ('https://python.readthedocs.io/en/latest/', None),
    'sphinx': ('https://sphinx.readthedocs.io/en/latest/', None),
}
htmlhelp_basename = 'MethpypeDoc'
latex_documents = [
    ('index', 'MethpypeDoc.tex', u'Methpype Documentation',
     u'Life Epigenetics', 'manual'),
]
man_pages = [
    ('index', 'methpypedoc', u'Methpype Documentation',
     ['Life Epigenetics'], 1),
]

exclude_patterns = [
    # 'api' # needed for ``make gettext`` to not die.
]

language = 'en'

locale_dirs = [
    'locale/',
]
gettext_compact = False

html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#html_logo = 'img/logo.svg'
#html_theme_options = {
#    'logo_only': True,
#    'display_version': False,
#}

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# Activate autosectionlabel plugin
autosectionlabel_prefix_document = True

# sphinx-notfound-page
# https://github.com/rtfd/sphinx-notfound-page
notfound_context = {
    'title': 'Page Not Found',
    'body': '''
<h1>Page Not Found</h1>
<p>Sorry, we couldn't find that page.</p>
<p>Try using the search box or go to the homepage.</p>
''',
}

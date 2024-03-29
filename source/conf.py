# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# -- Project information -----------------------------------------------------

project = 'OrdinoR'
copyright = '2021, Jing Yang'
author = 'Jing (Roy) Yang'

# The full version, including alpha/beta/rc tags
version = '0.1.0'
release = version


# -- General configuration ---------------------------------------------------
master_doc = 'index'
html_show_sourcelink = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'numpydoc',
    'sphinx_rtd_theme',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_rtd_theme'
html_theme = 'pydata_sphinx_theme'

html_logo = 'ordinor_logo_transparent.png'

html_theme_options = {
    # outlook
    'show_prev_next': False,
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/roy-jingyang/OrdinoR',
            'icon': 'fab fa-github-square',
        }
    ],

    # navigation
    "navigation_with_keys": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------
# numpydoc config options, see
# https://numpydoc.readthedocs.io/en/latest/install.html#sphinx-config-options 
numpydoc_show_class_members = True
numpydoc_show_inherited_class_members = False
numpydoc_use_blockquotes = True

# intersphinx config options, see
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_mapping
intersphinx_mapping = {
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'sklearn': ('http://scikit-learn.org/stable', None),
    'networkx': ('https://networkx.github.io/documentation/stable', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    #'pm4py': ('https://pm4py.fit.fraunhofer.de/static/assets/api/2.0.0/index.html', None)
}

# autodoc config options, see
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'awesome-sphinx'
copyright = '2022, team useblockjs'
author = 'team useblockjs'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_needs',
    'sphinxcontrib.plantuml']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = ['custom.css']


#  NEED CONFIG

needs_id_regex = r'.*'
needs_types = [dict(directive="sw", title="Software", prefix="S_", color="#BFD8D2", style="card"),
           ]


needs_extra_options = [
    'category',
    'sphinx_type',
    'license',
    'monthly',
    'overall',
    'code',
    'pypi',
    'website',
    ]


needs_string_links = {
    # Links to the related github issue
    'links': {
        'regex': r'^(?P<value>.*)$',
        'link_url': '{{value}}',
        'link_name': '{{value}}',
        'options': ['code', 'pypi', 'website']
    }
}
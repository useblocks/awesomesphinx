# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from ast import arg
from datetime import datetime
import os
import sys
from sphinx_needs.api import add_dynamic_function

# Make Python aware of the project config file
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from projects import PROJECT_TAGS

project = 'awesome-sphinx'
copyright = '2022, team useblockjs'
author = 'team useblockjs'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_needs',
    'sphinxcontrib.plantuml',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_awesome_templates']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_context = {
    'project_tags': PROJECT_TAGS
}

#  NEED CONFIG

needs_id_regex = r'.*'
needs_types = [
    dict(directive="sw", title="Software", prefix="S_", color="#BFD8D2", style="card"),
    dict(directive="test", title="test", prefix="S_", color="#BFD8D2", style="card")
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
    'release_date',
    'release_name',
    'release_days',
    'points',
    'code_nice',
    'pypi_nice',
    'website_nice',
    'featured',
    'color',
    'deprecated'
    ]


needs_string_links = {
    # Links to the related github issue
    'links': {
        'regex': r'^(?P<value>.*)$',
        'link_url': '{{value}}',
        'link_name': '{{value}}',
        'options': ['code', 'pypi', 'website']
    },
    'links_nice': {
        'regex': r'^(?P<value>.*)$',
        'link_url': '{{value}}',
        'link_name': 'Link',
        'options': ['code_nice', 'pypi_nice', 'website_nice']
    }
}

# This automatically sets some values for all needs. Mostly dynamic functions
# calls to calucalte some value for needs.
# See https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-global-options
needs_global_options = {
   'collapse': 'True',
   'release_days': ("[[days_since_build('release_date')]]", "type == 'sw'"),
   'points': ("[[points()]]", "type == 'sw'"),
   'code_nice': ("[[copy('code')]]", "type == 'sw'"),
   'pypi_nice': ("[[copy('pypi')]]", "type == 'sw'"),
   'website_nice': ("[[copy('website')]]", "type == 'sw'"),
   'color': [
        ("blue", "sphinx_type=='extension'"),
        ("green", "sphinx_type=='theme'"),
        ("red", "sphinx_type=='other'"),
   ],
   'style': [
        ("awesome_[[copy('color')]]", "type=='sw'"),
   ],
}

needs_variant_options = ["status"]  # Not needed, but workarund to avoid a bug and some warnings

def days_since_build(app, need, needs, *args, **kwargs):
    """
    Calculates the days from now to a given date, which is normally in the past.

    Usage::

        .. need:: My_need
           :date: 2020-09-08T11:05:55.2340Z
           :days: [[days_since_build('date')]]

    """
    date_option = args[0]
    date = need[date_option]
    
    date_obj = datetime.fromisoformat(date)
    delta = datetime.now() - date_obj

    return delta.days

def points(app, need, needs, *args, **kwargs):
    
    
    release_points = 0
    if need['release_days'] is not None and need['release_days'].isdigit():
        release_days = int(need['release_days'])
        
        if release_days < 100:
            release_points = 5
        elif release_days < 200:
            release_points = 4
        elif release_days < 400:
            release_points = 3
        elif release_days < 600:
            release_points = 2
        else:
            release_points = 0
    

    download_points = 0
    if need['monthly'] is not None and need['monthly'].isdigit():
        monthly = int(need['monthly']) 
        if monthly > 50000:
            download_points = 5
        elif monthly > 5000:
            download_points = 4
        elif monthly > 1000:
            download_points = 3
        elif monthly > 500:
            download_points = 2
        elif monthly > 100:
            download_points = 1
        else:
            download_points = 0

    points = release_points + download_points
    return points

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    
    Source: https://ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/
    """
    src = source[0]
    rendered = app.builder.templates.render_string(
        src, app.config.html_context
    )
    source[0] = rendered

def setup(app):
        app.connect("source-read", rstjinja, 50000)
        
        add_dynamic_function(app, days_since_build)
        add_dynamic_function(app, points)
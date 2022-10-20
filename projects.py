"""
Configuration for projects to collect or ignore
"""

# List of classifiers, which are used to identify projects on PYPI.
PROJECT_FILTERS = [
    ['Framework :: Sphinx'],
    ['Framework :: Sphinx :: Extension'],
    ['Framework :: Sphinx :: Theme']
]


# List of projects, which do not have set the above classifiers but shall be
# documented as well.
EXTRA_PROJECTS = [
    'sphinx-copybutton',
    'doxysphinx'
]

# List of of projects, which have set one of the above classifiers, but shall be ignored.
# Mostly because they are not reallyy related to Sphinx or just use Sphinx for documentation.
IGNORE_PROJECTS = [

]

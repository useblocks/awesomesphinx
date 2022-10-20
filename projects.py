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
    'sphinx-test-reports',
    'sphinx-collections',
    'sphinx-preview',
    'sphinx-data-viewer',
    'sphinx-copybutton',
    'doxysphinx',
    'breathe'
]

# List of of projects, which have set one of the above classifiers, but shall be ignored.
# Mostly because they are not reallyy related to Sphinx or just use Sphinx for documentation.
IGNORE_PROJECTS = [

]

# Dict of allowed tags for a project.
# Is used to generate tag specific overviews.
# Key is used for filtering, the value as documentation
PROJECT_TAGS = {
    'needs': 'All Sphinx-Needs related extensions and maybe themes.',
    'image_processing': 'Extensions dealing with images and their presentation.',
    'layout':  'Extension which help to structure your dcument data e.g. by grids or dropdowns.',
    'pdf': 'Extensions which are dealing with PDFs.',
}
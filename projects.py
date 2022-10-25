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
    "ALVEOLUS"
]

# Dict of tags to document.
# Is used to generate tag specific overviews.
# Key is used for filtering, the value as documentation
PROJECT_TAGS = {
    'needs': 'All `Sphinx-Needs <https://www.sphinx-needs.com/>`__ related extensions and maybe themes.',
    'layout':  'Extensions which help to structure your dcument data e.g. by grids or dropdowns.',
    'pdf': 'Extensions which are dealing with PDFs.',
    'hacktoberfest': 'Projects, which are part of the `Hacktoberfest <https://hacktoberfest.com/>`__.',
    'markdown': 'Extensions and tools, which support Markdown in Sphinx projects.',
    'doxygen': 'Doxygen support inside Sphinx.',
    'python': 'Support of the Python programming language',
}

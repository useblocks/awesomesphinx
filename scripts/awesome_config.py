"""
Configuration for the awesomesphinx scripts
"""
import sys
import os

# Make Python aware of the awesom_config file
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from projects import PROJECT_FILTERS, EXTRA_PROJECTS, IGNORE_PROJECTS

# A list of tags, which shall not be set, as they are too commonly used.
PROJECT_IGNORE_TAGS = [
    "sphinxcontrib",
    "sphinx",
    "documentation",
    "sphinx-theme",
    "sphinx-extension",
    "theme",
    "extension",
    "documentation-tool",
    "documentation-generator",
]

##################################################
# PYPI_JSON.PY configs
##################################################
JSON_FILE = 'pypi_data.json'


# Used during development to reduce amount of data to fetch
# Normally a search contains ~600 findings
MAX_DATA = 5000

API_SLEEP = 2  # Wait time for API, if too many requests were made

# Maximum amount of API sleeps in a row, until the loop gets stopped
MAX_API_SLEEPS = 10


# SQL Query for getting downloads numbers
# Add comma separated list of project must be added, e.g. "pytest","sphinx","flask"
# https://packaging.python.org/en/latest/guides/analyzing-pypi-package-downloads/
BIGQUERY_DL_MONTH = """
SELECT COUNT(*) AS num_downloads, project
FROM `bigquery-public-data.pypi.file_downloads`
WHERE file.project in ('{}')
  -- Only query the last X days of history
  AND DATE(timestamp)
    BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
    AND CURRENT_DATE()
GROUP BY `project`
"""

##################################################
# NEEDS_JSON.PY configs
##################################################
PYPI_FILE = 'pypi_gh_data.json'
#PYPI_FILE = 'data/20221024_pypi_data.json'

NEED_FILE = 'awesome.json'

NEED_TYPE = 'sw'

MAX_NEEDS = 5000  # User for  development for faster tests


##################################################
# GITHUB_STATS.PY configs
##################################################
GH_JSON_FILE = 'pypi_gh_data.json'

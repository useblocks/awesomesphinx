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
MAX_DATA = os.environ.get('AWESOMESPHINX_AMOUNT', -1)
if MAX_DATA == -1:
  MAX_DATA = 1000

if MAX_DATA == '' or MAX_DATA is None:
  MAX_DATA == 1000
try: 
  MAX_DATA = int(MAX_DATA)
except ValueError:
  MAX_DATA = 3


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
    BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL {} DAY)
    AND CURRENT_DATE()
GROUP BY `project`
"""

# Amount of days to fetch data from PyPI
BIGQUERY_DAYS = int(os.environ.get('AWESOMESPHINX_DAYS', 30))

##################################################
# GITHUB_STATS.PY configs
##################################################
GH_JSON_FILE = 'pypi_gh_data.json'

GH_RATE_LIMIT_AMOUNT = 6
GH_RATE_LIMIT_WAIT = 600 # in s

GH_WAIT_COUNTER = 3  # Every x requests we make a break
GH_WAIT_DURATION = 3  # in s

##################################################
# NEEDS_JSON.PY configs
##################################################
PYPI_FILE = os.environ.get('AWESOMESPHINX_PYPI_FILE', GH_JSON_FILE) 
if PYPI_FILE is '' or PYPI_FILE is None:
  PYPI_FILE = GH_JSON_FILE

#PYPI_FILE = 'data/20221024_pypi_data.json'

NEED_FILE = 'awesome.json'

NEED_TYPE = 'sw'

MAX_NEEDS = MAX_DATA # Used for development for faster tests




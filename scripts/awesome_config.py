"""
Configuration for the awesomesphinx scripts
"""
import sys
import os

# Make Python aware of the awesom_config file
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from projects import PROJECT_FILTERS, EXTRA_PROJECTS, IGNORE_PROJECTS


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

BIGQUERY_DL_MONTH = """
SELECT COUNT(*) AS num_downloads
FROM `bigquery-public-data.pypi.file_downloads`
WHERE file.project = '{}'
  -- Only query the last 30 days of history
  AND DATE(timestamp)
    BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
    AND CURRENT_DATE()

"""

##################################################
# NEEDS_JSON.PY configs
##################################################
PYPI_FILE = 'data/20221019_pypi_data.json'
NEED_FILE = 'awesome.json'

NEED_TYPE = 'sw'

MAX_NEEDS = 5000  # User for  development for faster tests
"""
Creates a Sphinx-Needs compatilbe needs.json file from data collected by pypi_json.py script
"""

from datetime import datetime
import json
import sys
import os


# Make Python aware of the awesom_config file
sys.path.append(os.path.dirname(__file__))
from awesome_config import *


def classifiers_check(value, classifiers):
    for cl in classifiers:
        if value in cl:
            return True
    return False


print(f'Reading pypi data from {PYPI_FILE}')
with open(PYPI_FILE, 'r') as f:
    pypi_data = json.load(f)


needs = {}

print(f'Constructing data for {len(pypi_data)} needs:', end='')
counter = 0
for name, data in pypi_data.items():
    counter += 1
    if counter >= MAX_NEEDS:
        break
    
    # check  sphinx_type
    sphinx_type = 'other'
    if classifiers_check('Framework :: Sphinx :: Extension', data['info']['classifiers']):
        sphinx_type = 'extension'
    if classifiers_check('Framework :: Sphinx :: Theme', data['info']['classifiers']):
        sphinx_type = 'theme'

    # Check license
    license = data['info']['license']
    if classifiers_check('License :: OSI Approved :: BSD License', data['info']['classifiers']):
        license = "BSD"
    elif classifiers_check('License :: OSI Approved :: MIT License', data['info']['classifiers']):
        license = "MIT"
    elif classifiers_check('GNU General Public License v3', data['info']['classifiers']):
        license = "GPL3"
    elif classifiers_check('GNU General Public License v2', data['info']['classifiers']):
        license = "GPL2"
    elif classifiers_check('Apache Software License', data['info']['classifiers']):
        license = "Apache"

    # If no license was found or it contains a complete license text
    if license == '' or len(license) > 25:
        license = 'other'
      
   
    #stats
    try:
        monthly = data['awesome_stats']['month']
    except KeyError:
        monthly = 0

    try:
        overall = data['awesome_stats']['overall']
    except KeyError:
        overall = 0

    try:
        tags = []
        for tag in data['awesome_stats']['tags']:
            if tag not in PROJECT_IGNORE_TAGS:
                tags.append(tag)
    except KeyError:
        tags = []

    try:
        stars = data['awesome_stats']['stars']
    except KeyError:
        stars = 0

    # urls
    code = ""
    if data['info']['project_urls']:
        code = data['info']['project_urls'].get('Repository', data['info']['project_urls'].get('Code', ''))
    

    #last release
    release_date = '1970-01-01T00:00:01' 
    release_name = None
    for release_name, release in data['releases'].items():
        try:
            if release[0]['upload_time'] > release_date:
                release_date = release[0]['upload_time']
                release_name = release_name
        except Exception:
            pass


    needs[name] = {
        "id": name.upper(),
        #"description": data['info']['description'],
        "package_summary": data['info']['summary'],
        "description": "",
        "title": name,
        "type": NEED_TYPE,
        "sphinx_type": sphinx_type,
        "license": license,
        "monthly": monthly,
        # "overall": overall,  # currently not collected 
        "tags": tags,
        "stars": stars,
        "pypi": data['info']['package_url'],
        "code": code,
        "website": data['info']['home_page'],
        "release_date": release_date,
        "release_name": release_name,
    }
    
    print('.', end='')
print()

needs_data = {
    "created": datetime.now().isoformat(),
    "current_version": "1.0",
    "project": "needs test docs",
    "versions": {
        "1.0": {
            "created": datetime.now().isoformat(),
            "needs": needs
        }
    }
}

print(f'Writing need data to {NEED_FILE}')
with open(NEED_FILE, 'w') as f:
    json.dump(needs_data, f, sort_keys=True, indent=4)

with open(NEED_FILE, 'r') as f:
    need_test = json.load(f)

print(f'Reading back {len(need_test["versions"]["1.0"]["needs"])} needs from {NEED_FILE}')


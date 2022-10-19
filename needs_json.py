"""
Creates a Sphinx-Needs compatilbe needs.json file from data collected by pypi_json.py script
"""

import json

PYPI_FILE = 'data/20221019_pypi_data.json'
NEED_FILE = 'awesome.json'

NEED_TYPE = 'sw'


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
for name, data in pypi_data.items():
    
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
        monthly = None

    try:
        overall = data['awesome_stats']['overall']
    except KeyError:
        overall = None

    # urls
    code = ""
    if data['info']['project_urls']:
        code = data['info']['project_urls'].get('Repository', data['info']['project_urls'].get('Code', ''))
    


    needs[name] = {
        "id": name.upper(),
        #"description": data['info']['description'],
        "description": data['info']['summary'],
        "title": name,
        "type": NEED_TYPE,
        "sphinx_type": sphinx_type,
        "license": license,
        "monthly": monthly,
        "overall": overall,
        "tags": [],
        "pypi": data['info']['package_url'],
        "code": code,
        "website": data['info']['home_page'],
    }
    
    print('.', end='')
print()

needs_data = {
    "created": "2022-10-19T10:00:00.0",
    "current_version": "1.0",
    "project": "needs test docs",
    "versions": {
        "1.0": {
            "created": "2022-10-19T10:00:00.0",
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


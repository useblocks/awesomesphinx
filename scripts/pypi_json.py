"""
Collects Sphinx pakcage data from pypi and pypistats and stores the data in a json file
"""

import json
import xmlrpc.client
import requests
import time
import sys
import os
from threading import Thread
from google.cloud import bigquery

# Make Python aware of the awesom_config file
sys.path.append(os.path.dirname(__file__))
from awesome_config import *


def get_dl_month(name, results, counter):
    client = bigquery.Client()
    query_string = BIGQUERY_DL_MONTH.format(name)
    query_job = client.query(query_string)
    query_results = query_job.result()
    for row in query_results:
        month_stats = row.num_downloads
        project = row.project
        results[project] = month_stats
    
    print(f'{counter} query done')

def get_package_data(name, results):
    r = requests.get(f'https://pypi.org/pypi/{name}/json')
    tool_data = r.json()
    results[name] = tool_data
    print(f'Collected {name}')


client = xmlrpc.client.ServerProxy('https://pypi.org/pypi')


# Get and store tool
tools = []

counter = 0
api_sleeps = 0

while True:
    filter = PROJECT_FILTERS[counter]
    filter_tools = []
    try:
        package_releases = client.browse(filter)
        for release in package_releases:
            if release[0] not in filter_tools:
                filter_tools.append(release[0])
        print(f'Found {len(filter_tools)} tools for {filter}')
        tools = list(set(tools + filter_tools))
    except xmlrpc.client.Fault:
        print(f'Sleeping {API_SLEEP}s for API rate refresh')
        time.sleep(API_SLEEP)
        api_sleeps += 1
        if api_sleeps >= MAX_API_SLEEPS:
            break
    else:
        api_sleeps = 0
        counter += 1
        if counter > len(PROJECT_FILTERS) - 1:
            break

# Get tool specific data
tools_data = {}

# Add tools, which can not be found by above search
for tool in EXTRA_PROJECTS:
    if tool not in tools:
        tools.append(tool)

# Remove not wanted tools
for tool in IGNORE_PROJECTS:
    try:
        tools.remove(tool)
    except ValueError:
        pass


print(f'Found overall {len(tools)} sphinx tools')

# Stop data collection, if we only want to get some data and not all
tools = tools[0:MAX_DATA]
    

print('Collection package data')
threads = {}
results = {}
counter = 0
for name in tools:
    threads[name] = Thread(target=get_package_data, args=(name, results))
    threads[name].start()

for thre in threads.values():
    thre.join()

tools_data = results
    
# collect PyPi BigQuery downloads numbers
print(f'Collecting PyPi BigQuery Stats for {len(tools_data)} tools')

threads = {}
results = {}
counter = 0

# Chunks of project-names, to split a big query into smaller ones.
# Currently not needed (+580 projects), but maybe query-string gets to big
# in future
tools_chunks = [tools_data.keys()]

for chunk in tools_chunks:
    name = "','".join(chunk)
    threads[name] = Thread(target=get_dl_month, args=(name, results, counter))
    threads[name].start()
    counter += 1

for thre in threads.values():
    thre.join()


for name, package in tools_data.items():
    try:
        package['awesome_stats'] = {
            'month': results[name],
        }
        print(f'{name}: {results[name]:,}')
    except KeyError:
        package['awesome_stats'] = {
            'month': 0,
        }
    print(f"{name}: {package['awesome_stats']['month']:,}")



# Store tools_data as json
print(f'Storing data into {JSON_FILE}')
with open(JSON_FILE, 'w') as f:
    json.dump(tools_data, f, sort_keys=True, indent=4)

print('Done. Exit now!')


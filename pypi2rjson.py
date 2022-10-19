import json
import xmlrpc.client
import requests
import time
import pypistats

JSON_FILE = 'pypi_data.json'
FILTERS = [
    ['Framework :: Sphinx'],
    ['Framework :: Sphinx :: Extension'],
    ['Framework :: Sphinx :: Theme']
]

# Used during development to reduce amount of data to fetch
# Normally a search contains ~600 findings
MAX_DATA = 5000


SLEEP = 1  # Wait time for API, if too many requests were made

client = xmlrpc.client.ServerProxy('https://pypi.org/pypi')


# Get and store tool
tools = []

counter = 0
while True:
    filter = FILTERS[counter]
    filter_tools = []
    try:
        package_releases = client.browse(filter)
        for release in package_releases:
            if release[0] not in filter_tools:
                filter_tools.append(release[0])
        print(f'Found {len(filter_tools)} tools for {filter}')
        tools = list(set(tools + filter_tools))
    except xmlrpc.client.Fault:
        print(f'Sleeping {SLEEP}s for API rate refresh')
        time.sleep(SLEEP)
    else:
        counter += 1
        if counter > len(FILTERS) - 1:
            break

# Get tool specific data
tools_data = {}

print(f'Found overall {len(tools)} sphinx tools')

# Stop data collection, if we only want to get some data and not all
tools = tools[0:MAX_DATA]


for index, tool in enumerate(tools):
    r = requests.get(f'https://pypi.org/pypi/{tool}/json')
    tool_data = r.json()
    tools_data[tool] = tool_data
    print(f'{index}/{len(tools)}. Collected {tool}')
    

# collect pypistats downloads numbers
print(f'Collecting pypistats for {len(tools_data)} tools')
for name, package in tools_data.items():
    month_stats = json.loads(pypistats.recent(package['info']['name'], "month", format="json"))
    overall_stats = json.loads(pypistats.overall(package['info']['name'], mirrors=True, format="json"))

    month = int(month_stats['data']['last_month'])
    overall = int(overall_stats['data'][0]['downloads'])

    package['awesome_stats'] = {
        'month': month,
        'overall': overall
    }
    print(f'{name}: {month:,} / {overall:,}')

# Store tools_data as json
print(f'Storing data into {JSON_FILE}')
with open(JSON_FILE, 'w') as f:
    json.dump(tools_data, f, sort_keys=True, indent=4)

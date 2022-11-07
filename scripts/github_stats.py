"""
Collects GitHub stats from project in pypi_data.json
"""
import json
import sys
import os
from threading import Thread
import time
from github import Github, UnknownObjectException, RateLimitExceededException

# Make Python aware of the awesom_config file
sys.path.append(os.path.dirname(__file__))
from awesome_config import *


KEY = os.environ['GH_KEY']


def get_gh_topics(name, gh_project, results, counter, rate_limits=0):
    awesome_tags = []
    awesome_stars = -1
    try:
        repo = g.get_repo(gh_project)
        awesome_tags = repo.get_topics()
        awesome_stars = repo.stargazers_count
        print(f'{counter}/{len(pypi_data)} {name}: Tags retrieved: {awesome_tags}')
    except UnknownObjectException:
        pass
    except RateLimitExceededException:
        if rate_limits < GH_RATE_LIMIT_AMOUNT:
            print(f'{counter} waiting {GH_RATE_LIMIT_WAIT} ({rate_limits+1}/{GH_RATE_LIMIT_AMOUNT})')
            time.sleep(GH_RATE_LIMIT_WAIT)
            get_gh_topics(name, gh_project, results, counter, rate_limits=rate_limits+1)


    results[name] = {
        'tags': awesome_tags,
        'stars': awesome_stars
    }



print(f'Reading pypi data from {JSON_FILE}')
with open(JSON_FILE, 'r') as f:
    pypi_data = json.load(f)

gh_projects={}

for name, project  in pypi_data.items():
    # Collect possible github repository URLS
    from contextlib import suppress

    gh_urls = []
    with suppress(KeyError,TypeError):
        gh_urls.append(project['info']['project_urls']['Github'])
    with suppress(KeyError,TypeError):
        gh_urls.append(project['info']['project_urls']['Code'])
    with suppress(KeyError,TypeError):
        gh_urls.append(project['info']['project_urls']['Source Code'])
    with suppress(KeyError,TypeError):
        gh_urls.append(project['info']['project_urls']['Source'])
    with suppress(KeyError,TypeError):
        gh_urls.append(project['info']['project_urls']['Homepage'])
    with suppress(KeyError,TypeError):
        gh_urls.append(project['info']['home_page'])

        
    gh_urls_clean = []
    for url in gh_urls:
        if url is not None and 'github.com' in url and '/issues' not in url:
            url_clean = url.replace('https://github.com/', '').replace('https://github.com/', '').strip('/')
            gh_urls_clean.append(url_clean)

    if gh_urls_clean:
        gh_projects[name] = gh_urls_clean[0]
        
print(f'Github projects found: {len(gh_projects)}/{len(pypi_data)}')

g = Github(KEY)
counter = 0
results = {}
threads = {}

wait_counter = 0

for name, project in pypi_data.items():
    
    if wait_counter > GH_WAIT_COUNTER:
        time.sleep(GH_WAIT_DURATION)
        wait_counter = 0

    awesome_tags = []
    if name in gh_projects:
        gh_project = gh_projects[name]
        threads[name] = Thread(target=get_gh_topics, args=(name, gh_project, results, counter))
        threads[name].start()
        counter += 1

for thre in threads.values():
    thre.join()


print(f'Received {len(results)} tag-results from GitHub')

for name, project in pypi_data.items():
    project['awesome_stats']['tags'] = []
    project['awesome_stats']['stars'] = -1
    if name in results:
        project['awesome_stats']['tags'] = results[name]['tags']
        project['awesome_stats']['stars'] = results[name]['stars']

print(f'Storing data into {GH_JSON_FILE}')
with open(GH_JSON_FILE, 'w') as f:
    json.dump(pypi_data, f, sort_keys=True, indent=4)

print('Done. Exit now!')


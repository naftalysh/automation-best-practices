import aiohttp
import asyncio
import argparse
import time
from operator import itemgetter
from tabulate import tabulate
import json
from datetime import datetime

async def fetch(session, url, page):
    params = {'page': str(page), 'onlyActiveTags': 'true'}
    async with session.get(url, params=params) as response:
        return await response.text()

async def get_all_tags(url):
    tags = []
    page = 1
    async with aiohttp.ClientSession() as session:
        while True:
            print(f"Fetching page {page}")  # print the page number
            response = await fetch(session, url, page)
            data = json.loads(response)
            if not data['tags']:
                break
            tags.extend([(tag['name'], tag.get('last_modified', 'Unknown')) for tag in data['tags']])
            page += 1
    return tags

from datetime import datetime

def format_date(last_modified):
    # Parse the datetime string to a datetime object
    dt = datetime.strptime(last_modified, '%a, %d %b %Y %H:%M:%S %z')
    # Format the date, then manually adjust the timezone format
    formatted_date = dt.strftime('%a, %d %b %Y %H:%M:%S %z')
    # Remove the trailing ':00' from the timezone part
    if formatted_date.endswith('+0000'):
        formatted_date = formatted_date[:-2]  # Remove the last two zeros
    return formatted_date

def print_sorted_tags(tags):
    formatted_tags = []

    for tag in tags:
        name, last_modified = tag
        if last_modified != 'Unknown':
            formatted_date = format_date(last_modified)
        else:
            formatted_date = 'Unknown'
        
        formatted_tags.append((name, formatted_date))

    print(tabulate(formatted_tags, headers=['Name', 'Last Modified'], tablefmt='psql'))
    print(f"\nTotal number of tags: {len(tags)}")


parser = argparse.ArgumentParser(description='Get all tags from a Quay.io repository.')
parser.add_argument('url', help='The URL of the Quay.io repository.')

args = parser.parse_args()

start_time = time.time()

tags = asyncio.run(get_all_tags(args.url))
print_sorted_tags(tags)

end_time = time.time()

print(f"\n--- Execution took {end_time - start_time:.2f} seconds ---")


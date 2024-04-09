import aiohttp
import asyncio
import argparse
import time
import json
from datetime import datetime

async def fetch(session, url, page):
    params = {'page': str(page), 'onlyActiveTags': 'true'}
    async with session.get(url, params=params) as response:
        return await response.text()

async def delete_tag(session, url):
    async with session.delete(url) as response:
        return response.status

async def get_all_tags(url, token):
    tags = []
    page = 1
    async with aiohttp.ClientSession(headers={"Authorization": f"Bearer {token}"}) as session:
        while True:
            print(f"Fetching page {page}")  # print the page number
            response = await fetch(session, url, page)
            data = json.loads(response)
            if not data['tags']:
                break
            for tag in data['tags']:
                del_url = f"{url.rstrip('tag/')}{tag['name']}"
                print(f"Deleting tag: {tag['name']}")
                status = await delete_tag(session, del_url)
                print(f"Delete status: {status}")
            page += 1

parser = argparse.ArgumentParser(description='Delete all tags from a Quay.io repository.')
parser.add_argument('url', help='The URL of the Quay.io repository.')
parser.add_argument('token', help='The Quay.io OAuth Token.')

args = parser.parse_args()

start_time = time.time()

asyncio.run(get_all_tags(args.url, args.token))

end_time = time.time()

print("\n--- Execution took %s seconds ---" % (end_time - start_time))

# python deleteQuayTags.py https://quay.io/api/v1/repository/coreos/etcd/tag/ your-oauth-token
# python deleteQuayTags.py https://quay.io/api/v1/repository/nshprai/test-images/tag/  $QUAY_OAUTH_TOKEN


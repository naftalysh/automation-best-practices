import aiohttp
import asyncio
import argparse
import json

async def fetch(session, url, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with session.get(url, headers=headers) as response:
        return await response.text()

async def verify_token(url, token):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, url, token)
        data = json.loads(response)  # parse the response into a JSON object
        pretty_data = json.dumps(data, indent=4)  # pretty-print the JSON object
        print(pretty_data)

parser = argparse.ArgumentParser(description='Verify Quay.io OAuth Token.')
parser.add_argument('org', help='The Quay.io organization.')
parser.add_argument('repo', help='The Quay.io repository.')
parser.add_argument('token', help='The Quay.io OAuth Token.')

args = parser.parse_args()

repo_url = f"https://quay.io/api/v1/repository/{args.org}/{args.repo}"
asyncio.run(verify_token(repo_url, args.token))

# python verifyQuayToken.py your-organization your-repo your-oauth-token
# python verifyQuayToken.py nshprai test-images your-oauth-token


# Check you can access and read the tags
# curl -s -H "Authorization: Bearer ${TOKEN}" https://quay.io/api/v1/repository/${ORG}/${REPO}/tag/
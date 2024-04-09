import requests
import argparse
import json

def delete_repositories(api_token, org_name, prefix):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.get(f'https://quay.io/api/v1/repository?public=false&namespace={org_name}', headers=headers)

    if response.status_code == 200:
        repositories = response.json()['repositories']
        for repo in repositories:
            full_repo_name = repo['name']
            # Extract just the repository name part after the organization name
            repo_name = full_repo_name.replace(f"{org_name}/", "")
            # if repo name starts with prefix, delete it
            if repo_name.startswith(prefix):
                delete_response = requests.delete(f'https://quay.io/api/v1/repository/{org_name}/{repo_name}', headers=headers)
                if delete_response.status_code == 204:
                    print(f'Successfully deleted repository: {full_repo_name}')
                else:
                    error_message = json.loads(delete_response.text).get('message', 'An unknown error occurred.')
                    print(f'Failed to delete repository: {full_repo_name}. Error message: {error_message}')
    else:
        error_message = json.loads(response.text).get('message', 'An unknown error occurred.')
        print(f'Failed to retrieve repositories. Error message: {error_message}')

def main():
    parser = argparse.ArgumentParser(description="Delete Quay.io repositories")
    parser.add_argument("api_token", help="Your Quay.io API token")
    parser.add_argument("org_name", help="Your organization name in Quay.io")
    parser.add_argument("prefix", help="Prefix of the repositories you want to delete")

    args = parser.parse_args()

    delete_repositories(args.api_token, args.org_name, args.prefix)

if __name__ == "__main__":
    main()


# python deleteQuayRepos.py your_api_token_here orgx pre_
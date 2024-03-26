import requests
import argparse
import json

def delete_robots(api_token, org_name, prefix):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.get(f'https://quay.io/api/v1/organization/{org_name}/robots', headers=headers)

    if response.status_code == 200:
        robots = response.json()['robots']
        for robot in robots:
            full_robot_name = robot['name']
            # Extract just the robot name part after the organization name
            robot_name = full_robot_name.replace(f"{org_name}+", "")
            # if robot name starts with prefix, delete it
            if robot_name.startswith(prefix):
                delete_response = requests.delete(f'https://quay.io/api/v1/organization/{org_name}/robots/{robot_name}', headers=headers)
                if delete_response.status_code == 204:
                    print(f'Successfully deleted robot: {full_robot_name}')
                else:
                    error_message = json.loads(delete_response.text).get('message', 'An unknown error occurred.')
                    print(f'Failed to delete robot: {full_robot_name}. Error message: {error_message}')
    else:
        error_message = json.loads(response.text).get('message', 'An unknown error occurred.')
        print(f'Failed to retrieve robot accounts. Error message: {error_message}')

def main():
    parser = argparse.ArgumentParser(description="Delete Quay.io robot accounts")
    parser.add_argument("api_token", help="Your Quay.io API token")
    parser.add_argument("org_name", help="Your organization name in Quay.io")
    parser.add_argument("prefix", help="Prefix of the robot accounts you want to delete")

    args = parser.parse_args()

    delete_robots(args.api_token, args.org_name, args.prefix)

if __name__ == "__main__":
    main()

# python deleteQuayRobots.py your_api_token_here orgx pre_
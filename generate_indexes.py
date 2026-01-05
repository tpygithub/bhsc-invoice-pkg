import requests
import os

def generate_repository_indexes():
    """
    test: Function to post a request to Greptile API to generate indexes for the repository.
    Requires environment variables: GREPTILE_AUTH_TOKEN and GITHUB_TOKEN
    """
    url = "https://api.greptile.com/v2/repositories"

    auth_token = os.getenv('GREPTILE_AUTH_TOKEN')
    github_token = os.getenv('GITHUB_TOKEN')

    if not auth_token or not github_token:
        print("Error: Missing required environment variables GREPTILE_AUTH_TOKEN and/or GITHUB_TOKEN")
        return False, "Missing environment variables"

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "X-GitHub-Token": github_token
    }

    data = {
        "remote": "github",
        "repository": "tpygithub/bhsc-invoice-pkg",
        "branch": "main",
        "reload": True,
        "notify": True
    }

    try:
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            print("Repository indexes generation requested successfully")
            print(f"Response: {response.json()}")
            return True, response.json()
        else:
            print(f"Request failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return False, response.text

    except Exception as e:
        print(f"Error: {str(e)}")
        return False, str(e)

if __name__ == "__main__":
    generate_repository_indexes()

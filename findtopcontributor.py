
import requests
import json

# Your GitHub token for authentication (recommended for higher rate limits)
github_token = "your github token here"

headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

def get_top_contributor(repo_name):
    url = f"https://api.github.com/repos/{repo_name}/contributors"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        contributors = json.loads(response.text)
        if contributors:
            return contributors[0]['login']
    return None

if __name__ == "__main__":
    # Read the list of repositories from a file
    with open('repo_list_file.txt', 'r') as f:
        repo_list = [line.strip() for line in f.readlines()]

    for repo_name in repo_list:
        top_contributor = get_top_contributor(repo_name)
        if top_contributor:
            print(f"The top contributor of the repository {repo_name} is {top_contributor}.")
        else:
            print(f"Could not find information for the repository {repo_name}.")

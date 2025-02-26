""" Beginning of Main Application"""

# Import Modules
import os
from dotenv import load_dotenv
import httpx
import json
import truststore
truststore.inject_into_ssl()

# load the dotenv file
load_dotenv()

# Environmental Variables
gh_key = os.getenv('API_KEY')
gh_url = os.getenv('BASEURL')

# Authorization Header for Github API
headers = {
    "Authorization": f"Bearer {gh_key}"
    }

# Get the current working directory
current_directory = os.getcwd()

# Define the filename for the output file
filename = "repos.txt"

# Construct the full file path
filepath = os.path.join(current_directory, filename)

def repo_clone():
    # create the call to the API
    r = httpx.get(f'{gh_url}/user/repos', headers = headers)
    
    # Check if the call was successful
    if r.status_code == 200:
        with open(filepath, "w") as file:
            repos = r.json()
            for repo in repos:
                file.write(repo['name'] + "\n")

    # Read Repo list and clone repos
    with open(filepath, "r", encoding="utf-8") as repo_list:
        for line in repo_list:
            for repo in line.split():
                url = f"https://github.com/randallbullard/{repo}.git"
                clone_string = f"git clone {url}"
                os.system(clone_string)

# Execute the function
repo_clone()















# if __name__ == '__main__':
#     main()

# EOF
# Import Modules
import os
import truststore
truststore.inject_into_ssl()
from dotenv import load_dotenv
import httpx

# load the dotenv file
load_dotenv()

# Environmental Variables
gh_key = os.getenv('API_KEY')


with open('/home/randallbullard/programming/python/github_repos/git_clone_script/repos.txt', "r") as repo_list:
    for line in repo_list:
        for repo in line.split():
            url = f"https://github.com/randallbullard/{repo}.git"
            clone_string = f"git clone {url}"
            os.system(clone_string)
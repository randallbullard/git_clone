# Import Modules
import os
import httpx

# Read Repo list and clone repos
with open('/home/randallbullard/programming/python/github_repos/git_clone_script/repos.txt', "r") as repo_list:
    for line in repo_list:
        for repo in line.split():
            url = f"https://github.com/randallbullard/{repo}.git"
            clone_string = f"git clone {url}"
            os.system(clone_string)
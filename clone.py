""" Import Modules """

import os

# Read Repo list and clone repos
with open("./git_clone_script/repos.txt", "r", encoding="utf-8") as repo_list:
    for line in repo_list:
        for repo in line.split():
            url = f"https://github.com/randallbullard/{repo}.git"
            clone_string = f"git clone {url}"
            os.system(clone_string)

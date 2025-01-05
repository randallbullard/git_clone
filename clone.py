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


def list_folders(path='../'):
    """Lists all folders in the specified directory.

    Args:
        path (str): The path to the directory. Defaults to the current directory.

    Returns:
        list: A list of folder names.
    """

    folders = []
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            folders.append(entry)
    return folders

folders = list_folders()
user = "randallbullard"
password = gh_key

for folder in folders:
    if folder == "asteroids":
        r = httpx.get(f'https://github.com/randallbullard/{folder}.git') # Build list of repos request
        print(r.status_code)
    

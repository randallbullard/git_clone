""" Beginning of Main Application"""

# Import Modules
import os
import truststore
truststore.inject_into_ssl()
from dotenv import load_dotenv
import httpx
import json

# load the dotenv file
load_dotenv()

# Environmental Variables
gh_key = os.getenv('API_KEY')
gh_url = os.getenv('BASEURL')

headers = {'Authorization': f'Bearer {gh_key}'}
# print(headers)

owner = 'randallbullard' #str(input('Enter target username: '))

def main():
    print(f'{gh_url}/users/{owner}/repos')
    r = httpx.get(f'{gh_url}/users/{owner}/repos', headers=headers) # Build list of repos request
    if r.status_code == 200:
        r_dict = r.json() # Convert json into dictionary
        print(json.dumps(r_dict, indent=2, sort_keys=True)) # Pretty Printing JSON string back
    else:
        print(r.status_code)
    




main()















# if __name__ == '__main__':
#     main()

# EOF
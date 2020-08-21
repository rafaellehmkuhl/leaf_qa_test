import requests
import os
from pprint import pprint

TOKEN = os.environ['LEAF_TOKEN']
headers = {'Authorization': f'Bearer {TOKEN}'}
base_url = 'https://api.withleaf.io/services/fields/api'

get_endpoint = f'{base_url}/fields'
response_get = requests.get(get_endpoint, headers=headers)

leafUserId = response_get.json()[0].get('leafUserId')
post_endpoint = f'{base_url}/users/{leafUserId}/fields/'
response_post = requests.post(post_endpoint, headers=headers)

print('\n GET REQUEST: \n')
pprint(response_get.json())
print('\n ---------------------------------------------------------------- \n')

print('\n POST REQUEST: \n')
pprint(response_post.json())
print('\n ---------------------------------------------------------------- \n')

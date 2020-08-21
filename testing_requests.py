import requests
import os
from pprint import pprint

TOKEN = os.environ['LEAF_TOKEN']

endpoint = 'https://api.withleaf.io/services/fields/api/fields'
headers = {'Authorization': f'Bearer {TOKEN}'}

response = requests.get(endpoint, headers=headers)
pprint(response.json())

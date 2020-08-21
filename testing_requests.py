import requests
import os

TOKEN = os.environ['LEAF_TOKEN']

endpoint = 'https://api.withleaf.io/services/fields/api/fields'
headers = {'Authorization': f'Bearer {TOKEN}'}

response = requests.get(endpoint, headers=headers)
print(response.json())

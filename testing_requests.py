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
post_request_body = {
    "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
            [
                [
                    [-93.48821327980518, 41.77137549568163],
                    [-93.48817333680519, 41.77143534378164],
                    [-93.48821327390516, 41.76068857977987],
                    [-93.48821327980518, 41.77137549568163]
                ]
            ]
        ]
    }
}
response_post = requests.post(
    post_endpoint, headers=headers, json=post_request_body)

print('\n GET REQUEST: \n')
pprint(response_get.json())
print('\n ---------------------------------------------------------------- \n')

print('\n POST REQUEST: \n')
pprint(response_post.json())
print('\n ---------------------------------------------------------------- \n')

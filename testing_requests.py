from pprint import pprint
import os
from routes import get_fields, post_fields, get_user_Id, get_token

EMAIL = os.environ['LEAF_EMAIL']
PASS = os.environ['LEAF_PASS']
TOKEN = get_token(EMAIL, PASS)

post_body = {
    "geometry": {
        "type": "MultiPolygon",
        "coordinates": [[[
            [-93.48821327980518, 41.77137549568163],
            [-93.48817333680519, 41.77143534378164],
            [-93.48821327390516, 41.76068857977987],
            [-93.48821327980518, 41.77137549568163]
        ]]]
    }
}

response_get = get_fields(TOKEN)
response_post = post_fields(TOKEN, post_body)

print('\n GET REQUEST: \n')
pprint(response_get.json())
print('\n ---------------------------------------------------------------- \n')

print('\n POST REQUEST: \n')
pprint(response_post.json())
print('\n ---------------------------------------------------------------- \n')

import os
from routes import get_fields, get_token, delete_fields

EMAIL = os.environ['LEAF_EMAIL']
PASS = os.environ['LEAF_PASS']
TOKEN = get_token(EMAIL, PASS)

response_get = get_fields(TOKEN)

for field in response_get.json():
    id = field.get('id')
    delete_fields(TOKEN, id)

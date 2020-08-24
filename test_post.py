import os
from faker import Faker
from pprint import pprint
from routes import post_field, get_token, get_user_Id

fake = Faker()
Faker.seed(4321)

EMAIL = os.environ['LEAF_EMAIL']
PASS = os.environ['LEAF_PASS']
TOKEN = get_token(EMAIL, PASS)
USER_ID = get_user_Id(TOKEN)


def test_valid_coords():
    field_id = fake.uuid4()
    coords = [[[[-1.0, -1.0],
                [-1.0, +1.0],
                [+1.0, +1.0],
                [+1.0, -1.0],
                [-1.0, -1.0]]]]
    body = {
        "id": field_id,
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": coords
        }
    }
    response = post_field(TOKEN, body)
    pprint(response)
    pprint(response.json())
    assert(response.status_code == 201)
    assert(response.json().get('id') == field_id)
    assert(response.json().get('type') == 'ORIGINAL')
    assert(response.json().get('leafUserId') == USER_ID)
    assert(response.json().get('geometry').get('coordinates') == coords)


def test_unclosed_coords():
    field_id = fake.uuid4()
    coords = [[[[-1.0, -1.0],
                [-1.0, +1.0],
                [+1.0, +1.0],
                [+1.0, -1.0]]]]
    body = {
        "id": field_id,
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": coords
        }
    }
    response = post_field(TOKEN, body)
    pprint(response)
    pprint(response.json())
    assert(response.status_code == 400)
    assert('Points of LinearRing do not form a closed' in response.json().get('detail'))


def test_crossing_coords():
    field_id = fake.uuid4()
    coords = [[[[-1.0, -1.0],
                [-1.0, +1.0],
                [+1.0, -1.0],
                [+1.0, +1.0],
                [-1.0, -1.0]]]]
    body = {
        "id": field_id,
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": coords
        }
    }
    response = post_field(TOKEN, body)
    pprint(response)
    pprint(response.json())
    assert(response.status_code == 400)
    assert(response.json().get('errorKey') == 'invalidgeometry')

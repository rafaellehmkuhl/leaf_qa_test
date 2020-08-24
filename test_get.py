import os
from faker import Faker
from pprint import pprint
from routes import get_fields, get_token, get_user_Id

fake = Faker()
Faker.seed(4321)

EMAIL = os.environ['LEAF_EMAIL']
PASS = os.environ['LEAF_PASS']
TOKEN = get_token(EMAIL, PASS)
USER_ID = get_user_Id(TOKEN)


def test_for_existing_user_id():
    params = {'leafUserId': USER_ID}
    response = get_fields(TOKEN, params)
    pprint(response)
    pprint(response.json())
    assert(response.status_code == 200)
    found_wrong_user_id = next((True for item in response.json() if
                                item.get('leafUserId') != USER_ID), False)
    assert(not found_wrong_user_id)


def test_for_unexisting_user_id():
    params = {'leafUserId': '05fc1ab9-ea07-46d0-80e3-1d41ca70c222'}
    response = get_fields(TOKEN, params)
    pprint(response)
    pprint(response.json())
    assert(response.status_code == 200)
    assert(True if not response.json() else False)


def test_for_existing_field():
    field_id = fake.uuid4()
    coords = [[[[-1.0, -1.0],
                [-1.0, +1.0],
                [+1.0, +1.0],
                [+1.0, -1.0],
                [-1.0, -1.0]]]]
    response = get_fields(TOKEN)
    pprint(response)
    pprint(response.json())
    assert(response.status_code == 200)
    found_field = next((True for item in response.json() if
                        item.get('geometry').get('coordinates') == coords), False)
    assert(found_field)

from pprint import pprint
from conftest import EMAIL, PASS, TOKEN, USER_ID, valid_coords, valid_field_id
from routes import get_fields


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
    response = get_fields(TOKEN)
    pprint(response)
    pprint(response.json())
    assert(response.status_code == 200)
    found_field = next((item for item in response.json() if
                        item.get('geometry').get('coordinates') == valid_coords), False)
    assert(found_field)
    assert(found_field.get('id') == valid_field_id)

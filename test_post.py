from pprint import pprint
from conftest import EMAIL, PASS, TOKEN, USER_ID, valid_coords, valid_field_id
from routes import post_field


def test_valid_coords():
    body = {
        "id": valid_field_id,
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": valid_coords
        }
    }
    response = post_field(TOKEN, body)
    pprint(response)
    pprint(response.json())
    assert(response.status_code == 201)
    assert(response.json().get('id') == valid_field_id)
    assert(response.json().get('type') == 'ORIGINAL')
    assert(response.json().get('leafUserId') == USER_ID)
    assert(response.json().get('geometry').get('coordinates') == valid_coords)


def test_unclosed_coords():
    coords = [[[[-1.0, -1.0],
                [-1.0, +1.0],
                [+1.0, +1.0],
                [+1.0, -1.0]]]]
    body = {
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
    coords = [[[[-1.0, -1.0],
                [-1.0, +1.0],
                [+1.0, -1.0],
                [+1.0, +1.0],
                [-1.0, -1.0]]]]
    body = {
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

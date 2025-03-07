import requests

base_url = 'https://api.withleaf.io/services/fields/api'


def get_token(email, password):
    auth_url = "https://api.withleaf.io/api/authenticate"
    auth_data = {'username': email,
                 'password': password,
                 'rememberMe': 'true'}
    auth_response = requests.post(auth_url, json=auth_data)
    return auth_response.json().get('id_token')


def get_user_Id(token):
    response_get = get_fields(token)
    return response_get.json()[0].get('leafUserId')


def get_header(token):
    return {'Authorization': f'Bearer {token}'}


def get_fields(token, params=None):
    get_endpoint = f'{base_url}/fields'
    headers = get_header(token)
    return requests.get(get_endpoint, headers=headers, params=params)


def post_field(token, body):
    leafUserId = get_user_Id(token)
    post_endpoint = f'{base_url}/users/{leafUserId}/fields/'
    headers = get_header(token)
    return requests.post(post_endpoint, headers=headers, json=body)


def delete_fields(token, id):
    leafUserId = get_user_Id(token)
    delete_endpoint = f'{base_url}/users/{leafUserId}/fields/{id}'
    headers = get_header(token)
    requests.delete(delete_endpoint, headers=headers)

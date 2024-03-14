import requests
from pprint import pprint


def all_objects():
    response = requests.get('https://api.restful-api.dev/objects').json()
    pprint(response)


def one_object(object_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{object_id}')
    return response


def create_an_object():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)

    assert response.status_code == 200, 'Status code is not 200'
    assert response.json()['data']['price'] == 1849.99, 'Price is not correct'
    return response.json()['id']


def put_an_object():
    object_id = create_an_object()
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'https://api.restful-api.dev/objects/{object_id}', json=body, headers=headers)

    assert response.status_code == 200, 'Status code is not 200'
    assert response.json()['data']['price'] == 2049.99, 'Price is not correct'
    assert response.json()['id'] == object_id, 'Id is not correct'
    clear(object_id)


def patch_an_object():
    object_id = create_an_object()
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://api.restful-api.dev/objects/{object_id}', json=body, headers=headers)

    assert response.status_code == 200, 'Status code is not 200'
    assert response.json()['name'] == "Apple MacBook Pro 16 (Updated Name)", 'Name is not updated'
    assert response.json()['id'] == object_id, 'Id is not correct'
    clear(object_id)


def delete_an_object():
    object_id = create_an_object()
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')

    assert response.status_code == 200, 'Status code is not 200'
    assert 'error' in one_object(object_id).json().keys()


def clear(object_id):
    requests.delete(f'https://api.restful-api.dev/objects/{object_id}')

# all_objects()
# one_object()
# create_an_object()
# put_an_object()
# patch_an_object()
# delete_an_object()

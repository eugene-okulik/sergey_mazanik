import requests
import pytest


@pytest.fixture()
def new_object_id():
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
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'https://api.restful-api.dev/objects/{object_id}')


@pytest.fixture(scope='function')
def start_end_test():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture(scope='session')
def start_end_testing():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.mark.critical
@pytest.mark.parametrize('prices', [1849.99, '1849.99', None])
def test_create_an_object(start_end_test, start_end_testing, prices):
    price = None
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": price,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    object_id = response.json()['id']

    assert response.status_code == 200, 'Status code is not 200'
    assert response.json()['data']['price'] == price, 'Price is not correct'

    requests.get(f'https://api.restful-api.dev/objects/{object_id}')


@pytest.mark.medium
def test_put_an_object(new_object_id, start_end_test):
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
    response = requests.put(f'https://api.restful-api.dev/objects/{new_object_id}', json=body, headers=headers)

    assert response.status_code == 200, 'Status code is not 200'
    assert response.json()['data']['price'] == 2049.99, 'Price is not correct'
    assert response.json()['id'] == new_object_id, 'Id is not correct'


def test_patch_an_object(new_object_id, start_end_test):
    body = {"name": "Apple MacBook Pro 16 (Updated Name)"}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://api.restful-api.dev/objects/{new_object_id}', json=body, headers=headers)

    assert response.status_code == 200, 'Status code is not 200'
    assert response.json()['name'] == "Apple MacBook Pro 16 (Updated Name)", 'Name is not updated'
    assert response.json()['id'] == new_object_id, 'Id is not correct'


def test_delete_an_object(new_object_id, start_end_test):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')

    assert response.status_code == 200, 'Status code is not 200'
    assert 'error' in one_object(new_object_id).json().keys()


def one_object(object_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{object_id}')
    return response

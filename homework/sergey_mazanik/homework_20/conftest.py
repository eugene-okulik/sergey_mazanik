import pytest
import requests


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

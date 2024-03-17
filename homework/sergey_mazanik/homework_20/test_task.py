import requests
import pytest
import allure


@allure.feature('Object')
@allure.story('Create object')
@allure.title('Create an object')
@pytest.mark.critical
@pytest.mark.parametrize('prices', [1849.99, '0', None])
def test_create_an_object(start_end_test, start_end_testing, prices):
    with allure.step('Prepare test data'):
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
    with allure.step('Run post request for create an object'):
        response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
        object_id = response.json()['id']

    with allure.step('Check that status code is 200'):
        assert response.status_code == 200, 'Status code is not 200'
    with allure.step(f'Check that new object price is {price}'):
        assert response.json()['data']['price'] == price, 'Price is not correct'

    with allure.step(f'Run get request for an object with id {object_id}'):
        requests.get(f'https://api.restful-api.dev/objects/{object_id}')


@allure.feature('Object')
@allure.story('Update object')
@allure.title('Full update an object')
@pytest.mark.medium
def test_put_an_object(new_object_id, start_end_test):
    with allure.step('Prepare test data'):
        price = 2049.99
        body = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": price,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
                "color": "silver"
            }
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step(f'Run put request for object with id {new_object_id}'):
        response = requests.put(f'https://api.restful-api.dev/objects/{new_object_id}', json=body, headers=headers)

    with allure.step('Check that status code is 200'):
        assert response.status_code == 200, 'Status code is not 200'
    with allure.step(f'Check that new object price is {price}'):
        assert response.json()['data']['price'] == price, 'Price is not correct'
    with allure.step(f'Check that object id is {new_object_id}'):
        assert response.json()['id'] == new_object_id, 'Id is not correct'


@allure.feature('Example')
@allure.story('Update object')
@allure.title('partial update an object')
def test_patch_an_object(new_object_id, start_end_test):
    with allure.step('Prepare test data'):
        name = "Apple MacBook Pro 16 (Updated Name)"
        body = {"name": name}
        headers = {'Content-Type': 'application/json'}
    with allure.step(f'Run patch request for an object with id {new_object_id}'):
        response = requests.patch(f'https://api.restful-api.dev/objects/{new_object_id}', json=body, headers=headers)

    with allure.step('Check that status code is 200'):
        assert response.status_code == 200, 'Status code is not 200'
    with allure.step(f'Check that new object name is {name}'):
        assert response.json()['name'] == name, 'Name is not updated'
    with allure.step(f'Check that object id is {new_object_id}'):
        assert response.json()['id'] == new_object_id, 'Id is not correct'


@allure.feature('Object')
@allure.story('Delete object')
@allure.title('Delete an object')
def test_delete_an_object(new_object_id, start_end_test):
    with allure.step(f'Run delete request for delete an object with id {new_object_id}'):
        response = requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')

    with allure.step('Check that status code is 200'):
        assert response.status_code == 200, 'Status code is not 200'
    with allure.step(f'Check that an object with id {new_object_id} is deleted'):
        assert 'error' in one_object(new_object_id).json().keys(), f'Object with id {new_object_id} is not deleted'


def one_object(object_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{object_id}')
    return response

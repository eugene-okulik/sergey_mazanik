import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObjectPatch(Endpoint):

    @allure.step('Partial update an object')
    def make_partial_changes_in_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.url}/{object_id}', json=body, headers=headers)
        self.json = self.response.json()
        return self.response

    @allure.step('Check that new object name is correct')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name, 'Name is not correct'

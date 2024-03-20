import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete an object')
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')

    @allure.step('Get deleted object')
    def get_deleted_object(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()
        return self.json.keys()

    @allure.step('Check that object was deleted')
    def check_that_object_was_deleted(self, object_id):
        assert 'error' in self.get_deleted_object(object_id), 'Object was not deleted'

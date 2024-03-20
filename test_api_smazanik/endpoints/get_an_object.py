import requests
import allure
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Get an object')
    def get_object(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()
        return self.json

    @allure.step('Check that object was deleted')
    def check_that_object_was_deleted(self):
        assert 'error' in self.json.keys(), 'Object was not deleted'

    @allure.step('Check that status code is 404')
    def check_that_status_is_404(self):
        assert self.response.status_code == 404, 'Status code is not 404'

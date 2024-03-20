import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that new object price is correct')
    def check_response_price_is_correct(self, price):
        assert self.json['data']['price'] == price, 'Price is not correct'

    @allure.step('Check that status code is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, 'Status code is not 200'

    @allure.step('Check that new object has correct id')
    def check_response_id_is_correct(self, object_id):
        assert self.json['id'] == object_id, 'Id is not correct'

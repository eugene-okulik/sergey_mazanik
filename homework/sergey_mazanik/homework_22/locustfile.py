from locust import task, HttpUser
from random import randint


class ObjectUser(HttpUser):
    object_id = None
    year = randint(2010, 2024)
    created_objects = []

    @task
    def create_object(self):
        response = self.client.post(
            '/objects',
            headers={'Content-Type': 'application/json'},
            json={
                "name": "Apple MacBook Pro 16",
                "data": {
                    "year": self.year,
                    "price": 1849.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB"
                }
            }
        )
        self.object_id = response.json()['id']
        self.created_objects.append(self.object_id)

    @task
    def get_all_objects(self):
        self.client.get('/objects')

    @task
    def get_one_object(self):
        self.client.get(f'/objects/{self.object_id}')

    def on_stop(self):
        for created_object in self.created_objects:
            self.client.delete(f'/objects/{created_object}')

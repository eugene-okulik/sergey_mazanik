import requests

response = requests.get('https://api.restful-api.dev/objects').json()
print(response)

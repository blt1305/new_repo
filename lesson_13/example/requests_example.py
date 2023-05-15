import requests

URL = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(URL)
print(response.json())
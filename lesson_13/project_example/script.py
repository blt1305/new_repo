import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(os.environ.get("URL"))
print(response.json())

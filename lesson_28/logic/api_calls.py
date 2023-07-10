import requests

URL = "https://dummyjson.com/todo"


def get_todos():
    return requests.get(URL).json()

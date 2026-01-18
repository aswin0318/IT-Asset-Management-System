import requests

BASE_URL = "http://127.0.0.1:8000"


def get(endpoint: str):
    response = requests.get(f"{BASE_URL}{endpoint}")
    response.raise_for_status()
    return response.json()


def post(endpoint: str, data: dict):
    response = requests.post(f"{BASE_URL}{endpoint}", json=data)
    response.raise_for_status()
    return response.json()


def put(endpoint: str):
    response = requests.put(f"{BASE_URL}{endpoint}")
    response.raise_for_status()
    return response.json()


def download_file(endpoint: str):
    response = requests.get(f"{BASE_URL}{endpoint}")
    response.raise_for_status()
    return response.content

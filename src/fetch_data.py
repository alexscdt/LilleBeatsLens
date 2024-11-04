import requests
from requests import Response

def fetch_data(apiKey: str, apiUrl: str) -> Response:
    headers: dict = {"x-rapidapi-key": apiKey, "Content-Type": "application/json"}
    return requests.get(apiUrl, headers=headers)

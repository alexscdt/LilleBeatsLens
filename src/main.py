from dotenv import load_dotenv
import requests
import os

load_dotenv()
apiKey: str = os.getenv("API_KEY")
apiUrl: str = os.getenv("API_URL")

def main():
    headers: dict = {"x-rapidapi-key": apiKey, "Content-Type": "application/json"}
    response = requests.get(apiUrl, headers=headers)

    if response.status_code == 200:
        print('Success')
        print(response.json())
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    main()
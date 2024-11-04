from data_processor import process
from dotenv import load_dotenv
import os

load_dotenv()
apiKey: str = os.getenv("API_KEY")
apiUrl: str = os.getenv("API_URL")

def main():
    process(apiKey, apiUrl)


if __name__ == "__main__":
    main()
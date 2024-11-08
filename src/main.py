from data_processor import process
from post_tweet import post_tweet
from dotenv import load_dotenv
import os

load_dotenv()

apiKey: str = os.getenv("API_KEY")
apiUrl: str = os.getenv("API_URL")

XApiKey: str= os.getenv("X_API_KEY")
XApiSecret: str = os.getenv("X_API_SECRET_KEY")
XAccessToken: str = os.getenv("X_ACCESS_TOKEN")
XAccessTokenSecret: str = os.getenv("X_ACCESS_TOKEN_SECRET")

def main():
    last_win_message = process(apiKey, apiUrl)
    post_tweet(last_win_message, XApiKey, XApiSecret, XAccessToken, XAccessTokenSecret)

if __name__ == "__main__":
    main()

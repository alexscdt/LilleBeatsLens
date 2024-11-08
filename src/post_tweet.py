import tweepy

def post_tweet(message: str,
               api_key: str,
               api_secret: str,
               access_token: str,
               access_token_secret: str) -> None:
    try:
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

        response = client.create_tweet(text=message)
        print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")

    except tweepy.errors.Forbidden as e:
        print("\nPermission Error:")
        print(f"Error: {str(e)}")

    except tweepy.errors.Unauthorized as e:
        print("\nAuthentification Error:")
        print(f"Error: {str(e)}")

    except Exception as e:
        print(f"\nError: {str(e)}")

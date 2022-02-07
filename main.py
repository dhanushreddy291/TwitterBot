import tweepy, os
from dotenv import load_dotenv
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
auth.set_access_token(os.getenv('access_token'), os.getenv('access_secret'))
api = tweepy.API(auth)

api.update_status("Tweeting, using my VSCode")

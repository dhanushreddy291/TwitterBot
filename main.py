import tweepy, os
from dotenv import load_dotenv
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
auth.set_access_token(os.getenv('access_token'), os.getenv('access_secret'))
api = tweepy.API(auth)

media = api.media_upload("CuteCat.gif")
tweet = ""
if api.update_status(status=tweet, media_ids=[media.media_id]) is not None:
    print("Successfully Tweeted")

import tweepy, os, urllib.request
from PIL import Image
from dotenv import load_dotenv
from datetime import datetime
from flask import Flask
load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
    auth.set_access_token(os.getenv('access_token'), os.getenv('access_secret'))
    api = tweepy.API(auth)
    urllib.request.urlretrieve("https://cataas.com/cat/gif", "CuteCat.gif")
    media = api.media_upload("CuteCat.gif")
    if api.update_status(status="", media_ids=[media.media_id]) is not None:
        return "The, Tweet was successful " + datetime.now().strftime("%H:%M:%S")
    else:
        return "Tweet was not successful"

app.run()
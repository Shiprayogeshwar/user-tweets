# The third party stuff
from flask import Flask, jsonify
import tweepy

# The project stuff
from testingpro.schemas import TweetSchema

app = Flask(__name__)
app.config.from_object('config')

# These config variables come from 'config.py'
auth = tweepy.OAuthHandler(app.config['TWITTER_CONSUMER_KEY'],
                           app.config['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(app.config['TWITTER_ACCESS_TOKEN'],
                      app.config['TWITTER_ACCESS_TOKEN_SECRET'])
tweepy_api = tweepy.API(auth)


# Schema for Serializing/Deserializing Tweet objects
tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)


# API to list tweets of a given user
@app.route("/tweets/<string:screen_name>/", methods=['GET', ])
def show_tweets(screen_name):
    try:
        tweets = tweepy_api.user_timeline(screen_name=screen_name)
    except Exception as e:
        return str(e)
        # print("Sorry tweets can't be retrieved.")
    result = tweets_schema.dump(tweets)
    return jsonify(result.data)
import tweepy
from textblob import Textblob



consumer_key = '461Pxh0GbzIuLgJs1tPOzS5xW'
consumer_secret = '7LKCrBYWrCjzoXOxqevscjyVtjo4MM1m5C9wlgd4x8LfVqVOTl'

access_token = '848494246772527108-Mz0oKMub1gbfblZCfwnTgK1J5GuKkhh'
access_token_secret = 'KqNt488DD3yer4AscTUY2BAViy92sCL6sIOu0laj2Mh8Q'

# Authorization to consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)

 # Calling api 
api = tweepy.API(auth)  

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = Textblob(tweet.text)
	print(analysis.sentiment)


import tweepy
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from IPython.core.display import display

consumer_key = '461Pxh0GbzIuLgJs1tPOzS5xW'
consumer_secret = '7LKCrBYWrCjzoXOxqevscjyVtjo4MM1m5C9wlgd4x8LfVqVOTl'

access_token = '848494246772527108-Mz0oKMub1gbfblZCfwnTgK1J5GuKkhh'
access_token_secret = 'KqNt488DD3yer4AscTUY2BAViy92sCL6sIOu0laj2Mh8Q'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.search('Cyclone Vayu', count=200)


data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

display(data.head(10))


print(tweets[0].created_at)

import nltk
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()


listy = []

for index, row in data.iterrows():
  ss = sid.polarity_scores(row["Tweets"])
  listy.append(ss)
  
se = pd.Series(listy)
data['polarity'] = se.values

display(data.head(100))

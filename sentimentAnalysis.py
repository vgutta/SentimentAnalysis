import tweepy
from textblob import TextBlob

#Authenticate
consumer_key= 'h5sHb1mjXtQotMlQhUgldfW10'
consumer_secret= 'IlQRVCwIBh85q8h82vtyTNxh24rOVqfU3v83u8sMY2CnpdJYNc'

access_token='139280535-IloPxMxVd3x5X4sR4F7XFMXjOmFfM7Ex5kY7eZXs'
access_token_secret='g9ndatJ1SHkovCCQLjQVfEYpSjmTse0zHxEZ0ezKE6Men'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.search(input("What do you want to analyze on Twitter? (wrap your text in quotes):  "))

for tweet in tweets:
    print(tweet.text)

    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
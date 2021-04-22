import tweepy as twitterbot
import keys
import time
import datetime

auth = twitterbot.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)
api = twitterbot.API(auth)


def twitter_bot(hashtag, delay):
    while True:
        print(f'\n{datetime.datetime.now()}\n')
        for tweet in twitterbot.Cursor(api.search, q=hashtag, rpp=100).items(2):
            try:
                tweet_id = dict(tweet._json)["id"]
                tweet_text = dict(tweet._json)["text"]
                print("id" + str(tweet_id))
                print("text" + str(tweet_text))
                api.retweet(tweet_id)
            except twitterbot.TweepError as error:
                print(error.reason)
        time.sleep(delay)


twitter_bot("#100DaysOfCode", 5)

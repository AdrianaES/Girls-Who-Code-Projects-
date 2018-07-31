import tweepy
import random
CONSUMER_KEY    = '84xG97HASQy8mhIPi13E1lN85'
CONSUMER_SECRET = 'Czbu3T8UpKnQlhQjh9pvlqNRfTde3fBG68AlfSaM7upuSyJIpS'

ACCESS_TOKEN    = '1017155250308853766-mtw3cXuUrYUWzqN1y3JNurjffc6ats'
ACCESS_SECRET   = 'cIW0pZj2dkt2xYs7ObKSu4b59UichIMtrZS6niHmXvgKE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

tweets = ["Hello.", "Come here often?", "Nice weather we're having."]

count = 0
DMB_tweets = api.user_timeline("dailymemebot")

last_tweet = DMB_tweets[0].text
while True:
    DMB_tweets = api.user_timeline("dailymemebot")
    if DMB_tweets[0].text != last_tweet:
        last_tweet = DMB_tweets[0].text
        index = random.randint(0, len(tweets) - 1)
        api.update_status("@dailymemebot " + tweets[index] + str(count))

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity_values = []

for tweet in tweetData:
    tb = TextBlob(tweet["text"])
    print("{}: {}".format((tweet["text"]), tb.polarity))
    polarity_values.append(tb.polarity)

plt.hist(polarity_values)
plt.title("Tweet Polarity")
plt.xlabel("Polarity")
plt.ylabel("Count of Tweets")
plt.show()

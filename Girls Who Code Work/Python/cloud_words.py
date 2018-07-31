import json
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
tweets = []

for tweet in tweetData:
    tweets.append(tweet["text"])

giant_string = " ".join(tweets)
tb = TextBlob(giant_string)
list_of_words = giant_string.split()

positive = []
negative = []
neutral = []

for word in list_of_words:
    word = word.lower().rstrip().lstrip()
    if "http" in word:
        continue
    if word[0] in {",", ".", "?", "!," ":", "/", "'", '""', '#', '@'}:
        word = word[1:]
    if len(word) < 4:
        continue
    if word[-1] in {",", ".", "?", "!," ":", "/", "'", '""'}:
        word = word[:-1]
    word_polarity = TextBlob(word).polarity
    if word_polarity < -0.25:
        negative.append(word)
    elif word_polarity > 0.25:
        positive.append(word)
    else:
        neutral.append(word)

positive_word_count = {}
neutral_word_count = {}
negative_word_count = {}


for word in positive:
    positive_word_count[word] = positive_word_count.get(word, 0) + 1

for word in neutral:
    neutral_word_count[word] = neutral_word_count.get(word, 0) + 1

for word in negative:
    negative_word_count[word] = negative_word_count.get(word, 0) + 1

word_count_2 = {}
for word, count in word_count.items():
    if count < 2:
        continue
    else:
        word_count_2[word] = count

print(positive, neutral, negative)


# wordcloud = WordCloud().generate_from_frequencies(word_count_2)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.show()

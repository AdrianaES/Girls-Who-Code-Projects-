import json

file = open("tweets.json", "r")
data = json.load(file)

for d in data:
    # for info_category, info in d.items():
    #     print(info_category, info)

    for user_mention in d["user_mentions"]:
        print("Screen Name: ", user_mention["screen_name"])
        print("Text: ", d["text"])
        print("Favorites Count: ", d["user"]["favourites_count"])
        print("Retweets Count: ", d["retweet_count"])
    break

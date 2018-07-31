import json
file = open("answers.json", "r")
data = json.load(file)
print(data)

print("Least and Most Hours of Sleep in Participants:")
sleep_sort = sorted(data, key=lambda k: int(k["sleep"]))
print("Least: {}".format(sleep_sort[0]["sleep"]))
print("Most: {}".format(sleep_sort[-1]["sleep"]))

sign_count = {}

for d in data:
    sign_count[d["sign"]] = sign_count.get(d["sign"], 0) + 1
print ("Frequency of Zodiac Signs in Participants:")

for sign, count in sign_count.items():
    print("{}: {}".format(sign, count))
print()

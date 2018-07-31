def translate_shorthand(dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)

abbr = {
"lol" : "League of Legends",
"wow" : "World of Warcraft",
"smh" : "Shaking my head",
"imo" : "In my opinion",
"gwcsip" : "Girls Who Code Summer Immersion Program"
}

translate_shorthand(abbr)

story = """
Stacy was texting . She said lol noobs . smh . imo wow is better .
Are you going to the gwcsip this summer ?
"""

story_list = story.split()
print(story.split())

new_story_list = []
for words in story_list:
    if word in abbr.keys():
        new_story_list.append(abbr[word])
    else:
        new_story_list.append(word)
print(new_story_list)
print(" ".join(new_story_list))

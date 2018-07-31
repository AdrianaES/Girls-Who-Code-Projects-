# Question: What type of broadway is the most popular(sells the most)?
import broadway
import matplotlib.pyplot as plt
import numpy as np
list_of_production = broadway.get_shows()

broadway_types = []
musical_count = 0
play_count = 0
special_count = 0

for production in list_of_production:
    if production["Show"]["Type"] == "Play":
        play_count = play_count + 1
    if production["Show"]["Type"] == "Musical":
        musical_count = musical_count + 1
    if production["Show"]["Type"] == "Special":
        special_count = special_count + 1

broadway_types.append(musical_count)
broadway_types.append(play_count)
broadway_types.append(special_count)
print(musical_count, play_count, special_count)

objects = ("Musicals", "Plays", "Specials")
y_pos = np.arange(len(objects))

plt.bar(y_pos, broadway_types, align="center", alpha=1.0)
plt.title("Types of Broadways")
plt.xticks(y_pos, objects)
plt.ylabel("Number of Sales")
plt.show()

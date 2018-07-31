import json
import os

list_of_responses = []

questions = {"age": "How old are you?", "sleep": "How many hours of sleep do you usually get?", "sign": "What is your zodiac sign?"}

next_person = True

while next_person:
    responses = {}
    for category, question in questions.items():
        responses[category] = input(question)
    yes_or_no = input("Next person? Y/N ")

    if yes_or_no == "Y" or yes_or_no == "y":
        next_person = True
    elif yes_or_no =="N" or yes_or_no == "n":
        next_person = False

    list_of_responses.append(responses)

    if next_person == False:
        print(list_of_responses)

if os.path.isfile("answers.json"):
    file = open("answers.json", "r+")
    old_data = json.load(file)
    old_data.extend(list_of_responses)
    file.write(json.dumps(old_data))
    file.close()
else:
    file = open("answers.json", "w")
    file.write(json.dumps(list_of_responses))
    file.close()

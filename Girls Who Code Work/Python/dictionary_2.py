ages = {
'Sophia': 13,
'Isha': 16,
'Tish': 32,
'Ray': 34
}

print("These are the ages of some of my friends and family members:")

for key, value in ages.items():
    print(key,value)

average = sum(ages.values())/len(ages)
print("The average of these ages is... ")
print(average)

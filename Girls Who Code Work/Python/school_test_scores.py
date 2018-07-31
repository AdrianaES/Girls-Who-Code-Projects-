import school_scores
list_of_record = school_scores.get_all()

print(list_of_record)

for record in list_of_record:
    print(record["GPA"]["B"]["Verbal"])

mylist = [2,3,1,3,5]
has_duplicates = False

mylist.sort()

print()
for index in range(len(mylist) - 1):
    print("index: {}, element: {}".format(index, mylist[index]))
    print(mylist[index])

    if mylist[index] == mylist[index + 1]:
        has_duplicates = True
        break

print(has_duplicates)

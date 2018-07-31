def letter_frequency(word):
    frequency = {}

    for character in word:
        if character in frequency.keys():
            frequency[character] = frequency[character] + 1
        else:
            frequency[character] = 1
    print(frequency)
    
letter_frequency("pen pineapple apple pen")

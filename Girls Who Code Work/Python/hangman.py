def display(word, guessed_letters):
    new_str = ""
    for letter in phrase:
        if letter in guessed_letters:
            new_str += letter
        elif letter == " ":
            new_str += "  "
        else:
            new_str += "_ "
    print(new_str)
    return(new_str)

#Have a word/phrase
phrase = "girls who code"
#Keep track of user's guesses
guessed_letters = []
game_over = False

#Keep track of bad letters
bad = []
#Keep track of good letters
good = []

beginning = display(phrase, guessed_letters)
print(beginning)

while game_over != True:
    #Allow user to give input to computer
    guess = input("Enter a letter:")
    #Tell the user if they get the right letter
    if guess in phrase:
        print("You got a letter: {}".format(guess))
    #Tell the user if they get the worng letter
    else:
        print("{} is not in the phrase.".format(guess))
    #Add the guessed letter to our list of guessed letters
    guessed_letters.append(guess)

    wakeup = display(phrase, guessed_letters)
    print(wakeup)

if "_" in display:
    game_over = False
else:
    game_over = True

print("You Win!!")
#End the game if the user gets all the right letters in the word/phrase

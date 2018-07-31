import random

def computer_value():
    random_guess = random.randint(1,10)
    print("{}".format(computer_value))
    user_guess = input("Is this number even or odd?")
    if random_guess % 2 == 0 and user_guess == "even":
        print("Correct!")
    elif random_guess % 2 != 0 and user_guess == "odd":
        print("Correct!")
    elif random_guess % 2 == 0 and user_guess == "odd":
        print("Wrong!")
    elif random_guess % 2 != 0 and user_guess == "even":
        print("Wrong!")

computer_value()

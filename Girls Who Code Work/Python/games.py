#Guess The Number
import random

def guessthenumber():

    print ("What number am I thinking of? HINT: It is between 1 and 20.")

    def number_guess():
      random.randint(1,20)
      return random.randint(1,20)

    number_guess()
    computer_guess = number_guess()
    guess = int(input("Guess:"))

    while guess != computer_guess:
      if guess < computer_guess:
          print ("Guess higher:")
      elif guess > computer_guess:
          print("Guess lower:")
      else:
          print("You got it! Congradulations!")

#Rock Paper Scissors
import random

def rockpaperscissors():

    gestures = ["rock", "paper", "scissors"]

    computer = random.choice(gestures)

    move = input("Your Move: ")
    choices = ["rock", "paper", "scissors"]

    if move in choices:
        print("Computer chooses {}".format(computer.upper()))
    else:
        print("ERROR 404: Response Not Found")

    if computer == move:
        print("TIE")
    elif computer == "rock" and move == "paper" or computer =="paper" and move == "scissors" or computer == "scissors" and move == "rock":
        print("You Win!")
    elif computer == "paper" and move == "rock" or computer =="scissors" and move == "paper" or computer == "rock" and move == "scissors":
        print("You Lose!")

#Even or Odd
import random

def evenorodd():

    random_guess = random.randint(1,10)
    print("{}".format(random_guess))
    user_guess = input("Is this number even or odd?")
    if random_guess % 2 == 0 and user_guess == "even":
        print("Correct!")
    elif random_guess % 2 != 0 and user_guess == "odd":
        print("Correct!")
    elif random_guess % 2 == 0 and user_guess == "odd":
        print("Wrong!")
    elif random_guess % 2 != 0 and user_guess == "even":
        print("Wrong!")
    else:
        print("ERROR 404: Response Not Found")

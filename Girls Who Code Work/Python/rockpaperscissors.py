import random

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

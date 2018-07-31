import random

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

import games

available_games = ["Guess The Number", "Rock Paper Scissors", "Even or Odd"]

def display_games():
    for g in available_games:
        print(g)

def evaluate_choice():
    player_choice = input("""Welcome to the Online Arcade. Here you can play
    Guess The Number, Rock-Paper-Scissors, or Even or Odd.
    Just type 'gtn', 'rps', or 'eo'""")
    if player_choice == "gtn":
        games.guessthenumber()
    if player_choice == "rps":
        games.rockpaperscissors()
    if player_choice == "eo":
        games.evenorodd()
    else:
        print("ERROR 404: Response Not Found")
def main():
    repeat = True
    while repeat:
        display_games()
        evaluate_choice()
        play_again = input("Play again? (y/n)")
        if play_again == "y":
            repeat = True
        else:
            repeat = False
            print("Goodbye!")

if __name__ == "__main__":
    main()

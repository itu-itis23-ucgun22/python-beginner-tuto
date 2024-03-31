import random 

def get_choices():
  player_choice = input("enter one choice (rock,scissors,paper): ")
  options=["rock","scissors","paper"]
  com_choice = random.choice(options)
  choices = {"player" : player_choice, "computer":com_choice}
  return choices

def check_win(player,computer):
  print("You chose" + player + "computer chose" + computer)
  if player == computer:
    return "It's a tie"
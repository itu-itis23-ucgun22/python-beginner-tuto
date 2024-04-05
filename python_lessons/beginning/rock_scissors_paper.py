import random 

def get_choices():
  player_choice = input("enter one choice (rock,scissors,paper): ")
  options=["rock","scissors","paper"]
  com_choice = random.choice(options)
  choices = {"player" : player_choice, "computer":com_choice}
  return choices

def check_win(player,computer):
  print(f"You chose {player} computer chose {computer}")
  if player == computer:
    return "It's a tie"
  elif player == "rock":
    if computer == "paper":
      return "you lose"
    else: 
      return "you win"
  elif player == "paper":
    if computer == "scissors":
      return "you lose"
    else: 
      return "you win"
  elif player == "scissors":
    if computer == "rock":
      return "you lose"
    else: 
      return "you win"

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
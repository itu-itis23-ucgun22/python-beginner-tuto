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
  elif player == "rock" and computer == "scissors":
    return "You win"
  elif player == "scissors" and computer == "paper":
    return "You win"
  elif player == "scissors" and computer == "rock":
    return "You lose"
  elif player == "rock" and computer == "paper":
    return "You lose"
  elif player == "paper" and computer == "scissors":
    return "you lose"
  elif player == "paper" and computer == "rock ":
    return "you win"
  else:
    return "invalid choice"


check_win("rock","paper")
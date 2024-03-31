import random 

def get_choices():
  player_choice = input("enter a choice(rock,scissors,paper): ")
  options=["rock","scissors","paper"]
  com_choice = random.choice(options)
  choices = {"player" : player_choice, "computer":com_choice}
  return choices

choices = get_choices()
print(choices)
import random

<<<<<<< HEAD

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: select = ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player} computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You Win!"
        else:
            return "Paper covers rock! You Lose."
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cut paper! You Lose."
        else:
            return "Paper covers rock! You Win!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You Lose."
        else:
            return "Scissors cut paper! You Win."

=======
def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: select = ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player} computer chose {computer}.")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You Win!"
    else:
      return "Paper covers rock! You Lose." 
  elif player == "paper": 
    if computer == "scissors":
      return "Scissors cut paper! You Lose."
    else:
      return "Paper covers rock! You Win!"
  elif player == "scissors": 
    if computer == "rock":
      return "Rock smashes scissors! You Lose."
    else:
      return "Scissors cut paper! You Win."
>>>>>>> 4a8306bef4bd504093e1fb90f1bc80aec7ee50dc

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

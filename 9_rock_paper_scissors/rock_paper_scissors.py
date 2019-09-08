from random import randint

player = input("rock, paper, or scissors? ")
player = player.lower()

choices = ["rock", "paper", "scissors"]
random_number = randint(0, 2)
computer = choices[random_number]
print(f"The computer played: {computer}")

if player:
  if player == computer:
    print("Tie!")
  elif player == "rock":
    if computer == "scissors":
      print("You win!")
    else:
      print("Computer wins!")
  elif player == "paper":
    if computer == "rock":
      print("You win!")
    else:
      print("Computer wins!")
  elif player == "scissors":
    if computer == "paper":
      print("You win!")
    else:
      print("Computer wins!")
  else:
    print("What's that? Rock, paper, or scissors only!")
else:
  print("You didn't choose rock, paper, or scissors!")
from random import randint

# collect player choice
player = input("rock, paper, or scissors? ")
player = player.lower()

# generate computer choice from list and print choice
choices = ["rock", "paper", "scissors"]
random_number = randint(0, 2)
computer = choices[random_number]
print(f"The computer played: {computer}")


# if player isn't blank and correct choice made
  # print player wins if rock/scissors, paper/rock, scissors/paper
  # else print computer wins
# if player is blank or incorrect choice made, print error message
if player and (player == "rock" or player == "paper" or player == "scissors"):
  if player == computer:
    print("Tie!")
  elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
      print("You win!")
  else:
    print("Computer wins!")
else:
  print("You didn't choose rock, paper, or scissors!")
from random import randint

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    print(f"Player: {player_wins} | Computer: {computer_wins}")

    player = input("rock, paper, or scissors? ").lower()

    choices = ["rock", "paper", "scissors"]
    random_number = randint(0, 2)
    computer = choices[random_number]
    print(f"The computer plays: {computer}")

    if player and (player == "rock" or player == "paper" or player == "scissors"):
        if player == computer:
            print("Tie!")
        elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
            print("You win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    else:
            print("You didn't choose rock, paper, or scissors!")

print(f"FINAL SCORE... Player: {player_wins} | Computer: {computer_wins}")
if player_wins > computer_wins:
    print("CONGRATS, YOU WON!")
else:
    print("OH NO! THE COMPUTER WON :(")
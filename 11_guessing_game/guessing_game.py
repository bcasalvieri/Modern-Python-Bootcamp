from random import randint

computer = randint(1, 10)
player = None

while player != computer:
	player = input("Guess a number between 1 and 10: ")
	player = int(player)
	if player < computer:
		print("Too low, try again")
	elif player > computer:
		print("Too high, try again")
	else:
		print("You guessed it! You won!")
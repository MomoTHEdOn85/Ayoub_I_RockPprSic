from random import randint

choices = ["rock", "paper", "scissor"]

# player will be the wepapon the player choose via input
#Bolean values are True and False - you can use these to check state and then programming choicrs based on their value.
player = False

#player = input("Choose your weapon: rock, paper, scissor: ")

#comp = choices[randint(0, 2)]

#these lives need to decrement when a player loses a round
playerLives = 5
compLives = 5

while player is False:

	player = input("Choose your weapon: rock, paper, scissor:")

	comp = choices[randint(0, 2)]

	print("player chose: " + player)
	print("computer chose: " + comp)


	if (comp == player):
		# tie - nothing else to compare, so it'll sxit
		print("tie!!!! try agiain")


	elif (player == "rock"):
		if(comp == "paper"):
			print("you losee!!")
			playerLives = playerLives - 1
		else:
			print("you win")
			compLives = compLives - 1


	elif (player == "paper"):
		if(comp == "scissor"):
			print("you losee!!")
			playerLives = playerLives - 1
		else:
			print("you win")
			compLives = compLives - 1



	elif (player == "scissor"):
		if(comp == "rock"):
			print("you losee!!")
			playerLives = playerLives - 1
		else:
			print("you win")
			compLives = compLives - 1


	print("Player Life count: " + str(playerLives))
	print("Computer Life Count: " + str(compLives))

	player = False




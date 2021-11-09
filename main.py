from random import randint
from gameComponentss import winLose, gameVars



#create an infinite loop (for now) so that we can keep playing
while gameVars.player is False:

	gameVars.player = input("Choose your weapon: rock, paper, scissor:")
	gameVars.comp = gameVars.choices[randint(0, 2)]

	print("player chose: " + gameVars.player)
	print("computer chose: " + gameVars.comp)


	if (gameVars.comp == gameVars.player):
		# tie - nothing else to compare, so it'll sxit
		print("tie!!!! try agiain")


	elif (gameVars.player == "rock"):
		if(gameVars.comp == "paper"):
			print("you losee!!")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("you win")
			gameVars.compLives = gameVars.compLives - 1


	elif (gameVars.player == "paper"):
		if(gameVars.comp == "scissor"):
			print("you losee!!")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("you win")
			gameVars.compLives = gameVars.compLives - 1



	elif (gameVars.player == "scissor"):
		if(gameVars.comp == "rock"):
			print("you losee!!")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("you win")
			gameVars.compLives = gameVars.compLives - 1


	print("Player Life count: " + str(gameVars.playerLives))
	print("Computer Life Count: " + str(gameVars.compLives))

	if gameVars.playerLives == 0:
		# call the winorlose funtion here
		 winorlose("lost")

	elif gameVars.compLives == 0:
		 # call the wineorelose function here
		 winorlose("win")

	gameVars.player = False

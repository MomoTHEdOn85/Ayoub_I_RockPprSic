from gameComponents import gameVars

def compare():
	if (gameVars.comp == gameVars.player):
		# tie - nothing else to compare, so it'll sxit
		print("Tie!!!! Try agiain")


	elif (gameVars.player == "rock"):
		if(gameVars.comp == "paper"):
			print("---------------")
			print("| You Losee!! |")
			print("---------------")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("You Win")
			gameVars.compLives = gameVars.compLives - 1


	elif (gameVars.player == "paper"):
		if(gameVars.comp == "scissor"):
			print("---------------")
			print("| You Losee!! |")
			print("---------------")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("You Win")
			gameVars.compLives = gameVars.compLives - 1


	elif (gameVars.player == "scissor"):
		if(gameVars.comp == "rock"):
			print("---------------")
			print("| You Losee!! |")
			print("---------------")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("You Win")
			gameVars.compLives = gameVars.compLives - 1

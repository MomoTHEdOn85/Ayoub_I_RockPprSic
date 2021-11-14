from gameComponents import gameVars

def compare():
	if (gameVars.comp == gameVars.player):
		# tie - nothing else to compare, so it'll exit
		print("\033[1;37;40m ------------------ ")
		print("|  TIE ! try again |")
		print("\033[1;37;40m ------------------ ")


	elif (gameVars.player == "rock"):
		if(gameVars.comp == "paper"):
			print("\033[1;37;40m  ------------- ")
			print("\033[1;31;40m   You Losee!!  ")
			print("\033[1;37;40m  ------------- ")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("\033[1;37;40m  ------------- ")
			print("\033[1;32;40m    You Win!    ")
			print("\033[1;37;40m  ------------- ")
			gameVars.compLives = gameVars.compLives - 1


	elif (gameVars.player == "paper"):
		if(gameVars.comp == "scissor"):
			print("\033[1;37;40m  ------------- ")
			print("\033[1;31;40m   You Losee!!  ")
			print("\033[1;37;40m  ------------- ")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("\033[1;37;40m  ------------- ")
			print("\033[1;32;40m    You Win!    ")
			print("\033[1;37;40m  ------------- ")
			gameVars.compLives = gameVars.compLives - 1


	elif (gameVars.player == "scissor"):
		if(gameVars.comp == "rock"):
			print("\033[1;37;40m  ------------- ")
			print("\033[1;31;40m   You Losee!!  ")
			print("\033[1;37;40m  ------------- ")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("\033[1;37;40m  ------------- ")
			print("\033[1;32;40m    You Win!    ")
			print("\033[1;37;40m  ------------- ")
			gameVars.compLives = gameVars.compLives - 1

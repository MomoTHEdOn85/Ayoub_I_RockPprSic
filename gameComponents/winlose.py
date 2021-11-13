from gameComponents import gameVars

def winorlose(status):
	print("You " + status + "!. Would you like to play again?")
	choice = input(" y / n ?")

	if choice == "n":
		print("============== Alright. Better Luck Next Time !! ======================")
		exit()
	elif choice == "y":
		gameVars.playerLives = 5
		gameVars.compLives = 5
		gameVars.player = False


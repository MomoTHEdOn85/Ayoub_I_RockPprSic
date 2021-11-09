def winorlose(status):
	print("You" + status + "! Would you like to play again?")
	choice = input(" y / n ?")

	if choice == "n":
		print("===========better luck next time!===========")
		exit()
	else choice == "y":
		# reset and restart the game
		gameVars.playerLives = 5
		gameVars.compLives = 5
		gameVars.player = False

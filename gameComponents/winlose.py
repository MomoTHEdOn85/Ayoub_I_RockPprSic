from gameComponents import gameVars

def winorlose(status):
	print(" You" + status + "\033[1;37;40m !. Would you like to play again?")
	choice = input(" y / n ?")

	if choice == "n":
		print("============== Alright. Better Luck Next Time !! ======================")
		exit()
	elif choice == "y":
		print("---------------------------  OKAY! ------------------------------------")
		print("=======================================================================")
		print("                        LET THE BATTLE BEGIN !!                        ")
		print("=======================================================================")
		gameVars.playerLives = 5
		gameVars.compLives = 5
		gameVars.player = False


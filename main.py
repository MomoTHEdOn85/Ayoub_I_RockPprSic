from random import randint
from gameComponents import winlose, gameVars, comParison

# create an infinite loop (for now) so that we can keep playing

print("=======================================================================")
print("                         LET THE BATTLE BEGIN !!")
print("=======================================================================\n")

while gameVars.player is False:

	gameVars.player = input(" Choose your weapon: rock, paper, scissor:  ")
	gameVars.comp = gameVars.choices[randint(0, 2)]



	print("\033[1;35;40m ==================================")
	print("\033[1;33;40m Player chose: " + gameVars.player)
	print("\033[1;36;40m Computer chose: " + gameVars.comp)
	print("\033[1;35;40m ==================================")

# Game Logic
# Determining Winner
# Comparing player and computer choices and print the result.
	comParison.compare();

	print(" -----------------------------------------------")
	print("\033[1;33;40m Player Life count: " + str(gameVars.playerLives))
	print("\033[1;36;40m Computer Life Count: " + str(gameVars.compLives))
	print("\033[1;37;40m ----------------------------------------------- \n")

	if gameVars.playerLives == 0:
	   winlose.winorlose("\033[1;31;40m Lost")

	elif gameVars.compLives == 0:
	     winlose.winorlose("\033[1;32;40m Win")

	gameVars.player = False

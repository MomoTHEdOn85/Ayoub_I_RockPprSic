from random import randint
from emoji import emojize
from gameComponents import winlose, gameVars, comParison

# create an infinite loop (for now) so that we can keep playing
while gameVars.player is False:

	gameVars.player = input("Choose your weapon: rock, paper, scissor: ")
	gameVars.comp = gameVars.choices[randint(0, 2)]

	print("player chose: " + gameVars.player)
	print("computer chose: " + gameVars.comp)

# Game Logic
# Determining Winner
# Comparing player and computer choices and print the result.
	comParison.compare();

	print("Player Life count: " + str(gameVars.playerLives))
	print("Computer Life Count: " + str(gameVars.compLives))

	if gameVars.playerLives == 0:
	   winlose.winorlose("Lost")

	elif gameVars.compLives == 0:
	     winlose.winorlose("Win")

	gameVars.player = False

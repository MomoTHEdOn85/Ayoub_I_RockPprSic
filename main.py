from random import randint



choices = ["rock", "paper", "scissor"]

# player will be the wepapon the player choose via input
player = input("Choose your weapon: rock, paper, scissor: ")

comp = choices[randint(0, 2)]

print("player chose: " + player)
print("computer chose: " + comp)

if (comp == player):
	# tie - nothing else to compare, so it'll sxit
	print("tie!!!! try agiain")

elif (player == "rock"):
	if(comp == "paper"):
		print("you losee!!")
	else:
		print("you win")


elif (player == "paper"):
	if(comp == "scissor"):
		print("you losee!!")
	else:
		print("you win")


elif (player == "scissor"):
	if(comp == "rock"):
		print("you losee!!")
	else:
		print("you win")


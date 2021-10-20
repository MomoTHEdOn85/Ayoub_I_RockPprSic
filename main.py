from random import randint



choices = ["rock", "paper", "scissor"]

# player will be the wepapon the player choose via input
player = input("Choose your weapon: rock, paper, scissor: ")

comp = choices[randint(0, 2)]

print("player chose: " + player)
print("computer chose: " + comp)



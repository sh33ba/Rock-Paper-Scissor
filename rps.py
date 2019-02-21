#ROCK PAPER SCISSOR
from random import randint

t=["Rock","Paper","Scissors"]
computer = t[randint(0,2)]
player=False

while player == False:
    player=input("Rock, Paper, Scissors?\n")
    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="Paper":
            print("You LOSE ! ",computer," covers ",player)
        else:
            print("You WIN ! ",player," smashes ",computer)
    elif player=="Paper":
        if computer=="Rock":
            print("YOU WIN ! ",player," covers ",computer)
        else:
            print("YOU LOSE ! ",computer," cuts ", player)
    elif player=="Scissors":
        if computer=="Rock":
            print("YOU LOSE ! ",computer," smashes ",player)
        else:
            print("YOU WON ! ",player," cuts ",computer)
    else:
        print("INVALID INPUT !!! CHECK YOUR SPELLING!")

player=False
computer=t[randint(0,2)]




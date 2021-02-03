from modules.classes import Player
import time

go_on = True
while go_on:

    name_chosen = False
    while not name_chosen:
        name = input("Please enter a name : ")
        print("You entered", name)
        choice = input("Is this the name you want ? Y | N")
        if choice.upper() == "Y":
            name_chosen = True
            player = Player(name.capitalize(), 10, 20, 10, 1)
            break
        elif choice.upper() == "N":
            name_chosen = False

        else:
            go_on = False


print("Player name is", player.name)

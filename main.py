from modules.classes import Player
import time

#  get name
def intro_text():

    print(
        "\nOut exploring , you stumble upon an entrance in the middle of the woods...",
        "\nCurios,you peek inside,you hear faint sounds of someone sobbing...and someone else...screaming!...",
    )
    input("\n... enter ...")
    time.sleep(0.5)
    print(
        "\nYou enter shakingly and the door behind you slams shut !",
        "\nYou panic! and as your eyes begin to adjust to the darkness you can see the faint outline of what appears to be a maze...",
    )
    time.sleep(0.5)
    print("\nYou notice something glimmering in the dark and walk towards it...")
    time.sleep(0.5)
    input("\n...forward...")

    time.sleep(0.5)
    print(
        "\nIt's a sword!",
        "\n"
        "\nYou grip it firmly and push forward..."
        "\nYou arrive at an intersection..."
        "\n...the stench of rotting corpses fills the air...",
    )
    time.sleep(0.5)
    input("\n...push on...")


def player_class(c):

    if c == 1:
        player = Player(name.capitalize(), 5, 20, 10, 1)

    elif c == 2:
        player = Player(name.capitalize(), 10, 15, 5, 1)

    elif c == 3:
        player = Player(name.capitalize(), 15, 10, 5, 1)
    elif c == 4:
        player = Player(name.capitalize(), 20, 10, 0, 1)

    else:
        pass


while True:

    name = input("Please enter a name : ")

    print("You entered", name.capitalize())

    choice = str(input("Is this the name you want ? Y | N : "))

    if choice.upper() == "Y":
        name_chosen = True
        go_on = True

        break

    elif choice.upper() == "N":
        name_chosen = False

    else:
        continue

# class selection

while True:

    print("\nPlease select a class ")

    # name, attack, health, defense

    print("\n-------------\n[1]\nWarrior\nAttack:5\nHealth:20\nDefense:10")
    print("-------------\n[2]\nMage\nAttack:10\nHealth:15\nDefense:5")
    print("-------------\n[3]\nArcher:15\nHealth:10\nDefense:5")
    print("-------------\n[4]\nRogue\nAttack:20\nHealth:10\nDefense:0")
    print("-------------")

    class_choice = int(input("\nEnter your choice : "))

    if class_choice in range(4):
        pass
    else:
        continue

    sure = input("\nAre you sure ? Y | N : ")

    if sure.upper() == "Y":
        player_class(class_choice)
        break
    else:
        continue


# start the game


intro_text()

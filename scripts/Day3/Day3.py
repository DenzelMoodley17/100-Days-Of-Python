print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Game message start
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

initial_direction = input("You are at a crossroad Left or Right? ")
# Nested If statement to evaluate ability to create and manage them
if initial_direction == "Left":
    print("\nYou end up near a lake and across it is Treasure Island.")
    second_choice = input("Do you Swim accross or Wait? ")
    if second_choice == "Wait":
        print("\nA boat collects you and drops you off on the Island.")
        door = input("There are 3 doors on the Island. Red, Blue, or Yellow.\nPick 1. ")

        # If and elif statements to allow for multiple different results based on the selected door.
        if door == "Red":
            print('\nRoom is filled with Fire.\nGAME OVER')
        elif door == "Blue":
            print("\nRoom is filled with Beasts.\nGAME OVER")
        elif door == "Yellow":
            print("\nYou found the treasure.\nYOU WIN")
        else:
            print("GAME OVER")
    else:
        print("\nAttacked by a killer Trout.\nGAME OVER")
        
else:
    print("\nYou fall into a hole.\nGAME OVER")

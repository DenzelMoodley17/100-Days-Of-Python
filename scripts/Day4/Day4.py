import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to the Rock, Paper, Scissors match.\n")
print("Select 0 for Rock, 1 for Paper, 2 for Scissors\n")

user_choice = int(input("Choose 0, 1 or 2? \n"))
random_choice = random.randint(0, 2)

if user_choice == 0:

    print(Rock)

    if random_choice == 1:
        print(Paper)
        print("\nYou lose")
    elif random_choice == 2:
        print(Scissors)
        print("\nYou win")
    else:
        print(Rock)
        print("\nThis is a draw")

elif user_choice == 1:
    print(Paper)
    if random_choice == 1:
        print(Paper)
        print("\nThis is a draw")
    elif random_choice == 2:
        print(Scissors)
        print("\nYou lose")
    else:
        print(Rock)
        print("\nYou win")
elif user_choice == 2:
    print(Scissors)
    if random_choice == 1:
        print(Paper)
        print("\nYou win")
    elif random_choice == 2:
        print(Scissors)
        print("\nThis is a draw")
    else:
        print(Rock)
        print("\nThis lose")
else:
    print("Invalid input you lose")

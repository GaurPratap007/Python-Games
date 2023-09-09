rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random

play = 1
while (play!=0):
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    choice = int(choice)
    cpu_choice = random.randint(0, 2)
    print("Computer Chose:")
    if cpu_choice == 0:
        print(rock)
    elif cpu_choice == 1:
        print(paper)
    else:
        print(scissors)
    print("You Chose:")
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)
    if choice == cpu_choice:
        print("It's a draw!")
    elif choice == 0 and cpu_choice == 2:
        print("You win!")
    elif choice == 1 and cpu_choice == 0:
        print("You win!")
    elif choice == 2 and cpu_choice == 1:
        print("You win!")
    else:
        print("You lose!")
    play = input("Do you want to play again? Type 1 for yes or 0 for no.\n")
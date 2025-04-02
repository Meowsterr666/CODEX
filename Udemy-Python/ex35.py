import random

choices = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""", ]

com_choice = str(int(random.random() * 3))
user_choice = input("Choose..? 0 for Rock, 1 for Paper or 2 for Scissors! \n\n Your choice: ")

if user_choice == "0" and com_choice == "0":
    print(f" \nRock!\n {choices[0]}")
    print(f"Computer choice: {com_choice}")
    print(f"\nRock!\n {choices[int(com_choice)]}")
    print("A draw?!")
elif user_choice == "0" and com_choice == "1":
    print(f" \nRock!\n {choices[0]}")
    print(f"Computer choice: {com_choice}")
    print(f"\nPaper!\n {choices[int(com_choice)]}")
    print("You lose!")
elif user_choice == "0" and com_choice == "2":
    print(f" \nRock!\n {choices[0]}")
    print(f"Computer choice: {com_choice}")
    print(f"\nScissors!\n {choices[int(com_choice)]}")
    print("You win!")
elif user_choice == "1" and com_choice == "0":
    print(f" \nPaper!\n {choices[1]}")
    print(f"Computer choice: {com_choice}")
    print(f"\nRock!\n {choices[int(com_choice)]}")
    print("You win!")
elif user_choice == "1" and com_choice == "1":
    print(f" \nPaper!\n {choices[1]}")
    print(f"Computer choice: {com_choice}")
    print(f"\nPaper!\n {choices[int(com_choice)]}")
    print("A draw..")
elif user_choice == "1" and com_choice == "2":
    print(f" \nPaper!\n {choices[1]}")
    print(f"Computer choice: {com_choice}")
    print(f"\nScissors!\n {choices[int(com_choice)]}")
    print("You lose!")
elif user_choice == "2" and com_choice == "0":
    print(f" \nScissors!\n {choices[2]}")
    print(f"Computer choice: {com_choice}")
    print(f"\nRock!\n {choices[int(com_choice)]}")
    print("You lose!")
elif user_choice == "2" and com_choice == "1":
    print(f" \nScissors!\n {choices[2]}")
    print(f"Computer choice: {com_choice}")
    print(f"\nPaper!\n {choices[int(com_choice)]}")
    print("You win!")
elif user_choice == "2" and com_choice == "2":
    print(f" \nScissors!\n {choices[2]}")
    print(f"Computer choice: {com_choice}")
    print(f"\nScissors!\n {choices[int(com_choice)]}")
    print("It's a draw!")
else:
    print("\nInvalid Input\n")
    
"""
The code above is my solution to this interactive. 
I didn't think about the invalid input print, 
till I finished it until I've seen it in the solution, 
haha.
""" 
# The bottom code is part of Angela's ex. 35 solution

# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """

# paper = """
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# """

# scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """

# game_images = [rock, paper, scissors]

# user_choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# if user_choice1 >= 0 and user_choice1 <= 2:
#     print(game_images[user_choice1])
# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice1 >= 3 or user_choice1 < 0:
#     print("You typed an invalid number. You lose!")
# elif user_choice1 == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice1 == 2:
#     print("You lose!")
# elif computer_choice > user_choice1:
#     print("You lose!")
# elif user_choice1 > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice1:
#     print("It's a draw!")
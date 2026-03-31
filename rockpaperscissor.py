import random

print("Welcome to Python Rock, Paper and Scissors Tournament!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: "))

# Validate input
if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lost!")
    exit()

print("\nYou chose:")
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("\nComputer chose:")
print(game_images[computer_choice])

# Game logic
if user_choice == computer_choice:
    print("\nIt's a draw!")
elif user_choice == 0 and computer_choice == 2:
    print("\nYou win!")
elif user_choice == 1 and computer_choice == 0:
    print("\nYou win!")
elif user_choice == 2 and computer_choice == 1:
    print("\nYou win!")
else:
    print("\nYou lose!")

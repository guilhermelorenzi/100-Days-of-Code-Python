import random

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

# user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

# computer choice
computer_choice = random.randint(0,2)
if user_choice >= 0 and user_choice <= 2:
    print(f"Computer chose:")
    print(game_images[computer_choice])

# who wins

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == computer_choice:
    print("Draw!")
elif user_choice == 0 and computer_choice == 2: # Rock wins against scissors.
    print("You win! :D")
elif user_choice == 2 and computer_choice == 1: # Scissors win against paper.
    print("You win! :D")
elif user_choice == 1 and computer_choice == 0: # Paper wins against rock.
    print("You win! :D")

elif user_choice == 2 and computer_choice == 0: # Rock wins against scissors.
    print("You lose! :(")
elif user_choice == 1 and computer_choice == 2: # Scissors win against paper.
    print("You lose! :(")
elif user_choice == 0 and computer_choice == 1: # Paper wins against rock.
    print("You lose! :(")
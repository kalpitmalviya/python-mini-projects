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

import random

images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

if user_choice >= 0 and user_choice < 3:
    print(images[user_choice])

else:
    print("Invalid Choice !!")
    exit()

print("computer chose: ")
print(computer_choice)
print(images[computer_choice])

if user_choice == computer_choice:
    print(user_choice)
    print("It's Draw :| ")
elif user_choice == 0 and computer_choice == 2:
    print("You Win :) ")
elif user_choice == 1 and computer_choice == 0:
    print("You Win :) ")
elif user_choice == 2 and computer_choice == 1:
    print("You Win :)")
elif computer_choice == 2 and user_choice == 1:
    print("You Lose :(")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose :( ")
elif computer_choice == 1 and user_choice == 0:
    print("You Lose :( ")


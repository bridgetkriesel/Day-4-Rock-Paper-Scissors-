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

#Write your code below this line 👇

#figure out who lost 
#choose a random item 

import random
selection = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if human_choice >= 3 or human_choice < 0:
  print("You type an invalid number, you lose!")
print(selection[human_choice])

computer_choice = random.randint(0,2)
print(f"Computer Chose:")
print(selection[computer_choice])

#Rock beats Scissors (0 beats 2)
#Scissors beats paper ( 2 beats 1)
#Paper beats rock (1 beats 0)
#Rock = 0
#Paper = 1
#Scissors = 2

if human_choice == 0 and computer_choice == 0:
  print("You Tie!")
elif human_choice == 1 and computer_choice == 1:
  print("You Tie!")
elif human_choice == 2 and computer_choice == 2:
  print("You Tie!")
elif human_choice == 0 and computer_choice == 2:
  print ("You Win!")
elif human_choice == 2 and computer_choice == 1:
  print ("You Win!")
elif human_choice == 1 and computer_choice == 0:
  print ("You Win!")
elif human_choice == 2 and computer_choice == 0:
  print ("You Lose!")
elif human_choice == 1 and computer_choice == 2:
  print ("You Lose!")
elif human_choice == 0 and computer_choice == 1:
  print ("You Lose!")
else:
  print("Try again.")








import random
from collections import Counter
from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Rock, Paper, Scissors               *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

print("Welcome to the Rock, Paper Scissors game!\n")


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
---'    ____)____
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

rps = [('rock',rock), ('paper',paper),('scissors',scissors)]  # Created a tuple with key value pairing

player_choice = input("Please select 'R' for Rock, 'P' for Paper or 'S' for Scissors ").lower()

if player_choice == 'r':
    print(f"\n{Fore.YELLOW}You chose rock:{rock}{Style.RESET_ALL}")
    player_choice = rock

elif player_choice == 'p':
    print(f"\n{Fore.RED}You chose paper:{paper}{Style.RESET_ALL}")
    player_choice = paper

elif player_choice == 's':
    print(f"\n{Fore.BLUE}You chose scissors:{scissors}{Style.RESET_ALL}")
    player_choice = scissors

else:
    print("Please choose r, p, or s only, thankyou...\n")

computer_choice = random.choice(rps)

print(f"Computer choose:{Fore.RED} {computer_choice[0]}\n{computer_choice[1]}{Style.RESET_ALL}")


if player_choice == rock:
    if computer_choice[0] == 'scissors':
        print("Player Wins!!")
    elif computer_choice[0] == 'paper':
        print("Computer Wins!!")
    else:
        print("Its a tie!")

if player_choice == paper:
    if computer_choice[0] == 'scissors':
        print("Computer Wins!!")
    elif computer_choice[0] == 'rock':
        print("Computer Wins!!")
    else:
        print("Its a tie!")

if player_choice == scissors:
    if computer_choice[0] == 'paper':
        print("Player Wins!!")
    elif computer_choice[0] == 'rock':
        print("Computer Wins!!")
    else:
        print("Its a tie!")


###############################################################################################
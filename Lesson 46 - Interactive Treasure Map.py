import random
from collections import Counter
from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Interactive Treasure Map           *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

print("Welcome to the Interactive 3 by 3 Treasure Map!")

row1 = ['🎸','🎸','🎸']
row2 = ['🎸','🎸','🎸']
row3 = ['🎸','🎸','🎸']
row4 = ['🎸','🎸','🎸']
row5 = ['🎸','🎸','🎸'] # Detailing by hand the nested lists

map = [row1, row2, row3,row4,row5] # Here, map is a var that contains the nested lists
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}") # Here print f prints out to screen nicely formatted map

position = input("Where would you like to place the treasure? ") # User input query

horizontal = int(position[0]) # Takes 1st num typed by user and places it into the list starting from position 0 - across
vertical = int(position[1]) # Takes 2nd num typed by user and places it into the list starting from position 1 - down

map[vertical - 1][horizontal - 1] = "X" # As treasure map is not Zero based, this takes away 1 position back to adjust for this

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}") # Here print f prints out to screen nicely formatted map

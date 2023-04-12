
import random
from collections import Counter
from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Who'll Pay the bill?               *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

print("Welcome to Who'll pay the bill!")

names_string = input("Please type in everybody's names, separated by a comma , ")
names = names_string.split(",")
print(f"Today,{random.choice(names)} will pay the dinner bill")


import random
from collections import Counter
from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Adding Evens with Range          *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

print("Welcome to the Adding Evens Program.\n")

even_nums_total = 0

for nums in  range(2,101,2): # Need to start range at 2
    even_nums_total += nums
print(f"Total of even numbers added together using step in range is: {even_nums_total}")

########################################################################################################################

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Adding Evens with Range          *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

even_nums = 0
for nums in range(0,101):
    if nums %2 == 0:
        even_nums += nums

print(f"Total of even numbers added together using modulo is: {even_nums_total}")


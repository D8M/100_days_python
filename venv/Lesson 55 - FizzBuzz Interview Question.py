import random
from collections import Counter
from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         FizzBuzz Interview Question        *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

print("Welcome to the FizzBuzz Interview Question.\n")

for nums in range(1,101):
    if nums % 3 == 0 and nums % 5 == 0:
        print("fizzbuzz!")
    elif nums % 3 == 0:
        print("fizz")
    elif nums % 5 == 0:
        print("buzz")
    else:
        print(nums)


########################################################################################################################


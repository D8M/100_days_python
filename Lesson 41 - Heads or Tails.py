import my_module
import random
from collections import Counter
from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Heads or Tails                     *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

print("Welcome to Heads or Tails!")

randNum = random.randint(1,10)

if randNum > 0 and randNum <= 4 and randNum != 5:
    print("Heads!")
if randNum > 5 and randNum <= 10:
    print("Tails")
else:
    print("Coin balanced, try again!")




#print(my_module.pi)
# random_float = random.random()*5
# print(random_float)


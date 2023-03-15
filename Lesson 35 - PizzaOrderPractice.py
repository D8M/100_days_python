import colorama
from colorama import Fore
from colorama import Style

print(f"{Fore.GREEN}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*           Pizza Order Practice             *{Style.RESET_ALL}")
print(f"{Fore.GREEN}**********************************************\n{Style.RESET_ALL}")

size = input("Would you like to order a Small, Medium or Large pizza? Choose S,M or L ")

bill = 0

if size == 'S' or size == 's':
    bill += 15
if size == 'M' or size == 'm':
    bill += 20
if size == 'L' or size == 'l':
    bill += 25
# else:
#    print("Invalid order, try again")

extras = input("Would you like to order pepperoni? Then choose either Y/N ")

if extras == 'Y' or extras == 'y' and size == 'S' or size == 's':
    bill += 2

else:
    bill += 3
# if extras == 'Y' or extras == 'y' and size == 'M' or size == 'm' or size == 'L' or size == 'l':
#   bill += 3

cheese = input("Would you like to order cheese? Then choose either Y/N ")
if cheese == 'Y' or cheese == 'y':
    bill += 1

print(f"Your order total for {size} pizza is: ", bill)


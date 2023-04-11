import colorama
from colorama import Fore
from colorama import Style

print(f"{Fore.GREEN}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*             Odd or Even number             *{Style.RESET_ALL}")
print(f"{Fore.GREEN}**********************************************\n{Style.RESET_ALL}")

numToCheck = float(input("Please enter a number to check and see if its odd or even: "))

if numToCheck % 2 == 0:
    print(numToCheck,"number is even")
else:
    print(numToCheck, "number is odd")

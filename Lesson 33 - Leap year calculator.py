import colorama
from colorama import Fore
from colorama import Style

print(f"{Fore.GREEN}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*           Leap year Calculator             *{Style.RESET_ALL}")
print(f"{Fore.GREEN}**********************************************\n{Style.RESET_ALL}")

whichYear = int(input("Please enter a year: \n"))

if (whichYear % 4 == 0) and (whichYear % 100 != 0) or (whichYear % 400 == 0):
    print(whichYear, " is a leap year.\n")
else:
    print(whichYear,"is not a leap year\n")

    # This program checks firstly that whichYear inputted when modded 4, leaves no remainder, AND to see
    #  also that whichYear modded 100 leaves no remainder. So if the first two checks are true then that
    # part of the expression evaluates to true, then the 2nd part of the expression is checked to see
    # if whichYear mod 400 leaves no remainder,then if this is also true then it's a leap year.
    # If any of the checks turn out to be false, then it's not a leap year.


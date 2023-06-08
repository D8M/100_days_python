from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Function with Inputs               *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")


# def greet_with_name(name):
#     print(f"Hello there {name}")
#
#
# name = input("Please type in your name?")
# greet_with_name(name)


def greet_with_name(firstName, secondName):
    print(f"Hello there {firstName} {secondName}")


firstName,secondName = input("Please type in your name?").split(" ")
greet_with_name(firstName,secondName)
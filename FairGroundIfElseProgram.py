import colorama
from colorama import Fore
from colorama import Style

print(f"{Fore.GREEN}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*        Fairground ride age verifier        *{Style.RESET_ALL}")
print(f"{Fore.GREEN}**********************************************\n{Style.RESET_ALL}")

customerHeight = int(input("Hello, please enter your height in M: "))

if customerHeight < 120:
    print("We're sorry, you can't take the ride just yet...")
elif customerHeight >= 120:
    customerAge = int(input("Hello, please enter your age in years: "))
    if customerAge < 12:
        print("Welcome, please pay 5 euro")
    elif 12 <= customerAge <= 18:
        print("Welcome, please pay 7 euro")
    else:
        print("Welcome, please pay 12 euro")



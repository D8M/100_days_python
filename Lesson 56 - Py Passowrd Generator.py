import random
from collections import Counter
from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Py Password Generator              *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

print("Welcome to the Py Password Generator.\n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

numOfLetters = nr_letters
numOfSymbols = nr_symbols
numOfNumbers = nr_numbers

password = []
tempLetters = ''
tempSymbols = ''
tempNumbers = 0

for i in range(numOfLetters):
    password += random.choice(letters)


for j in range(numOfSymbols):
    password += random.choice(symbols)


for k in range(numOfNumbers):
    password += random.choice(numbers)

random.shuffle(password)

yourPassword = ''.join(password)

print(f"\nYour password code is:  {yourPassword}")


#########################################################################################################################





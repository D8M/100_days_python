import colorama
from colorama import Fore
from colorama import Style

print("**********************************************")
print("*             Tip Calculator                 *")
print("**********************************************\n")

print("Hello and welcome to the tip calculator\n")

totalBill = float(input("What was the total bill? "))

percent = float(input("What percentage tip would you wish to give? 10, 12, or 15%? "))
howManyPeeps = int(input("How many to split the bill? "))

newTotal = float((percent/100 * totalBill) + totalBill)


print(f"The total bill including tip at {percent}% is: {Fore.BLUE}{newTotal:.2f}{Style.RESET_ALL} euro,"
      f" and each person splitting the bill "
      f"should pay  {Fore.GREEN}{(newTotal/howManyPeeps):.2f}{Style.RESET_ALL} each.")



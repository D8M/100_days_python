print("**********************************************")
print("*             Tip Calculator                 *")
print("**********************************************\n")

print("Hello and welcome to the tip calculator\n")

totalBill = float(input("What was the total bill? "))

percent = float(input("What percentage tip would you wish to give? 10, 12, or 15%? "))
howManyPeeps = int(input("How many to split the bill? "))

newTotal = float("{:.2f}".format((percent/100 * totalBill) + totalBill))


print(f"The total bill including tip is: {newTotal} euro"
      f" and each person splitting the bill "
      f"should pay {(newTotal/howManyPeeps):.2f}")



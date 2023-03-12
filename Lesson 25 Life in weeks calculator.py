print("**********************************************")
print("*         Life in Weeks Calculator           *")
print("**********************************************\n")

print("Welcome to the Life length calculator ;)\n")

firstName, yourAge = input("Please enter your  first name and age: \n").split()

lengthOfLife = 100
wksInLife = 4680
daysInLife = 32760
monthsInLife = 1080

print(f"Hi {firstName}, you should have at least {int(lengthOfLife) - int(yourAge)} years,")
print(f"or {int(monthsInLife) - int(yourAge) * 12 } months,")
print(f"or {int(wksInLife) - int(yourAge) * 52 } weeks,")
print(f"or {int(daysInLife) - float(yourAge) * 365.25 } days.")
print("left in your lovely long life ;)")




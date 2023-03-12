print("**********************************************")
print("*              BMI Calculator                *")
print("**********************************************\n")

yourWeight = input("Please enter your weight in kgs:")
yourHeight = input("Please enter your height in M's:")

BMI = float(yourWeight)/(float(yourHeight) ** 2)

print("Your BMI is: ",round(BMI,2))


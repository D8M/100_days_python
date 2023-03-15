print("**********************************************")
print("*              BMI Calculator                *")
print("**********************************************\n")

yourWeight = input("Please enter your weight in kgs:")
yourHeight = input("Please enter your height in M's:")

BMI = float(yourWeight)/(float(yourHeight) ** 2)

print("Your BMI is: ",round(BMI,2))

if BMI <= 18.5:
    print(" You may be underweight\n")
elif 18.5 < BMI < 25:
    print("You are in the normal weight zone.\n")
elif 25 < BMI <= 30:
    print(" You may be overweight\n")
elif 30 < BMI > 35:
    print(" You may be obese\n")
else:
    print(" You may be clinically obese\n")






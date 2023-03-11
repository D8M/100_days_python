
print("**********************************************")
print("*      The 2 Digit Adder Program*")
print("**********************************************\n")

enterNum = input("Please enter a number:\n" )

leftHS = enterNum[0]  # [0] = subscript
rightHS = enterNum[1]

newTotal = int(leftHS) + int(rightHS)

print(f"The number you entered totals:{newTotal} ")



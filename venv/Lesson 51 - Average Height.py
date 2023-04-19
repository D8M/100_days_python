import random
from collections import Counter
from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Average Height Checker          *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

print("Welcome to the Average height Checker.\n")

student_heights = [180, 124, 165, 173, 189, 169, 146]

sum_of_height_values_in_list = 0
count_of_values_in_list = 0

for total_height in student_heights:
    sum_of_height_values_in_list += total_height
    count_of_values_in_list += 1

print(sum_of_height_values_in_list)
print(count_of_values_in_list)
print(round(sum_of_height_values_in_list/count_of_values_in_list))


########################################################################################################################

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Largest Number finder          *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

print("Welcome to the Largest Number finder.\n")

student_scores = [78, 65, 89, 86, 55, 91, 64, 89, 99, 22, 7, 48, 52]

count = 0
highest_score = 0
for score in student_scores:
    count += 1
    #print(score)
    if score > highest_score:
        highest_score = score
        #print(highest_score)

print(f"The highest score in the class is: {highest_score}")

########################################################################################################################



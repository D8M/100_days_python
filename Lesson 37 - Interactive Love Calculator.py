from collections import Counter
from colorama import Fore
from colorama import Style

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Interactive Love Calculator        *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")

print("Welcome to the love calculator!")

name1 = input("Please enter the first persons name? ").lower()
name2 = input("Please enter the second persons name? ").lower()

combinedString = name1 + name2

t_count = combinedString.count('t')
r_count = combinedString.count('r')
u_count = combinedString.count('u')
e_count = combinedString.count('e')

l_count = combinedString.count('l')
o_count = combinedString.count('o')
v_count = combinedString.count('v')
e_count = combinedString.count('e')

# true = t + r + u + e
# love = l + o + v + e
# love_score = str(true) + str(love)


print(f"T occurs {combinedString.count('t')}")
print(f"R occurs {combinedString.count('r')}")
print(f"U occurs {combinedString.count('u')}")
print(f"E occurs {combinedString.count('e')}\n")

print(f"L occurs {combinedString.count('l')}")
print(f"O occurs {combinedString.count('o')}")
print(f"V occurs {combinedString.count('v')}")
print(f"E occurs {combinedString.count('e')}\n")


score1 = t_count + r_count + u_count + e_count
print("Score is: ", score1)

score2 = l_count + o_count + v_count + e_count
print(f"Score is: {score2}\n")

print(f"Your score is: {score1}{score2 }.")

comparisonScore = score1 + score2

if comparisonScore > 40 and comparisonScore < 50:
    print(f"Your Love Score is: {score1}{score2 } you are alright together")

if comparisonScore < 10 or comparisonScore < 90:
    print(f"Your Love Score is: {score1}{score2 } you go together like coke and mentos.")

# -----------------------------------------------------------------------------------------------------------
# Earlier Code Below
# -----------------------------------------------------------------------------------------------------------

# collection1 = Counter(name1.lower())
# collection2 = Counter(name2.lower())
#
# combined_counts = collection1 + collection2
#
# true_love = "true love"
#
# # Calculate the score using the built-in `sum()` function
# score = sum(combined_counts.get(letter, 0) for letter in "true love")
#
# print(f"Compatibility score: {score}")

# t_count = name1 + name2.count('t')
# r_count = name1 + name2.count('r')
# u_count = name1 + name2.count('u')
# e_count = name1 + name2.count('e')
#
# l_count = name1 + name2.count('l')
# o_count = name1 + name2.count('o')
# v_count = name1 + name2.count('v')
# e_count = name1 + name2.count('e')
#
# score1 = t_count + r_count + u_count + e_count + l_count + o_count + v_count + e_count
# print("Score is: ", score1)
#
# print(f"T occurs {name1.count('t')}")
# print(f"R occurs {name1.count('r')}")
# print(f"U occurs {name1.count('u')}")
# print(f"E occurs {name1.count('e')}\n")
#
# print(f"L occurs {name1.count('l')}")
# print(f"O occurs {name1.count('o')}")
# print(f"V occurs {name1.count('v')}")
# print(f"E occurs {name1.count('e')}\n")
#
# ##########################################################################
#
# # t2_count = name2.count('t')
# # r2_count = name2.count('r')
# # u2_count = name2.count('u')
# # e2_count = name2.count('e')
# #
# # l_count = name2.count('l')
# # o_count = name2.count('o')
# # v_count = name2.count('v')
# # e_count = name2.count('e')
# #
# # print(f"T occurs {name2.count('t')} ")
# # print(f"R occurs {name2.count('r')} ")
# # print(f"U occurs {name2.count('u')} ")
# # print(f"E occurs {name2.count('e')} ")
# #
# # print(f"L occurs {name2.count('l')}")
# # print(f"O occurs {name2.count('o')}")
# # print(f"V occurs {name2.count('v')}")
# # print(f"E occurs {name2.count('e')}\n")
# #
# # score2 = t2_count + r2_count + u2_count + e2_count
# # #print("Total Score is: ", score1 + score2)
# #
# # comparisonScore = int(str(score1) + (str(score2)))
# #
# # if 40 < comparisonScore <= 50:
# #     print(f"Your Love Score is: {score1}{score2 } you are alright together")
# #
# # if 10 < comparisonScore <= 90:
# #     print(f"Your Love Score is: {score1}{score2 } you go together like coke and mentos.")
#
#
# # print(f"Your Love Score is: {score1}{score2 }")
# # if comparisonScore







import random
from collections import Counter
from hangman_words import word_list
from hangman_art import logo, stages
from colorama import Fore
from colorama import Style

end_of_game = False

print(f"{Fore.RED}**********************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*         Py Hangman                       *{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**********************************************\n{Style.RESET_ALL}")
#Step 4
print(logo)


#Set 'lives' to equal 6.


print("Welcome to the Py Hangman game!\n")
#word_list = ["aardvark", "baboon", "camel", "dad",
#             "bob"]  # Word list ot choose randomly from 1st: Prog scans list index to see what it contains
display = []  # List for each letter in the chosen word # Same here

lives = 6

index = random.randint(0,len(word_list) - 1)  # Imports random mod from C:\, notes the 0, the len, word list,then places the words into word_list here,
# which then becomes 5, so 0, 5 -1,becomes 0, 4, Index accepts 0

#

chosen_word = word_list[index]  # It places the list into chosen_word, and makes the index 0 & chooses random word from above random mod.
print(chosen_word)
word_length = len(chosen_word)
# word_length = len(word_list)

for letter in range(word_length):
    display += "_"

while lives != 0:

    while not end_of_game:
        guess = input("Please guess a letter of the word: ").lower()

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        print(display)

        if letter not in guess:
            lives -= 1
            print("Lives equal: ", lives)
            if lives == 0:
                # end_of_game = True
                print("Sorry, you lost...")
                play_again = input("Would you like to play again Y/N? : ").lower()
                if play_again == 'y':
                    end_of_game = False

                else:
                    end_of_game = True

        if "_" not in display:
            end_of_game = True
            print("U win ; )")

        print(stages[lives])

lives = lives - 1
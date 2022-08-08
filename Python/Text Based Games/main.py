# Text based games
import random
from random import shuffle

# Global variables
wordslist = ["elephant", "giraffe", "python", "characteristic", "feature", 
"alphabet", "approximate", "precision", "major", "league", "hacking", 
"schedule", "confusion", "command", "acceleration", "velocity"]

print("""
Hey everybody! 
Hope you're having fun! If not, let's have some fun here!😄

Press 1 to play Rock-Paper-Scissor.
Press 2 to play Guess-number.
Press 3 to play Jumbled-letters.
""")
usr_choice = int(input("Enter your choice: "))
if(usr_choice == 1):
    print("\nRock-Paper-Scissor\n")
    print("""\nThe winning rules are as follows:
    Rock wins against scissors.
    Scissors win against paper.
    Paper wins against rock.\n
    """)
    while True: 
        print("Choices: \n 1 => Rock \n 2 => paper \n 3 => scissor ")
        choice = int(input("Enter your choice: ")) 
        while choice > 3 or choice < 1:
            choice = int(input("Enter valid input: ")) 
        if choice == 1: 
            choice_name = 'Rock'
        elif choice == 2: 
            choice_name = 'Paper'
        else: 
            choice_name = 'Scissor'
        print("Your choice is: " + choice_name) 
        print("\nNow its computer turn.......") 
        c_choice = random.randint(1, 3) 
        while c_choice == choice: 
            c_choice = random.randint(1, 3) 
        if c_choice == 1: 
            c_choice_name = 'Rock'
        elif c_choice == 2: 
            c_choice_name = 'Paper'
        else: 
            c_choice_name = 'Scissor'
        print("Computer choice is: " + c_choice_name + "\n") 
        print(choice_name + " V/s " + c_choice_name) 
        if((choice == 1 and c_choice == 2) or
        (choice == 2 and c_choice ==1 )): 
            print("Paper wins!!!\n", end = "") 
            result = "Paper"
            
        elif((choice == 1 and c_choice == 3) or
            (choice == 3 and c_choice == 1)): 
            print("Rock wins!!!\n", end = "") 
            result = "Rock"
        else: 
            print("Scissor wins!!!\n", end = "") 
            result = "Scissor"
        if result == choice_name: 
            print("\n<== !!!User wins!!! ==>") 
        else: 
            print("\n<== !!!Computer wins!!! ==>") 
            
        print("\nDo you want to play again? (Y/N)") 
        ans = input() 
        if ans == 'n' or ans == 'N': 
            break

elif(usr_choice == 2):
    print("\nGuess-number\n")
    while True:
        num = random.randint(0,100)
        # print(num)
        nchances = 5 # player has 5 chances
        while(nchances):
            usr_guess = int(input("Enter a number betwqeen 0 and 100: "))
            if(usr_guess == num):
                print("\nCongrats! You guessed the correct number.\n")
                break
            else:
                if(nchances == 1):
                    print("You didn't guess the number in 5 chances.")
                    print("The number is " + str(num))
                    break
                else:
                    nchances -= 1
                    if(usr_guess > num):
                        print("Enter a lower number.")
                    else:
                        print("Enter a higher number.")
                    print("\nYour guess was wrong. You have " + str(nchances) + " more chances.\n")

        print("\nDo you want to play again? (Y/N)") 
        ans = input() 
        if ans == 'n' or ans == 'N': 
            break
elif(usr_choice == 3):
    print("\nJumbled Letters\n")
    while True:
        ind = random.randint(0,15)
        word = wordslist[ind]
        # print(word)
        s_word = list(word)
        shuffle(s_word)
        s_word = "".join(s_word)
        # print(s_word)
        print("The Jumbled word is: " + s_word)
        nchances = 5 # player has 5 chances
        while(nchances):
            usr_guess = input("Enter the word that has been Jumbled here: ")
            if(usr_guess.lower() == word):
                print("\nCongrats! You guessed the correct word.\n")
                break
            else:
                if(nchances == 1):
                    print("You didn't guess the word in 5 chances.")
                    print("The word is " + word)
                    break
                else:
                    nchances -= 1
                    print("\nYour guess was wrong. You have " + str(nchances) + " more chances.\n")

        print("\nDo you want to play again? (Y/N)") 
        ans = input() 
        if ans == 'n' or ans == 'N': 
            break
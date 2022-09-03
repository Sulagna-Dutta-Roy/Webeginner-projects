# Text based games
import random
from random import shuffle

print("\nRock-Paper-Scissor\n")
print("""The winning rules are as follows:
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
""")

user_score = 0
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
    if((choice == 1 and c_choice == 2) or (choice == 2 and c_choice ==1 )): 
        print("Paper wins!!!\n", end = "") 
        result = "Paper"
            
    elif((choice == 1 and c_choice == 3) or (choice == 3 and c_choice == 1)): 
        print("Rock wins!!!\n", end = "") 
        result = "Rock"
    else: 
        print("Scissor wins!!!\n", end = "") 
        result = "Scissor"
    if result == choice_name: 
        print("\n<== !!!User wins!!! ==>") 
        user_score += 1
    else: 
        print("\n<== !!!Computer wins!!! ==>") 
    print("The user's score is: " + str(user_score))
            
    print("\nDo you want to play again? (Y/N)") 
    ans = input() 
    if ans == 'n' or ans == 'N': 
        break

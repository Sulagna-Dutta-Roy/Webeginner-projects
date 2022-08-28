import random

user_input = 0
random_number = random.randint(1,100)
chances = 0

while user_input != random_number:
	chances += 1
	user_input = int(input("Enter a number between 1 and 100 "))
	if user_input > random_number:
		print("Lesser than you guess")
	if user_input < random_number:
		print("Higher than you guess")

print("You guessed the number with {} chances".format(chances))

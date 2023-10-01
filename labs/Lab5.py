import random
import math

lower = int(input("Enter beginning of number range:- "))


upper = int(input("Enter end of number range:- "))


x = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1,2)),
	" chances to guess the integer!\n")


count = 0

while count < math.log(upper - lower + 1, 2):
	count += 1

	
	guess = int(input("Guess a number:- "))

	
	if x == guess:
		print("Congratulations! You did it in ",
			count, " tries!")
		
		break
	elif x > guess:
		print("You guessed too low!")
	elif x < guess:
		print("You Guessed too high!")


if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")



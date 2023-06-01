# Number Guessing Project
import math
import random

# Taking Inputs
lower = int(input("Enter lower bound:-"))

# Taking Inputs
upper = int(input("Enter upper bound:-"))


# Genrating the num between lower to upper
x = random.randint(lower, upper)
print("\n\t You have only", round(math.log(upper - lower + 1, 2)),
      "Chances to guess the integer")

# Initialaizing the counting
count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1


# taking guessing number as input
guess = int(input("Enter the value"))

# Condition testing
if x == guess:
    print("Congratulation you did it", count, "try")

elif x > guess:
    print("You guessed it too high")
elif x < guess:
    print("You guessed it too low")


# if guesses is more than required show this message
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" %x)
    print("\tBetter Luck Next time!")

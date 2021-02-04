"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730333306"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune: int = randint(1,100)
print("Your fortune cookie says...")
if fortune <= 20:
    print("Something positive is heading your way.")
else:
    if fortune <= 60:
        print("A mysterious figure will soon sow discord in your life.")
    else:
        if fortune <= 90:
            print("Plan for many pleasures ahead.")
        else:
            print("Success will soon surround you.")
print("Now, go spread positive vibes!")
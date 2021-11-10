"""
As the name of the program suggests, we will be imitating a rolling dice.
This is one of the interesting python projects and will generate a random 
number each dice the program runs, and the users can use the dice repeatedly
for as long as he wants. When the user rolls the dice, the program will
generate a random number between 1 and 6 (as on a standard dice).
"""

import random,sys
while True:
    choice = input("Enter 'r' to roll a die and 'q' to quit:  ")
    if choice == 'r':
        die_value = random.randint(1,6)
        print("The die shows: ", die_value)
    elif choice == 'q':
        sys.exit()
    else:
        print("Enter the correct option")
    
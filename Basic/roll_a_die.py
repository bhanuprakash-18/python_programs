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
    
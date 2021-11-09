# This is a simple and fun game to play for a while
# This game guesses the final result after performing some operations on your assumed number
# Lets play the game and get excited

import random
from pygame import encode_file_path
secret_num = 1
while secret_num%2 != 0:
    secret_num = random.randint(2,100)
def continue_thegame():
    print()
    Flag = int(input("Press 1 to continue\n"))
    while Flag== 1:
        print()
        break
print()
print("___ Read each instruction carefully before you continue the game ___")
continue_thegame()
print("*** THINK OF A NUMBER ***")
print("    -----------------    ")
continue_thegame()
print("*** DOUBLE YOUR NUMBER ***")
print("    ------------------    ")
continue_thegame()
print("*** ADD ", secret_num, "TO THE RESULT ***")
print("    ----------------------    ")
continue_thegame()
print("*** DIVIDE THE RESULT BY 2 ***")
print("    ----------------------    ")
continue_thegame()
print("*** SUBTRACT THE ASSUMED NUMBER FROM THE RESULT ***")
print("    -------------------------------------------    ")
continue_thegame()
print("*** NOW ITS TIME TO REVEAL THE RESULT YOU GOT ***")
print("    -----------------------------------------    ")
print()
print("___ The RESULT is ", secret_num/2, "___")

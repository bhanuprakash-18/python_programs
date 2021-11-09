import sys, random

wins = 0
loses = 0
tie = 0
print("\n___Lets start the game - RockPaperScissor___")

def c_choice():
        computer_choice_num = random.randint(1,3)
        if computer_choice_num == 1:
            return 'r'
        if computer_choice_num == 2:
            return 'p'
        if computer_choice_num == 3:
            return 's'
            
def display_score():
    print("Wins:",wins, "  Loses:", loses,"  Tie: ", tie)

while True:
    computer_choice = c_choice()
    player_choice = input("\n\nEnter your choice (r)ock or (p)aper or (s)cissor or (q)uit\n")
    if player_choice == 'q':
        print("___Thank you for playing the game___\n")
        sys.exit()

    if player_choice == computer_choice:
        tie = tie + 1
        print("Tie")
        display_score()
    
    if (player_choice == 'r') and (computer_choice == 's'):
        wins = wins + 1
        print("*** Rock vs \n Scissor ***")
        print("You win")
        display_score()
    if (player_choice == 'p') and (computer_choice == 'r'):
        wins = wins + 1
        print("*** Paper vs \n Rock ***")
        print("You win")
        display_score()
    if (player_choice == 's') and (computer_choice == 'p'):
        wins = wins + 1
        print("*** Scissor vs \n Paper ***")
        print("You win") 
        display_score()

    if (player_choice == 'r') and (computer_choice == 'p'):
        loses = loses + 1
        print("*** Rock vs \n Paper ***")
        print("You lose")
        display_score()
    if (player_choice == 'p') and (computer_choice == 's'):
        loses = loses + 1
        print("*** Paper vs \n Scissor ***")
        print("You lose")
        display_score()
    if (player_choice == 's') and (computer_choice == 'r'):
        loses = loses + 1
        print("*** Scissor vs \n Rock ***")
        print("You lose")  
        display_score()
    





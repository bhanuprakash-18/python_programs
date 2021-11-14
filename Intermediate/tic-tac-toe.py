import sys

def printboard():
    for k, v in board.items():
        print(v, end="      ")
        if k.endswith("R"):
            print()


flag = "X"


def checklogic(i):
    global choice
    if ((board["topL"] == board["topM"]) and (board["topM"] == board["topR"])):
        if board["topM"] == "X" :
            print("Wins X")
            print(board["topL"],",", board["topM"],",",board["topR"],",")
            sys.exit()
        elif board["topM"] == "O":
            print("Wins O")
            print(board["topL"],",", board["topM"],",",board["topR"],",")
            sys.exit()
    if ((board["middleL"] == board["middleM"]) and (board["middleM"] == board["middleR"])):
        if board["middleM"] == "X":
            print("Wins X")
            sys.exit()
        elif board["middleM"] == "O":
            print("Wins O")
            sys.exit()
    if ((board["bottomL"] == board["bottomM"]) and (board["bottomR"] == board["bottomM"])):
        if board["bottomM"] == "X":
            print("Wins X")
            sys.exit()
        elif board["bottomM"] == "O":
            print("Wins O")
            sys.exit()
    if ((board["topL"] == board["middleL"]) and (board["middleL"] == board["bottomL"])):
        if board["bottomL"] == "X":
            print("Wins X")
            sys.exit()
        elif board["bottomL"] == "O":
            print("Wins O")
            sys.exit()
    if ((board["topM"] == board["middleM"]) and (board["middleM"] == board["bottomM"])):
        if board["bottomM"] == "X":
            print("Wins X")
            sys.exit()
        elif board["bottomM"] == "O":
            print("Wins O")
            sys.exit()
    if ((board["topR"] == board["middleR"]) and (board["middleR"] == board["bottomR"])):
        if board["bottomR"] == "X":
            print("Wins X")
            sys.exit()
        elif board["bottomR"] == "O":
            print("Wins O")
            sys.exit()
    if ((board["topL"] == board["middleM"]) and (board["middleM"] == board["bottomR"])):
        if board["bottomR"] == "X":
            print("Wins X")
            sys.exit()
        elif board["bottomR"] == "O":
            print("Wins O")
            sys.exit()
    if ((board["topR"] == board["middleM"]) and (board["middleM"] == board["bottomL"])):
        if board["bottomL"] == "X":
            print("Wins X")
            sys.exit()
        elif board["bottomL"] == "O":
            print("Wins O")
            sys.exit()
    if i==8:
        print("TIE")
        choice = int(input("Enter 1 to play again 0 to exit "))
    

    
choice =1
while(choice):
    board = {
    "topL":" ", "topM":" ", "topR":" ",
    "middleL":" ", "middleM": " ", "middleR":" ",
    "bottomL":" ", "bottomM": " ", "bottomR":" "
    }
    for i in range(9):
        print("Enter your", flag, " move position:")
        move = input()
        if board[move] == " ":
            board[move] = flag
            printboard()
        else:
            print("Position is full")
            i = i-1
        if flag == "X":
            flag = "O"
        else:
            flag = "X"
        checklogic(i)



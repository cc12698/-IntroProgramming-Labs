# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Your Name Here
# Created: YYYY-MM-DD


symbol = [ " ", "x", "o" ]


def printBoard(board):
    boarder = "+-----------+"
    print(boarder)
    print("|" +squareToStr[0][0]+ "|" +squareToStr[0][1]+ "|" +squareToStr[0][2]+ "|")
    print(boarder)
    print("|" +squareToStr[1][0]+ "|" +squareToStr[1][1]+ "|" +squareToStr[1][2]+ "|")
    print(boarder)
    print("|" +squareToStr[2][0]+ "|" +squareToStr[2][1]+ "|" +squareToStr[2][2]+ "|")
    print(boarder)
    pass

def squareToStr(square):
    return square[symbol]

def markBoard(board, row, col, player):
    pass # TODO implement this function
         # Return a boolean indicating success/failure
         
def getPlayerMove():
    input("your move:(x,y): ")
    pass # TODO implement this function
    return (row,col)

def hasBlanks(board):
    pass # TODO implement this function

def main():
    board = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    player = 1

    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn

main()  

<<<<<<< HEAD
turn = 0

boardMatrix = [
             [0 , 0 , 0]
            ,[0 , 0 , 0]
            ,[0 , 0 , 0]
            ]

spacesMatrix = [
        ["A" , "B" , "C"]
    ,   ["D" , "E" , "F"]
    ,   ["G" , "H" , "I"]
    ]

stringMatrix =[
        ["" , "" , ""]
    ,   ["" , "" , ""]
    ,   ["" , "" , ""]
    ]

def showBoard(board):
    printBoarder()
    for i in range(0,3):
        print(rowOutput(i,board))
        printBoarder()
    print()

def printBoarder():
    print("+-----------+")

def rowOutput(i, board):
    output = "|"
    for n in range (0,3):
        output = output + " " + str(board[i][n]) + " " + "|"
    return output

def toLetter(ref , new):
    if new == stringMatrix:
        isString = True
    else:
        isString = False
    
    for i in range (0 , 3):
        for n in range (0 , 3):
            if isString == True:
                if ref[i][n] == 0:
                    new[i][n] = " "
            if ref[i][n] == 1:
                new[i][n] = "X"
            elif ref[i][n] == 2:
                new[i][n] = "O"
    return new

def win(stringMatrix , string):
    for i in range (0 , 3):
        if stringMatrix[i][0] == string and stringMatrix[i][1] == string and stringMatrix[i][0] == string:
            stringMatrix[i][0] = stringMatrix[i][1] = stringMatrix[i][0] = "-"
            return True
    for i in range (0 , 3):
        if stringMatrix[0][i] == string and stringMatrix[1][i] == string and stringMatrix[2][i] == string:
            stringMatrix[0][i] = stringMatrix[1][i] = stringMatrix[2][i] = "|"
            return True
    for i in range (0 , 3):
        if stringMatrix[0][0] == string and stringMatrix[1][1] == string and stringMatrix[2][2] == string:
            stringMatrix[0][0] = stringMatrix[1][1] = stringMatrix[2][2] = "\\"
            return True
    for i in range (0 , 3):
        if stringMatrix[0][2] == string and stringMatrix[1][1] == string and stringMatrix[2][0] == string:
            stringMatrix[0][2] = stringMatrix[1][1] = stringMatrix[2][0] = "/"
            return True
    return False

def move(boardMatrix):
    global turn
    turn+=1
    if turn % 2 == 0:
        player = 1 #repersents "X"
        print("\"X\"'s turn\n")
    else:
        player = 2 #repersents "O"
        print("\"O\"'s turn\n")
        
    space = str(input("What space would you like to mark?: "))
    
    if space == "A":
        boardMatrix[0][0] = player
    elif space == "B":
        boardMatrix[0][1] = player
    elif space == "C":
        boardMatrix[0][2] = player
    elif space == "D":
        boardMatrix[1][0] = player
    elif space == "E":
        boardMatrix[1][1] = player
    elif space == "F":
        boardMatrix[1][2] = player
    elif space == "G":
        boardMatrix[2][0] = player
    elif space == "H":
        boardMatrix[2][1] = player
    elif space == "I":
        boardMatrix[2][2] = player
    return boardMatrix

def main():

    while win(boardMatrix , 1) == False and win(stringMatrix , 2) == False:
        toLetter(boardMatrix , stringMatrix)
        showBoard(stringMatrix)
        toLetter(boardMatrix , spacesMatrix)
        showBoard(spacesMatrix)
        move(boardMatrix)

        if win(stringMatrix , 1) == True:
            print("\nX wins!\n")
            showBoard(stringMatrix)
        elif win(boardMatrix , 2) == True:
            print("\nO wins!\n")
            showBoard(stringMatrix)

main()
=======
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
>>>>>>> 4124721e5a10ec286f043da758863109a9cd11b2

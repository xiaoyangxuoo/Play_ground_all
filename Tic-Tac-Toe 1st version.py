from random import randrange
board = [[1, 2, 3],[4, 'X', 6], [7, 8, 9]]
boardDict = {
    1 : (0,0),
    2 : (0,1),
    3 : (0,2),
    4 : (1,0),
    5 : (1,1),
    6 : (1,2),
    7 : (2,0),
    8 : (2,1),
    9 : (2,2)
}


def DisplayBoard(board):
    print('+-------+-------+-------+', '\n', end="")
    print('|       |       |       |','\n',end="")
    print('|  ',board[0][0],'  |  ',board[0][1],'  |  ',board[0][2],'  |','\n',end="")
    print('|       |       |       |', '\n',end="")
    print('+-------+-------+-------+', '\n',end="")
    print('|       |       |       |', '\n',end="")
    print('|  ',board[1][0],'  |  ',board[1][1],'  |  ',board[1][2],'  |','\n',end="")
    print('|       |       |       |', '\n',end="")
    print('+-------+-------+-------+', '\n',end="")
    print('|       |       |       |', '\n',end="")
    print('|  ',board[2][0],'  |  ',board[2][1],'  |  ',board[2][2],'  |','\n',end="")
    print('|       |       |       |', '\n',end="")
    print('+-------+-------+-------+', '\n',end="")
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console




#

def EnterMove(board):
    moveNum = int(input('Please enter the move: '))
    if boardDict.get(moveNum) in MakeListOfFreeFields(board):
        board[boardDict.get(moveNum)[0]][boardDict.get(moveNum)[1]] = 'O'
    else:
        return None
        
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields(board):
    freeLst = []
    for i in range(len(board)):
        for j in range(len(board[i])):
        if type(board[i][j])!=str:
            freeLst.append((i,j))
    return freeLst
#
    
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def VictoryFor(board, sign):

    # 下完了
    if board[0][0]==board[0][1]==board[0][2]=="O" or\
    board[1][0]==board[1][1]==board[1][2]=="O" or\
    board[2][0]==board[2][1]==board[2][2]=="O" or\
    board[0][0]==board[1][0]==board[2][0]=="O" or\
    board[0][1]==board[1][1]==board[2][1]=="O" or\
    board[0][2]==board[1][2]==board[2][2]=="O" or\
    board[0][0]==board[1][1]==board[2][2]=="O" or\
    board[2][0]==board[1][1]==board[0][1]=="O":
        print('You win! ')
    elif board[0][0]==board[0][1]==board[0][2]=="X" or\
    board[1][0]==board[1][1]==board[1][2]=="X" or\
    board[2][0]==board[2][1]==board[2][2]=="X" or\
    board[0][0]==board[1][0]==board[2][0]=="X" or\
    board[0][1]==board[1][1]==board[2][1]=="X" or\
    board[0][2]==board[1][2]==board[2][2]=="X" or\
    board[0][0]==board[1][1]==board[2][2]=="X" or\
    board[2][0]==board[1][1]==board[0][1]=="X":
        print('You lose! ')
    else:
        if MakeListOfFreeFields(board) == []:
            print('Tie! ')
        else:
            print('Game not finished, please continue: ')
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove(board):
    moveNum = randrange(9) + 1
    if boardDict.get(moveNum) in MakeListOfFreeFields(board):
        board[boardDict.get(moveNum)[0]][boardDict.get(moveNum)[1]] = 'X'
    else:
        return None
    
#
# the function draws the computer's move and updates the board
#
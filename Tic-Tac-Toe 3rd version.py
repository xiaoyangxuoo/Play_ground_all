from random import randrange
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
def EnterMove(board):
    
    
    moveNum = int(input('Please enter the move: '))
    if boardDict.get(moveNum) in MakeListOfFreeFields(board):
        board[boardDict.get(moveNum)[0]][boardDict.get(moveNum)[1]] = "O"
        MakeListOfFreeFields(board)
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
global BL
BL = False
def VictoryFor(board,sign):

    if board[0][0]==board[0][1]==board[0][2]==sign or\
    board[1][0]==board[1][1]==board[1][2]==sign or\
    board[2][0]==board[2][1]==board[2][2]==sign or\
    board[0][0]==board[1][0]==board[2][0]==sign or\
    board[0][1]==board[1][1]==board[2][1]==sign or\
    board[0][2]==board[1][2]==board[2][2]==sign or\
    board[0][0]==board[1][1]==board[2][2]==sign or\
    board[2][0]==board[1][1]==board[0][2]==sign:
      return True
    else:
        if MakeListOfFreeFields(board) == []:
                 
            print('Tie! ')
            global BL
            BL = True
            #return True

            
        
            
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove(board):
    while MakeListOfFreeFields(board)!=[]:
      moveNum = randrange(1, 10) 
      if boardDict.get(moveNum) in MakeListOfFreeFields(board):
        break
    if MakeListOfFreeFields(board)==[]:
      return None
    board[boardDict.get(moveNum)[0]][boardDict.get(moveNum)[1]] = "X"
    DisplayBoard(board)
    MakeListOfFreeFields(board)
    #else:
    #  if boardDict.get(moveNum) in MakeListOfFreeFields(board):
    #    DisplayBoard(board)
    #    MakeListOfFreeFields(board)
    
#
# the function draws the computer's move and updates the board
#

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



DisplayBoard(board)
while True:
  if BL == True:
    break
  
  EnterMove(board)
  if VictoryFor(board,"O"):
    print("You win! ")
    break
  DrawMove(board)
  if VictoryFor(board, "X"):  
    print("You lose")
    break
  

#while True:
#  if VictoryFor(board,"O"):
 #   print("You win! ") 
 #   break
 # elif VictoryFor(board, "X"):
 #   print("You lose! ")
 #   break
 # EnterMove(board)
#  DrawMove(board)

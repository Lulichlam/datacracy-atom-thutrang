#Tic-Tac-Toe Board
theBoard = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
turn = 'X'
print('welcome to tic-tac-toe board, each turn X or O will replace number in the board 3x3')
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space ? (input number)')
    spaceleft =[]; #list contain blank position without X or O inputted
    for v in theBoard.values():
      if not (v=="X" or v=="O"):
        spaceleft.append(v)   
    move = input()
    while not move in spaceleft:
      print('invalid position, pls try in this list',end=": ")
      print(spaceleft)
      move = input()
    
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
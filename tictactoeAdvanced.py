import random
import os
import time

board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentPlayer = "X"
winner = None
gameRunning = None


# printing the game board
def printBoard(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])


# take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    else:
        print('Oops already taken!')
        switchPlayer()


# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != '-':
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != '-':
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != '-':
        winner = board[5]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if '-' not in board:
        printBoard(board)
        print('It is a tie!')
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkVertical(board) or checkHorizontal(board):
        print(f'The winner is {winner}')
        gameRunning = False

# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

# computer
def computer(board):
    while currentPlayer == 'O':
        position = random.randint(0,8)
        if board[position] == '-':
            board[position] = 'O'
            switchPlayer()

#ready to start
start = input('Are you ready to play? Y or N\n')
if start == 'Y' or 'y':
    gameRunning = True
else:
    gameRunning = False


# game running loop
while gameRunning:
    os.system('cls')
    printBoard(board)
    playerInput(board)
    os.system('cls')
    printBoard(board)
    checkWin()
    if gameRunning == False:
       break
    checkTie(board)
    switchPlayer()
    time.sleep(3)
    computer(board)
    checkWin()
    checkTie(board)
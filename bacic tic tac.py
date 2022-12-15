# Basic tic-tac-toe game using lists

'''Basic flow of the program is:
Visual Representation -> User Input -> Function -> Updates -> New Visual'''

import random

def view_board(board):
    print('   |   |')
    print(' ' + board[7]+ ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print(' ' + board[4]+ ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print(' ' + board[1]+ ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
def player_input():
    mark = ''
    while not (mark == 'X' or mark == 'O'):
        mark = input('Player 1 : You want to be X or O ??').upper()
    if mark == 'X':
        return('X','O')
    else:
        return('O','X')

def placement(board, mark, position):
    board[position]=mark

def winner_check(board,mark):
    return((board[7]==mark and board[8]==mark and board[9]==mark) or
           (board[4]==mark and board[5]==mark and board[6]==mark) or
           (board[1]==mark and board[2]==mark and board[3]==mark) or
           (board[7]==mark and board[4]==mark and board[1]==mark) or
           (board[8]==mark and board[5]==mark and board[2]==mark) or
           (board[9]==mark and board[6]==mark and board[3]==mark) or
           (board[7]==mark and board[5]==mark and board[3]==mark) or
           (board[9]==mark and board[5]==mark and board[1]==mark))

def turn():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'

def check(board, position):
    return board[position]==' '

def full_check(board):
    for i in range(1,10):
        if check(board, i):
            return False
    return True

def choice(board):
    pos = 0
    while pos not in [1,2,3,4,5,6,7,8,9] or not check(board, pos):
        pos = int(input('Choose your next position : (1-9)'))
    return pos

def replay():
    return input('Do you want to play again ? Enter Yes or No : ').lower().startswith('y')

print('Welcome to Tic Tac Toe')
print('Three in a row')

while True:
    board=[' ']*10
    player1_mark, player2_mark = player_input()
    turn = turn()
    print(turn+' will start')
    play = input('Are you ready to play ? Yes or No')
    if play.lower()[0]=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='Player 1':
            view_board(board)
            pos=choice(board)
            placement(board, player1_mark, pos)
            if winner_check(board, player1_mark):
                view_board(board)
                print('Congratulations !! Player 1 has won the game')
                game_on= False
            else:
                if full_check(board):
                    view_board(board)
                    print('The game is a draw')
                    game_on=False
                else:
                    turn = 'Player 2'
        else:
            view_board(board)
            pos = choice(board)
            placement(board, player2_mark, pos)
            if winner_check(board, player2_mark):
                view_board(board)
                print('Congratulations !! Player 2 has won the game')
                game_on= False
            else:
                if full_check(board):
                    view_board(board)
                    print('The game is a draw')
                    game_on=False
                else:
                    turn = 'Player 1'


    if not replay():
        break
                
























































           

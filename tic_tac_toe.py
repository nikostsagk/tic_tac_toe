import sys
import warnings
import numpy as np
from random import shuffle
from moves import make_move, available_moves, human_move
from conditions import winner, gameover
from tempo import tempo
from minimax import minimax
warnings.simplefilter(action='ignore', category=FutureWarning)

def initialization():
        print('Choose the size of the board.\nPress 3 or 5.')
        print('Winning conditions: For size 3x3 you need 3 in a row (or diagonally).\nOtherwise you need 4\n')
        bsize = input('Enter board size:\n');
        while bsize not in ['3','5']:
            bsize = input('Incorrect input. Please choose 3, 5.\n');
        h = input('Pick X or O: \n').upper();
        while h not in ['X','O']:
            h = input('Incorect input. Pick X or O.\n').upper();
        f = input('Do you want to play first? Press y/n.\n').upper();
        while f not in ['Y','N']:
            f = input('Incorrect input. Please press y or n\n').upper();        
        if f == 'Y':
            f = 'player';
        else:
            f = 'computer';
        return (h,bsize,f)
                
def display_board(b):
    if len(b) == 3:
        print('  0 | 1 | 2')
        print('0', b[0,0], '|', b[0,1], '|', b[0,2])
        print('-------------')
        print('1', b[1,0], '|', b[1,1], '|', b[1,2])
        print('-------------')
        print('2',b[2,0], '|', b[2,1], '|', b[2,2],'\n')
    elif len(b) == 5:
        print('  0 | 1 | 2 | 3 | 4')
        print('0', b[0,0], '|', b[0,1], '|', b[0,2], '|', b[0,3], '|', b[0,4])
        print('---------------------')
        print('1', b[1,0], '|', b[1,1], '|', b[1,2], '|', b[1,3], '|', b[1,4])
        print('---------------------')
        print('2', b[2,0], '|', b[2,1], '|', b[2,2], '|', b[2,3], '|', b[2,4])
        print('---------------------')
        print('3', b[3,0], '|', b[3,1], '|', b[3,2], '|', b[3,3], '|', b[3,4])
        print('---------------------')
        print('4', b[4,0], '|', b[4,1], '|', b[4,2], '|', b[4,3], '|', b[4,4])

##### Selecting preferences
human, bsize, turn = initialization()
if human == 'X':
    comp = 'O'
else:
    comp = 'X'


#Set an empty board
bsize = int(bsize)
if bsize == 3:
    order = 'normal'
else:
    order = 'tempo' #changes the order of possible moves

board = np.array([' ']*(bsize**2)).reshape(bsize,bsize)
display_board(board)

terminal_test = False #decides whether to stop or not
while (terminal_test == False):
    if turn == 'player': #player move
        print('\nYour turn: ')
        #input row number followed by column number: e.g: 21 (row 2, column 1)
        human_move(board,human)
        #board, best_score, c = minimax(board, 2, True, human, comp,-1000,1000,order,0) #comp vs comp
        #print('Minimax called: ',c-1,' times recursively.')
        display_board(board) #refresh the board
        if winner(board,human):
            print('\nYou won!')
            terminal_test = True;
            break
        if gameover(board):
            print('\nIts a tie!')
            terminal_test = True;
            break
    turn = 'computer'
    if turn == 'computer': #computer turn
        print('\nMy turn: ')
        board, best_score, c = minimax(board, 4, True, comp, human,-1000,1000,order,0)
        print('Minimax called: ',c-1,' times recursively.')
        display_board(board) #refresh the board
        if winner(board,comp):
            print('\nYou lost! ')
            terminal_test = True;
            break
        if gameover(board):
            print('\nIts a tie! ')
            terminal_test = True;
            break
    turn = 'player'

            
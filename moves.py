import copy
import numpy as np

def check_valid_move(board):
    """ This function checks if the input move is a valid move.

    Args
        board : the current state of the board
    Returns
        A list of integers (the inserted move).
    """
    case = -1
    message = 'Choose a valid move:\n(Input row number followed by column number.)\n'
    while case != 0:
        row_column = list(input(message))

        try:
            row = int(row_column[0])
            col = int(row_column[1])
        except ValueError:
            case = 1 # not integer numbers
            message = 'Input should be integers, choose again:\n(E.g: 21 for r=2, c=1)\n'
            continue

        if (row in range(len(board))) and (col in range(len(board))):
            if (board[row, col] == ' '):
                case = 0 # correct
                return row_column
            else:
                case = 2 # unavailable move
                message = 'This move is unavailable, choose again:'
        else:
            case = 3 # out of range
            message = 'This move is out of range, choose again:'

def make_move(b,i,j,sign):
    """ This function fills an empty space on the board with a sign.
    Args
        b    : board
        i    : row
        j    : column
        sign : sign
    Returns
        The updated board or 'False' if the move is unavailable
    """
    if b[i,j] == ' ': #You can make this move
        b[i,j] = sign
        return b
    else:
        return False
        
def available_moves(board,letter,ordering):
    """ This function returns the list with the available moves.

    Args
        board : board
        letter : the assigning letter
        ordering : the order 'normal', 'shuffle' or 'tempo'
    Returns
        A list of ordered boards.
    """
    coordinates = list(range(len(board)))
    possible_moves = []
    for i in coordinates:
        for j in coordinates:
            new_board = board.copy()
            new_board = make_move(new_board,i,j,letter)
            if new_board != False:
                symmetries =  [np.rot90(new_board,1), np.rot90(new_board,2), 
                           np.rot90(new_board,3), np.flip(new_board,0) ,np.flip(new_board,1), new_board.T, 
                               np.fliplr(np.fliplr(new_board).T)]
                counter = 0 
                for move in possible_moves:
                    for s in symmetries:
                        if np.all(move == s):
                            counter+=1
                if counter == 0:
                    possible_moves.append(new_board)
    possible_moves = [i for i in possible_moves if i is not False]
    if ordering == 'shuffle':
        return shuffle(possible_moves)
    elif ordering == 'tempo':
        heuristic_2 = [tempo(x,letter,2) for x in possible_moves]
        heuristic_3 = [2.5*tempo(x,letter,3) for x in possible_moves]
        idx= [x + y for x, y in zip(heuristic_2, heuristic_3)]
        idx = sorted(range(len(idx)), key=lambda i: idx[i],reverse=True)
        possible_heur = sorted(zip(idx,possible_moves))
        possible_moves = [possible_moves[m] for m in idx]
        return possible_moves
    else: #normal
        return possible_moves

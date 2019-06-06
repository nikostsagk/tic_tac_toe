import copy
import numpy as np

def make_move(board,i,j,sign): #returns a new board
    if board[i,j] == ' ': #You can make this move
        board[i,j] = sign
        return board
    else:
        return False
        
def available_moves(board,letter,ordering): #returns a list with all the available moves
    """ ordering: "shuffle" or "tempo" """
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

def human_move(b,sign):
    coordinates = list(range(len(b)))
    flag1 = True
    flag2 = True
    while flag2:
        inp = list(input('Choose a valid move: '))
        if (int(inp[0]) and int(inp[1])) in coordinates:
            flag2 = False
    while flag1:
        if make_move(b,int(inp[0]),int(inp[1]),sign) != False:
            flag1 = False
            return b
        print('Unavailable move, choose again.')
        inp = list(input('Choose an available move: '))

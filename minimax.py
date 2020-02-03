from conditions import winner, gameover
from moves import available_moves

def minimax(board, depth, maximizing, computer_letter, human_letter, alpha, beta, order, c):
    """ This function implements the minimax algorithm for depth=depth.

    Args
        board           : game's board
        depth           : maximum depth (Suggested values: 9 for board size=3, 4 or less for board size=4.)
        maximizing      : maximizing state 'True' or 'False'
        computer_letter : computer's sign 'X' or 'O'
        human_letter    : human' sign 'X' or 'O'
        alpha           : alpha score (int)
        beta            : beta score (int)
        order           : available moves' order 'normal', 'shuffle' or 'tempo'
        c               : recursive counter
    Returns
        (best_move, best_score, c)
        best_move       : A new board with the new move
        best_score      : The score of the move
        c               : The recursive counter
    """

    if winner(board, human_letter):
        score = -1000
        return board,score,c
    if winner(board, computer_letter): 
        score = 1000
        return board,score,c
    
    if gameover(board):
        score = 0 #If no winner we don't care aboardout the score
        return board,score,c
    elif (depth == 0 and len(board) == 5): #The only occasion we care aboardout the current score
        score = -(tempo(board,human_letter,2) + 2.5*tempo(board,human_letter,3)) \
                +(tempo(board,computer_letter,2) + 2.5*tempo(board,computer_letter,3))
        return board,score,c;
    else:
        score = 1;
        
    if maximizing:
        best_score = -1000
        possible_moves_final = available_moves(board, computer_letter, order)
        if len(board) == 5:
            if maximizing:
                if len(possible_moves_final) > 10: #further pruning
                    possible_moves = [possible_moves_final[m] for m in range(10)]
                else:
                    possible_moves = possible_moves_final
            else:
                possible_moves = possible_moves_final
        else:
            possible_moves = possible_moves_final
    else:
        best_score = 1000
        possible_moves = available_moves(board,human_letter,order)
    best_move = None
    for move in possible_moves:
        junk, utility,c = minimax(move, depth-1, not(maximizing), computer_letter, human_letter,alpha,beta,order,c+1)
        if maximizing:
            if utility >= best_score:
                best_move = move
                best_score = utility
            if alpha > utility:
                alpha = utility
            if beta <= alpha:
                break
        else:
            if utility <= best_score:
                best_move = move
                best_score = utility
            if beta < utility:
                beta = utility
            if beta <= alpha:
                break
    return best_move, best_score,c+1
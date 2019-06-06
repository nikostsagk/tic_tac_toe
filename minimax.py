from conditions import winner, gameover
from moves import available_moves

def minimax(b, d, maximizing, computer_letter, human_letter, alpha,beta,order,c):
    """ b: board, d: maximum depth, computer_letter: comp sign, human_letter" human sign, alpha/beta: for alpha beta pruning,
        order: "shuffle" or "tempo" (shuffles the available moves or sorts them with tempo evaluation),
        c: counts how many times minimax is called recursively """
    
    if winner(b,human_letter):
        score = -1000
        return b,score,c
    if winner(b,computer_letter): 
        score = 1000
        return b,score,c
    
    if gameover(b):
        score = 0 #If no winner we don't care about the score
        return b,score,c
    elif (d == 0 and len(b) == 5): #The only occasion we care about the current score
        score = -(tempo(b,human_letter,2) + 2.5*tempo(b,human_letter,3)) \
                +(tempo(b,computer_letter,2) + 2.5*tempo(b,computer_letter,3))
        return b,score,c;
    else:
        score = 1;
        
    if maximizing:
        best_score = -1000
        possible_moves_final = available_moves(b,computer_letter,order)
        if len(b) == 5:
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
        possible_moves = available_moves(b,human_letter,order)
    best_move = None
    for move in possible_moves:
        junk, utility,c = minimax(move, d-1, not(maximizing), computer_letter, human_letter,alpha,beta,order,c+1)
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

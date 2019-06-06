import numpy as np

def winner(b,sign):
    """ b: board, sign: "X" or "O" """
    if len(b) == 3:
        for r in range(3):
            if ((b[r,:] == sign).sum() == 3):
                return True
        b = np.transpose(b)
        for c in range(3):
            if ((b[c,:] == sign).sum() == 3):
                return True
        b = np.transpose(b)
        if ((b[0,0] == b[1,1] == b[2,2] == sign) or 
            (b[2,0] == b[1,1] == b[0,2] == sign)):
            return True
    elif len(b) == 5:
        for r in range(5):
            if ((b[r,0:4] == sign).sum() == 4) or ((b[r,1:5] == sign).sum() == 4):
                return True
        b = np.transpose(b)
        for c in range(5):
            if ((b[c,0:4] == sign).sum() == 4) or ((b[c,1:5] == sign).sum() == 4):
                return True
        b = np.transpose(b)
        if ((b[0,0] == b[1,1] == b[2,2] == b[3,3] == sign) or (b[1,1] == b[2,2] == b[3,3] == b[4,4] == sign) or
            (b[4,0] == b[3,1] == b[2,2] == b[1,3] == sign) or (b[3,1] == b[2,2] == b[1,3] == b[0,4] == sign) or
            (b[0,1] == b[1,2] == b[2,3] == b[3,4] == sign) or (b[1,0] == b[2,1] == b[3,2] == b[4,3] == sign) or
            (b[0,3] == b[1,2] == b[2,1] == b[3,0] == sign) or (b[4,1] == b[3,2] == b[2,3] == b[1,4] == sign)):
            return True 
    return False

def gameover(b):
    """ b: board """
    if ((b == ' ').sum() == 0):
        return True
    else:
        return False

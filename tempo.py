def tempo(b,sign,n):
    """ This function accepts a board, and quantises the advantage (tempo) of the player.
        tempo = sum( 2_adjacent_tiles + 2.5 * 3_adjacent_tiles )

    Args
        b    : board
        sign : the sign of the player
        n    : the number of the adjacent tiles to be examined (2 or 3).
    Returns
        An int.
    """
    if n == 2:
        counter=0
        for r in range(5):
            if (b[r,0:2] == sign).sum() == 2: counter+=1
            if (b[r,1:3] == sign).sum() == 2: counter+=1
            if (b[r,2:4] == sign).sum() == 2: counter+=1
            if (b[r,3:5] == sign).sum() == 2: counter+=1
        b = np.transpose(b)
        for c in range(5):
            if (b[c,0:2] == sign).sum() == 2: counter+=1
            if (b[c,1:3] == sign).sum() == 2: counter+=1
            if (b[c,2:4] == sign).sum() == 2: counter+=1
            if (b[c,3:5] == sign).sum() == 2: counter+=1
        b = np.transpose(b)
        for x in range(-3,4):
            l=np.diag(b,x)
            for i in range(len(l)-1):
                if (l[i:i+2] == sign).sum() == 2: counter+=1
        for x in range(-3,4):
            l=np.diag(np.fliplr(b),x)
            for i in range(len(l)-1):
                if (l[i:i+2] == sign).sum() == 2: counter+=1
    if n == 3:
        counter=0
        for r in range(5):
            if (b[r,0:3] == sign).sum() == 3: counter+=1
            if (b[r,1:4] == sign).sum() == 3: counter+=1
            if (b[r,2:5] == sign).sum() == 3: counter+=1
        b = np.transpose(b)
        for c in range(5):
            if (b[c,0:3] == sign).sum() == 3: counter+=1
            if (b[c,1:4] == sign).sum() == 3: counter+=1
            if (b[c,2:5] == sign).sum() == 3: counter+=1
        b = np.transpose(b)
        for x in range(-2,3):
            l=np.diag(b,x)
            for i in range(len(l)-2):
                if (l[i:i+3] == sign).sum() == 3: counter+=1
        for x in range(-2,3):
            l=np.diag(np.fliplr(b),x)
            for i in range(len(l)-2):
                if (l[i:i+3] == sign).sum() == 3: counter+=1
    return counter
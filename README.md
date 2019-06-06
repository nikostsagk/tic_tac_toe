# Tic tac toe
This repository contains an implementation of the game __tic tac toe__ using ```minimax``` with alpha-beta pruning. 
Apart from the classic 3 x 3 game version, there is implemented a 5 x 5 variant where the player needs 4-in-a-row to win.

The idea behind 5 x 5 version, is to see how ```minimax``` scales with depth and how to control it. It was proposed a
ranking of the opponent moves, known as "__tempo__", and discarding the ones with the smallest value. Introducing a way to 
evaluate the "goodness" of the move and keeping only the best is a good heuristic to start with, but needs improvement. 

### Files:
- ```conditions.py```: contains functions to evaluate the board
- ```minimax.py```: contains an implementation of the minimax algorithm
- ```moves.py```: move availability, other move related functions
- ```tempo.py```: contains a heuristic algorithm that assigns points to moves regarding their goodness. Needs improvement
- ```tic_tac_toe.py```: Initializes the game and display the board in console.

The algorithm was developed as a second part for the Foundations of AI coursework (COMP6231).

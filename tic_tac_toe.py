import sys
import warnings
import numpy as np
from random import shuffle
import moves
import conditions
from tempo import tempo
from minimax import minimax
warnings.simplefilter(action='ignore', category=FutureWarning)

class tic_tac_toe:

    def __init__(self):
        """ This function initialises the game settings.
        """
        print('Choose the size of the board.\nPress 3 or 5.')
        print('Winning conditions: For size 3x3 you need 3 in a row (or diagonally).\nOtherwise you need 4\n')

        self.board_size = input('Enter board size:\n');                       # Game board size
        while self.board_size not in ['3', '5']:
            self.board_size = input('Incorrect input. Please choose 3 or 5.\n');
        self.board_size = int(self.board_size)

        self.human_sign = input('Pick X or O: \n').upper();                   # Human's sign
        while self.human_sign not in ['X','O']:
            self.human_sign = input('Incorect input. Pick X or O.\n').upper();

        self.computer_sign = 'O' if self.human_sign == 'X' else 'X'           # Computer's sign

        self.turn = input('Do you want to play first? Press y/n.\n').upper(); # First, true or false
        while self.turn not in ['Y','N']:
            self.turn = input('Incorrect input. Please press y or n\n').upper();


        self.turn = 'human' if self.turn == 'Y' else 'computer'
        self.order = self._available_moves_order()
        self.board = self._generate_board()                                        # Initialise board
                
    def display_board(self):
        """ This function prints the current state of the board.
        """
        if self.board_size == 3:
            print('  0 | 1 | 2')
            print('0', self.board[0,0], '|', self.board[0,1], '|', self.board[0,2])
            print('-------------')
            print('1', self.board[1,0], '|', self.board[1,1], '|', self.board[1,2])
            print('-------------')
            print('2',self.board[2,0], '|', self.board[2,1], '|', self.board[2,2],'\n')
        elif self.board_size == 5:
            print('  0 | 1 | 2 | 3 | 4')
            print('0', self.board[0,0], '|', self.board[0,1], '|', self.board[0,2], '|', self.board[0,3], '|', self.board[0,4])
            print('---------------------')
            print('1', self.board[1,0], '|', self.board[1,1], '|', self.board[1,2], '|', self.board[1,3], '|', self.board[1,4])
            print('---------------------')
            print('2', self.board[2,0], '|', self.board[2,1], '|', self.board[2,2], '|', self.board[2,3], '|', self.board[2,4])
            print('---------------------')
            print('3', self.board[3,0], '|', self.board[3,1], '|', self.board[3,2], '|', self.board[3,3], '|', self.board[3,4])
            print('---------------------')
            print('4', self.board[4,0], '|', self.board[4,1], '|', self.board[4,2], '|', self.board[4,3], '|', self.board[4,4])

    def check_winner(self, sign):
        """ This function returns True if input sign wins or False if not.

        Args
            sign    :   sign to be checked
        Returns
            A boolean variable. 
        """
        return conditions.winner(self.board, sign)

    def check_gameover(self):
        """ This function returns True if the board is filled or False if not.

        Returns
            A boolean variable.
        """
        return conditions.gameover(self.board)

    def whose_turn(self):
        """ This function returns who's turn it is.

        Returns
            'human' or 'computer'
        """
        return self.turn

    def change_turn(self):
        """ this function changes turn.
        """
        self.turn = 'human' if self.whose_turn() == 'computer' else 'computer'

    def get_board(self):
        """ This function returns the board.

        Returns
            A 2D array.
        """
        return self.board

    def get_board_size(self):
        """ This function returns the board size.
        
        Returns
            An int.
        """
        return self.board_size

    def get_human_sign(self):
        """ This function returns human's sign.

        Returns
            'X' or 'O'
        """
        return self.human_sign

    def get_computer_sign(self):
        """ This function returns computer's sign.

        Returns
            'X' or 'O'
        """
        return self.computer_sign

    def get_order(self):
        """ This function returns the available moves' order.
        Returns
            'normal' or 'tempo'
        """
        return self.order

    def make_move(self, rc):
        """ This function makes a move on the board depending on the input with the sign of the player's turn.

        Args
            rc : the input row followed by the column (list<str>)
        """
        fill_with_sign = self.human_sign if self.turn == 'human' else self.computer_sign
        self.board[int(rc[0]),int(rc[1])] = fill_with_sign

    def update_board(self, board):
        """ This function sets the input board as the tic_tac_toe.board .
            It is used for convenience to update the board after computer's turn.

        Args
            board : board
        """
        self.board = board

    def _available_moves_order(self, shuffle=False):
        """ This function re-arranges the possible moves regarding their value.
        This depends from the board size.

        Args
            shuffle : 'True' or 'False'
        Returns
            'normal' for board size == 3 or 'tempo' for board size == 5 or 'shuffle' if set explicitly.
        """
        if shuffle:
            return 'shuffle'
        else:
            return 'normal' if int(self.board_size) == 3 else 'tempo'

    def _generate_board(self):
        """ This function generates the board.

        Returns
            A 2D array
        """
        return np.array([' ']*(self.board_size**2)).reshape(self.board_size,self.board_size)


if __name__=='__main__':
    game = tic_tac_toe()
    game.display_board()
    terminal_test = False # Decides whether to stop or not
    while (terminal_test == False):
        if game.whose_turn() == 'human': # Human's turn
            print('\nYour turn:')
            #rc = moves.check_valid_move(game.get_board())
            game.make_move(moves.check_valid_move(game.get_board()))

            # Computer vs computer
            #board, best_score, c = minimax(board, 2, True, human, comp,-1000,1000,order,0) #comp vs comp
            #print('Minimax called: ',c-1,' times recursively.')

            game.display_board()
            if game.check_winner(game.get_human_sign()):
                print('\nYou won!')
                terminal_test = True;
                break
            if game.check_gameover():
                print('\nIts a tie!')
                terminal_test = True;
                break
        game.change_turn()
        if game.whose_turn() == 'computer': # Computer's turn
            print('\nMy turn: ')

            new_board, _, recursive_counter = minimax(
                board=game.get_board(),
                depth=4, 
                maximizing=True, 
                computer_letter=game.get_computer_sign(), 
                human_letter=game.get_human_sign(),
                alpha=-1000,
                beta=1000,
                order=game.get_order(),
                c=0) # recursive counter
            print('Minimax called: ',recursive_counter-1,' times recursively.')
            
            game.update_board(new_board)
            game.display_board()
            if game.check_winner(game.get_computer_sign()):
                print('\nYou lost! ')
                terminal_test = True;
                break
            if game.check_gameover():
                print('\nIts a tie! ')
                terminal_test = True;
                break
        game.change_turn()

            
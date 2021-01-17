#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below
class Player:
    
    def __init__(self, checker):
        """ a constuctor for Player object """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """ returns a string representing a Player object.
        """
        return 'Player ' + self.checker
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker 
            of the Player object’s opponent.
        """
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'

    def next_move(self, b):
        """ accepts a Board object b as a parameter and returns the 
            column where the player wants to make the next move. 
            input b: a board object
        """
        self.num_moves += 1
        col = int(input("Enter a column: "))
        while b.can_add_to(col) == False:
            print('Try again!')
            col = int(input("Enter a column : "))
        return col

#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        super().__init__(checker)
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        """ returns a string representing an AIPlayer object. 
        """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the 
            board, and that returns the index of the column with the maximum 
            score. 
            input score: a list scores containing a score for each column of the 
            board
        """
        n = max(scores)
        s = []
        for i in range(len(scores)):
            if scores[i] == n:
                s += [i]
        if self.tiebreak == 'LEFT':
            return s[0]
        elif self.tiebreak == 'RIGHT':
            return s[-1]
        elif self.tiebreak == 'RANDOM':
            return random.randint(0, len(s))
   
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s 
            scores for the columns in b.
            input b: a board object
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = opponent.scores_for(b)
                maxscore = max(opp_scores)
                if maxscore == 100:
                    scores[col] = 0
                elif maxscore == 0:
                    scores[col] = 100
                else:
                    scores[col] = maxscore
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """ return the called AIPlayer‘s judgment of its best possible move.
        """
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))
        
    
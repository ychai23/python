#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 23:18:50 2019

@author: yuanmingchai
"""
class Board:
    
    def __init__(self, height, width):
        """ a constructor for Board objects """
        self.height = height
        self.width = width
        self.slots = [[' ']*width for r in range(height)]
    
    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string
    
        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'  # newline at the end of the row
        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.
        for col in range(self.width*2+1):
            s += '-'
        s += '\n'
        
        s += ' '
        n = 0
        for col in range(self.width):
            s += str(n) + " "
            n += 1
            if n > 9:
                n = 0
        return s
    
    def add_checker(self, checker, col):
        """ Adds the specified checker to column col 
            input checker: a specified checker
            input col: the column check goes in
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
    
        # put the rest of the method here
        row = 0
        if self.slots[self.height-1][col] == ' ':
            self.slots[self.height-1][col] = checker
        else:
            while self.slots[row][col] == ' ':
                row += 1
            self.slots[row-1][col] = checker
    
    def reset(self):
        """ Reset the Board object on which it is called by 
            setting all slots to contain a space character.
        """
        for i in range(self.width):
                for k in range(self.height):
                    self.slots[i][k] = ' ' 
        
    
    def add_checkers(self, colnums):
        """ Takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
            
    def can_add_to(self, col):
        """ Returns True if it is valid to place a checker in the column 
            col on the calling Board object. Otherwise, it should return False.
            input col: the column check goes in
        """
        if col < 0 or col > self.width-1:
            return False
        if self.slots[0][col] != ' ':
            return False
        else:
            return True
        
    def is_full(self):
        """ Returns True if the called Board object is completely full of 
            checkers, and returns False otherwise.
        """
        for col in range(self.width):
            if self.slots[0][col] == ' ':
                return False
        return True
    
    def remove_checker(self,col):
        """ Reset the Board object on which it is called 
            by setting all slots to contain a space character.
            input col: the column check goes in
        """
        for k in range(self.height):
            if self.slots[k][col] != ' ':
                self.slots[k][col] = ' '
                break
    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
            input checker: a specified checker
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
    
        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
            input checker: a specified checker
        """
        for col in range(self.width):
            for row in range(self.height - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False
    
    def is_down_diagonal_win(self, checker):
        """ Checks for a down-horizontal win for the specified checker.
            input checker: a specified checker
        """
        for col in range(self.width-3):
            for row in range(self.height-3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                   return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Checks for a up-diagonal win for the specified checker.
            input checker: a specified checker
        """
        for col in range(self.width-3):
            for row in range(3, self.height):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                   return True
        return False
    
                
    def is_win_for(self, checker):
        """ Accepts a parameter checker that is either 'X' or 'O', 
            and returns True if there are four consecutive slots 
            containing checker on the board. Otherwise, it should 
            return False.
            input checker: a specified checker
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
           return True
        return False
        
    
                
        


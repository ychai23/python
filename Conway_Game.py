#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111  
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps7pr2.py instead.

from ps7pr2 import *
from gol_graphics import *
import random

def count_neighbors(cellr, cellc, grid):
    """ returns the number of alive neighbors of the cell at position [cellr][cellc] in the specified grid.
        input cellr: row position of the cell
        input cellc: colom position of the cell
        input grid: any grid
    """
    n = 0
    if grid[cellr-1][cellc-1] == 1:
        n += 1
    if grid[cellr-1][cellc] == 1:
        n += 1
    if grid[cellr-1][cellc+1] == 1:
        n += 1
    if grid[cellr][cellc-1] == 1:
        n += 1
    if grid[cellr][cellc+1] == 1:
        n += 1
    if grid[cellr+1][cellc-1] == 1:
        n += 1
    if grid[cellr+1][cellc] == 1:
        n += 1
    if grid[cellr+1][cellc+1] == 1:
        n += 1
    return n

def next_gen(grid):
    """ takes a 2-D list called grid that represents the current generation 
        of cells, and that uses the rules of the Game of Life (see above) to 
        create and return a new 2-D list representing the next generation of cells.
        input grid: any grid
    """
    new_grid = copy(grid)
    print_grid(new_grid)
    for r in range(1, len(new_grid)-1):
        for c in range(1, len(new_grid[0])-1):
            count = count_neighbors(r, c, grid)
            if count < 2:
                new_grid[r][c] = 0
            elif count > 3:
                new_grid[r][c] = 0
            elif count == 3:
                new_grid[r][c] = 1
    return new_grid
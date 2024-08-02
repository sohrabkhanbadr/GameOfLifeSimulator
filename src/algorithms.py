 # algorithms.py

import numpy as np

def update_grid(grid):
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        for j in range(cols):
            live_neighbors = np.sum(grid[max(0, i-1):min(rows, i+2), max(0, j-1):min(cols, j+2)]) - grid[i, j]
            
            if grid[i, j] == 1:
                if live_neighbors in [2, 3]:
                    new_grid[i, j] = 1
            else:
                if live_neighbors == 3:
                    new_grid[i, j] = 1

    return new_grid

def create_block(grid, top_left):
    i, j = top_left
    grid[i:i+2, j:j+2] = 1

def create_glider(grid, top_left):
    i, j = top_left
    grid[i, j+1] = 1
    grid[i+1, j+2] = 1
    grid[i+2, j] = 1
    grid[i+2, j+1] = 1
    grid[i+2, j+2] = 1


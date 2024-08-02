# create_spaceship_example.py

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# اضافه کردن دایرکتوری src به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from algorithms import update_grid
from utils import count_alive_cells

def create_spaceship(grid, top_left):
    x, y = top_left
    spaceship_coords = [(x, y+1), (x, y+2), (x+1, y), (x+1, y+1), (x+2, y+1), (x+2, y+2), (x+3, y+1)]
    for coord in spaceship_coords:
        grid[coord] = 1

def display_grid(grid, step):
    plt.imshow(grid, cmap='binary')
    plt.title(f'Step {step}')
    plt.show()

# تنظیمات اولیه
grid_size = (20, 20)
grid = np.zeros(grid_size, dtype=int)

# اضافه کردن Spaceship
create_spaceship(grid, (5, 5))

# شبیه‌سازی چند مرحله
steps = 10
for step in range(steps):
    display_grid(grid, step)
    grid = update_grid(grid)
    print(f"Number of alive cells at step {step}: {count_alive_cells(grid)}")

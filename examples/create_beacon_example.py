# create_beacon_example.py

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# اضافه کردن دایرکتوری src به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from algorithms import update_grid
from utils import count_alive_cells

def create_beacon(grid, top_left):
    x, y = top_left
    beacon_coords = [(x, y), (x, y + 1), (x + 1, y), (x + 1, y + 1), (x + 2, y + 2), (x + 2, y + 3), (x + 3, y + 2), (x + 3, y + 3)]
    for coord in beacon_coords:
        grid[coord] = 1

def display_grid(grid, step):
    plt.imshow(grid, cmap='binary')
    plt.title(f'Step {step}')
    plt.show()

# تنظیمات اولیه
grid_size = (10, 10)
grid = np.zeros(grid_size, dtype=int)

# اضافه کردن Beacon
create_beacon(grid, (3, 3))

# شبیه‌سازی چند مرحله
steps = 5
for step in range(steps):
    display_grid(grid, step)
    grid = update_grid(grid)
    print(f"Number of alive cells at step {step}: {count_alive_cells(grid)}")

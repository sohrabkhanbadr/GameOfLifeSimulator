# create_pulsar_example.py

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# اضافه کردن دایرکتوری src به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from algorithms import update_grid
from utils import count_alive_cells

def create_pulsar(grid, top_left):
    x, y = top_left
    pulsar_coords = [
        (x + 1, y + 2), (x + 1, y + 3), (x + 1, y + 4), (x + 1, y + 8), (x + 1, y + 9), (x + 1, y + 10),
        (x + 2, y + 1), (x + 2, y + 6), (x + 2, y + 7), (x + 2, y + 12),
        (x + 3, y + 1), (x + 3, y + 6), (x + 3, y + 7), (x + 3, y + 12),
        (x + 4, y + 1), (x + 4, y + 6), (x + 4, y + 7), (x + 4, y + 12),
        (x + 6, y + 2), (x + 6, y + 3), (x + 6, y + 4), (x + 6, y + 8), (x + 6, y + 9), (x + 6, y + 10),
        (x + 7, y + 1), (x + 7, y + 6), (x + 7, y + 7), (x + 7, y + 12),
        (x + 8, y + 1), (x + 8, y + 6), (x + 8, y + 7), (x + 8, y + 12),
        (x + 9, y + 1), (x + 9, y + 6), (x + 9, y + 7), (x + 9, y + 12),
        (x + 10, y + 2), (x + 10, y + 3), (x + 10, y + 4), (x + 10, y + 8), (x + 10, y + 9), (x + 10, y + 10),
        (x + 12, y + 2), (x + 12, y + 3), (x + 12, y + 4), (x + 12, y + 8), (x + 12, y + 9), (x + 12, y + 10),
    ]
    for coord in pulsar_coords:
        grid[coord] = 1

def display_grid(grid, step):
    plt.imshow(grid, cmap='binary')
    plt.title(f'Step {step}')
    plt.show()

# تنظیمات اولیه
grid_size = (15, 15)
grid = np.zeros(grid_size, dtype=int)

# اضافه کردن Pulsar
create_pulsar(grid, (1, 1))

# شبیه‌سازی چند مرحله
steps = 10
for step in range(steps):
    display_grid(grid, step)
    grid = update_grid(grid)
    print(f"Number of alive cells at step {step}: {count_alive_cells(grid)}")

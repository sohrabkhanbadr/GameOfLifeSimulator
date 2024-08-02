# simulate_life_example.py

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# اضافه کردن دایرکتوری src به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from algorithms import create_glider, update_grid
from utils import count_alive_cells

# تنظیمات اولیه
grid_size = (20, 20)
grid = np.zeros(grid_size, dtype=int)

# اضافه کردن گلایدر
create_glider(grid, (5, 5))

def display_grid(grid, step):
    plt.imshow(grid, cmap='binary')
    plt.title(f'Step {step}')
    plt.show()

# شبیه‌سازی چند مرحله
steps = 10
for step in range(steps):
    display_grid(grid, step)
    grid = update_grid(grid)
    print(f"Number of alive cells at step {step}: {count_alive_cells(grid)}")

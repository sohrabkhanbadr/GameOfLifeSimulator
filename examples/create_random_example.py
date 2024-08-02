# create_random_example.py

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# اضافه کردن دایرکتوری src به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from algorithms import update_grid
from utils import count_alive_cells

def create_random_grid(grid_size, alive_prob=0.2):
    return np.random.choice([0, 1], size=grid_size, p=[1-alive_prob, alive_prob])

def display_grid(grid, step):
    plt.imshow(grid, cmap='binary')
    plt.title(f'Step {step}')
    plt.show()

# تنظیمات اولیه
grid_size = (20, 20)
grid = create_random_grid(grid_size)

# شبیه‌سازی چند مرحله
steps = 10
for step in range(steps):
    display_grid(grid, step)
    grid = update_grid(grid)
    print(f"Number of alive cells at step {step}: {count_alive_cells(grid)}")

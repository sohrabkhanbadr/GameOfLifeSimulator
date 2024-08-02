 
# main.py

from algorithms import update_grid, create_block, create_glider
from utils import count_alive_cells
import numpy as np
import matplotlib.pyplot as plt

# تنظیمات اولیه
grid_size = (20, 20)
grid = np.zeros(grid_size, dtype=int)

# اضافه کردن الگوها
create_block(grid, (1, 1))
create_glider(grid, (5, 5))

def display_grid(grid):
    plt.imshow(grid, cmap='binary')
    plt.title('Game of Life')
    plt.show()

# شبیه‌سازی چند مرحله
for _ in range(10):
    display_grid(grid)
    grid = update_grid(grid)

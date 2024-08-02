# create_block_example.py

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# اضافه کردن دایرکتوری src به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from algorithms import create_block
from utils import count_alive_cells

# تنظیمات اولیه
grid_size = (10, 10)
grid = np.zeros(grid_size, dtype=int)

# اضافه کردن بلوک
create_block(grid, (3, 3))

def display_grid(grid):
    plt.imshow(grid, cmap='binary')
    plt.title('Block Pattern')
    plt.show()

# نمایش الگوی بلوک و تعداد سلول‌های زنده
display_grid(grid)
print(f"Number of alive cells: {count_alive_cells(grid)}")

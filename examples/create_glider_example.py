# create_glider_example.py

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# اضافه کردن دایرکتوری src به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from algorithms import create_glider
from utils import count_alive_cells

# تنظیمات اولیه
grid_size = (10, 10)
grid = np.zeros(grid_size, dtype=int)

# اضافه کردن گلایدر
create_glider(grid, (2, 2))

def display_grid(grid):
    plt.imshow(grid, cmap='binary')
    plt.title('Glider Pattern')
    plt.show()

# نمایش الگوی گلایدر و تعداد سلول‌های زنده
display_grid(grid)
print(f"Number of alive cells: {count_alive_cells(grid)}")

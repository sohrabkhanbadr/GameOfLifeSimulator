 
# مثال‌ها

در این بخش، چندین مثال از ایجاد و شبیه‌سازی الگوهای مختلف بازی زندگی ارائه شده است.

## `create_block_example.py`

ایجاد و نمایش یک بلوک ثابت.

```python
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from algorithms import create_block
from utils import count_alive_cells

grid_size = (10, 10)
grid = np.zeros(grid_size, dtype=int)
create_block(grid, (3, 3))

def display_grid(grid):
    plt.imshow(grid, cmap='binary')
    plt.title('Block Pattern')
    plt.show()

display_grid(grid)
print(f"Number of alive cells: {count_alive_cells(grid)}")

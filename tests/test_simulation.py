 
# test_simulation.py

import unittest
import numpy as np
from algorithms import update_grid, create_block, create_glider

class TestSimulation(unittest.TestCase):

    def test_simulation_steps(self):
        grid = np.zeros((5, 5), dtype=int)
        create_glider(grid, (1, 1))
        for _ in range(4):  # شبیه‌سازی 4 مرحله
            grid = update_grid(grid)
        expected = np.array([[0, 0, 0, 0, 0],
                             [0, 0, 1, 1, 0],
                             [0, 1, 1, 0, 0],
                             [0, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0]], dtype=int)
        np.testing.assert_array_equal(grid, expected)

if __name__ == '__main__':
    unittest.main()

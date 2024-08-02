 
# test_algorithms.py

import unittest
import numpy as np
from algorithms import update_grid, create_block, create_glider

class TestGameOfLife(unittest.TestCase):

    def test_create_block(self):
        grid = np.zeros((4, 4), dtype=int)
        create_block(grid, (1, 1))
        expected = np.array([[0, 0, 0, 0],
                             [0, 1, 1, 0],
                             [0, 1, 1, 0],
                             [0, 0, 0, 0]])
        np.testing.assert_array_equal(grid, expected)

    def test_create_glider(self):
        grid = np.zeros((6, 6), dtype=int)
        create_glider(grid, (1, 1))
        expected = np.array([[0, 0, 0, 0, 0, 0],
                             [0, 1, 1, 0, 0, 0],
                             [1, 0, 1, 0, 0, 0],
                             [0, 1, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0]])
        np.testing.assert_array_equal(grid, expected)

    def test_update_grid(self):
        grid = np.array([[0, 0, 0],
                         [0, 1, 0],
                         [0, 0, 0]], dtype=int)
        new_grid = update_grid(grid)
        expected = np.array([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]], dtype=int)
        np.testing.assert_array_equal(new_grid, expected)

if __name__ == '__main__':
    unittest.main()

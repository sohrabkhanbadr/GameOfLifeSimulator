 # test_utils.py

import unittest
import numpy as np
from utils import count_alive_cells

class TestUtils(unittest.TestCase):

    def test_count_alive_cells(self):
        grid = np.array([[0, 1, 0],
                         [1, 1, 0],
                         [0, 0, 1]], dtype=int)
        self.assertEqual(count_alive_cells(grid), 4)

if __name__ == '__main__':
    unittest.main()


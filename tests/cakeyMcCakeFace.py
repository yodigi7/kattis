import unittest
from KattisProjects.kattis.cakeyMcCakeFace import *


class KattisTest(unittest.TestCase):
    def test_get_num_times_empty_lists(self):
        self.assertEqual(0, get_num_times([], [], 0))
        self.assertEqual(0, get_num_times([], [1, 2, 3], 1))
        self.assertEqual(0, get_num_times([1, 2, 3], [], 2))

    def test_get_non_empty_lists(self):
        self.assertEqual(1, get_num_times([1], [2], 1))
        self.assertEqual(1, get_num_times([1], [20], 19))
        self.assertEqual(3, get_num_times([10, 20, 30], [10, 20, 30], 0))
        self.assertEqual(2, get_num_times([10, 20, 30], [10, 20, 30], 10))
        self.assertEqual(1, get_num_times([10, 20, 30], [10, 20, 30], 20))
        self.assertEqual(0, get_num_times([10, 20, 30], [10, 20, 30], 21))
        self.assertEqual(0, get_num_times([10, 20, 30], [1, 2, 3], 2))


if __name__ == '__main__':
    unittest.main()

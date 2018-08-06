import unittest
from drmMessages import *


class TestDRMMessages(unittest.TestCase):
    """
        Unit Test for DRM Messages
    """

    def setUp(self):
        self.problem = Problem("EWPGAJRB")

    def test_divide(self):
        self.assertEqual(("EWPG", "AJRB"), self.problem._divide())

    def test_rotate(self):
        self.assertEqual(["ZRKB", "BKSC"], self.problem._rotate(("EWPG", "AJRB")))

    def test_merge(self):
        self.assertEqual("ABCD", self.problem._merge(["ZRKB", "BKSC"]))

    def test_solve(self):
        self.assertEqual("ABCD", Problem("EWPGAJRB").solve())


if __name__ == '__main__':
    unittest.main()

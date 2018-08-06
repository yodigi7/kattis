import unittest
from alienNumbers import *

class AlienNumbersTest(unittest.TestCase):

    def test_format_answer(self):
        self.assertEqual(format_answer("message", 10), "Case #10: message")

    def test_message_to_number(self):
        self.assertEqual([9], message_to_number("9", "0123456789"))

    def test_convert_message(self):
        self.assertEqual("bcde", convert_message([1, 2, 3, 4], "abcde"))

'''
    def test_solve(self):
        self.assertEqual("Case #1: Foo", solve(1))'''


if __name__ == '__main__':
    unittest.main()

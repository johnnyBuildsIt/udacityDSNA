import unittest
from ReversePolishNotation import ReversePolishNotation


class ReversePolishNotationTest(unittest.TestCase):

    def test1(self):
        in_list = ["3", "1", "+", "4", "*"]

        result = ReversePolishNotation.evaluate_post_fix(in_list)

        self.assertEqual(result, 16)

    def test2(self):
        in_list = ["4", "13", "5", "/", "+"]

        result = ReversePolishNotation.evaluate_post_fix(in_list)

        self.assertEqual(result, 6)

    def test3(self):
        in_list = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

        result = ReversePolishNotation.evaluate_post_fix(in_list)

        self.assertEqual(result, 22)


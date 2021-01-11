import unittest
from BalancedParentheses import BalancedParentheses
from BalancedParentheses import Stack


class BalancedParenthesesTest(unittest.TestCase):

    def testBalancedEquation(self):
        equation = "((3**2+8) * (5/2)) / (2+6)"

        result = BalancedParentheses.equation_checker(equation)

        self.assertTrue(result)

    def testNonBalancedEquation(self):
        equation = "((3**2+8 * (5/2)) / (2+6)"

        result = BalancedParentheses.equation_checker(equation)

        self.assertFalse(result)

    def testOnlyOpeningParens(self):
        equation = "(((("

        result = BalancedParentheses.equation_checker(equation)

        self.assertFalse(result)

import unittest

from recursion.Recursion import Recursion


class RecursionTest(unittest.TestCase):

    def testSumIntsFive(self):
        recurser = Recursion()

        result = recurser.sum_ints_upto(5)

        self.assertEqual(result, 15)

    def testFactorialOfFour(self):
        recurser = Recursion()

        result = recurser.factorial(4)

        self.assertEqual(result, 24)

    def testReverseString(self):
        recurser = Recursion()

        result = recurser.reverse_string("abc", -1)

        self.assertEqual(result, "cba")

    def testIsPalindromeEvenLen(self):
        recurser = Recursion()

        result = recurser.is_palindrome("abba")

        self.assertTrue(result)

    def testIsPalindromeOddLen(self):
        recurser = Recursion()

        result = recurser.is_palindrome("madam")

        self.assertTrue(result)

    def testIsPalindromeFalse(self):
        recurser = Recursion()

        result = recurser.is_palindrome("house")

        self.assertFalse(result)

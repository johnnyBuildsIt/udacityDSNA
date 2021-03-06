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

    def testAddOneSimple(self):
        recurser = Recursion()

        result = recurser.add_one([1, 2, 3, 4])

        self.assertEqual(result, [1, 2, 3, 5])

    def testAddOneLessSimple(self):
        recurser = Recursion()

        result = recurser.add_one([1, 2, 3, 9])

        self.assertEqual(result, [1, 2, 4, 0])

    def testAddOneLeastSimplest(self):
        recurser = Recursion()

        result = recurser.add_one([9, 9, 9, 9])

        self.assertEqual(result, [1, 0, 0, 0, 0])

    def testPermute(self):
        recurser = Recursion()

        result = recurser.permute([0, 1, 2])

        self.assertEqual([[0, 1, 2], [1, 0, 2], [1, 2, 0], [0, 2, 1], [2, 0, 1], [2, 1, 0]], result)

    def testKeypadCombinations23(self):
        recurser = Recursion()

        result = recurser.keypad(23)

        self.assertEqual(sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]), sorted(result))

    def testStaircase1(self):
        recurser = Recursion()

        result = recurser.staircase(1)

        self.assertEqual(result, 1)

    def testStaircase2(self):
        recurser = Recursion()

        result = recurser.staircase(2)

        self.assertEqual(result, 2)

    def testStaircase3(self):
        recurser = Recursion()

        result = recurser.staircase(3)

        self.assertEqual(result, 4)

    def testStaircase4(self):
        recurser = Recursion()

        result = recurser.staircase(4)

        self.assertEqual(result, 7)

    def testStaircaseCache(self):
        recurser = Recursion()

        result = recurser.staircase_cache(8)

        self.assertEqual(result, 81)

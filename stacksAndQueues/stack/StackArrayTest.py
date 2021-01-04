import unittest
from StackArray import StackArray


class StackArrayTest(unittest.TestCase):

    def testPush(self):
        stack = StackArray()

        stack.push(0)
        stack.push(1)

        self.assertEqual([0, 1, None, None, None, None, None, None, None, None], stack.arr)
        self.assertEqual(2, stack.next_index)
        self.assertEqual(2, stack.num_elements)

    def testPushingTooManyItems(self):
        stack = StackArray()

        stack.push(0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        stack.push(7)
        stack.push(8)
        stack.push(9)
        stack.push(10)

        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, None, None, None, None, None, None, None, None], stack.arr)

    def testSizeMethod(self):
        stack = StackArray()

        stack.push(0)
        stack.push(1)
        stack.push(2)

        self.assertEqual(3, stack.size())

    def testIsEmptyOnEmptyStack(self):
        stack = StackArray()

        self.assertTrue(stack.is_empty())

    def testIsEmptyOnNonEmptyStack(self):
        stack = StackArray()

        stack.push(0)
        stack.push(1)
        stack.push(2)

        self.assertFalse(stack.is_empty())

    def testPopOnEmptyStack(self):
        stack = StackArray()

        self.assertEqual(None, stack.pop())

    def testPopOnNonEmptyStack(self):
        stack = StackArray()

        stack.push(0)
        stack.push(1)
        stack.push(2)

        self.assertEqual(2, stack.pop())

import unittest
from ReverseStack import ReverseStack
from stacksAndQueues.stack.stackLinkedListImplementation.StackLinkedList import StackLinkedList


class ReverseStackTest(unittest.TestCase):

    def test1(self):
        stack = StackLinkedList()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

        reversed_stack = ReverseStack.reverse(stack)

        self.assertEqual(1, reversed_stack.pop())
        self.assertEqual(2, reversed_stack.pop())
        self.assertEqual(3, reversed_stack.pop())
        self.assertEqual(4, reversed_stack.pop())

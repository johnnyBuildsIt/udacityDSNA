from arraysAndLinkedLists.linkedList.Node import Node
from StackLinkedList import StackLinkedList
import unittest


class StackLinkedListTest(unittest.TestCase):

    def testPush(self):
        stack = StackLinkedList()

        stack.push(0)
        stack.push(1)

        self.assertEqual(2, stack.num_elements)

    def testSizeMethod(self):
        stack = StackLinkedList()

        stack.push(0)
        stack.push(1)
        stack.push(2)

        self.assertEqual(3, stack.size())

    def testIsEmptyOnEmptyStack(self):
        stack = StackLinkedList()

        self.assertTrue(stack.is_empty())

    def testIsEmptyOnNonEmptyStack(self):
        stack = StackLinkedList()

        stack.push(0)
        stack.push(1)
        stack.push(2)

        self.assertFalse(stack.is_empty())

    def testPopOnEmptyStack(self):
        stack = StackLinkedList()

        self.assertEqual(None, stack.pop())

    def testPopOnNonEmptyStack(self):
        stack = StackLinkedList()

        stack.push(0)
        stack.push(1)
        stack.push(2)

        self.assertEqual(2, stack.pop())
        self.assertEqual(2, stack.size())

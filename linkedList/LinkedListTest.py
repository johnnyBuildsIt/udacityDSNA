import unittest
from LinkedList import LinkedList


class MyTestCase(unittest.TestCase):
    def testPrependToEmptyList(self):
        linked_list = LinkedList()
        linked_list.prepend(1)

        self.assertEqual(linked_list.to_list(), [1])

    def testPrependToNonEmptyList(self):
        linked_list = LinkedList()
        linked_list.prepend(1)
        linked_list.prepend(2)

        self.assertEqual(linked_list.to_list(), [2, 1])

    def testAppendToEmptyList(self):
        linked_list = LinkedList()
        linked_list.append(1)

        self.assertEqual(linked_list.to_list(), [1])

    def testAppendToNonEmptyList(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)

        self.assertEqual(linked_list.to_list(), [1, 2])

    def testSearchForAValue(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        self.assertEqual(linked_list.search(1).value, 1)
        self.assertEqual(linked_list.search(4).value, 4)

    def testSearchForNonExistingValue(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        self.assertEqual(linked_list.search(7), None)

    def testSearchForValueInEmptyList(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.search(10), None)


if __name__ == '__main__':
    unittest.main()

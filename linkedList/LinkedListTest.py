import unittest
from LinkedList import LinkedList


class MyTestCase(unittest.TestCase):
    # Prepend Tests
    def testPrependToEmptyList(self):
        linked_list = LinkedList()
        linked_list.prepend(1)

        self.assertEqual(linked_list.to_list(), [1])

    def testPrependToNonEmptyList(self):
        linked_list = LinkedList()
        linked_list.prepend(1)
        linked_list.prepend(2)

        self.assertEqual(linked_list.to_list(), [2, 1])

    # Append Tests
    def testAppendToEmptyList(self):
        linked_list = LinkedList()
        linked_list.append(1)

        self.assertEqual(linked_list.to_list(), [1])

    def testAppendToNonEmptyList(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)

        self.assertEqual(linked_list.to_list(), [1, 2])

    # Search Tests
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

    def testRemoveFromEmptyList(self):
        linked_list = LinkedList()

        linked_list.remove(10)

        self.assertEqual(linked_list.to_list(), [])

    def testRemoveOnlyItemInList(self):
        linked_list = LinkedList()
        linked_list.append(1)

        linked_list.remove(1)

        self.assertEqual(linked_list.to_list(), [])

    def testRemoveItemThatExistsInList(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        linked_list.remove(4)

        self.assertEqual(linked_list.to_list(), [1, 2, 3])

    def restRemoveItemThatDoesNotExistInList(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        self.assertEqual(linked_list.to_list(), [1, 2, 4, 3 ])


if __name__ == '__main__':
    unittest.main()

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

    # Remove Tests
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

    def testRemoveItemThatDoesNotExistInList(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        linked_list.remove(8)

        self.assertEqual(linked_list.to_list(), [1, 2, 4, 3])

    # Pop Tests
    def testPopOnEmptyList(self):
        linked_list = LinkedList()

        value = linked_list.pop()

        self.assertEqual(value, None)
        self.assertEqual(linked_list.to_list(), [])

    def testPopOnListWithOneItem(self):
        linked_list = LinkedList()
        linked_list.append(4)

        value = linked_list.pop()

        self.assertEqual(value, 4)
        self.assertEqual(linked_list.to_list(), [])

    def testPopOnListWithMultipleItems(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        value = linked_list.pop()

        self.assertEqual(value, 1)
        self.assertEqual(linked_list.to_list(), [2, 4, 3])

    # Insert Tests
    def testInsertOnEmptyListAtAppropriatePosition(self):
        linked_list = LinkedList()

        linked_list.insert(4, 0)

        self.assertEqual(linked_list.to_list(), [4])

    def testInsertOnEmptyListAtInappropriatePosition(self):
        linked_list = LinkedList()

        linked_list.insert(4, 5)

        self.assertEqual(linked_list.to_list(), [4])

    def testInsertOnPopulatedListAtAppropriatePosition(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        linked_list.insert(10, 2)

        self.assertEqual(linked_list.to_list(), [1, 2, 10, 3, 4])

    def testInsertOnPopulatedListAtInappropriatePosition(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        linked_list.insert(10, 20)

        self.assertEqual(linked_list.to_list(), [1, 2, 3, 4, 10])


if __name__ == '__main__':
    unittest.main()

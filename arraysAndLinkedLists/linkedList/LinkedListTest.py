import unittest
from LinkedList import LinkedList


class LinkedListTest(unittest.TestCase):
    # Prepend Tests
    def testPrependToEmptyList(self):
        linked_list = LinkedList()
        linked_list.prepend(1)

        self.assertEqual([1], linked_list.to_list())

    def testPrependToNonEmptyList(self):
        linked_list = LinkedList()
        linked_list.prepend(1)
        linked_list.prepend(2)

        self.assertEqual([2, 1], linked_list.to_list())

    # Append Tests
    def testAppendToEmptyList(self):
        linked_list = LinkedList()
        linked_list.append(1)

        self.assertEqual([1], linked_list.to_list())

    def testAppendToNonEmptyList(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)

        self.assertEqual([1, 2], linked_list.to_list())

    # Search Tests
    def testSearchForAValue(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        self.assertEqual(1, linked_list.search(1).value)
        self.assertEqual(4, linked_list.search(4).value)

    def testSearchForNonExistingValue(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        self.assertEqual(None, linked_list.search(7))

    def testSearchForValueInEmptyList(self):
        linked_list = LinkedList()

        self.assertEqual(None, linked_list.search(10))

    # Remove Tests
    def testRemoveFromEmptyList(self):
        linked_list = LinkedList()

        linked_list.remove(10)

        self.assertEqual([], linked_list.to_list())

    def testRemoveOnlyItemInList(self):
        linked_list = LinkedList()
        linked_list.append(1)

        linked_list.remove(1)

        self.assertEqual([], linked_list.to_list())

    def testRemoveItemThatExistsInList(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        linked_list.remove(4)

        self.assertEqual([1, 2, 3], linked_list.to_list())

    def testRemoveItemThatDoesNotExistInList(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        linked_list.remove(8)

        self.assertEqual([1, 2, 4, 3], linked_list.to_list())

    def testRemoveFirstItemInList(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        linked_list.remove(1)

        self.assertEqual([2, 4, 3], linked_list.to_list())

    # Pop Tests
    def testPopOnEmptyList(self):
        linked_list = LinkedList()

        value = linked_list.pop()

        self.assertEqual(value, None)
        self.assertEqual([], linked_list.to_list())

    def testPopOnListWithOneItem(self):
        linked_list = LinkedList()
        linked_list.append(4)

        value = linked_list.pop()

        self.assertEqual(value, 4)
        self.assertEqual([], linked_list.to_list())

    def testPopOnListWithMultipleItems(self):
        linked_list = LinkedList()
        linked_list.prepend(2)
        linked_list.prepend(1)
        linked_list.append(4)
        linked_list.append(3)

        value = linked_list.pop()

        self.assertEqual(value, 1)
        self.assertEqual([2, 4, 3], linked_list.to_list())

    # Insert Tests
    def testInsertOnEmptyListAtAppropriatePosition(self):
        linked_list = LinkedList()

        linked_list.insert(4, 0)

        self.assertEqual([4], linked_list.to_list())

    def testInsertOnEmptyListAtInappropriatePosition(self):
        linked_list = LinkedList()

        linked_list.insert(4, 5)

        self.assertEqual([4], linked_list.to_list())

    def testInsertOnPopulatedListAtAppropriatePosition(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        linked_list.insert(10, 2)

        self.assertEqual([1, 2, 10, 3, 4], linked_list.to_list())

    def testInsertOnPopulatedListAtInappropriatePosition(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        linked_list.insert(10, 20)

        self.assertEqual([1, 2, 3, 4, 10], linked_list.to_list())

    # Size Tests
    def testSizeOfEmptyList(self):
        linked_list = LinkedList()

        self.assertEqual(0, linked_list.size())

    def testSizeOfListWithOneElement(self):
        linked_list = LinkedList()
        linked_list.append(1)

        self.assertEqual(1, linked_list.size())

    def testSizeOfListWithMultipleElements(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        self.assertEqual(4, linked_list.size())

    # Reverse Tests
    def testReverseEmptyList(self):
        linked_list = LinkedList()

        linked_list.reverse()

        self.assertEqual([], linked_list.to_list())

    def testReverseListWithOneElement(self):
        linked_list = LinkedList()
        linked_list.append(1)

        linked_list.reverse()

        self.assertEqual([1], linked_list.to_list())

    def testReverseListWithMultipleElements(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        linked_list.reverse()

        self.assertEqual([4, 3, 2, 1], linked_list.to_list())


if __name__ == '__main__':
    unittest.main()

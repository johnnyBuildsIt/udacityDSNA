from LinkedListHelpers import LinkedListHelpers
from LinkedList import LinkedList
import unittest


class LinkedListHelpersTest(unittest.TestCase):

    # Merges Tests
    def testMergeTwoEmptyLinkedLists(self):
        linked_list = LinkedList()
        linked_list1 = LinkedList()

        merged_list = LinkedListHelpers.merge(linked_list, linked_list1)

        self.assertEqual([], merged_list.to_list())

    def testMergeTwoNonEmptyLinkedLists(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(5)
        linked_list1 = LinkedList()
        linked_list1.append(2)
        linked_list1.append(4)

        merged_list = LinkedListHelpers.merge(linked_list, linked_list1)

        self.assertEqual([1, 2, 3, 4, 5], merged_list.to_list())

    def testMergeEmptyAndNonEmptyLinkedList(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(5)
        linked_list1 = LinkedList()

        merged_list = LinkedListHelpers.merge(linked_list, linked_list1)

        self.assertEqual([1, 3, 5], merged_list.to_list())

    # Flatten Tests
    def testFlattenEmptyLinkedList(self):
        linked_list = LinkedList()

        flattened_list = LinkedListHelpers.flatten(linked_list)

        self.assertEqual([], flattened_list.to_list())

    def testFlattenFlatList(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(5)

        flattened_list = LinkedListHelpers.flatten(linked_list)

        self.assertEqual([1, 3, 5], flattened_list.to_list())

    def testFlattenNestedListWithTwoNodes(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(5)
        linked_list1 = LinkedList()
        linked_list1.append(2)
        linked_list1.append(4)
        nested_list = LinkedList()
        nested_list.append(linked_list)
        nested_list.append(linked_list1)

        flattened_list = LinkedListHelpers.flatten(nested_list)

        self.assertEqual([1, 2, 3, 4, 5], flattened_list.to_list())

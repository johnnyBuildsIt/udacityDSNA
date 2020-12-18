from LinkedListHelpers import LinkedListHelpers
from LinkedList import LinkedList
import unittest


class LinkedListHelpersTest(unittest.TestCase):

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

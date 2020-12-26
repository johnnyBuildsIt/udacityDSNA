from .EvenAfterOdd import EvenAfterOdd
from ..linkedList.LinkedList import LinkedList
import unittest


class EvenAfterOddTest(unittest.TestCase):

    def testOneToTenInput(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        linked_list.append(6)
        linked_list.append(7)
        linked_list.append(8)
        linked_list.append(9)
        linked_list.append(10)
        even_after_odd = EvenAfterOdd()

        even_after_odd_list = even_after_odd.arrange_list(linked_list)

        self.assertEqual([1, 3, 5, 7, 9, 2, 4, 6, 8, 10], even_after_odd_list.to_list())

    def testAllOddInput(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(5)
        linked_list.append(7)
        linked_list.append(9)
        even_after_odd = EvenAfterOdd()

        even_after_odd_list = even_after_odd.arrange_list(linked_list)

        self.assertEqual([1, 3, 5, 7, 9], even_after_odd_list.to_list())

    def testAllEvenInput(self):
        linked_list = LinkedList()
        linked_list.append(2)
        linked_list.append(4)
        linked_list.append(6)
        linked_list.append(8)
        linked_list.append(10)
        even_after_odd = EvenAfterOdd()

        even_after_odd_list = even_after_odd.arrange_list(linked_list)

        self.assertEqual([2, 4, 6, 8, 10], even_after_odd_list.to_list())

    def testWithOddAfterEvenInput(self):
        linked_list = LinkedList()
        linked_list.append(2)
        linked_list.append(4)
        linked_list.append(6)
        linked_list.append(8)
        linked_list.append(10)
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(5)
        linked_list.append(7)
        linked_list.append(9)
        even_after_odd = EvenAfterOdd()

        even_after_odd_list = even_after_odd.arrange_list(linked_list)

        self.assertEqual([1, 3, 5, 7, 9, 2, 4, 6, 8, 10], even_after_odd_list.to_list())

    def testWithOneOddAtEnd(self):
        linked_list = LinkedList()
        linked_list.append(2)
        linked_list.append(4)
        linked_list.append(6)
        linked_list.append(8)
        linked_list.append(10)
        linked_list.append(1)
        even_after_odd = EvenAfterOdd()

        even_after_odd_list = even_after_odd.arrange_list(linked_list)

        self.assertEqual([1, 2, 4, 6, 8, 10], even_after_odd_list.to_list())

    def testWithOneEvenAtStart(self):
        linked_list = LinkedList()
        linked_list.append(2)
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(5)
        linked_list.append(7)
        linked_list.append(9)
        even_after_odd = EvenAfterOdd()

        even_after_odd_list = even_after_odd.arrange_list(linked_list)

        self.assertEqual([1, 3, 5, 7, 9, 2], even_after_odd_list.to_list())

    def testWithEmptyInput(self):
        linked_list = LinkedList()
        even_after_odd = EvenAfterOdd()

        even_after_odd_list = even_after_odd.arrange_list(linked_list)

        self.assertEqual([], even_after_odd_list.to_list())

    def testWithSingleOddInput(self):
        linked_list = LinkedList()
        linked_list.append(1)
        even_after_odd = EvenAfterOdd()

        even_after_odd_list = even_after_odd.arrange_list(linked_list)

        self.assertEqual([1], even_after_odd_list.to_list())

    def testWithSingleEvenInput(self):
        linked_list = LinkedList()
        linked_list.append(2)
        even_after_odd = EvenAfterOdd()

        even_after_odd_list = even_after_odd.arrange_list(linked_list)

        self.assertEqual([2], even_after_odd_list.to_list())
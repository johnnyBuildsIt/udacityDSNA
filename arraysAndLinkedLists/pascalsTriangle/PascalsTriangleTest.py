from PascalsTriangle import PascalsTriangle
import unittest


class PascalsTriangleTest(unittest.TestCase):

    def testPascalsTriangleN0(self):
        pascals_triangle = PascalsTriangle()

        expected = pascals_triangle.return_nth_row(0)

        self.assertEqual([1], expected)

    def testPascalsTriangleN1(self):
        pascals_triangle = PascalsTriangle()

        expected = pascals_triangle.return_nth_row(1)

        self.assertEqual([1, 1], expected)

    def testPascalsTriangleN2(self):
        pascals_triangle = PascalsTriangle()

        expected = pascals_triangle.return_nth_row(2)

        self.assertEqual([1, 2, 1], expected)

    def testPascalsTriangleN3(self):
        pascals_triangle = PascalsTriangle()

        expected = pascals_triangle.return_nth_row(3)

        self.assertEqual([1, 3, 3, 1], expected)

    def testPascalsTriangleN4(self):
        pascals_triangle = PascalsTriangle()

        expected = pascals_triangle.return_nth_row(4)

        self.assertEqual([1, 4, 6, 4, 1], expected)
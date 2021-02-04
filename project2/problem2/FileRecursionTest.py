from FileRecursion import FileRecursion
import unittest


class FileRecursionTest(unittest.TestCase):

    def test1(self):
        finder = FileRecursion()
        print(finder.find_files(".c", "testdir"))

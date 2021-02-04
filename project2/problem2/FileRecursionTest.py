from FileRecursion import FileRecursion
import unittest


class FileRecursionTest(unittest.TestCase):

    def test1(self):
        finder = FileRecursion()

        search_list = finder.find_files(".c", "testdir")

        self.assertEqual(sorted(search_list), sorted(['b.c', 't1.c', 'a.c', 'a.c']))
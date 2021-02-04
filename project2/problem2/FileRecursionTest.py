from FileRecursion import FileRecursion
import unittest


class FileRecursionTest(unittest.TestCase):

    def testFindCFiles(self):
        finder = FileRecursion()

        search_list = finder.find_files(".c", "testdir")

        self.assertEqual(sorted(search_list), sorted(['testdir/subdir1/a.c',
                                                      'testdir/subdir3/subsubdir1/b.c',
                                                      'testdir/subdir5/a.c',
                                                      'testdir/t1.c']))

    def testFindHFiles(self):
        finder = FileRecursion()

        search_list = finder.find_files(".h", "testdir")

        self.assertEqual(sorted(search_list), sorted(['testdir/subdir1/a.h',
                                                      'testdir/subdir3/subsubdir1/b.h',
                                                      'testdir/subdir5/a.h',
                                                      'testdir/t1.h']))

    def testFindGitFiles(self):
        finder = FileRecursion()

        search_list = finder.find_files(".gitkeep", "testdir")

        self.assertEqual(sorted(search_list), sorted(['testdir/subdir2/.gitkeep', 'testdir/subdir4/.gitkeep']))

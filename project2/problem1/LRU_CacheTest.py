from LruCache import LruCache
import unittest


class LruCacheTest(unittest.TestCase):

    def testSetOneAndGetOne(self):
        lru_cache = LruCache(5)
        lru_cache.set(1, 1)

        result = lru_cache.get(1)

        self.assertEqual(result, 1)

    def testSetOneThenTwoShouldOverWriteOne(self):
        lru_cache = LruCache(1)
        lru_cache.set(1, 1)
        lru_cache.set(2, 2)

        result1 = lru_cache.get(1)
        result2 = lru_cache.get(2)

        self.assertEqual(result1, -1)
        self.assertEqual(result2, 2)

    def testDontAddDuplicateElements(self):
        lru_cache = LruCache(1)
        lru_cache.set(1, 1)
        lru_cache.set(1, 1)
        lru_cache.set(1, 1)

        size = lru_cache.lruNodes.size

        self.assertEqual(size, 1)

    def testUdacity1(self):
        our_cache = LruCache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)

        self.assertEqual(1, our_cache.get(1))
        self.assertEqual(2, our_cache.get(2))
        self.assertEqual(-1, our_cache.get(9))

    def testUdacity2(self):
        our_cache = LruCache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)
        our_cache.get(1)
        our_cache.get(2)
        our_cache.set(5, 5)
        our_cache.set(6, 6)

        self.assertEqual(-1, our_cache.get(3))

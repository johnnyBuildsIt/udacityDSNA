from LruCache import LruCache
import unittest


class LruCacheTest(unittest.TestCase):

    def test1(self):
        our_cache = LruCache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)

        self.assertEqual(1, our_cache.get(1))
        self.assertEqual(2, our_cache.get(2))
        self.assertEqual(-1, our_cache.get(9))

    def test2(self):
        our_cache = LruCache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)
        our_cache.get(1)
        our_cache.get(2)

        self.assertEqual(-1, our_cache.get(3))

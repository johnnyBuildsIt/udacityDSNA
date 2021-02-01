from pyllist import dllist


class LruCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cacheKeys = {}
        self.lruNodes = dllist()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cacheKeys:
            node = self.cacheKeys[key]
            self.lruNodes.remove(node)
            self.lruNodes.appendleft(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.lruNodes.size == self.capacity:
            self.cacheKeys.pop(self.lruNodes.pop())

        node = self.lruNodes.appendleft(value)
        self.cacheKeys[key] = node

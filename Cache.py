"""
store(key)
fetch(*key)
purge(key)
_update
"""
from collections import OrderedDict


class Cache:
    def __init__(self, size):
        self._cache = dict()
        self.size = size

    def store(self, key, value):
        if len(self._cache) == self.size - 1:
            key_list = self._cache.keys()
            self.purge(key_list(0))
        self._cache[key] = value

    def fetch(self, *keys):
        temp = {self._cache.get(key) for key in keys}
        for k, v in temp:
            self.store(k, v)
        return temp

    def purge(self, key):
        self._cache.pop(key)

    def _update(self):
        pass


# cache = Cache(1000)
# cache.store('a', '1')
# cache.fetch('a')
# cache.purge('a')

class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.cache = OrderedDict()

    def get(self, key):
        if self.cache.get(key):
            val = self.cache.get(key)
            self.cache.pop(key)
            self.cache[key] = val
        else:
            val = -1
        return val

    def put(self, key, val):
        if len(self.cache) >= self.cap:
            keyslist = list(self.cache.keys())
            self.cache.pop(keyslist[0])
        self.cache[key] = val

    def display(self):
        for k, v in self.cache.items():
            print(k, v)


lruc = LRUCache(2)
lruc.put(1, "a")
lruc.put(2, "b")
print(lruc.get(1))
lruc.put(3, "c")
print(lruc.get(1))
print(lruc.get(2))
lruc.display()


class DoubleLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCacheDLL:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}  # key -> DLL Node
        self.head = DoubleLinkedList(0, 0)
        self.tail = DoubleLinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # when accessed, remove from DLL and put back in the front to make it most recently used.
        if self.cache.get(key):
            node = self.cache.get(key)
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key, val):
        # if new key, put to the cache, add to the DLL near the head
        # if existing key, remove from DLL, add key with new val near head.
        if key in self.cache.get(key):
            node = self.cache.get(key)
            self._remove(node)
        node = DoubleLinkedList(key, val)
        self._add(node)
        if len(self.cache) > self.cap:
            self._remove(self.tail.prev)

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def _add(self, node):
        nxt = self.head.next
        node.next = nxt
        nxt.prev = node
        self.head.next = node
        node.prev = self.head

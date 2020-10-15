"""
store(key)
fetch(*key)
purge(key)
_update
"""


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


cache = Cache(1000)
cache.store('a', '1')
cache.fetch('a')
cache.purge('a')

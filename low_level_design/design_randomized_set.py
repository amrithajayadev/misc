"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""
import random


class RandomizedSet:
    def __init__(self):
        self.num_hash = {}
        self.num_list = []

    def insert(self, val):
        if val in self.num_hash:  # O(1)
            return False
        else:
            self.num_list.append(val)  # O(1)
            self.num_hash[val] = len(self.num_list) - 1  # O(1)
            return True

    def remove(self, val):
        if val in self.num_hash:
            pos = self.num_hash[val]
            self.num_list[pos] = self.num_list[-1]
            self.num_hash[self.num_list[-1]] = pos
            self.num_list.pop()  # O(1)
            self.num_hash.pop(val)  # O(1)
            return True
        else:
            return False

    def getRandom(self):
        return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
"""
1. Can we use builtin random functions?
2. What happens if only 1 element is present in the map and list
"""
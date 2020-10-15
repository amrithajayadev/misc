# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:06:57 2019

@author: jayada1

create heap from an unsorted array


"""


class BinaryHeap():
    def __init__(self):
        self.heap = []

    def insert(self, val):
        i = self.size()
        self.heap.append(val)

        while i != 0:
            p = self.parent(i)
            if self.get(i) > self.get(p):
                self.swap(i, p)
            i = p

    def insert_simple(self, arr):
        for i in arr:
            self.heap.append(i)
        return self.heap

    def delete(self):
        self.heap.pop(0)

    # The method size returns the number of elements in the heap.
    def size(self):
        return len(self.heap)

    # The method parent takes an index as argument and returns the index of the parent.
    def parent(self, index):
        return (index - 1) // 2

    # The method left takes an index as argument and returns the index of its left child.
    def left(self, index):
        return 2 * index + 1

    # The method right takes an index as argument and returns the index of its right child.
    def right(self, index):
        return 2 * index + 2

        # The method get takes an index as argument and returns the key at the index.

    def get(self, index):
        return self.heap[index]

        # The method get_max returns the maximum element in the heap by returning the first element in the list items.

    def get_max(self):
        if self.size == 0:
            return None
        return self.heap[0]

    # The method extract_max returns the the maximum element in the heap and removes it.
    def extract_max(self):
        pop = self.heap.index(self.get_max())
        return self.heap.pop(pop)

    # The method max_heapify takes an index as argument and modifies
    # the heap structure at and below the node at this index to make it
    # satisfy the heap property.
    def max_heapify(self, index):
        pass

    def swap(self, index, maxval_i):
        self.heap[index], self.heap[maxval_i] = self.heap[maxval_i], self.heap[index]

    def heapify(self, index):
        heap = self.heap

        ri = self.right(index)
        li = self.left(index)
        size = self.size()
        print(ri, li, sep=' ')

        if li < size and heap[li] > heap[index]:
            maxval_i = li
        if ri < size and heap[ri] > heap[maxval_i]:
            maxval_i = ri
        elif maxval_i != index:
            self.swap(index, maxval_i)
            self.heapify(index)


bheap = BinaryHeap()

print('Menu')
print('insert <data>')
print('max get')
print('max extract')
print('print')
print('heapify')
print('quit')

while True:
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        bheap.insert(data)
    elif operation == 'max':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Maximum value: {}'.format(bheap.get_max()))
        elif suboperation == 'extract':
            print('Maximum value removed: {}'.format(bheap.extract_max()))
    elif operation == 'print':
        print(bheap.heap)
    elif operation == 'heapify':
        heap = bheap.insert_simple([7, 10, 4, 3, 20, 15])
        for i in range(len(heap), 0, -1):
            bheap.heapify(i)
    elif operation == 'quit':
        break

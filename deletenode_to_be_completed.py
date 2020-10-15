# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:24:23 2019

@author: jayada1
Delete a node from given position in a doubly linked list.

Input:

In this problem, method takes two argument: the address of the head of the linked list 
and the node you have to delete. The function should not read any input from stdin/console.
The Node structure has a data part which stores the data and a next pointer 
which points to the next element of the linked list. 
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Your task is to complete this function
# function should just delete the Node
# function shouldn't print or return any data
def deleteNode(head, x):
    # Code here
    curr = head
    pos = 1
    if x == 1:
        head = curr.next
        head.prev = None
    pos = 1
    while curr is not None:
        if pos == x:
            prev = curr.prev
            nexts = curr.next
            prev.next = nexts
            nexts.prev = prev
        curr = curr.next
        
        
arr = [1,2,3,4,5]
if 5 in arr:
    print("True")
else:
    print("false")
    
    
for i in range(0,5,2):
    print (arr[i])
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 21:40:23 2019

@author: jayada1
"""
''' This is a function problem.You only need to complete the function given below '''
#function Template for python3
"""
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""
# your task is to complete this function
# function shouldn't return anything
# use self.head to access head in the method

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

     
def reverseList(self):
    # Code here
    if self.head is None:
        return None

    current = self.head
    prev = None
    while current is not None:
        nexts = current.next
        current.next = prev
        prev = current
        current = nexts
    self.head = prev
    


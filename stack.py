# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 21:10:09 2019

@author: jayada1
"""

# function should append an element on to the stack
def push(arr, ele):
    # Code here
    arr.insert(0,ele)
# Function should pop an element from stack
def pop(arr):
    # Code here
    arr.pop(0)
# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    if len(arr)==n:
        return True
    else:
        return False
# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    return False if len(arr)==0 else True
# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    return min(arr)
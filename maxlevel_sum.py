# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 01:20:29 2019

@author: jayada1

Given a Binary Tree having positive and negative nodes, the task is to find maximum sum level in it.

Examples:

Input :               4
                    /   \
                   2    -5
                  / \    /\
                -1   3 -2  6
Output: 6
Explanation :
Sum of all nodes of 0'th level is 4
Sum of all nodes of 1'th level is -3
Sum of all nodes of 0'th level is 6
Hence maximum sum is 6

Input :          1
               /   \
             2      3
           /  \      \
          4    5      8
                    /   \
                   6     7  
Output :  17
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def getSum(root, level):
    if root is None:
        return 0
    if level == 1:
        return root.data
    return getSum(root.left, level-1) + getSum(root.right, level-1)
    
    
def height(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    
    h = lheight+1 if lheight > rheight else rheight +1
    
    return h
    
    
def maxLevelSum(root):
    # Code here
    h = height(root)
    suml = 0
    max_sum = 0
    
    for l in range(1,h+1):
        suml = getSum(root, l)
        if suml > max_sum:
            max_sum= suml
    return max_sum
        

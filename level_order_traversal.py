# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:47:28 2019

@author: jayada1
"""

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Tree:
    def createNode(self, data):
        return Node(data)
            
    def traverse(self, root):
        if root is not None:
            self.traverse(root.left)
            print(root.data, end=' ')
            self.traverse(root.right)
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        tree = Tree()
        lis = {}
        root = None
        root = tree.createNode(int(arr[0]))
        lis[root.data]=root
        k=0
        for j in range(n):
            if int(arr[k]) in lis:
                ptr = tree.createNode(int(arr[k+1]))
                if arr[k+2]=='L':
                    lis[int(arr[k])].left = ptr
                else:
                    lis[int(arr[k])].right = ptr
                lis[int(arr[k+1])] = ptr
                k+=3
        levelOrder(root)
        print()
# Contributed by: Harshit Sidhwa

''' This is a function problem.You only need to complete the function given below '''
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
# Your task is to complete this function
# Function should print the level order of the tree in required format
# only input to function is the root of the tree
def height(root):
    if root is None:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right)
    
    h = lheight+1 if lheight>rheight else rheight + 1
    return h
    
def get_nodes(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    get_nodes(root.left, level-1)
    get_nodes(root.right, level-1)
    
def levelOrder( root ):
    # Code here
    h = height(root)
    for l in range(1,h+1):
        get_nodes(root, l)
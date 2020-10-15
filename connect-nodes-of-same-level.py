# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:05:11 2019

@author: jayada1
"""

{
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict # default dict used as a map, to store node-value mapping.
#Contributed by : Nagendra Jha
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        self.nextRight = None
# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)
    def Insert(self,parent, child,dir):
        if self.root is None:
            root_node = Node(parent)
            child_node = Node(child)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return
        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        self.map_nodes[child] = child_node
        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return
def InOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated in order Traversal of the given tree.
    '''
    if root is None: # check if the root is none
        return
    InOrder(root.left) # do in order of left child
    print(root.data, end=" ")  # print root of the given tree
    InOrder(root.right) # do in order of right child
def printSpecial(root):
    leftmost_node = root
    while leftmost_node :
        curr_node = leftmost_node
        leftmost_node = None
        if curr_node.left :
            leftmost_node = curr_node.left
        elif curr_node.right :
            leftmost_node = curr_node.right
        print(curr_node.data,end=" ")
        while curr_node.nextRight :
            print(curr_node.nextRight.data,end=" ")
            curr_node = curr_node.nextRight
    print()
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list
        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.
        connect(tree.root)
        printSpecial(tree.root)
        InOrder(tree.root)
        print()

}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3

def connect(root):
    '''
    :param root: root of the given tree
    :return: none, just connect accordingly.
    {
        # Node Class:
        class Node:
            def __init__(self,val):
                self.data = val
                self.left = None
                self.right = None
                self.nextRight = None
    }
    '''
    
    #h = height(root)
    if root is None:
        return
    q = list()
    q.append(root)
    while len(q)>0:
        node = q.pop(0)
        
        node.nextRight = q[0] if len(q)>0 else None
        
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
        
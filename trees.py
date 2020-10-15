# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 07:54:55 2019

@author: jayada1
"""

"""
Write Code to Determine if Two Trees are Identical
Two trees are identical when they have same data and arrangement of data is also same.
To identify if two trees are identical, we need to traverse both trees simultaneously, and while traversing we need to compare data and children of the trees.
"""

class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        

def identical_trees(a,b):
    if a is not None and b is not None:
        if a.data == b.data and identical_trees(a.right, b.right) and identical_trees(a.left, b.left):
            return True
        else:
            return False

def insert_tree(node, data):
    if node is None:
        return Node(data)
    else:
        if data < node.data:
            node.left = insert_tree(node.left, data)
        else:
            node.right = insert_tree(node.right, data)
    return node

"""
       Print trees in order
       1
      /\
     3  2
       / \
       5  4   inorder traversal : 3 1 5 2 4
"""
def print_inOrder(node) :
    if (node == None):  
        return
          
    print_inOrder(node.left)  
    print(node.data, end = " ")  
    print_inOrder(node.right)  
 
"""
1. check if left node is leaf. if not, mirror
2. check if right node is a leaf. If nor mirror
3. else swap the nodes.
"""    


def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=" ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)
    
    
def mirror(root):
    # Code here
    if root.left is not None:
        mirror(root.left)
    if root.right is not None:
        mirror(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp

"""
// Convert a given tree to a tree where every node contains sum of values of
// nodes in left and right subtrees in the original tree
"""
def sumTree(node):
    if node is None:
        return 0
    old_val = node.data
    node.data = sumTree(node.left) + sumTree(node.right)
    return old_val + node.data

def sum_tree(node):
    if node is None:
        return 0
    else:
        return node.data + sum_tree(node.left) + sum_tree(node.right)


"""
Given a Binary Tree, find the maximum width of it. Maximum width is defined as the maximum number of nodes in any level.
For example, maximum width of following tree is 4 as there are 4 nodes at 3rd level.

          1
       /     \
     2        3
   /    \    /    \
  4    5   6    7
    \
      8
 """
def getHeight(node):
    if node is None:
        return 0
    else:
        lheight = getHeight(node.left)
        rheight = getHeight(node.right)
        height = lheight +1 if lheight>rheight else rheight+1
        return height
 
def getWidth(node, level):
    if node is None:
        return 0
    if level == 1:
        return 1
    else:
        return getWidth(node.left, level-1) + getWidth(node.right, level-1)
    
def getMaxWidth(node):
    h = getHeight(node)
    max_width = 0
    for level in range (1,h+1):
        width = getWidth(node, level)
        if width > max_width:
            max_width = width
    return max_width

        
def isBalanced(root):
    
    #add code here
    lheight = getHeight(root.left)
    rheight = getHeight(root.right)
    
    if lheight > rheight:
        if lheight-rheight ==1:
            return True
    else:
        if rheight-lheight ==1:
            return True
    return False

def printSpiral(root, level):
    # Code here
    node = root
    if node is not None:
        level += 1
        if(level == 1): 
            print(root.data, end = " ")  
        elif level > 1 and level%2 == 1:
            printSpiral(node.left, level)
            printSpiral(node.right, level)         
        else:
            printSpiral(node.right, level)
            printSpiral(node.left, level)

"""
Given a simple expression tree, which is also a full binary tree consisting of 
basic binary operators i.e., + , – ,* and / and some integers, 
Your task is to evaluate the expression tree.
     +
    / \
   *   -
  / \ / \
 5  4 100 20

5*4 + 100-20 = 20+80 =100
"""
def evalExpressionTree(root):
    # Code here
    node = root
    if node.left is None and node.right is None:
        return node.data
    a = evalExpressionTree(node.left)
    b = evalExpressionTree(node.right)
    
    if node.data == '-':
        return int(a)-int(b)
    elif node.data == '+':
        return int(a)+int(b)
    elif node.data == '*':
        return int(a)*int(b)
    elif node.data == "/":
        return int(a)//int(b)
    
        
def main():
    #construct the trees
    """
       1
      / \
     2   3
    / \  
    4  5
    """
    root1 = Node(1) 
    root2 = Node(1) 
    root1.left = Node(2) 
    root1.right = Node(3) 
    root1.left.left = Node(4) 
    root1.left.right = Node(5) 
      
    root2.left = Node(2) 
    root2.right = Node(3) 
    root2.left.left = Node(4) 
    root2.left.right = Node(5) 
    
    print("sum_tree", sum_tree(root1))
    print("printing spiral")
    printSpiral(root1, 0)
    print("\n")
    """
    if identical_trees(root1, root2): 
        print("Both trees are identical")
    else: 
        print("Trees are not identical")
    """
    print_inOrder(root1)
    print("new tree")
    mirror(root1)
    print_inOrder(root1)
    print("new tree in preorder")
    preOrderTraversal(root1)
    print("sum tree in preorder")
    sumTree(root1)
    print_inOrder(root1)
    print("\nmax height: "+ str(getMaxWidth(root1)))
    print("\nis balanced or not: "+ str(isBalanced(root1)))
main()
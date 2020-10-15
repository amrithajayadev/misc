# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:11:21 2019

@author: jayada1
You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. The task is to delete the node. Pointer/ reference to head node is not given. 

Note: No head reference is given to you.

Logic: copy delete_node's next data to that node and delete next node.
"""

def deleteNode(curr_node):
    #code here
    curr = curr_node
    if curr is not None and curr.next is not None:
        curr.data = curr.next.data
        curr.next = curr.next.next
    else:
        return
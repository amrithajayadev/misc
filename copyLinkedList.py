# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 08:51:53 2019

@author: jayada1
You are given a Singly Linked List with N nodes where each node next pointing to its next node. 
You are also given M random pointers , where you will be given M number of pairs denoting two nodes a and b  i.e. a->arb = b.
Input:
First line of input contains number of testcases T. For each testcase, first line of input contains two integers N and M. 
Next line of input contains values of N nodes of the linked list and last line contains M pairs denoting arbitrary connecting  nodes,
for which each ith node is connected to any jth node. ( ith->arb = jth )

NOTE : If their is any node whose arbitrary pointer is not given then its by default null.

Output:
For each testcase, clone the given linked list.

Your Task:
The task is to complete the function copyList() which takes one argument the head of the linked list to be cloned and should return the head of the cloned linked list.
"""

class Node:
    def __init__(self, val, arb):
        self.next = None
        self.val = val
        self.arb = arb

def InsertNode(val, arb):
    node = Node(val, arb)
    return node

def printLinkedList(head):
    node = head
    while node is not None:
        print(node.val, end="->")
        node = node.next

def copyLinkedList(ll,arb):
    node = None
    for item in ll:
        if node is None:
            head = InsertNode(item, None)
            node = head
        else:
            node.next = InsertNode(item, None)
            node= node.next
    printLinkedList(head)

linkedlist = [1,2,3,4]
arb=[1,2,2,4]        
copyLinkedList(linkedlist, arb)

"""        
t = int(input())
while t>0:
    linkedlist= list(map(int , input().strip().split()))
    arb = list(map(int , input().strip().split()))
    copyLinkedList(linkedlist, arb)
    t -=1
"""
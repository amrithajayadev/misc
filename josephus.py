# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:19:44 2019

@author: jayada1
Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle in a fixed direction.​
The task is to choose the safe place in the circle so that when you perform these operations starting from 1st place in the circle, you are the last one remaining and survive.

Input Format:
The first line of input contains an integer T denoting the number of test cases . Then T test cases follow. Each test case contains 2 integers n and k .

Output Format:
For each test case, in a new line, output will be the safe position which satisfies the above condition.

Your Task:
This is a function problem. You are required to complete the function josephus that takes two parameters n and k and returns an integer denoting safe position .
"""

def josephus(n,k):
    pos = [i for i in range(1,n+1)]
    skip = k-1
    pop_pos = k-1
    n = len(pos)
    
    while n>1:
        pos.pop(pop_pos)
        print(pos)
        n -= 1
        pop_pos = (pop_pos + skip)%n

    return pos[0]

josephus(3,2)
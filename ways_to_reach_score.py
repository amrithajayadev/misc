# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:22:27 2019

@author: jayada1
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of distinct combinations to reach the given score.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow.The first line of each test case is n.

Output:
For each testcase, in a new line, print number of ways/combinations to reach the given score.
"""
#code
t = int(input())

def find_ways(n):
    a = [0 for i in range(n+1)]
    
    a[0] = 1
    
    for i in range(3,n+1):
        a[i] += a[i-3]
    for i in range(5,n+1):
        a[i] += a[i-5]
    for i in range(10,n+1):
        a[i] += a[i-10]
        
    print(a[n])
while t>0:
    n = int(input())
    find_ways(n)
    t -= 1

word_dict = dict()

l = list()
l.append(1)
l.pop(2)

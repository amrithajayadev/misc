# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 13:04:06 2019

@author: jayada1
"""

"""
Given an MxN matrix, find the number of ways of reaching bottom right element from top left element
only right and down movements allowed.
"""


#Solution 1: Recursion
def numpaths(m,n):
    if m==1 or n==1:
        return 1
    else:
        return numpaths(m-1,n) + numpaths(m,n-1)
    
print(numpaths(3,3))



#Solution 2: Dynamic programming
def numpaths_dp(m,n):
    count = [[0 for i in range(n)] for j in range(m)]
    for i in range(1,n):
        count[0][i] = 1
    for i in range(1,m):
        count[i][0] = 1
    for i in range(1,m):
        for j in range (1,n):
            count[i][j] = count[i-1][j] + count[i][j-1]
    return count[m-1][n-1]
            
print(numpaths_dp(3,3))

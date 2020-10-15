# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:42:19 2019

@author: jayada1

Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

Input:
The first line contains T, denoting the number of testcases. Then follows description of testcases.
Each case begins with a single positive integer N denoting the size of array. 
The second line contains the N space separated positive integers denoting the elements of array A.

Output:
For each testcase, print "Yes" or  "No" whether it is Pythagorean Triplet or not (without quotes).

"""

#code
t = int(input())
def pythagorean(arr,n):
    sqr = [i*i for i in arr]
    sqr.sort()
    j=0
    k=n-2
    for i in range(n-1,0, -1):
        while j < k:
            if sqr[j] + sqr[k] == sqr[i]:
                return True
            if sqr[j] + sqr[k] < sqr[i]:
                j +=1
            elif sqr[j] + sqr[k] > sqr[i]:
                k -=1
        j=0
        k=i-1
                
    return False
        

while t>0:
    n = int(input())
    arr = list(map(int,input().strip().split()))
    if pythagorean(arr,n):
        print('Yes')
    else:
        print('No')
    t -=1
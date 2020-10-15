# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:24:48 2019

@author: jayada1
"""

def sort_arr(arr, n):
    count_0 = 0 
    count_1 = 0
    count_2 = 0
    for i in arr:
        if i==0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        elif i == 2:
            count_2 += 1
    
    arr2=list()
    for i in range(count_0):
        arr2.append(0)
    for i in range(count_1):
        arr2.append(1)
    for i in range(count_2):
        arr2.append(2)
    print(arr2)

arr1 = [0,1,2,2,1,1,0]
arr = [0, 2, 1, 2, 0,1,1]
sort_arr(arr, len(arr))
"""
t = int(input())
while t>0:
    n = int(input())
    arr = list(map(int,input().strip().split()))
    sort_arr(arr, n)
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 01:23:14 2019

@author: jayada1
"""

def printPattern(n,rows):
    for i in range(1,rows+1):
        for j in range(i):
            print(n, end=" ")
            n -= 1
        print()
        

def ifPattern(n):
    i=1
    while i<n:
        if n==i*(i+1)//2:
            printPattern(n,i)
            return
        else:
            i += 1
    print("-1")
            
ifPattern(10)

arr1 = "DIDI"
arr = "IIDDD"
nums =  [1,2,3,4,5,6,7,8,9]

i = 0
curr_max = 0
last = 0
while i < len(arr):
    num_ds = 0
    if arr[i] == 'I':        
        j = i+1
        while j < len(arr) and arr[j]=='D':
            num_ds += 1
            j += 1
        if i == 0:
            curr_max += 2
            last += 1
            print(last, end="")
            print(curr_max, end="")
        else:
            curr_max += num_ds + 1
            last = curr_max
            print(last, end="")
        
        k = 0
        while k < num_ds:
            last-= 1
            print(last,end="")
            i += 1
            k += 1
    else:
        if i == 0:
            j = i+1
            while j < len(arr) and arr[j]=='D':
                num_ds += 1
                j += 1
                
            curr_max = num_ds + 2
            print(curr_max, end="")
            print(curr_max-1, end="")
            last = curr_max - 1
        else:
            print(last-1, end="")
            last -= 1
    i += 1
    
        
            
            
        
         
        
        
    
         

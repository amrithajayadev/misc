# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:22:02 2019

@author: jayada1


t = int(input())

def find_negative_in_window(arr, k, n):
    for i in range(n):
        
        

    
while t > 0:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    find_negative_in_window(arr, n)
    k = int(input())
    t -= 1


You are given an array A of size N. Your task is to find the minimum number of operations needed to convert the given array to 'Palindromic Array'.

Palindromic Array:
[23,15,23] is a ‘Palindromic Array’ but [2,0,1] is not.

"""    

#code

def check_palindrome(a):
    pass
def find_operations(a, n):
    i = 0
    j = n-1
    op = 0
    
    while i<j:
        if a[i] == a[j]:
            i += 1
            j -= 1
        elif a[i] < a[j]:
            a[i+1] += a[i]
            a.pop(i)
            j -= 1
            op += 1
        else:
            a[j-1] += a[j]
            a.pop(j)
            j -= 1
            op += 1
    return op

arr1 = [3,2,3,3,5]
arr=[5,3,3,4]
print(find_operations(arr, len(arr)))
"""
while t>0:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(find_operations(arr, n))
    t -= 1
"""
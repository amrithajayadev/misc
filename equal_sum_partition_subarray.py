# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:26:39 2020

@author: jayada1
"""

def is_subset_sum(arr, target_sum, n):
    if target_sum == 0:
        return True
    if n == 0 and target_sum != 0:
        return False
    if arr[n-1] > target_sum:
        return is_subset_sum(arr, target_sum, n-1)
    return is_subset_sum(arr, target_sum - arr[n-1], n-1) or is_subset_sum(arr, target_sum, n-1)

def is_partition_sum(arr, n):
    array_sum = sum(arr)
    if array_sum % 2 != 0:
        return False
    if arr[n-1] < array_sum//2:
        return is_subset_sum(arr, array_sum / 2, n)
    else:
        return False

arr1 = [3, 34, 4, 12, 5, 2]
arr2 = [1,5,11,5]
"""
if is_subset_sum(arr, 9, len(arr)) == True:
    print("yes")
else:
    print("no")
"""
    
if is_partition_sum(arr2, len(arr2)) == True:
    print("yes")
else:
    print("no")
    

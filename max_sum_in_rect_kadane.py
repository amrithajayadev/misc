# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 02:06:33 2019

@author: jayada1


Kadanes algorithm to find max subarray
Example : -2, 1, -3, 4, -1, 2, 1, -5, 4
solution = 6 = 4-1+2+1


logic: what is the best the subarray sum so far ? Or is the current element better?
compare the current index value to sum of subarray till then + now and choose whether to continue or start a new 
subarray

"""
arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr = [1,-1,1,1,1,-1,-1,-1,1,1]
def kadane(arr):
    max_sum = list()
    max_sum.append(arr[0])
    print(max_sum)
    for i in range(1, len(arr)):
        max_sum.append(max([arr[i], max_sum[i-1] + arr[i]]))
        print(max_sum)
    
    print(max(max_sum))
        
kadane(arr)

rectangle = [[6, -5, -7, 4, -4],
             [-9, 3, -6, 5, 2],
             [-10, 4, 7, -6, 3],
             [-8, 9, -3, 3, -7]]

#finding max sum rectangle
left = 0
right =0
right_bound = len(rectangle[0])
row_bound = len(rectangle)
for left in range(right_bound):
    running_row_sum = [rectangle[row][left] for row in range(row_bound)]
    rect_sum = kadane(running_row_sum)
    for right in range(left+1, right_bound):
       for val in running_row_sum:
           val += rectangle[row][left]
        
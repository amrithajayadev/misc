# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:34:10 2019

@author: jayada1
"""

arr = [1,2,3,4,5,6,7]
d = 2
n = 7
def rotate(arr, d, n):
    new_arr = arr[d:]
    new_arr.extend(arr[0:d])
    return new_arr
    
print(rotate(arr, d, n))


"""
num = 123
output : 231, 312

num = 1445
output: 4451, 4514, 5144
"""

def find_num_digits(num):
    count = 0
    while num>0 :
        num = int(num /10)
        count += 1
    return count

def generate_all_left_rotations(num):
    n = find_num_digits(num) - 1
    for i in range (0,n):
        first_digit = int(num / (10**n))
        remain_digits = num % (10**n)
        num = remain_digits * 10 + first_digit
        print(num)

generate_all_left_rotations(1445)


arr =    [2,3,4,1,5]  
arr2 = [2,31,1,38,29,5,44,6,12,18,39,9,48,49,13,11,7,27,14,33,50,21,46,23,15,26,8,47,40,3,32,22,34,42,16,41,24,10,4,28,36,30,37,35,20,17,45,43,25,19]  
arr3 = [8,45,35,84,79,12,74,92,81,82,61,32,36,1,65,44,89,40,28,20,97,90,22,87,48,26,56,18,49,71,23,34,59,54,14,16,19,76,83,95,31,30,69,7,9,60,66,25,52,5,37,27,63,80,24,42,3,50,6,11,64,10,96,47,38,57,2,88,100,4,78,85,21,29,75,94,43,77,33,86,98,68,73,72,13,91,70,41,17,15,67,93,62,39,53,51,55,58,99,46]
def minimumSwaps(arr):
    sorted_arr = arr.copy()
    arr.sort()
    n = len(arr)
    err = 0
    for i in range(0,n):
        if arr[i]==sorted_arr[i]:
            err += 1
    if err!=0:
        return n - err - 1
        
err = minimumSwaps(arr3)
print(err)


'Array' == 'array'
    
"""
Rearrange an array such that arr[i] = i 

Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
              11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
         11, 12, 13, 14, 15, 16, 17, 18, 19]
"""

def array_rearrange(arr):
    l = len(arr)
    new_arr = [None] * l
    for i in range(0, l):
        if i in arr:
            new_arr[i] = i
        else:
            new_arr[i] = -1
    print(new_arr)
    
array_rearrange([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1])
array_rearrange([19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
              11, 10, 9, 5, 13, 16, 2, 14, 17, 4])
    
l = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

"""
Move all zeroes to end of array
Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0};

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
Output : arr[] = {1, 2, 3, 6, 0, 0, 0};
"""

def move_zeroes_to_end_while(arr):
    n = len(arr)-1
    i = 0
    j = 0
    while j <= n:
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
        else:
            i = i + 1
        j += 1
    print(arr)

#test cases    
move_zeroes_to_end_while([1, 2, 0, 4, 3, 0, 5, 0])
move_zeroes_to_end_while([1, 2, 0, 0, 0, 3, 6])
move_zeroes_to_end_while([0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9])

"""
Rearrange positive and negative numbers using inbuilt sort function
Given an array of positive and negative numbers, arrange them such that all negative integers appear before all the positive integers in the array without using any additional data structure like hash table, arrays, etc. The order of appearance should be maintained.

Examples:

Input :  arr[] = [12, 11, -13, -5, 6, -7, 5, -3, -6]
Output : arr[] = [-13, -5, -7, -3, -6, 12, 11, 6, 5]

Input :  arr[] = [-12, 11, 0, -5, 6, -7, 5, -3, -6]
Output : arr[] =  [-12, -5, -7, -3, -6, 0, 11, 6, 5]

"""
   
    
def Rearrange(arr): 
  
    # First lambda expression returns list of negative numbers 
    # in arr. 
    # Second lambda expression returns list of positive numbers 
    # in arr. 
    return [x for x in arr if x < 0] + [x for x in arr if x >= 0] 
  
arr = [12, 11, -13, -5, 6, -7, 5, -3, -6] 
print(Rearrange(arr) )
    
    
"""
Rearrange an array in order – smallest, largest, 2nd smallest, 2nd largest, ..
Given an array of integers, task is to print the array in the order – smallest number, Largest number, 2nd smallest number, 2nd largest number, 3rd smallest number, 3rd largest number and so on…..

Examples:

Input : arr[] = [5, 8, 1, 4, 2, 9, 3, 7, 6]
Output :arr[] = {1, 9, 2, 8, 3, 7, 4, 6, 5}

Input : arr[] = [1, 2, 3, 4]
Output :arr[] = {1, 4, 2, 3}
"""

def rearrange_s_l(arr):
    n = int(len(arr)/2)
    arr.sort()
    new_arr = [None]*len(arr)
    j = 0
    for i in range(n):
        new_arr[j]=arr[i]
        new_arr[j+1]=arr[-i-1]
        j += 2
    new_arr[len(arr)-1] = arr[n]
    print(new_arr)

rearrange_s_l([5, 8, 1, 4, 2, 9, 3, 7, 6])  
rearrange_s_l([1, 2, 3, 4]) 
    
    
"""
Double the first element and move zero to end
Given an array of integers of size n. Assume ‘0’ as invalid number and all other as valid number. Convert the array in such a way that if next valid number is same as current number, double its value and replace the next number with 0. After the modification, rearrange the array such that all 0’s are shifted to the end.

Examples:

Input : arr[] = {2, 2, 0, 4, 0, 8}
Output : 4 4 8 0 0 0

Input : arr[] = {0, 2, 2, 2, 0, 6, 6, 0, 0, 8}
Output :  4 2 12 8 0 0 0 0 0 0
"""

def make_new_arr(arr):
    n= len(arr)-1
    count = 0
    for i in range(n):
        if arr[i]==0:
            count += 1
            arr.pop(i)
        if arr[i] == arr[i+1]:
            arr[i] *= 2
            arr.pop(i+1)
            count += 1
        for j in range(count):
            arr.append(0)
        
    print(arr)
    
make_new_arr([2, 2, 0, 4, 0, 8])

with open('C:/Users/jayada1/Desktop/backup/study/portalscv.txt','r') as f:
    for line in f:
        print(line)
    
def minimumSwaps(arr):
    count = 0
    n = len(arr)
    sorted_arr = [i for i in range(1,n+1)]

    diff_arr = [i1-i2 for i1,i2 in zip(sorted_arr,arr)]
    for item in diff_arr:
        if item != 0:
            count+=1

    return count-1

#arr = [2,31,1,38,29,5,44,6,12,18,39,9,48,49,13,11,7,27,14,33,50,21,46,23,15,26,8,47,40,3,32,22,34,42,16,41,24,10,4,28,36,30,37,35,20,17,45,43,25,19]
arr = [1,3,5,2,4,6,7]
minimumSwaps(arr)

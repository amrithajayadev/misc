# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:43:16 2019

@author: jayada1
"""

def find_modular_exp(a,b,c):
    mod_pattern_dict = dict()
    i = a%c
    y = 1
    while True:
        val = pow(a,y)%c
        if val in mod_pattern_dict.values():
            break
        mod_pattern_dict[y] = val
        y += 1
    print(mod_pattern_dict)
    #print("length=",len(mod_pattern_dict))
    pattern_length = len(mod_pattern_dict)
    if pattern_length == 1:
        val_to_be_found = 1
    else:
        val_to_be_found = b%pattern_length if b!=pattern_length else b
    #print("pos=",val_to_be_found)
    print(mod_pattern_dict.get(val_to_be_found))
    #return key

#a,b,c = 450, 768 ,517
#a,b,c = 10 ,9 ,6
#a,b,c = 3,2,4
a,b,c = 1746, 5229, 4092
find_modular_exp(a,b,c)

arr = (i for i in range(1,10))
a = [1,2,3]
a.insert()

def swap_in_s1(s1, c1,c2):
    
    s1_arr = [c for c in s1]
    
    x =s1_arr.index(c1)
    y =s1_arr.index(c2)
    s1_arr[x] = c2
    s1_arr[y] = c1
    s1 = ''.join(s1_arr)
    print(s1)
    
swap_in_s1('geeks', 'g','k')


import math
math.factorial()

#code
t = int(input())
while t>0:
    n = int(input())
    intervals = list(map(int, input().strip().split()))
    find_overlaps(intervals, n)
    t -= 1

intervals1 = [6,8,1,9,2,4,4,7]     
intervals = [1,3,2,4,6,8,9,10]       
arr = [[intervals[i],intervals[i+1]] for i in range(0,8,2)]
print(arr)
#arr = [[1, 9], [2, 4], [4, 7], [6, 8]]
    
for i,j in enumerate(range(1,len(arr))):
        #if arr[i][1] > arr[j][0]:
    #print(arr[i][0],arr[j][0],arr[i][1],arr[j][1])
    if arr[i][1] > arr[j][0]:
            arr[i][1] = max(arr[j][1], arr[i][1])
            arr.pop(j)
    print(arr)
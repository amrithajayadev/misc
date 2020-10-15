# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 00:28:23 2019

@author: jayada1
"""


def make_2d(d_arr, n, m):
    arr = []
    j = 0
    for i in range(0, len(d_arr)-m+1, m):
        arr.append(d_arr[i:i+m])
    print(arr)

d1_arr = [1 ,0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
make_2d(d1_arr, 3,4)

import math

math.pow(2, 3)
math.floor(math.log2(9))

import re
re.findall('1[0-9]*1','10101')

def find_paths(m,n):
    arr = [[0 for i in range(n)] for j in range(m)]
    print(arr)
    
find_paths(2,3)

mod_dict = {1: 450, 2: 353, 3: 131, 4: 12, 5: 230, 6: 100, 7: 21, 8: 144, 9: 175, 
            10: 166, 11: 252, 12: 177, 13: 32, 14: 441, 15: 439, 16: 56, 17: 384, 
            18: 122, 19: 98, 20: 155, 21: 472, 22: 430, 23: 142, 24: 309, 25: 494, 
            26: 507, 27: 153, 28: 89, 29: 241, 30: 397, 31: 285, 32: 34, 33: 307, 
            34: 111, 35: 318, 36: 408, 37: 65, 38: 298, 39: 197, 40: 243, 41: 263, 
            42: 474, 43: 296, 44: 331, 45: 54, 46: 1}
mod_dict.get(768%len(mod_dict))
#mod_dict.get(0)
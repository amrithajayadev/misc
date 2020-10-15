# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 23:22:04 2019

@author: jayada1
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" or "i like sam sung".

"""

s= "ilikesamsung"
dictionary = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice',
  'cream', 'icecream', 'man', 'go', 'mango']

a = [[0 for i in range(len(s))] for j in range(len(s))]

size = len(s)

for l in range(0,size):
    for i in range(0,size-l):
        start_pos=i
        end_pos=i+l
        if s[start_pos:end_pos] in dictionary:
            a[start_pos][end_pos] = True
        else:
            flag = False
            for split in range(start_pos, end_pos):
                if a[start_pos][split] and a[split+1][end_pos]:
                    flag = True
                    break
            
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:48:10 2019

@author: jayada1
"""


arr = “abcCkDdppGGa”
copy = [‘a’,’b’,’k’, ‘p’,’p’,’G’, ‘G’, ]
n = len(arr)
i = 0
while i < n-1:
	if arr[i] == arr[i+1]
		copy.append(arr[i])
			if i > n-1:
				break
			else:
				i += 1
	elif arr[i] != arr[i+1]:
		if lower(arr[i]) == lower(arr[i+1]):
			if i > n-2:
				break
			else:
				i += 2	
		else:
			copy.append(arr[i])
			i += 1
if i == n-1:
	copy.append(arr[i])


# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:37:33 2019

@author: jayada1
Given an array arr[] of positive integers. Find the length of the longest sub-sequence such that elements 
in the subsequence are consecutive integers, the consecutive numbers can be in any order.

Input:
The first line of input contains T, number of test cases. First line of line each test case contains a single integer N.
Next line contains N integer array.

Output:
Print the output of each test case in a seprate line.
"""


def length_subsequence(arr):
    arr.sort()
    length = 0
    max_length = 0
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != 1:
            length = 0
        else:
            length += 1
        if max_length <= length:
            max_length = length

    print(max_length + 1)
    print(arr)


arr1 = [1, 9, 3, 10, 4, 20, 2, 21, 22, 23, 24]
arr2 = [2, 6, 1, 9, 4, 5, 3, 11, 13, 14, 15, 12, 10]
arr3 = [2, 6, 1, 9, 4, 5, 3]
arr4 = [1, 9, 3, 10, 4, 20, 2]
# length_subsequence(arr4)


string1 = "geeksforgeeks"
string2 = "geeksgeeks"

t = list()
t = [[-1 for i in range(0, len(string2) + 1)] for j in range(0, len(string1) + 1)]
print(t)


# with recursion
def find_lcs_length(string1, string2, n, m):
    if m == 0 or n == 0:
        return 0
    if string1[n - 1] == string2[m - 1]:
        return 1 + find_lcs_length(string1, string2, n - 1, m - 1)
    else:
        return max(find_lcs_length(string1, string2, n - 1, m), find_lcs_length(string1, string2, n, m - 1))


def find_lcs_length_memoization(string1, string2, n, m):
    print(t)
    if m == 0 or n == 0:
        return 0
    if string1[n - 1] == string2[m - 1]:
        return 1
    if t[m][n] != 1:
        return t[m][n]
    if string1[n - 1] == string2[m - 1]:
        t[m][n] = 1 + find_lcs_length(string1, string2, n - 1, m - 1)
        return t[m][n]
    else:
        t[m][n] = max(find_lcs_length(string1, string2, n - 1, m), find_lcs_length(string1, string2, n, m - 1))
        return t[m][n]


#print(find_lcs_length(string1, string2, len(string1), len(string2)))
print(find_lcs_length_memoization(string1, string2, len(string1), len(string2)))
print(t)

# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:38:20 2019

@author: jayada1
Given two strings, A and B, of equal length, find whether it is possible to cut both strings at a common point such that the first part of A and the second part of B form a palindrome.

Extension1. How would you change your solution if the strings could be cut at any point (not just a common point)?
"""


def ispalindrome(s):
    n = len(s)
    l = 0
    r = n - 1
    while l < r:
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True


def cut_palindrome(a, b):
    n = len(a)
    for i in range(1, n):
        s = a[0:i + 1] + b[i:n]
        if ispalindrome(s):
            print("Yes")
            return
    print("No")


a = "abcd"
b = "zyca"


# cut_palindrome(a, b)


def cut_palindrome2(a, b, point):
    if len(a) == 0 | len(a) < point:
        return False
    ab = a[:point] + b[point:]
    if ab == ab[::-1]:
        return True
    else:
        return False


cut_palindrome2(a, b, 2)

"""Question: You are given 2 strings which are exactly same but 1 string has an extra character. Find that character.

Approach: Sort the strings and keep matching until you find that extra character because it won’t be present in other string. Time Complexity – O(nlogn).

He asked me to code the solution. After this he asked me to further optimise it without sorting the strings.
"""

# a = "abbd"
# b = "abdbe"
#
# set_a = set(a)
# set_b = set(b)
#
# set_b.difference(set_a)

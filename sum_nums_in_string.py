# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:03:19 2019

@author: jayada1
Given a string str containing alphanumeric characters, calculate sum of all numbers present in the string.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a string containing alphanumeric characters.

Output:
Print the sum of all numbers present in the string.

Constraints:
1<=T<=105
1<=length of the string<=105

Example:
Input:
4
1abc23
geeks4geeks
1abc2x30yz67
123abc

Output:
24
4
100
123
"""

import re

def find_sum_regex(string):
    l = list(map(int,re.findall('\d+',string)))
    print(sum(l))

find_sum_regex('geeks123geeks4')  
t = int(input())
def find_sum(string):
    temp="0"
    sum_nums=0
    for c in string:
        if c.isdigit():
            temp+=c
        else:
            sum_nums+=int(temp)
            temp="0"
    print(sum_nums + int(temp))
    
while t>0:
    string = input().strip()
    find_sum(string)
    t -=1
    




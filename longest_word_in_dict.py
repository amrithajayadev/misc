# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 23:04:55 2019

@author: jayada1
Giving a dictionary and a string ‘str’, your task is to find the longest string in dictionary of size x which can be formed by deleting some characters of the given ‘str’.

Examples:

Input : dict = {"ale", "apple", "monkey", "plea"}   
        str = "abpcplea"  
Output : apple

Input  : dict = {"pintu", "geeksfor", "geeksgeeks", 
                                        " forgeek"} 
         str = "geeksforgeeks"
Output : geeksgeeks
"""


dictionary = ["ale", "apple", "monkey", "plea"]
input_str = "abpcplea"

def is_a_subsequence(word, input_str):
    ret = False
    length = 0
    for c in word:
        if c not in input_str:
            ret = False
            break
        else:
            length += 1
    if length == len(word):
        ret = True                
    
    return ret

def find_longest_sub(dictionary, input_str):
    length = 0
    max_len = 0
    for word in dictionary:
        if is_a_subsequence(word, input_str):
            length = len(word)
        if max_len< length:
            max_len = length
            output_word = word
    print(output_word)
    
t= int(input())
while t>0:
    n = int(input())
    dictionary = input().strip().split()
    input_string = input().strip()
    find_longest_sub(dictionary, input_string)
    t -=1

 
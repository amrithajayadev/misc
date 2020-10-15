# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:02:10 2020

@author: jayada1
1 2 3
4 5 6

paths: 
1-2-3-6
1-2-5-6
1-4-5-6


1 2 3 4
5 6 7 8
9 10 11 12
"""

def find_longest_word(dictionary, word):
    letters = list(word)
    length = 0
    longest_word = ""
    for item in dictionary:
        item_letters = list(item)
        temp = letters[:]
        for char in temp:
            if char not in item_letters:
                temp.remove(char)
        resultant = ''.join(temp)
        if item in resultant and len(item)>length:
            length = len(item)
            longest_word = item
            
    print(longest_word)
        
find_longest_word(['ale', 'apple', 'monkey', 'plea'], "abpcplea")
find_longest_word(["pintu" ,"geeksfor", "geeksgeeks", "forgeek"], "geeksforgeeks")
        
    
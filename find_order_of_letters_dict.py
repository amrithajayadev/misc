# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 00:09:36 2020

@author: jayada1
"""

def find_order(words):
    cols = max([len(w) for w in words])
    rows = len(words)
    matrix = list()
    for word in words:
        word_col = list(word)
        word_col.extend([None]*(cols-len(word)))
        matrix.append(word_col)
    letter_list = list()
    for j in range(0, rows):
        if matrix[j][0] not in letter_list:
            letter_list.append(matrix[j][0])
    print(letter_list)
    
                
            
    
    


words = ["baa", "abcd", "abca", "cab", "cad"]
find_order(words)
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 00:41:12 2019

@author: jayada1
"""

def enclosing_list_printer(a):
    print(a)
    
    def print_list_space():
        for item in a:
            print(item, end= " ")
    
    return print_list_space
    
e = enclosing_list_printer([1,2,3,4])
e()

"""


e()
enclosing_list_printer() --> print_list_space()

"""
add = lambda x,y: x+y
add(3,5)
double_number = lambda i: 2*i
print(list(map(double_number, [1,2,4,5,6])))

import functools
print( functools.reduce( lambda x,y: x + y, [1,2,3,4,5]))
print( functools.reduce( lambda x: x*2, [1,2,3,4,5]))
convert_number_to_digit_list = lambda n: list(map(int,[i for i in str(n)]))
print(functools.reduce(lambda x,y: x+y, list(map(int,[i for i in str(444)]))))
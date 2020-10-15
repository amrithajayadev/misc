# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:11:46 2019

@author: jayada1
"""

import sys

def main(file):
    with open(file, mode='rt', encoding='utf-8') as f:
        for line in f:
            #print(line) #print line adds new line after each line.
            #sys.stdout.write(line) #does not add new line on it's own.
            sys.stdout.writelines(line)


if __name__ == "__main__":
    main(sys.argv[1])
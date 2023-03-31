# https://leetcode.com/problems/string-compression-ii/
from collections import Counter


def compress_string(inp_str):
    compressed = ""
    stack = [inp_str[0]]
    count = 0
    for c in inp_str:
        if stack[-1] == c:
            count += 1
        else:
            stack.append(str(count))
            count = 1
            stack.append(c)
    stack.append(str(count))
    print(stack)
    for c in stack:
        if c=='1' or c=='0':
            continue
        compressed+=c
    print(compressed)

compress_string("aaabccd")
compress_string("aabbaa")
compress_string("aaaaaaaaaaa")
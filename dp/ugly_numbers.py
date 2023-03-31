# https://www.geeksforgeeks.org/ugly-numbers/
"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.
Given a number n, the task is to find n’th Ugly number.

Examples:

Input  : n = 7
Output : 8
"""


def check_num_ugly(num):
    while num % 2 == 0:
        num = num // 2
    while num % 3 == 0:
        num = num // 3
    while num % 5 == 0:
        num = num // 5
    if num == 1:
        return True
    else:
        return False


def generate_ugly_num(n):
    count = 1
    num = 1
    while count < n:
        num += 1
        if check_num_ugly(num):
            count += 1
    return num


print(generate_ugly_num(7))
print(generate_ugly_num(15))
print(generate_ugly_num(10))
print(generate_ugly_num(150))
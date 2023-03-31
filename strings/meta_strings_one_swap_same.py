# https://www.geeksforgeeks.org/meta-strings-check-two-strings-can-become-swap-one-string/

def count_zeroes(ord_list):
    count = 0
    for i in ord_list:
        if i == 0:
            count+=1
    return count


def check_swap_same(str1, str2):
    if len(str1) != len(str2):
        return False
    ord_list = []
    for c1, c2 in zip(str1, str2):
        ord_list.append(ord(c1) - ord(c2))

    print(ord_list)
    count_of_zeroes = count_zeroes(ord_list)
    if sum(ord_list) == 0 and count_of_zeroes == len(str1) - 2:
        print("true")
    else:
        print("False")


check_swap_same("geekswq", "keegsqw")

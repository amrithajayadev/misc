# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

def remove_min_and_max(arr):
    min_i, min_n = 0, float('inf')
    max_i, max_n = 0, float('-inf')

    for i, num in enumerate(arr):
        if min_n > num:
            min_i = i
            min_n = num

    for i, num in enumerate(arr):
        if max_n < num:
            max_i = i
            max_n = num

    n = len(arr)

    # remove both from front, back
    front = max(min_i + 1, max_i + 1)
    back = max(n - min_i, n - max_i)

    # remove min from front and max from back and vice-versa
    min_front = min_i + 1 + n - max_i
    max_front = max_i + 1 + n - min_i

    return min(front, back, min_front, max_front)

print(remove_min_and_max([2,10,7,5,4,1,8,6])) # 5
print(remove_min_and_max([0,-4,19,1,8,-2,-3,5])) #3
print(remove_min_and_max([101])) #1
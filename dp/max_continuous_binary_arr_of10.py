"""
Maximum consecutive one’s (or zeros) in a binary array
Given binary array, find count of maximum number of consecutive 1’s present in the array.

Examples :

Input  : arr[] = {1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1}
Output : 4

Input  : arr[] = {0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1}
Output : 1
"""


def max_consecutive(nums):
    n = len(nums)
    curr_sum = nums[0]
    max_sum = curr_sum
    nums_copy = []
    for nu in nums:
        nums_copy.append(-99 if nu == 0 else nu)
    for i in range(1, n):
        curr_sum = max(curr_sum + nums_copy[i], nums_copy[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum


x = max_consecutive([1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1])
# x = max_consecutive([0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
print(x)

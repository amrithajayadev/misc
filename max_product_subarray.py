# https://leetcode.com/problems/maximum-product-subarray/
"""
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""


def find_max_product(nums):
    max_pos_product = nums[0]
    max_neg_product = nums[0]
    ans = nums[0]
    for i in range(1, len(nums)):
        x = max(nums[i], max_pos_product * nums[i], max_neg_product * nums[i])
        y = min(nums[i], max_pos_product * nums[i], max_neg_product * nums[i])

        max_neg_product, max_pos_product = y, x
        ans = max(ans, max_pos_product)
    return ans


# print(find_max_product([2, 3, -2, -3, 0]))


def find_max_product1(nums):
    max_so_far = 1
    neg_prod = 1
    pos_prod = 1
    for i in range(len(nums)):
        tmp = pos_prod * nums[i]
        pos_prod = max(neg_prod * nums[i], pos_prod * nums[i], nums[i])
        neg_prod = min(neg_prod * nums[i], tmp, nums[i])
        max_so_far = max(max_so_far, pos_prod, neg_prod)
        print(max_so_far)


# nums = [2, 3, -2, 4]
nums = [2, -5, -2, -4, 3]
"""
neg = [1, 2, -10, 20, -80]
pos = [1, 2, -10, 20, -80]
n= 2
p = 2
m= 1

n = 2
p = 6
m = 6

n = -12
p = 6
m = 6

n = -12
p = 24

"""
find_max_product1(nums)

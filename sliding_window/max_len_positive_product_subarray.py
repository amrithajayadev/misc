# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
import unittest


class TestMaxLen(unittest.TestCase):
    def test_1(self):
        nums = [0, 1, -2, -3, -4]  # works o/p=3
        actual = max_len_pos_product_subarray_non_window(nums) # max_len_pos_product_subarray(nums)
        print(actual)
        assert actual == 3

    def test_2(self):
        nums = [-1, -2, -3, 0, 1]  # works o/p=2
        actual = max_len_pos_product_subarray_non_window(nums) # max_len_pos_product_subarray(nums)
        print(actual)
        assert actual == 2

    def test_3(self):
        nums = [1, -2, -3, 4]  # works o/p=4
        actual = max_len_pos_product_subarray_non_window(nums) #max_len_pos_product_subarray(nums)
        print(actual)
        assert actual == 4

    def test_4(self):
        nums = [-1, 2]  # works o/p=1
        actual = max_len_pos_product_subarray_non_window(nums) #max_len_pos_product_subarray(nums)
        print(actual)
        assert actual == 1

    def test_5(self):
        nums = [-16, 0, -5, 2, 2, -13, 11, 8]  # o/p=6 #works
        actual = max_len_pos_product_subarray_non_window(nums) # max_len_pos_product_subarray(nums)
        print(actual)
        assert actual == 6

    def test_6(self):
        nums = [6, 2, 10, 1, -2, 8]  # o/p=4 #works
        actual = max_len_pos_product_subarray_non_window(nums) #max_len_pos_product_subarray(nums)
        print(actual)
        assert actual == 4

    def test_7(self):
        nums = [-17, -9, 17, -3, -5, -13, 2, 6, 0]  # o/p=7, works
        actual = max_len_pos_product_subarray_non_window(nums) #max_len_pos_product_subarray(nums)
        print(actual)
        assert actual == 7


def max_len_pos_product_subarray(nums):
    i = 0
    j = 0
    n = len(nums)
    p = 1
    max_l = 0
    while j < n:
        if nums[j] != 0:
            p = p * nums[j]
        else:
            if j + 1 < n:
                i = j + 1
                p = 1
            elif p < 0:
                while p < 0:
                    p = p // nums[i]
                    i += 1
                max_l = max(max_l, j - i + 1)

        if p > 0:
            max_l = max(max_l, j - i + 1)
        j += 1
    return max_l


def max_len_pos_product_subarray_non_window(nums):
    pos = [0] * len(nums)
    neg = [0] * len(nums)
    for i in range(len(nums)):
        if nums[i] == 0:
            pos[i] = 0
            neg[i] = 0
        elif nums[i] > 0:
            pos[i] = pos[i-1] + 1
            neg[i] = 0 if neg[i-1] == 0 else neg[i-1] + 1
        else:
            pos[i] = 0 if neg[i-1] == 0 else neg[i-1] + 1
            neg[i] = pos[i-1] + 1
    return max(pos)
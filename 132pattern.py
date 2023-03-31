# https://leetcode.com/problems/132-pattern/

def find132pattern(nums) -> bool:
    i = 0
    j = 0
    k = 0

    n = len(nums)
    while i < j < k < n:
        if nums[i] < nums[k] < nums[j]:
            return True
        if nums[j] < nums[k]:
            k += 1
            if nums[i] > nums[k]:
                i += 1
                j += 1
        else:
            if i < j < k < n:
                i += 1
                j += 1
                k += 1
    return False


# nums = [1, 2, 3, 4] # works
# nums = [3,1,4,2] # works
# nums = [-1, 3, 2, 0] # works
# nums = [3, 5, 0, 3, 4]
nums = [-2, 1, 2, -2, 1, 2]
if find132pattern(nums):
    print("True")
else:
    print("False")

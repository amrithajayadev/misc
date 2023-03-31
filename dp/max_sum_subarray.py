nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(nums)


def max_subarray(nums, n):
    curr_sum = nums[0]
    max_sum = curr_sum

    for i in range(n):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(curr_sum, max_sum)
    return max_sum


print(max_subarray(nums, n))

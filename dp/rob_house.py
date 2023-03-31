def rob(nums, i):
    if i < 0:
        return 0
    return max(rob(nums, i - 2) + nums[i], rob(nums, i - 1))


amt = 0
nums = [1, 2, 3, 1]

print(rob(nums, len(nums) - 1))


def rob_2(nums):
    n = len(nums) - 1
    if n == 0:
        return nums[0]
    if n == 1:
        return max(nums)
    res = [nums[-1], max(nums[-1], nums[-2])]
    for i in range(n - 2, -1, -1):
        res.append(max(res[n - i - 1], res[n - i - 2] + nums[i]))
        print(n - i - 1, n - i - 2)
        print(res)
    return max(res)


nums = [2, 7, 9, 3, 1]
print(rob_2(nums))
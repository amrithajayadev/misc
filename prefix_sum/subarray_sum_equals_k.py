# https://leetcode.com/problems/subarray-sum-equals-k/

def subarray_sum_k(nums, i, k, count):
    if k == 0:
        return 1
    if i > len(nums) - 1 or k < 0:
        return 0
    for j in range(i, len(nums)):
        count += subarray_sum_k(nums, j + 1, k - nums[j], count)
    return count


# nums = [1,2,3]
# k = 3

# nums = [1,1,1]
# k = 2
# print(subarray_sum_k(nums, 0, k, 0))

def subarray_sum_k_bruteforce(nums, k):
    count = 0
    for i in range(len(nums)):
        sum1 = 0
        for j in range(i, len(nums)):
            sum1 += nums[j]
            if sum1 == k:
                count += 1
    return count


# nums = [1,2,3]
# k = 3

nums = [1,1,1]
k = 2

# nums = [1, 2, 1, 2, 1]
# k = 3
print(subarray_sum_k_bruteforce(nums, k))


def subarray_sum_k_prefix(nums, k):
    curr_sum = 0
    res = 0
    prefix_map = {0: 1}
    for n in nums:
        curr_sum += n
        diff = curr_sum - k
        res += prefix_map.get(diff, 0)
        prefix_map[curr_sum] = 1 + prefix_map.get(curr_sum, 0)
    return res


print(subarray_sum_k_prefix(nums, k))
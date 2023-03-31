def search_key_range(nums, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return search_key_range(nums, target, start, mid-1)
    elif nums[mid] < target:
        return search_key_range(nums, target, mid + 1, end)

#
nums = [5, 7, 7, 8, 8, 10]
target = 8
# nums = [1]
# target = 1
idx = search_key_range(nums, target, 0, len(nums) - 1)
low = search_key_range(nums, target, 0, idx)
high = search_key_range(nums, target, idx + 1, len(nums) - 1)

print(low, high, idx)
print(idx)